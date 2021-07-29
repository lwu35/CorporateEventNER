import torch
from torch import nn
from torch.nn import CrossEntropyLoss
from torch.nn import Dropout
from torch.utils.data import DataLoader
from transformers import AdamW
from transformers import BertModel, BertTokenizer, BertTokenizerFast, DistilBertTokenizer, DistilBertModel, RobertaTokenizer, RobertaModel
import pandas as pd
import numpy as np
import csv
import os
import time
from tqdm import tqdm
import csv
import os
import configparser


config = configparser.ConfigParser()
config.read('configg.ini')


seed = config['bert_model']['random_seed']
seed = int(seed)
np.random.seed(seed)
torch.manual_seed(seed)
torch.cuda.manual_seed(seed)

class ParserModel(torch.nn.Module):
    def __init__(self,
                 model_name_or_path: str,
                 dropout: float,
                 num_intent_labels: int):
        super(ParserModel, self).__init__()
        self.bert_model = BertModel.from_pretrained(model_name_or_path)
        self.dropout = Dropout(dropout)
        self.num_intent_labels = num_intent_labels
        # 52 -> 7
        self.intent_classifier = nn.Linear(self.bert_model.config.hidden_size, num_intent_labels)
        #print(num_intent_labels)

    def forward(self,
                input_ids: torch.tensor,
                token_type_ids: torch.tensor,
                intent_label: torch.tensor = None
                ):

        last_hidden_states, pooler_output = self.bert_model(input_ids=input_ids,
                                  token_type_ids=token_type_ids,
                                   return_dict=False)
        
        #print(self.bert_model.config)
        #print(last_hidden_states)    
        #sigmoid
        #print(last_hidden_states.size())
        intent_logits = self.intent_classifier(self.dropout(pooler_output)) 
        #print(intent_logits.size()) # 7 close to 0 or 1, if not apply sigmoid
        loss_fct = CrossEntropyLoss() #BCE multiclass
        # Compute losses if labels provided
        #print("...")
        intent_loss = loss_fct(intent_logits.view(-1, self.num_intent_labels), intent_label.type(torch.long))

        return intent_logits, intent_loss


train_file = config['bert_model']['train_file']
df = pd.read_csv(train_file)
print(df.head())
event_tags = df['event_type'].tolist()
#print(event_tags)

texts = df['event_text'].astype(str).str.replace('\xa0', ' ').tolist()

def extractDigits(lst):
    return [[el] for el in lst]
raw_event_text = extractDigits(texts) 

intent_vocab = ['Sales Results','Guidance']
for intent in event_tags:
    if intent not in intent_vocab:
        intent_vocab.append(intent)
# print(len(intent_vocab))
# print(intent_vocab)
# 1. For mapping slots between ints and string


intent2id = {intent:id for id,intent in enumerate(intent_vocab)}
id2intent = {id:intent for intent,id in intent2id.items()}


# 2. Tokenize utterances for BERT to accept
# Load pre-trained model tokenzier (vocab)
tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased', do_lower_case=True)

split_text = []
for sent in raw_event_text:
    split_text.append(' '.join(sent).split())


#print(split_text)
# 4. pads to longest sequence, truncates to maximum allowed length by model, 
# Gives encodings, token type_ids -> https://huggingface.co/transformers/glossary.html#token-type-ids 
# and offset_mappings
train_encodings = tokenizer(split_text, return_offsets_mapping=True,is_split_into_words=True, padding=True, truncation=True)



def encode_intents(intents, mapping):
    #pytorch so no need to one hot encode
    labels = [mapping[intent] for intent in intents]
    #print(labels)
    return labels

train_intent_labels =  encode_intents(event_tags, intent2id)


class EventDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, intent_labels):
        self.encodings = encodings
        self.intent_labels = intent_labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['intent_labels'] = torch.tensor(self.intent_labels[idx])
        return item

    def __len__(self):
        return len(self.intent_labels)

train_encodings.pop("offset_mapping") # we don't want to pass this to the model
train_dataset = EventDataset(train_encodings, train_intent_labels)

dropout = config['bert_model']['dropout']
dropout = float(dropout)

num_intent_labels = len(intent_vocab)

model = ParserModel(model_name_or_path='bert-base-uncased',
                    dropout=dropout,
                    num_intent_labels=num_intent_labels,
                   )

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

model.to(device)
model.train()


bs = config['bert_model']['batch_size']
bs = int(bs)
train_loader = DataLoader(train_dataset, batch_size=bs, shuffle=True)

lra = config['bert_model']['lr']
lra = float(lra)
print(lra)
optim = AdamW(model.parameters(), lr=lra)

# Number of training epochs (authors recommend between 2 and 4)
# input_ids: torch.tensor,
#                 token_type_ids: torch.tensor,
#                 slot_labels: torch.tensor = None

epochs = config['bert_model']['epochs']
epochs = int(epochs)
for epoch in tqdm(range(epochs)):
    for batch in train_loader:
        optim.zero_grad()
        input_ids = batch['input_ids'].to(device)
        token_type_ids = batch['token_type_ids'].to(device)
        intent_labels = batch['intent_labels'].to(device)
        outputs = model(input_ids=input_ids,
                        token_type_ids=token_type_ids, 
                        intent_label=intent_labels)
        intent_loss = outputs[1]
        print(intent_loss)
        intent_loss.backward() #need to retain_graph  when working with multiple losses
        optim.step()
#print(model.eval())
#run predictions on new dataset currently running on training set

model_name = config['bert_model']['model_name']
torch.save(model.state_dict(), model_name)



#print(predictions)
#print(event_tags)
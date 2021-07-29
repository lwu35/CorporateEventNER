import torch
from torch import nn
from torch.nn import CrossEntropyLoss
from torch.nn import Dropout
from torch.utils.data import DataLoader
from transformers import BertModel, BertTokenizerFast
import numpy as np


np.random.seed(123)
torch.manual_seed(123)
torch.cuda.manual_seed(123)


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
        self.intent_classifier = nn.Linear(
            self.bert_model.config.hidden_size, num_intent_labels)
        # print(num_intent_labels)

    def forward(self,
                input_ids: torch.tensor,
                token_type_ids: torch.tensor,
                intent_label: torch.tensor = None
                ):

        last_hidden_states, pooler_output = self.bert_model(input_ids=input_ids,
                                                            token_type_ids=token_type_ids,
                                                            return_dict=False)

        # print(self.bert_model.config)
        # print(last_hidden_states)
        # sigmoid
        # print(last_hidden_states.size())
        intent_logits = self.intent_classifier(self.dropout(pooler_output))
        # print(intent_logits.size()) # 7 close to 0 or 1, if not apply sigmoid
        loss_fct = CrossEntropyLoss()  # BCE multiclass
        # Compute losses if labels provided
        # print("...")
        intent_loss = loss_fct(
            intent_logits.view(-1, self.num_intent_labels), intent_label.type(torch.long))

        return intent_logits, intent_loss


def encode_intents(intents, mapping):
    # pytorch so no need to one hot encode
    labels = [mapping[intent] for intent in intents]
    # print(labels)
    return labels


class EventDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, intent_labels):
        self.encodings = encodings
        self.intent_labels = intent_labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx])
                for key, val in self.encodings.items()}
        item['intent_labels'] = torch.tensor(self.intent_labels[idx])
        return item

    def __len__(self):
        return len(self.intent_labels)


def bert_init(dropout_value, saved_model):

    intent_vocab = ['Sales Results', 'Guidance', 'Shareholder Meeting', 'None/Other',
                    'Earnings Release', 'Merger/Acquisition', 'Conference', 'Earnings Call']

    # 1. For mapping slots between ints and string

    intent2id = {intent: id for id, intent in enumerate(intent_vocab)}
    id2intent = {id: intent for intent, id in intent2id.items()}

    # 2. Tokenize utterances for BERT to accept
    # Load pre-trained model tokenzier (vocab)
    tokenizer = BertTokenizerFast.from_pretrained(
        'bert-base-uncased', do_lower_case=True)

    dropout = dropout_value
    num_intent_labels = len(intent_vocab)

    model = ParserModel(model_name_or_path='bert-base-uncased',
                        dropout=dropout,
                        num_intent_labels=num_intent_labels,
                        )

    model.load_state_dict(torch.load(saved_model))

    return model, intent2id, id2intent, tokenizer


def bert_predict(raw_event_text, model, intent2id, id2intent, tokenizer):
    raw_event_text = [raw_event_text]

    eval_intent_labels = encode_intents(['None/Other'], intent2id)

    eval_encodings = tokenizer(raw_event_text, return_offsets_mapping=True,
                               is_split_into_words=False, padding=True, truncation=True)

    eval_dataset = EventDataset(eval_encodings, eval_intent_labels)

    model.eval()
    val_loader = DataLoader(eval_dataset, batch_size=1, shuffle=False)

    for batch in val_loader:
        input_ids = batch['input_ids']
        token_type_ids = batch['token_type_ids']
        intent_labels = batch['intent_labels']
        outputs = model(input_ids=input_ids,
                        token_type_ids=token_type_ids,
                        intent_label=intent_labels)
        intent_logits = outputs[0]
        intent_loss = outputs[1]

        # intent
        intent_probability_value = torch.softmax(intent_logits, dim=1)
        intent_idxs = torch.argmax(intent_probability_value, dim=1)
        #true = [id2tag[id.item()] for id in labels[0]]
        intent_prediction = [id2intent[id.item()] for id in intent_idxs]
        return intent_prediction[0]

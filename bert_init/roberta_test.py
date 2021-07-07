import torch
from torch import nn
from torch.nn import CrossEntropyLoss
from torch.nn import Dropout
from torch.utils.data import DataLoader
from transformers import AdamW
from transformers import BertModel, BertTokenizer, BertTokenizerFast, DistilBertTokenizer, DistilBertModel, RobertaModel, RobertaTokenizer, RobertaTokenizerFast
import pandas as pd
import numpy as np
import csv
import os
import time
from tqdm import tqdm



class ParserModel(torch.nn.Module):
    def __init__(self,
                 model_name_or_path: str,
                 dropout: float,
                 num_intent_labels: int):
        super(ParserModel, self).__init__()
        self.bert_model = RobertaModel.from_pretrained(model_name_or_path)
        self.dropout = Dropout(dropout)
        self.num_intent_labels = num_intent_labels
        self.intent_classifier = nn.Linear(self.bert_model.config.hidden_size, num_intent_labels)

    def forward(self,
                input_ids: torch.tensor,
                attention_mask: torch.tensor,
                token_type_ids: torch.tensor,
                intent_label: torch.tensor = None
                ):
      
        last_hidden_states, pooler_output = self.bert_model(input_ids=input_ids,
                                  attention_mask=attention_mask,
                                  token_type_ids=token_type_ids,
                                   return_dict=False)
        
        #print(self.bert_model.config)


        intent_logits = self.intent_classifier(self.dropout(pooler_output))

        loss_fct = CrossEntropyLoss()
        # Compute losses if labels provided

        intent_loss = loss_fct(intent_logits.view(-1, self.num_intent_labels), intent_label.type(torch.long))

        return intent_logits, intent_loss


# slot_vocab = ['O',
#  'PAD',
#  'ORG',
#  'F_Y',
#  'F_P',
#  'Earnings_R',
#  'Earnings_C',
#  'S_Meeting',
#  'Sales_R',
#  'Guidance',
#  'Conference',
#  'Merger/A',
#  'Date',
#  'Time',
#  'TimeZ',
#  'Lang',
#  'PhoneN',
#  'WebcastURL',
#  'EOS']

# event_text = [['2021','Astronics','Corporation','Annual','Meeting','of','Shareholders','May','25','2021','10:00am','EDT','Orlando','Florida'],
#              ['Fourth','Quarter','2020','Earnings','FEB','26','2021','AT','8:30','AM','EST','https://edge.media-server.com/mmc/p/6h793499']]

event_tags = ['Shareholder Meeting','None','Earnings Release','Conference','Conference','Earnings Call','Stockholder Meeting','Conference','Conference','Shareholder Meeting',
'Shareholder Meeting','Conference','Earnings Call','Earnings Call','Earnings Call','Earnings Release','Conference','Earnings Call','Earnings Release','Earnings Call','Earnings Release',
'Earnings Release','Earnings Call','Earnings Release','Earnings Release','Shareholder Meeting','Earnings Release','Earnings Release','Earnings Call','Earnings Call','Earnings Call',
'Earnings Release','Earnings Call','Earnings Call','None','Earnings Call','Earnings Release','Conference','Earnings Call','Earnings Release','Shareholder Meeting','Earnings Release','Conference',
'Earnings Call','Earnings Call','Earnings Call','Merger/Acquisition','Earnings Call','Earnings Call','Earnings Call','Earnings Call','Earnings Release']


raw_event_text = [["2021 Astronics Corporation Annual Meeting of Shareholders May 25, 2021 • 10:00am EDT Orlando, Florida"],
["Jan 26, 2021 Our Heritage"],
["Fourth Quarter 2020 Earnings Feb 26, 2021 at 8:30 AM EST https://edge.media-server.com/mmc/p/6h793499"],
["Jun 3, 2021 at 10:00 AM CDT Bernstein’s 2021 Strategic Decisions Conference Add to Outlook Add to Google Calendar"],
["MAY 19, 2021 5:00PM EDTSutro Biopharma Announces Additional Data for Dose-Escalation Phase 1 Study of STRO-002 to be Presented at ASCO 2021"],
["May 10, 2021 5:00 PM ET Switch Inc. First Quarter 2021 Earnings Conference Call https://services.choruscall.com/links/swch210510.html"],
["MAY 18, 2021 • 9:00AM ET 2021 Annual Meeting of Stockholders Virtual Meeting Webcast Proxy Statement https://computershare.lumiagm.com/?fromUrl=272940211"],
["May 24, 2021 2:45 PM ET J.P. Morgan 49th Annual Global Technology, Media and Communications Conference https://jpmorgan.metameetings.net/events/tmc21/sessions/37824-juniper-networks-inc/webcast?gpu_only=true&kiosk=true"],
["Cowen 49th Annual Technology Media & Telecom Conference June 1, 2021 09:10 – 9:40 am EDT https://wsw.com/webcast/cowen90/crnt/1966227"],
["Annual Meeting of Shareholders May 7, 2021 • 11:00am ET Virtual Meeting https://viewproxy.com/tonixpharma/2021/VM/"],
["The PNC Financial Services Group 2021 Annual Meeting of Shareholders Tuesday, April 27, 2021 11:00 am EDT"],
["Apr 12, 2021 at 8:45 AM EDT Needham Virtual Healthcare Conference https://event.webcasts.com/starthere.jsp?ei=1458098&tp_key=969aca0df4"],
["03/12/2021 10:00 AM ET Bimini Capital Management Fourth Quarter 2020 Earnings Call"],
["Thursday, April 29, 2021 11:00am - 12:00pm CDT Listen to the Webcast 1Q 2021 Continental Resources, Inc. Earnings Conference Call More"],
["Q3 Fiscal 2021 Earnings Release & Conference Call Webcast Click Here May 03, 2021 09:30 AM ET"],
["May 10, 2021 at 4:30 PM EDT Arcturus Therapeutics to Report First Quarter 2021 Financial Results and Provide Corporate Update on May 10, 2021"],
["5/12/2021 Open Lending Bear and Bull Debates Conference Call"],
["May 6, 2021 at 5:00 PM EDT PDF Solutions, Inc. First Quarter Earnings Release Results Call View Webcast"],
["2021	3rd Quarter	 pdf 2021 Q3 Earnings Release	Listen to Q3FY2021 Webcast View the Presentation Slides View Transcript"],
["Cnova’s 1st Quarter 2021 Financial Results Conference Call & Webcast 6 May 2021"],
["2021	4th Quarter	 pdf 2021 Q4 Earnings Release"],
["Transcat 2021 3rd quarter earnings release"],
["Collegium Pharmaceutical 2021 Q1 earnings call 05/06/2021 4:30 PM EDT"],
["Itron 2021 Q1 earnings release 05/03/2021 10:00 AM EDT"],
["eplus 2020 Q4 earnings release 02/03/2021 4:30 PM Eastern Time https://event.on24.com/wcc/r/2929350/375079A13DB8E9A35EA0D08E7B32AC02"],
["Berkshire Hills Bancorp shareholder meeting 05/20/2021"],
["Whitestone Reit 2020 Q4 earnings release 02/24/2021"],
["BBVA USA Bancshares 2021 Q1 earnings release 04/30/2021 8:30 AM CDT"],
["BrightView 2021 Q2 earnings call 05/06/2021 10:00 AM EST https://event.on24.com/wcc/r/3080115/0C88CA80C39716461742284AE9B1087F"],
["ArcBest 2021 Q1 earnings call 05/04/2021 9:30 AM EDT 800 682-8539 https://event.webcasts.com/starthere.jsp?ei=1447325&tp_key=5e6751b165"],
["Oasis Midstream 2021 Q1 earnings call may 06 2021 12:00 PM CDT https://www.webcaster4.com/Webcast/Page/1777/41033"],
["Zynex 2020 Q4 + Y earnings release 02/25/2021 2:15 PM MST https://www.webcaster4.com/Webcast/Page/1487/40106"],
["05.27.21 04:45 PM EDT	Q1 2022 Hess Earnings Conference Call"],
["Bernstein Fireside Chat: Dorothea von Boxberg, CEO, Lufthansa Cargo Tuesday, May 18, 2021 10:00AM EDT | 3:00PM BST | 10:00PM HKT"],
["Electronic Arts Q4 earnings call 05/11/2021 02:00 PM PT 866 324-3683 https://event.on24.com/wcc/r/3082295/44574BD8DABA0634EBAFFF035D3C8A3E"],
["SB Financial Group 2020 Y earnings release 03/11/2021"],
["Guess 2021 Q4 Earnings Calls 03/31/2021 04:45 PM EST https://edge.media-server.com/mmc/p/tg6sh5s5"],
["7th Annual Communications Infrastructure Summit BOULDER, CO / VIRTUAL |AUG 09–12, 2021"],
["Q1 2021 Aon plc Earnings Conference Call April 30, 2021 07:30 AM CST"],
["3/11/2021 2020 Annual Report"],
["Varian Investor Day 2019 Friday, November 15, 2019 Listen to the Webcast"],
["May 5, 2021 Q121 Earnings Press Release"],
["March 17, 2021 1:10 PM EDT	Oppenheimer 31st Annual Healthcare Conference"],
["Misonix 2021 Q3 Earnings Calls 05/06/2021 4:30PM EST https://edge.media-server.com/mmc/p/c8ptybs2"],
["Q1 2021 Lantheus Holdings, Inc. Earnings Conference Call Tuesday, May 4, 2021 at 8:00 AM EDT"],
["Adaptive Biotechnologies First Quarter Financial Results May 5, 2021 at 4:30 PM EDT"],
["efi + sirus capital group acquisition"],
["Friday, April 30, 2021 9:00 AM ET Q1 Earnings Conference Call"],
["May 4, 2021 4:30 PM EDT Pulmonx Q1 2021 Earnings Conference Call Click here for webcast"],
["Q1 2021 Summit Hotel Properties Earnings Conference Call Wednesday, May 5, 2021 at 9:00 AM ET/8:00 AM CT Participant Toll-Free Dial-In Number: (877) 930-8101 Conference ID: 3758235"],
["THURSDAY, APRIL 29, 2021 AT 8:30 AM ET Navios Maritime Partners First Quarter 2021 Earnings Conference Call Webcast Click Here for Webcast"],
["May 5, 2021 at 10:30 AM EDT Avista Corporation Q1 2021 Earnings Conference Call Click here for webcast"],
["May 06, 2021 Alleghany Corporation 2021 First Quarter Results"]]


# 1. For mapping slots between ints and string
intent2id = {intent:id for id,intent in enumerate(event_tags)}
id2intent = {id:intent for intent,id in intent2id.items()}


# 2. Tokenize utterances for BERT to accept
# Load pre-trained model tokenzier (vocab)
tokenizer = RobertaTokenizerFast.from_pretrained('roberta-base', do_lower_case=True, add_prefix_space=True)


# 4. pads to longest sequence, truncates to maximum allowed length by model, 
# Gives encodings, token type_ids -> https://huggingface.co/transformers/glossary.html#token-type-ids and attention_masks
# and offset_mappings
train_encodings = tokenizer(raw_event_text, return_offsets_mapping=True,is_split_into_words=True, padding=True, truncation=True)

def encode_intents(intents, mapping):
    labels = [mapping[intent] for intent in intents]
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

dropout = 0.2

num_intent_labels = len(event_tags)

model = ParserModel(model_name_or_path='roberta-base',
                    dropout=dropout,
                    num_intent_labels=num_intent_labels,
                   )

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

model.to(device)
model.train()

train_loader = DataLoader(train_dataset, batch_size=4, shuffle=True)

optim = AdamW(model.parameters(), lr=5e-5)

# Number of training epochs (authors recommend between 2 and 4)
# input_ids: torch.tensor,
#                 attention_mask: torch.tensor,
#                 token_type_ids: torch.tensor,
#                 slot_labels: torch.tensor = None
for epoch in tqdm(range(3)):
    for batch in train_loader:
        optim.zero_grad()
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        token_type_ids = None
        intent_labels = batch['intent_labels'].to(device)
        outputs = model(input_ids=input_ids, 
                        attention_mask=attention_mask,
                        token_type_ids=token_type_ids, 
                        intent_label=intent_labels,)
        intent_loss = outputs[1]
        intent_loss.backward(retain_graph=True) #need to retain_graph  when working with multiple losses
        optim.step()

#evluate on data currently same as training data, but will change
model.eval()
acc = 0
predictions = []
def evaluate(model):
  model.eval()
  model.to(device)
  val_loader = DataLoader(train_dataset, batch_size=1, shuffle=False)
  losses = []
  for batch in val_loader:
    input_ids = batch['input_ids'].to(device)
    attention_mask = batch['attention_mask'].to(device)
    token_type_ids = None
    intent_labels = batch['intent_labels'].to(device)
    outputs = model(input_ids=input_ids, 
                    attention_mask=attention_mask,
                    token_type_ids=token_type_ids, 
                    intent_label=intent_labels)
    intent_logits = outputs[0]
    intent_loss = outputs[1]
    # intent
    intent_probability_value = torch.softmax(intent_logits,dim=1)
    intent_idxs = torch.argmax(intent_probability_value,dim=1)
    #true = [id2tag[id.item()] for id in labels[0]]
    intent_prediction = [id2intent[id.item()] for id in intent_idxs]
    predictions.append(intent_prediction)
    with open('predictions.csv', 'w+', newline ='') as f:
        write = csv.writer(f)
        write.writerows(predictions)    
    print(intent_prediction)
    # print(slot_loss) 

evaluate(model)


print(predictions)
print(event_tags)
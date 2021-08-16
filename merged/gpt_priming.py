from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from happytransformer import HappyGeneration
from fuzzywuzzy import fuzz
import configparser

# Input: text content (string)
# Output: event tag
def gpt_predict(text):
    gpt_type = config['gpt_model']['model']
    happy_gen = HappyGeneration("GPT-NEO", gpt_type)
    tags_vocab = ['None/Other', 'Earnings Release', 'Earnings Call', 'Shareholder Meeting', 'Sales Results', 'Conference']
    
    test1 = ''' Text: 2021 ACOG Annual Meeting April 30 – May 2, 2021
    Type:None/Other

    Text: "NO EVENTS FOUND"
    Type:None/Other

    Text: 03/30/20	 RH Reports Record Fiscal 2019 Results
    Type:None/Othe

    Text: 09/09/20	 RH Reports Record Second Quarter 2020 Results
    Type:None/Other

    Text: July 19, 2021	 China Internet– are we there yet? Expert views on data security (US).. New York
    Type:None/Other

    Text: 2nd Quarter  2021 Q2 Earnings Release October 27, 2020
    Type:Earnings Release

    Text: 02/22/18 CVR Partners Q4 2017 Earnings Report
    Type:Earnings Release

    Text: Columbia Sportswear 1st Quarter 2021 Earnings Release Conference Call Apr 29, 2021 ? 5:00 pm EDT Earnings ReleasePDFHTML AUDIOEarnings Webcast CFO Commentary and Financial Review
    Type:Earnings Release

    Text: Adaptive Biotechnologies Second Quarter Financial Results Aug 4, 2021 at 4:30 PM EDT Listen to webcast
    Type:Earnings Release

    Text: Tuesday, July 20, 2021 8:30 AM ET Second Quarter 2021 Results
    Type:Earnings Release

    Text: CORPORATE UPDATE CONFERENCE CALL JANUARY 7, 2021 ? 4:15 PM
    Type:Earnings Call

    Text: May 5, 2021 at 10:30 AM EDT Avista Corporation Q1 2021 Earnings Conference Call Click here for webcast
    Type:Earnings Call

    Text: Wednesday, May 5, 2021 at 5:00 PM EDT Q1 2021 Nu Skin Enterprises Earnings Conference Call
    Type:Earnings Call

    Text: Q4 2020 Collegium Pharmaceutical Inc Earnings Conference Call Feb 25, 2021 at 4:30 PM EST Click Here for Webcast
    Type:Earnings Call

    Text: Q4 2020 H.B. FULLER COMPANY EARNINGS CONFERENCE CALL JANUARY 26, 2021 10:30 AM ET
    Type:Earnings Call

    Text: 2021 Virtual Annual Shareholder Meeting  Thursday, April 29, 2021  10:00am EDT
    Type:Shareholder Meeting

    Text: The PNC Financial Services Group 2021 Annual Meeting of Shareholders Tuesday, April 27, 2021 11:00 am EDT
    Type:Shareholder Meeting

    Text: MAY 18, 2021 ? 9:00AM ET 2021 Annual Meeting of Stockholders
    Type:Shareholder Meeting

    Text: Special Meeting of Stockholders Jun 11, 2021 at 8:30 AM EDT Shareholder control number required to join Listen to Webcast
    Type:Shareholder Meeting

    Text: 06/02/2021 09:00 AM PT Cerus Corporation's Annual Meeting of Stockholders Webcast (opens in new window)
    Type:Shareholder Meeting

    Text: Chiasma Q4 2020 Financial Results Call Mar 4, 2021 at 5:00 PM EST Listen to webcast
    Type:Sales Results

    Text: MAY 7, 2020 04:30 PM ET First Solar, Inc. First Quarter 2020 Financial Results Webcast(Opens In New Window)
    Type:Sales Results

    Text: Wednesday, August 4, 2021 JEFFERIES VIRTUAL INDUSTRIALS CONFERENCE
    Type:Conference

    Text: Universal Display Corporation's Fourth Quarter and Fiscal Year 2020 Teleconference February 18, 2021 05:00 PM ET
    Type:Conference

    Text: March 3, 2021 at 8:40 AM PST Seer, Inc. at Cowen 41st Annual Healthcare Conference
    Type:Conference

    Text: Digitalization in Energy Virtual Conference October 6, 2021 Streaming On-Demand
    Type:Conference

    Text: Stifel 2021 Virtual Jaws & Paws Conference June 2, 2021 at 9:00 AM EDT Listen to Webcast
    Type:Conference
    
     '''
    
    question = "Text: " + text + "\n" + 'Type:'
    top_k_sampling_settings = GENSettings(no_repeat_ngram_size=int(config['gpt_model']['no_repeat_ngram_size']),
                                          do_sample=config['gpt_model']['do_sample'], early_stopping=config['gpt_model']['early_stopping'], top_k=int(config['gpt_model']['top_k']), temperature=float(config['gpt_model']['temperature']))
    result = happy_gen.generate_text(
        test1 + question, args=top_k_sampling_settings)

    max_ratio = 10
    max_tag = "None/Other"
    for j in tags_vocab:
        ratio = fuzz.ratio(j, result.text.splitlines()[0])

        if ratio > max_ratio:
            max_ratio = ratio
            max_tag = j
    # print(max_tag + '\n')

    return max_tag


test1 = ''' Text: 2021 ACOG Annual Meeting April 30 – May 2, 2021
Type:None/Other

Text: "NO EVENTS FOUND"
Type:None/Other

Text: 03/30/20	 RH Reports Record Fiscal 2019 Results
Type:None/Othe

Text: 09/09/20	 RH Reports Record Second Quarter 2020 Results
Type:None/Other

Text: July 19, 2021	 China Internet– are we there yet? Expert views on data security (US).. New York
Type:None/Other

Text: 2nd Quarter  2021 Q2 Earnings Release October 27, 2020
Type:Earnings Release

Text: 02/22/18 CVR Partners Q4 2017 Earnings Report
Type:Earnings Release

Text: Columbia Sportswear 1st Quarter 2021 Earnings Release Conference Call Apr 29, 2021 ? 5:00 pm EDT Earnings ReleasePDFHTML AUDIOEarnings Webcast CFO Commentary and Financial Review
Type:Earnings Release

Text: Adaptive Biotechnologies Second Quarter Financial Results Aug 4, 2021 at 4:30 PM EDT Listen to webcast
Type:Earnings Release

Text: Tuesday, July 20, 2021 8:30 AM ET Second Quarter 2021 Results
Type:Earnings Release

Text: CORPORATE UPDATE CONFERENCE CALL JANUARY 7, 2021 ? 4:15 PM
Type:Earnings Call

Text: May 5, 2021 at 10:30 AM EDT Avista Corporation Q1 2021 Earnings Conference Call Click here for webcast
Type:Earnings Call

Text: Wednesday, May 5, 2021 at 5:00 PM EDT Q1 2021 Nu Skin Enterprises Earnings Conference Call
Type:Earnings Call

Text: Q4 2020 Collegium Pharmaceutical Inc Earnings Conference Call Feb 25, 2021 at 4:30 PM EST Click Here for Webcast
Type:Earnings Call

Text: Q4 2020 H.B. FULLER COMPANY EARNINGS CONFERENCE CALL JANUARY 26, 2021 10:30 AM ET
Type:Earnings Call

Text: 2021 Virtual Annual Shareholder Meeting  Thursday, April 29, 2021  10:00am EDT
Type:Shareholder Meeting

Text: The PNC Financial Services Group 2021 Annual Meeting of Shareholders Tuesday, April 27, 2021 11:00 am EDT
Type:Shareholder Meeting

Text: MAY 18, 2021 ? 9:00AM ET 2021 Annual Meeting of Stockholders
Type:Shareholder Meeting

Text: Special Meeting of Stockholders Jun 11, 2021 at 8:30 AM EDT Shareholder control number required to join Listen to Webcast
Type:Shareholder Meeting

Text: 06/02/2021 09:00 AM PT Cerus Corporation's Annual Meeting of Stockholders Webcast (opens in new window)
Type:Shareholder Meeting

Text: Chiasma Q4 2020 Financial Results Call Mar 4, 2021 at 5:00 PM EST Listen to webcast
Type:Sales Results

Text: MAY 7, 2020 04:30 PM ET First Solar, Inc. First Quarter 2020 Financial Results Webcast(Opens In New Window)
Type:Sales Results

Text: Wednesday, August 4, 2021 JEFFERIES VIRTUAL INDUSTRIALS CONFERENCE
Type:Conference

Text: Universal Display Corporation's Fourth Quarter and Fiscal Year 2020 Teleconference February 18, 2021 05:00 PM ET
Type:Conference

Text: March 3, 2021 at 8:40 AM PST Seer, Inc. at Cowen 41st Annual Healthcare Conference
Type:Conference

Text: Digitalization in Energy Virtual Conference October 6, 2021 Streaming On-Demand
Type:Conference

Text: Stifel 2021 Virtual Jaws & Paws Conference June 2, 2021 at 9:00 AM EDT Listen to Webcast
Type:Conference
 '''

gpt_type = config['gpt_model']['model']
happy_gen = HappyGeneration("GPT-NEO", gpt_type)
tags_vocab = ['None/Other', 'Earnings Release', 'Earnings Call', 'Shareholder Meeting', 'Sales Results', 'Conference']

with open('dev.txt', 'r', encoding='utf-8') as f:
        raw_event_text = []
        lines = f.readlines()
        for i in lines:
            raw_event_text.append([i.replace('\n', '')])
            

tags = []
for i in range(len(raw_event_text)):
    test1 = "Text: " + raw_event_text[i][0] + "\n"
    question = 'Type:'
    top_k_sampling_settings = GENSettings(no_repeat_ngram_size=2,
                                          do_sample=True, early_stopping=False, top_k=5, temperature=0.7)
    result = happy_gen.generate_text(
        test1 + question, args=top_k_sampling_settings)
        
    max_ratio = 10
    max_tag = "None/Other"
    for j in tags_vocab:
        ratio = fuzz.ratio(j, result.text.splitlines()[0])

        if ratio > max_ratio:
            max_ratio = ratio
            max_tag = j
    tags.append(max_tag + '\n')
# print(tags)
pred_types = tags
with open('dev_tags.txt', 'r', encoding='utf-8') as f:
    true_tpyes = []
    lines = f.readlines()
    for i in lines:
        true_tpyes.append([i])
count = 0
for i in range(len(pred_types)):
  if pred_types[i] == true_tpyes[i][0]:
    count = count + 1

        
print("Accuracy:{:.2f}%".format(count/200*100))

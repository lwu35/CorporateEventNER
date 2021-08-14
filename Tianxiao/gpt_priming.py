from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from happytransformer import HappyGeneration
from fuzzywuzzy import fuzz
happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")

test1 = ''' Text: Astronics 2021 y Shareholder Meeting 05-25-2021 10:00 am EDT 
Type: Shareholder Meeting

Text: Full house resorts 2021 y Shareholder Meeting 05-19-2021 10:00 am PDT https://events.Q4inc.com/vsm/FLL/2021 
Type: Shareholder Meeting

Text: Extended Stay America 2020 Q4 Earnings Call 02-26-2021 8:30 am EST https://edge.media-server.com/mmc/p/6h793499 
Type: Earnings Call

Text: Kimberly-Clark 2021 y Shareholder Meeting 04-29-2021 9:00 am CDT https://computershare.lumiagm.com/?fromUrl=277152589 
Type: Shareholder Meeting

Text: Sutro Biopharma Other 05-20-2021 2:40 pm EDT 
Type: Other

Text: Switch 2021 Q1 Earnings Call 05-10-2021 5:00 pm ET https://services.choruscall.com/links/swch210510.html 
Type: Earnings Call

Text: Infusystem 2021 y Stockholders meetings 05-18-2021 9:00 am ET https://computershare.lumiagm.com/?fromUrl=272940211 
Type: Shareholder Meeting

Text: Juniper Networks 2021 Q1 Earnings Call 04-27-2021 2:00 pm PT https://event.on24.com/wcc/r/3079918/E0E8DFD021CDFF89394C7A147656AD2E 
Type: Earnings Call

Text: CERAGON y Conference 05-19-2021 8:45 am ET https://www.ceragon.com/investors/webcasts 
Type: Conference

Text: Tonix Pharmaceuticals y Shareholder Meeting 05-07-2021 11:00 am ET https://viewproxy.com/tonixpharma/2021/VM/ 
Type: Shareholder Meeting

Text: PNC financial services group 2021 y Shareholder Meeting 04-27-2021 11:00 am EDT 
Type: Shareholder Meeting

Text: angiodynamics Conference 04-12-2021 8:45 am EDT https://wsw.com/webcast/needham107/ango/2233330 
Type: Conference 

Text: Bimini capital management 2020 Q4 Earnings Call 03-12-2021 10:00 am ET https://event.on24.com/wcc/r/3044623/44A10F5CBA50FE24174070B2D837F793 
Type: Earnings Call 

Text: Continental Resources Q1 2021 Earnings Call 04-29-2021 11:00am CDT https://www.webcaster4.com/Webcast/Page/2083/40546 
Type: Earnings Call 

Text: estee lauder companies 2021 Q3 Earnings Call 05-03-2021 9:30 AM ET https://services.choruscall.com/links/el210503xk8KQ58x.html 
Type: Earnings Call 

Text: arcturus therapeutics 2021 Q1 Earnings Release 05-10-2021 4:30pm EDT http://public.viavid.com/player/index.php?id=144682 
Type: Earnings Release 

Text: Stephens Conference 05-12-2021 
Type: Conference 

Text: PDF Solutions Q1 earnings call 05/06/2021 5:00 PM EDT https://edge.media-server.com/mmc/p/ziup3tnz 
Type: Earnings Call 

Text: Transcat 2021 3rd quarter Earnings Release http://public.viavid.com/index.php?id=142934 
Type: Earnings Release 

Text: Collegium Pharmaceutical 2021 Q1 earnings call 05/06/2021 4:30 PM EDT 
Type: Earnings Call 

Text: Itron 2021 Q1 Earnings Release 05/03/2021 10:00 AM EDT https://edge.media-server.com/mmc/p/fv39vg3s 
Type: Earnings Release 

Text: eplus 2020 Q4 Earnings Release 02/03/2021 4:30 PM Eastern Time https://event.on24.com/wcc/r/2929350/375079A13DB8E9A35EA0D08E7B32AC02 
Type: Earnings Release 

Text: Berkshire Hills Bancorp shareholder meeting 05/20/2021 
Type: Shareholder Meeting 

Text: Whitestone Reit 2020 Q4 Earnings Release 02/24/2021 
Type: Earnings Release 

Text: BBVA USA Bancshares 2021 Q1 Earnings Release 04/30/2021 8:30 AM CDT 
Type: Earnings Release 

Text: BrightView 2021 Q2 earnings call 05/06/2021 10:00 AM EST https://event.on24.com/wcc/r/3080115/0C88CA80C39716461742284AE9B1087F 
Type: Earnings Call 

Text: ArcBest 2021 Q1 earnings call 05/04/2021 9:30 AM EDT 800 682-8539 https://event.webcasts.com/starthere.jsp?ei=1447325&tp_key=5e6751b165 
Type: Earnings Call 

Text: Oasis Midstream 2021 Q1 earnings call may 06 2021 12:00 PM CDT https://www.webcaster4.com/Webcast/Page/1777/41033 
Type: Earnings Call 

Text: Zynex 2020 Q4 + Y Earnings Release 02/25/2021 2:15 PM MST https://www.webcaster4.com/Webcast/Page/1487/40106 
Type: Earnings Release 

Text: Hess Corporation 2021 Q1 earnings call 04/28/2021 10:00 AM EDT 
Type: Earnings Call 

Text: Bernstein Other 05/18/2021 10:00 AM EDT 
Type: Other 

Text: Electronic Arts Q4 earnings call 05/11/2021 02:00 PM PT 866 324-3683 https://event.on24.com/wcc/r/3082295/44574BD8DABA0634EBAFFF035D3C8A3E 
Type: Earnings Call 

Text: SB Financial Group 2020 Y Earnings Release 03/11/2021 
Type: Earnings Release 

Text: The Philadelphia Inquirer 2021 Other 4/12/2021 8:08 AM https://www.businesswire.com/news/home/20210412005289/en/ 
Type: Other 

Text: Guess 2021 Q4 Earnings Call 03/31/2021 04:45 PM EST https://edge.media-server.com/mmc/p/tg6sh5s5 
Type: Earnings Call 

Text: Cowen Other 08/09/2021 
Type: Other 

Text: Aon 2021 Q1 Earnings Call 04/30/2021 07:30AM CST https://event.on24.com/wcc/r/3079953/6F8A69D109C1B6F1C88B816B82F5F2D7 
Type: Earnings Call 

Text: Varian 2019 Other 11/15/2019 https://event.webcasts.com/starthere.jsp?ei=1272740&tp_key=89d69aebee 
Type: Other 

Text: fleetcor 2021 Q1 Earnings Release 05-05-2021 
Type: Earnings Release 

Text: Oppenheimer 2021 Conference 03/17/2021 1:10PM EST https://wsw.com/webcast/oppenheimer9/iova/2720795 
Type: Conference 

 
 '''

tags_vocab = ['Other', 'Earnings Release', 'Earnings Call', 'Shareholder Meeting', 'Sales Results', 'Guidance', 'Conference', 'Merger/Acquisition']

with open('gpt_test.txt', 'r', encoding='utf-8') as f:
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
    max_tag = "Other"
    for j in tags_vocab:
        ratio = fuzz.ratio(j, result.text.splitlines()[0])

        if ratio > max_ratio:
            max_ratio = ratio
            max_tag = j
    tags.append(max_tag + '\n')
# print(tags)
pred_types = tags
with open('dev_eval.txt', 'r', encoding='utf-8') as f:
    true_tpyes = []
    lines = f.readlines()
    for i in lines:
        true_tpyes.append([i])
count = 0
for i in range(len(pred_types)):
  if pred_types[i] == true_tpyes[i][0]:
    count = count + 1

        
print("Accuracy:{:.2f}%".format(count/200*100))

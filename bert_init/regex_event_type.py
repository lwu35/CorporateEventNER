import csv
import regex

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

raw_event_text_eval = [["Jul 23, 2021 at 9:00 AM CDT Second Quarter 2021 Earnings"],
["Oct 25, 2021 at 9:00 AM CDT Third Quarter 2021 Earnings"],
["Jun 3, 2021 at 10:00 AM CDT Bernstein’s 2021 Strategic Decisions Conference Click here for webcast Printable Slides"],
["Apr 29, 2021 at 9:00 AM CDT 2021 Annual Meeting of Stockholders Click here for live webcast of Annual Meeting Event Password: KMB2021 Inspection of Stockholder List"],
["Apr 23, 2021 at 9:00 AM CDT First Quarter 2021 Earnings Click here for webcast KMB 1Q 2021 Earnings Press Release KMB 1Q 2021 Prepared Management Remarks"],
["June 15, 2021 11:55 AM ET Credit Suisse 23rd Annual Communications Conference"],
["June 09, 2021 3:20 PM ET   Stifel 2021 Cross Sector Insight Conference"],
["June 02, 2021 3:50 PM ET   Cowen 49th Annual Technology, Media & Telecom Conference"],
["June 01, 2021 3:00 PM ET   William Blair 41st Annual Growth Stock Conference"],
["May 25, 2021 RBC Capital Markets Global Datacenter, Cloud and Broadband Infrastructure Conference"],
["10:20 AM EDT Jefferies Virtual Consumer Conference Presentation Supporting Materials Jefferies Virtual Consumer Conference Presentation"],
["June 29, 2021 4:30 PM EDT Iovance Biotherapeutics Update Call"],
["June 17, 2021 2:00 PM EDT JMP Securities Life Sciences Conference"],
["June 06, 2021 12:00 PM EDT ASCO Update Call"],
["Thursday, July 29, 2021 10:00 AM ET EQC Q2 2021 Earnings Conference Call"],
["May 24, 2021 Martin Marietta Announces Acquisition of Lehigh Hanson’s West Region Business MLM Acquisition Announcement MLM Acquisition Supplemental Information"],
["May 04, 2021 11:00 AM EDT Martin Marietta Q1 2021 Earnings Conference Call Click here for webcast MLM Q1 2021 Earnings Release MLM Q1 2021 Supplemental Information"],
["Feb 25, 2021 10:30 AM EST Martin Marietta Investor Day Click here for replay 2021 Investor Day Presentation Investor Day FAQs"],
["Feb 09, 2021 11:00 AM EST Martin Marietta Q4 and Full Year 2020 Earnings Conference Call Click here for webcast MLM Q4 2020 Earnings Release MLM Q4 2020 Supplemental Information"],
["May 5, 2021Turtle Beach Investor Presentation – May 2021"],
["May 5, 2021 at 05:00 PM EDT Turtle Beach First Quarter 2021 Conference Call  Listen to Webcast Supporting Materials  Q1 Earnings Presentation"],
["Mar 4, 2021 at 05:00 PM EST Turtle Beach Fourth Quarter and Full Year 2020 Conference Call  Listen to Webcast Supporting Materials  Q4 Earnings Presentation"],
["Nov 5, 2020 at 05:00 PM EST Turtle Beach Third Quarter 2020 Conference Call  Listen to Webcast Supporting Materials  Q3 Earnings Presentation"],
["Sep 10, 2020 at 09:30 AM PDT 9th Annual Gateway Conference  Listen to Webcast"],
["May 13, 2021 Q4 2021 Haemonetics Corporation Earnings Conference Call"],
["Mar 16, 2021 Morgan Stanley Corporate Access Day Investor Presentation"],
["Stifel 2021 Virtual Cross Sector Insight Conference JUNE 10, 2021 AT 12:40 PM EDT"],
["First Quarter 2021 Earnings Call MAY 17, 2021 AT 5:00 PM EDT"],
["Fourth Quarter and Full Year 2020 Earnings Call MARCH 24, 2021 AT 5:00 PM EDT"],
["05.11.2021 3:30 PM EDT Bank of America Securities 2021 Healthcare Conference"],
["05.10.2021 1:30 PM PDT Shockwave Medical, Inc. Q1 2021 Earnings Conference Call"],
["03.30.2021 10:00 AM PDT Wells Fargo CEO Spotlight Call"],
["02.17.2021 1:30 PM PST Shockwave Medical, Inc. Q4 2020 Earnings Conference Call"],
["12.02.2020 8:30 AM EST Piper Sandler 32nd Annual Virtual Healthcare Conference"],
["May 6, 2021 at 5:00 PM EDT Corcept Therapeutics Q1 2021 Earnings Conference Call"],
["Feb 8, 2021 at 5:00 PM EST Corcept Therapeutics Q4 2020 Earnings Conference Call"],
["Nov 3, 2020 at 5:00 PM EST Corcept Therapeutics Q3 2020 Earnings Conference Call"],
["Aug 4, 2020 at 5:00 PM EDT Corcept Therapeutics Q2 2020 Earnings Conference Call"],
["Jun 2 - Jun 4, 2020 Jefferies Virtual Healthcare Conference"],
["June 30, 2021 PROS to Help Drive Hawaiian Airlines’ Revenue Growth Strategy"],
["June 2, 2021 PROS Announces Virtual Investment Conference Schedule for June 2021"],
["June 1, 2021 PROS Holdings, Inc. Announces Appointment of Leland T. Jourdan to Board of Directors"],
["May 18, 2021 PROS and Diggintravel Redefine the End-to-End Travel Experience"],
["May 11, 2021 PROS Announces Virtual Investment Conference Schedule for May 2021"],
["2019 Q3 Financial Results Conference Call Presentation November 6, 2019"],
["2019 Q2 Financial Results Conference Call Presentation August 7, 2019"],
["5/5/2021Q1 2021 Investor Presentation"],
["4/30/20212021 Annual Shareholder Meeting Audio and Presentation"],
["2/3/2021Q4 2020 Investor Presentation"],
["11/4/2020Q3 2020 Investor Presentation"],
["First Quarter 2021 Financial Results May 6, 2021 9:30am ET"],
["Q2 2021 Occidental Earnings Conference Call Wednesday, August 4, 2021 1:00 p.m. EST"],
["Jul 22, 2021  10:00 am CDT   BancorpSouth Q2 2021 Earnings Conference Call and Webcast"],
["Apr 22, 2021 BancorpSouth Q1 2021 Earnings Conference Call and Webcast"],
["Apr 12, 2021 BancorpSouth - Cadence Merger Conference Call"],
["2021 Annual Meeting of Stockholders JUN 9, 2021 • 8:30AM CDT"],
["Citi 2021 Global Energy and Utilities Virtual Conference MAY 12, 2021 • 12:50PM EDT",],
["J.P. Morgan 2020 Energy, Power & Renewables Conference JUN 16, 2020 • 3:40PM EDT"],
["2020 Annual Meeting of Stockholders JUN 10, 2020 • 8:30AM CDT"],
["2019 Annual Meeting of Stockholders JUN 5, 2019 • 8:30AM CDT"]]

split_text = []
#for sent in raw_event_text:
for sent in raw_event_text_eval:    
    split_text.append(' '.join(sent).split())

split_text = [[string.lower() for string in sublist] for sublist in split_text]

event_predictions = []
for sent in split_text:
    if 'merger' in sent or 'acquisition' in sent:
        event_predictions.append('Merger/Acquisition')
    elif ('earnings' in sent or ('financial' in sent and 'results' in sent)) and ('call' in sent or 'calls' in sent):
        event_predictions.append('Earnings Call')
    elif 'earnings' in sent or ('financial' in sent and 'results' in sent):
        event_predictions.append('Earnings Release')
    elif 'stockholders' in sent or 'shareholders' in sent or 'investor' in sent or 'shareholder' in sent:
        event_predictions.append('Shareholder Meeting')
    elif 'conference' in sent and 'earnings' not in sent or 'summit' in sent:
        event_predictions.append('Conference')
    elif 'guidance' in sent:
        event_predictions.append('Guidance')
    else:
        event_predictions.append('None/Other')

#print(event_predictions)    
file = open('predictions_eval.csv', 'w+', newline ='')
#file = open('predictions.csv', 'w+', newline ='')
with file:    
    write = csv.writer(file)
    write.writerows([c.strip() for c in r.strip(', ').split(',')]
                     for r in event_predictions)

#print(len(event_predictions))

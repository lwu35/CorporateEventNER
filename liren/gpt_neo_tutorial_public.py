from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from happytransformer import HappyGeneration


happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")
# happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")

prompt = 'html. Astronics. Investors. Careers. IR Calendar. Home. /. Investors. /. IR News & Events. /. IR Calendar. Section Navigation. IR News & Events. Press Releases. IR Calendar. Email Alerts. Upcoming Events. There are no upcoming events scheduled at this time.. Sign up here. to receive notices about upcoming events and press releases.. Past Events. UBS Global Industrials and Transportation Virtual Conference. Jun 8, 2021. .date. PDF. Presentation. .text. 2021 Astronics Corporation Annual Meeting of Shareholders. May 25, 2021 10:00am EDT. .date. Orlando, Florida. .text. Q1 2021 Astronics Earnings Conference Call. May 6, 2021 11:00am EDT. .date. PDF. HTML. Earnings Release. Audio. Earnings Webcast. PDF. Conference Call Transcript. PDF. HTML. 10-Q. Filing. XBRL. ZIP. XLS. HTML. XBRL. .text. Q4 2020 Astronics Earnings Conference Call. Feb 23, 2021 11:00am EDT. .date. A telephonic replay is available through Tuesday, March 2, 2021. To listen to the archived call, dial (412) 317-6671 and enter replay pin number 13715117.. PDF. HTML. Earnings Release. PDF. Conference Call Transcript. PDF. HTML. 10-K. Filing. XBRL. ZIP. XLS. HTML. XBRL. PDF. Annual Report. .text. View All Past Events. //container. Email Alerts. Tear Sheet. Contacts. RSS News Feed. Products & Solutions. Aircraft Data Systems. Aircraft Electrical Power Systems. Custom Design & Manufacturing. Emergency Systems. Enhanced Vision Systems. IFC Antennas and Radome Systems. Inflight Entertainment System Hardware. Instrumentation. Interiors & Structures. Lighting Systems. Seat Actuation Systems. Simulation & Training. Systems Certification. Test & Measurement. VIP IFEC & CMS Systems. View All Products. Subsidiaries. Astronics Advanced Electronic Systems. Astronics AeroSat. Astronics Ballard Technology. Astronics Connectivity Systems and Certification. Astronics Custom Control Concepts. Astronics DME. Astronics Luminescent Systems Inc. Astronics PECO Inc. Astronics PGA. Astronics Test Systems. View All Subsidiaries. FAQS. CONTACT US. SITE FEEDBACK. Sign Up for Astronics Email. Privacy Policy. |. Legal. |. Terms Of Use. 2021 Astronics Corporation. All rights reserved.. Market Data copyright 2021. QuoteMedia. . Data delayed 15 minutes unless otherwise indicated (view. delay times. for all exchanges).. =Real-Time,. =End of Day,. =Previous Day. Market Data powered by. QuoteMedia. Terms of Use. ..'
question = ' the first event is UBS Global Industrials and Transportation Virtual Conference. Jun 8, 2021.'

args = GENSettings(do_sample=False, early_stopping=False,
                   top_k=20, temperature=0.9)
result = happy_gen.generate_text(
    prompt + question, args=args)
print(result.text)

prompt = "html. Passpartu. Passpartu End. Presentations. Jan 26, 2021. Our Heritage. Mar 12, 2020. 4Q19 Earnings Call Slides. Oct 31, 2019. 3Q19 Earnings Call Slides. Aug 8, 2019. 2Q19 Earnings Call Slides. Mar 18, 2019. Macquarie Consumer Bright Ideas Conference. Dec 7, 2018. ROTH Deer Valley Corporate Access Event. Mar 13, 2018. Investor Conferences March 2018. Mar 1, 2018. Bronco Billys Expansion Renderings. Nov 22, 2017. The Case for Cripple Creek. Nov 7, 2017. Bronco Billys Expansion Highlights. Next . //container. Email Alerts. Tear Sheet. Contacts. RSS News Feed. Container End. Full Width. Contacts. 702-221-7800. fhri@fullhouseresorts.com. 1980 Festival Plaza Dr., Suite 680. Las Vegas, NV 89135. Latest News, Click. here. Stay Informed, click. here. Container End. 2021 Full House Resorts, Inc. All rights reserved.. Copyrights End. //main page."
question = ' the first event is Jan 26, 2021. Our Heritage.'

args = GENSettings(do_sample=False, early_stopping=False,
                   top_k=20, temperature=0.9)
result = happy_gen.generate_text(
    prompt + question, args=args)
print(result.text)


prompt = "html. Skip to main navigation. Menu. news. company news. events. quarterly reports. filings. sec filings. tax filings. Events. Upcoming Events. More events are coming soon.. Past Events. Special Meeting of Stockholders. Jun 11, 2021 at 8:30 AM EDT. Shareholder control number required to join. Listen to Webcast. Fourth Quarter 2020 Earnings. Feb 26, 2021 at 8:30 AM EST. Listen to Webcast. Third Quarter 2020 Earnings. Nov 10, 2020 at 8:30 AM EST. Listen to Webcast. J.P. Morgan Gaming, Lodging, Restaurant & Leisure Forum. Sep 15, 2020 at 11:20 AM EDT. Listen to Webcast. Second Quarter 2020 Earnings. Aug 11, 2020 at 8:30 AM EDT. Listen to Webcast. Stifel 2020 Cross Sector Insight Conference. Jun 10, 2020 at 9:20 AM EDT. Listen to Webcast. First Quarter 2020 Earnings. May 7, 2020 at 8:30 AM EDT. Listen to Webcast. Fourth Quarter 2019 Earnings. Feb 27, 2020 at 8:30 AM EST. Listen to Webcast. Third Quarter 2019 Earnings. Nov 7, 2019 at 8:00 AM EST. Listen to Webcast. Second Quarter 2019 Earnings. Aug 7, 2019 at 8:30 AM EDT. Listen to Webcast. /.boxton. Company news. Presentations. Events. Quarterly reports. Stock Information. esg information. stock quote. historic prices. dividends. annual reports. proxy materials. Shareholder services. email alerts. contact information. Overview. about esa. why esa. awards. Corporate Governance. extended stay america. ESH hospitality. Filings. SEC filings. tax filings. News. company news. presentations. events. CONTACT INFORMATION. Extended Stay America, Inc.. 11525 N. Community House Rd. Suite 100. Charlotte, NC 28277. (980) 345-1600. Investor Relations. (980) 345-1546. investorrelations@extendedstay.com. American Stock Transfer. American Stock Transfer & Trust Company LLC. 6201 15th Avenue, Brooklyn, NY 11219. (800) 937-5449. www.astfinancial.com. info@astfinancial.com. EMAIL ALERTS. sign up for ESA news & notifications."
question = ' the first event is Special Meeting of Stockholders. Jun 11, 2021 at 8:30 AM EDT.'

args = GENSettings(do_sample=False, early_stopping=False,
                   top_k=20, temperature=0.9)
result = happy_gen.generate_text(
    prompt + question, args=args)
print(result.text)


prompt = "html. Skip to main navigation. Google Tag Manager (noscript). End Google Tag Manager (noscript). HEADER START HERE. BODY SECTION : EMPLOYEES PAGE START HERE. INVESTORS. nav will go here. Overview. Press Releases. Events & Presentations. Corporate Governance. Financial. Annual Reports. SEC Filings. Proxy Statement. Investment Calculator. Stock Information. Historic Stock Lookup. Dividend/Split History. Individual Investor Services. Email Alerts. Investor Contacts. Home. Investors. Company. Events & Presentations. Events & Presentations. Events & Presentations. Upcoming Events. Date. Title. Jul 23, 2021 at 9:00 AM CDT. Second Quarter 2021 Earnings. Click here for webcast. Add to Outlook. Add to Google Calendar. Oct 25, 2021 at 9:00 AM CDT. Third Quarter 2021 Earnings. Add to Outlook. Add to Google Calendar. Archived Events. Date. Title. Jun 3, 2021 at 10:00 AM CDT. Bernsteins 2021 Strategic Decisions Conference. Click here for webcast. Printable Slides. 844.4 KB. Apr 29, 2021 at 9:00 AM CDT. 2021 Annual Meeting of Stockholders. Click here for live webcast of Annual Meeting. Event Password: KMB2021. Inspection of Stockholder List. 89.1 KB. Apr 23, 2021 at 9:00 AM CDT. First Quarter 2021 Earnings. Click here for webcast. KMB 1Q 2021 Earnings Press Release. 167.5 KB. KMB 1Q 2021 Prepared Management Remarks. 128.3 KB. Feb 18, 2021 at 2:10 PM CST. 2021 CAGNY Conference. Click here for webcast. Non-GAAP Disclosure. 159 KB. Printable Slides. 2.8 MB. Jan 25, 2021 at 9:00 AM CST. Fourth Quarter 2020 Earnings Conference Call. Click here for webcast. Printable Slides. 910.3 KB. Oct 22, 2020 at 9:00 AM CDT. Third Quarter 2020 Earnings Conference Call. Click here for webcast. Printable Slides. 849.4 KB. Sep 9, 2020 at 9:00 AM CDT. Barclays 2020 Global Consumer Staples Conference. Click here for webcast. Non-GAAP Disclosure. 157.9 KB. Printable Slides. 967.2 KB. Jul 23, 2020 at 9:00 AM CDT. Second Quarter 2020 Earnings Conference Call. Click here for webcast. Printable Slides. 953.5 KB. /.boxton."
question = ' the first event is Jul 23, 2021 at 9:00 AM CDT. Second Quarter 2021 Earnings.'

args = GENSettings(do_sample=False, early_stopping=False,
                   top_k=20, temperature=0.9)
result = happy_gen.generate_text(
    prompt + question, args=args)
print(result.text)


prompt = "html. header of the page. contain main informative part of the site. promo section. main visual title area. IR Calendar. breadcrumbs of page. Home. Investor Relations. IR Calendar. twocolumns section. contain the main content of the page. Upcoming Events. No results. There are no upcoming events scheduled at this time.. Sign up here. to receive notices about upcoming events and press releases.. Past Events. June 2, 2021. Craig-Hallum 18th Annual Institutional Investor Conference. Virtual. May 18, 2021 9:00am ET. 2021 Annual Meeting of Stockholders. Virtual Meeting. Meeting Replay. Proxy Statement. May 6, 2021 9:00am ET. InfuSystem Holdings, Inc. First Quarter 2021 Financial Results Conference Call. Related Documents. Q1 2021. Quarterly Results. Earnings Release. HTML. Earnings Release. Webcast. Filing. HTML. 10-Q. Filing. XBRL. HTML. XBRL. March 25, 2021 9:15am ET. Sidotis Spring 2021 Virtual Conference. Virtual Conference. Webcast. March 17, 2021 9:00 am ET. Fourth Quarter and Full Year 2020 Financial Results. A replay of the call will be available for 90 days or by calling (877) 344-7529 or (412) 317-0088, confirmation code 10152717, through March 24, 2021.. Related Documents. Q4 2020. Quarterly Results. Earnings Release. HTML. Earnings Release. Webcast. Filing. HTML. 10-K. Filing. XBRL. HTML. XBRL. More past events . contain sidebar of the page. Investor Relations. Overview. News / Events. Press Releases. IR Calendar. Email Alerts. Company Information. Profile. Leadership Team. Presentations. IR Contacts. Analyst Coverage. Financial Information. Financials. Financial Results. Stock Data. Quote. Charts. Historical Data. SEC Filings. All SEC Filings. Annual Reports. Quarterly Reports. Section 16 Filings. Corporate Governance. Board of Directors. Board Committees. Governance Docs. Corporate Presentations. Corporate Presentations. Email Us. Get A Quote. Stock Snapshot. INFU. Symbol. NYSE American. Market. Market Cap. Price. Change. Volume."
question = ' the first event is June 2, 2021. Craig-Hallum 18th Annual Institutional Investor Conference.'

args = GENSettings(do_sample=False, early_stopping=False,
                   top_k=20, temperature=0.9)
result = happy_gen.generate_text(
    prompt + question, args=args)
print(result.text)

prompt = "html. Home. Investor Relations. Events. Upcoming Events. Upcoming Events. Past Events. Date. Event. Jul 27, 2021. 02:00 PM PST. Juniper Networks Q2 2021 Financial Results Conference Call. Webcast. Past Events. Investor Relations - Home. Upcoming Events. Upcoming Events. Past Events. July 27, 2021. 02:00 PM PST. Juniper Networks Q2 2021 Financial Results Conference Call. Webcast. Receive Email Alerts:. Email Address. Mailing Lists. Releases. SEC Filings. Events. Enter the code shown above.. Un-subscribe from Juniper Networks email alerts.. Un-subscribe form Juniper Networks. email alerts.. Solutions. About Juniper. Partners. Community. Request a Quote. How to Buy. Feedback. Contact Us. Careers. Image Library. RSS Feeds. Accessibility. Privacy Policy. Legal Notices. Site Map. Country Selector. United States. Deutschland - Germany. France. United Kingdom. - China. - Japan. - Korea. 1999 - 2020 Juniper Networks, Inc. All rights reserved. script."
question = ' the first event is '

args = GENSettings(do_sample=False, early_stopping=False,
                   top_k=20, temperature=0.9)
result = happy_gen.generate_text(
    prompt + question, args=args)
print(result.text)


# args = GENTrainArgs(num_train_epochs=1)
# happy_gen.train("output.txt", args=args)

# test1 = "html <DIV> INVESTORS <DIV> nav will go here <DIV> Overview <DIV> Press Releases <DIV> Events & Presentations <DIV> Email Alerts <DIV> Investor Contacts <DIV> Home <DIV> Investors <DIV> Company <DIV> Events & Presentations <DIV> Events & Presentations <DIV> Events & Presentations <DIV> Upcoming Events <DIV> Date <DIV> Title <DIV> Jun 3, 2021 at 10:00 AM CDT <DIV> Bernsteins 2021 Strategic Decisions Conference <DIV>"
# question = 'The event is'
# top_k_sampling_settings = GENSettings(
#     do_sample=True, early_stopping=False, top_k=10, temperature=0.7)
# result = happy_gen.generate_text(
#     test1 + question, args=top_k_sampling_settings)
# print(result.text)

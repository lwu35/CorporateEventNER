from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from happytransformer import HappyGeneration


happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")


args = GENSettings(no_repeat_ngram_size=2)
result = happy_gen.generate_text(
    "To solve world hunger we must invest in ", args=args)
print(result.text)


args = GENTrainArgs(num_train_epochs=1)
happy_gen.train("output.txt", args=args)

test1 = "html <DIV> Skip to main navigation <DIV> Google Tag Manager (noscript) <DIV> End Google Tag Manager (noscript) <DIV> HEADER START HEREBODY SECTION : EMPLOYEES PAGE START HERE <DIV> INVESTORS <DIV> nav will go here <DIV> Overview <DIV> Press Releases <DIV> Events & Presentations <DIV> Corporate Governance <DIV> Financial <DIV> Annual Reports <DIV> SEC Filings <DIV> Proxy Statement <DIV> Investment Calculator <DIV> Stock Information <DIV> Historic Stock Lookup <DIV> Dividend/Split History <DIV> Individual Investor Services <DIV> Email Alerts <DIV> Investor Contacts <DIV> Home <DIV> Investors <DIV> Company <DIV> Events & Presentations <DIV> Events & Presentations <DIV> Events & Presentations <DIV> Upcoming Events <DIV> Date <DIV> Title <DIV> Jun 3, 2021 at 10:00 AM CDT <DIV> Bernsteins 2021 Strategic Decisions Conference <DIV> Click here for webcast <DIV> Add to Outlook <DIV> Add to Google Calendar <DIV> Jul 23, 2021 at 9:00 AM CDT <DIV> Second Quarter 2021 Earnings <DIV> Add to Outlook <DIV> Add to Google Calendar <DIV> Oct 25, 2021 at 9:00 AM CDT <DIV> Third Quarter 2021 Earnings <DIV> Add to Outlook <DIV> Add to Google Calendar <DIV> Archived Events <DIV> Date <DIV> Title <DIV> Apr 29, 2021 at 9:00 AM CDT <DIV> 2021 Annual Meeting of Stockholders <DIV> Click here for live webcast of Annual Meeting <DIV> Event Password: KMB2021 <DIV> Inspection of Stockholder List <DIV> 89.1 KB <DIV> Apr 23, 2021 at 9:00 AM CDT <DIV> First Quarter 2021 Earnings <DIV> Click here for webcast <DIV> KMB 1Q 2021 Earnings Press Release <DIV> 167.5 KB <DIV> KMB 1Q 2021 Prepared Management Remarks <DIV> 128.3 KB <DIV> Feb 18, 2021 at 2:10 PM CST <DIV> 2021 CAGNY Conference <DIV> Click here for webcast <DIV> Non-GAAP Disclosure <DIV> 159 KB <DIV> Printable Slides <DIV> 2.8 MB <DIV> Jan 25, 2021 at 9:00 AM CST <DIV> Fourth Quarter 2020 Earnings Conference Call <DIV> Click here for webcast <DIV> Printable Slides <DIV> 910.3 KB <DIV> Oct 22, 2020 at 9:00 AM CDT <DIV> Third Quarter 2020 Earnings Conference Call <DIV> Click here for webcast <DIV> Printable Slides <DIV> 849.4 KB <DIV> Sep 9, 2020 at 9:00 AM CDT <DIV> Barclays 2020 Global Consumer Staples Conference <DIV> Click here for webcast <DIV> Non-GAAP Disclosure <DIV> 157.9 KB <DIV> Printable Slides <DIV> 967.2 KB <DIV> Jul 23, 2020 at 9:00 AM CDT <DIV> Second Quarter 2020 Earnings Conference Call <DIV> Click here for webcast <DIV> Printable Slides <DIV> 953.5 KB <DIV> May 28, 2020 at 10:00 AM CDT <DIV> Bernsteins 2020 Annual Strategic Decisions Conference <DIV> Click here for webcast <DIV> Printable Slides <DIV> 545.9 KB <DIV> /.boxton <DIV>"
question = 'The event is'
top_k_sampling_settings = GENSettings(
    do_sample=True, early_stopping=False, top_k=10, temperature=0.7)
result = happy_gen.generate_text(
    test1 + question, args=top_k_sampling_settings)
print(result.text)

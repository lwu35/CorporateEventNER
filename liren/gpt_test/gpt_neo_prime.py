from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from happytransformer import HappyGeneration


happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")
# happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")

prompt = 'May 18, 2021 PROS and Diggintravel Redefine the End-to-End Travel Experience.'
question = ' the date is May 18, 2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = '02.17.2021 1:30 PM PST Shockwave Medical, Inc. Q4 2020 Earnings Conference Call.'
question = ' the date is 02.17.2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = '2019 Q2 Financial Results Conference Call Presentation August 7, 2019.'
question = ' the date is August 7, 2019'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = 'June 30, 2021 PROS to Help Drive Hawaiian Airlines’ Revenue Growth Strategy.'
question = ' the date is June 30, 2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = '2020 Annual Meeting of Stockholders JUN 10, 2020 • 8:30AM CDT.'
question = ' the date is JUN 10, 2020'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = 'May 24, 2021 Martin Marietta Announces Acquisition of Lehigh Hanson’s West Region Business MLM Acquisition Announcement MLM Acquisition Supplemental Information.'
question = ' the date is May 24, 2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = 'Mar 4, 2021 at 05:00 PM EST Turtle Beach Fourth Quarter and Full Year 2020 Conference Call  Listen to Webcast Supporting Materials  Q4 Earnings Presentation.'
question = ' the date is Mar 4, 2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = 'May 11, 2021 PROS Announces Virtual Investment Conference Schedule for May 2021.'
question = ' the date is May 11, 2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = 'Apr 29, 2021 at 9:00 AM CDT 2021 Annual Meeting of Stockholders Click here for live webcast of Annual Meeting\nEvent Password: KMB2021 Inspection of Stockholder List.'
question = ' the date is Apr 29, 2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = 'June 15, 2021 11:55 AM ET Credit Suisse 23rd Annual Communications Conference.'
question = ' the date is June 15, 2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

prompt = 'Citi 2021 Global Energy and Utilities Virtual Conference MAY 12, 2021 • 12:50PM EDT.'
question = ' the date is MAY 12, 2021'
args = GENSettings(min_length=3, temperature=0.9, max_length=10)
result = happy_gen.generate_text(
    prompt + question, args=args)

# prompt = 'June 2, 2021 PROS Announces Virtual Investment Conference Schedule for June 2021.'
# question = ' the date is '
prompt = 'May 24, 2021 Martin Marietta Announces Acquisition of Lehigh Hanson’s West Region Business MLM Acquisition Announcement MLM Acquisition Supplemental Information.'
question = ' the date is '
args = GENSettings(min_length=3, temperature=0.9, max_length=5)
result = happy_gen.generate_text(
    prompt + question, args=args)
print(result.text)

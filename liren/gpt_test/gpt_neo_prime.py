from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from happytransformer import HappyGeneration
import re

FILE_NAME = 'train.txt'
# GPT_MODEL = "EleutherAI/gpt-neo-125M"
GPT_MODEL = "EleutherAI/gpt-neo-1.3B"


def prime_gpt(file_name, model_name):

    prompt = []
    context = []

    with open(file_name) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.encode("ascii", "ignore")
        line = line.decode()
        line = re.sub(' +', ' ', line)
        if i % 2 == 0:
            context.append(line)
        else:
            prompt.append(line)

    happy_gen = HappyGeneration("GPT-NEO", model_name)

    # Prime training examples
    for i in range(len(context)):
        args = GENSettings(min_length=2, temperature=0.9, max_length=7)
        result = happy_gen.generate_text(context[i] + prompt[i], args=args)

    question = f"{prompt[0].split(' is ')[0]} is "
    return happy_gen, question


def predict(raw_event_text, happy_gen, question):
    args = GENSettings(min_length=2, temperature=0.9, max_length=7)
    result = happy_gen.generate_text(
        raw_event_text + question, args=args)
    print(result.text)


happy_gen, question = prime_gpt(FILE_NAME, GPT_MODEL)
prompt = 'May 24, 2021 Martin Marietta Announces Acquisition of Lehigh Hanson’s West Region Business MLM Acquisition Announcement MLM Acquisition Supplemental Information.'
predict(prompt, happy_gen, question)

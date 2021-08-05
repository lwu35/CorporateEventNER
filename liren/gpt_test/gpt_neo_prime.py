from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from happytransformer import HappyGeneration
import re

TRAIN_FILE = "gpt_train.txt"
TEST_FILE = "gpt_test.txt"
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


happy_gen, question = prime_gpt(TRAIN_FILE, GPT_MODEL)

with open(TEST_FILE) as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = line.encode("ascii", "ignore")
    line = line.decode()
    line = re.sub(' +', ' ', line)
    if i % 2 == 0:
        predict(line, happy_gen, question)

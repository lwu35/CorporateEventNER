import re

from happytransformer import HappyGeneration
from happytransformer import GENTrainArgs
from happytransformer import GENSettings


'''https://colab.research.google.com/drive/1Bg3hnPOoypUi9gi1wWa2c0Voux-rPqq9?usp=sharing#scrollTo=6LAVUXMfonCz'''

TRAIN_FILE = "gpt_train.txt"
TEST_FILE = "gpt_test.txt"

happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")
# happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")

args = GENTrainArgs(num_train_epochs=3)
happy_gen.train(TRAIN_FILE, args=args)

prompt = []
context = []
predicted = []

with open(TEST_FILE) as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line = line.encode("ascii", "ignore")
    line = line.decode()
    line = re.sub(' +', ' ', line)
    if i % 2 == 0:
        context.append(line)
    else:
        prompt.append(line)

temp_prompt = prompt[0]
parse_prompt = temp_prompt.split(' is ')
question = parse_prompt[0] + " is "
question = f"{parse_prompt[0]} is "

# Prime training examples
for i in range(len(context)):
    args = GENSettings(min_length=2, temperature=0.9, max_length=7)
    result = happy_gen.generate_text(context[i] + question, args=args)
    print(result.text)
    predicted.append(result.text)

print(predicted)

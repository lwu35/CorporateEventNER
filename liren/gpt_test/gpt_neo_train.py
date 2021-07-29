from happytransformer import HappyGeneration
from happytransformer import GENTrainArgs
from happytransformer import GENSettings

'''https://colab.research.google.com/drive/1Bg3hnPOoypUi9gi1wWa2c0Voux-rPqq9?usp=sharing#scrollTo=6LAVUXMfonCz'''

happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")
# happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")

args = GENTrainArgs(num_train_epochs=10)
happy_gen.train("train.txt", args=args)

prompt = 'May 2, 2021 PROS Announces Virtual Investment Conference Schedule for May 2020.'
question = 'The <EVENT_DATE> is asdlkjas;lkjlakds'


args = GENSettings(min_length=2, temperature=0.9, max_length=7)
result = happy_gen.generate_text(
    prompt + question, args=args)
print(result.text)

# prompt = 'May 24, 2021 Martin Marietta Announces Acquisition of Lehigh Hanson’s West Region Business MLM Acquisition Announcement MLM Acquisition Supplemental Information'
# question = ' the date is '
# args = GENSettings(min_length=3, temperature=0.9, max_length=10)
# result = happy_gen.generate_text(
#     prompt + question, args=args)
# print(result.text)

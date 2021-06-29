from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from happytransformer import HappyGeneration


happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-125M")

test1 = "<DIV> Jun 3, 2021 at 10:00 AM CDT <DIV>The event is Bernsteins 2021 Strategic Decisions Conference <DIV>"
question = 'The event is'

args = GENSettings(no_repeat_ngram_size=2)
result = happy_gen.generate_text(
    test1 + question, args=args)
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

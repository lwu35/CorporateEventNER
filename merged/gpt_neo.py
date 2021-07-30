from happytransformer import HappyGeneration
from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from fuzzywuzzy import fuzz
import configparser


# Input: training file name
# Output: fine-tuned model
def gpt_train(train_file):
    gpt_type = config['gpt_model']['model']
    happy_gen = HappyGeneration("GPT-NEO", gpt_type)
    epochs = config['gpt_model']['epochs']
    args = GENTrainArgs(num_train_epochs=int(epochs))
    happy_gen.train(train_file, args=args)
    return happy_gen

# Input: text content (string)
# Output: event tag
def gpt_predict(text,happy_gen):
    tags_vocab = ['Other', 'Earnings Release', 'Earnings Call', 'Shareholder Meeting', 'Sales Results', 'Guidance', 'Conference', 'Merger/Acquisition']
    test1 = "Text: " + text + "\n"
    question = 'Type:'
    top_k_sampling_settings = GENSettings(no_repeat_ngram_size=int(config['gpt_model']['no_repeat_ngram_size']),
                                          do_sample=config['gpt_model']['do_sample'], early_stopping=config['gpt_model']['early_stopping'], top_k=int(config['gpt_model']['top_k']), temperature=float(config['gpt_model']['temperature']))
    result = happy_gen.generate_text(
        test1 + question, args=top_k_sampling_settings)

    max_ratio = 0
    max_tag = "Other"
    for j in tags_vocab:
        ratio = fuzz.ratio(j, result.text.splitlines()[0])

        if ratio > max_ratio:
            max_ratio = ratio
            max_tag = j
    # print(max_tag + '\n')

    return max_tag

# Input: a list of text content (string)
# Output: a list ofevent tag
def gpt_predicts(raw_event_text,happy_gen):
    tags_vocab = ['Other', 'Earnings Release', 'Earnings Call', 'Shareholder Meeting', 'Sales Results', 'Guidance', 'Conference', 'Merger/Acquisition']
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
        # print(max_tag + '\n')
    return tags


if __name__ == "__main__":
    happy_gen = gpt_train('gpt_train.txt')
    happy_gen.save("model/")
    
    with open('gpt_test.txt', 'r', encoding='utf-8') as f:
        raw_event_text = []
        lines = f.readlines()
        for i in lines:
            raw_event_text.append([i.replace('\n', '')])
    print(gpt_predicts(raw_event_text,happy_gen))


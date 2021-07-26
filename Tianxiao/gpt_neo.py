from happytransformer import HappyGeneration
from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from fuzzywuzzy import fuzz


# Input: text content (string)
# Output: event tag
def gpt_predict(text,happy_gen):
    tags_vocab = ['Other', 'Earnings Release', 'Earnings Call', 'Shareholder Meeting', 'Sales Results', 'Guidance', 'Conference', 'Merger/Acquisition']
    test1 = "Text: " + text + "\n"
    question = 'Type:'
    top_k_sampling_settings = GENSettings(no_repeat_ngram_size=2,
                                          do_sample=True, early_stopping=False, top_k=5, temperature=0.7)
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
    happy_gen = HappyGeneration("GPT-NEO", "EleutherAI/gpt-neo-1.3B")
#     args = GENTrainArgs(num_train_epochs=3)
    with open('gpt_train.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(50):
            with open('gpt_train'+str(i)+'.txt', 'w', encoding='utf-8') as f1:
                f1.writelines(lines[i*3])
                f1.writelines(lines[i*3+1])
    for i in range(50):
        train_file = 'gpt_train'+str(i)+'.txt'
        happy_gen.train(train_file)
    happy_gen.save("model/")
    
    with open('gpt_test.txt', 'r', encoding='utf-8') as f:
        raw_event_text = []
        lines = f.readlines()
        for i in lines:
            raw_event_text.append([i.replace('\n', '')])
    print(gpt_predicts(raw_event_text,happy_gen))

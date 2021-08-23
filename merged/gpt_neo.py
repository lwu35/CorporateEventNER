from happytransformer import HappyGeneration
from happytransformer import GENTrainArgs
from happytransformer import GENSettings
from fuzzywuzzy import fuzz
import configparser

config = configparser.ConfigParser()
config.read('configg.ini')

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


def gpt_predict(text, happy_gen):
    test1 = "Text: " + text + "\n"
    question = 'Type:'
    top_k_sampling_settings = GENSettings(no_repeat_ngram_size=int(config['gpt_model']['no_repeat_ngram_size']),
                                          do_sample=config['gpt_model']['do_sample'], early_stopping=config['gpt_model']['early_stopping'], top_k=int(config['gpt_model']['top_k']), temperature=float(config['gpt_model']['temperature']))
    result = happy_gen.generate_text(
        test1 + question, args=top_k_sampling_settings)

    max_tag = "None/Other"
    gen_text = result.text.splitlines()[0].lower()
    sent = text.lower() + gen_text

    if 'call' in text and ('earnings' in sent or 'financial' in sent):
        max_tag = 'Earnings Call'
    elif 'earnings' in sent or 'financial' in sent:
        max_tag = 'Earnings Release'
    elif 'stockholders' in sent or 'shareholders' in sent or 'investor' in sent or 'shareholder' in sent:
        max_tag = 'Shareholder Meeting'
    elif 'conference' in sent:
        max_tag = 'Conference'
    elif 'result' in sent:
        max_tag = 'Sales Results'

    return max_tag

# Input: a list of text content (string)
# Output: a list ofevent tag


def gpt_predicts(raw_event_text, happy_gen):
    tags = []
    for i in range(len(raw_event_text)):
        test1 = "Text: " + raw_event_text[i] + "\n"
        question = 'Type:'
        top_k_sampling_settings = GENSettings(no_repeat_ngram_size=2,
                                              do_sample=True, early_stopping=False, top_k=5, temperature=0.7)
        result = happy_gen.generate_text(
            test1 + question, args=top_k_sampling_settings)

        max_tag = "None/Other"
        gen_text = result.text.splitlines()[0].lower()
        sent = raw_event_text[i].lower() + gen_text

        if 'call' in sent and ('earnings' in sent or 'financial' in sent):
            max_tag = 'Earnings Call'
        elif 'earnings' in sent or 'financial' in sent:
            max_tag = 'Earnings Release'
        elif 'stockholders' in sent or 'shareholders' in sent or 'investor' in sent or 'shareholder' in sent:
            max_tag = 'Shareholder Meeting'
        elif 'conference' in sent:
            max_tag = 'Conference'
        elif 'result' in sent:
            max_tag = 'Sales Results'

        tags.append(max_tag + '\n')

    return tags


def fine_tuning_single():
    happy_gen = gpt_train('train.txt')
    happy_gen.save("model/")
    with open('dev.txt', 'r', encoding='utf-8') as f:
        raw_event_text = []
        lines = f.readlines()
        for i in lines:
            raw_event_text.append([i.replace('\n', '')])
    pred_types = gpt_predicts(raw_event_text, happy_gen)
    with open('dev_tags.txt', 'r', encoding='utf-8') as f:
        true_tpyes = []
        lines = f.readlines()
        for i in lines:
            true_tpyes.append([i])
    count = 0
    for i in range(len(pred_types)):
        if pred_types[i] == true_tpyes[i][0]:
            count = count + 1

    print("Accuracy:{:.2f}%".format(count/200*100))


def fine_tuning_split():
    gpt_type = config['gpt_model']['model']
    happy_gen = HappyGeneration("GPT-NEO", gpt_type)
    epochs = config['gpt_model']['epochs']
    args = GENTrainArgs(num_train_epochs=int(epochs))

    with open('train.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(len(lines)//3):
            with open('train'+str(i)+'.txt', 'w', encoding='utf-8') as f1:
                f1.writelines(lines[i*3])
                f1.writelines(lines[i*3+1])
    for i in range(len(lines)//3):
        train_file = 'train'+str(i)+'.txt'
        happy_gen.train(train_file, args=args)
    happy_gen.save("model/")

    with open('dev.txt', 'r', encoding='utf-8') as f:
        raw_event_text = []
        lines = f.readlines()
        for i in lines:
            raw_event_text.append([i.replace('\n', '')])
    pred_types = gpt_predicts(raw_event_text, happy_gen)
    with open('dev_tags.txt', 'r', encoding='utf-8') as f:
        true_tpyes = []
        lines = f.readlines()
        for i in lines:
            true_tpyes.append([i])
    count = 0
    for i in range(len(pred_types)):
        if pred_types[i] == true_tpyes[i][0]:
            count = count + 1

    print("Accuracy:{:.2f}%".format(count/200*100))

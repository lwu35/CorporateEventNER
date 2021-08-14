import pandas as pd
import logging
from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs

TRAIN_FILE = 'cleaned_train.csv'
DEV_FILE = 'cleaned_dev.csv'

TAG = 'company'
LOWER = True

df = pd.read_csv(TRAIN_FILE)

event_texts = df['event_text']
labels = df[TAG]

train_data = []
for i in range(len(event_texts)):
    cur_q = {}

    if LOWER:
        txt = event_texts[i].lower()
        label = labels[i].lower()
    else:
        txt = event_texts[i].upper()
        label = labels[i].upper()

    first_word = label.split()[0]
    cur_q['context'] = txt
    cur_q['qas'] = []
    cur_qas = {}
    cur_qas['question'] = f'What is the {TAG}?'
    cur_qas['answers'] = []
    cur_qas['id'] = str(i)
    if label == 'NONE' or label == 'none':
        cur_qas['is_impossible'] = True
    else:
        cur_qas['is_impossible'] = False
        answer_idx = txt.index(first_word)
        cur_a = {'text': label, 'answer_start': answer_idx}
        cur_qas['answers'].append(cur_a)
    cur_q['qas'].append(cur_qas)
    train_data.append(cur_q)

df = pd.read_csv(DEV_FILE)

event_texts = df['event_text']
labels = df[TAG]

dev_data = []
for i in range(len(event_texts)):
    cur_q = {}

    if LOWER:
        txt = event_texts[i].lower()
        label = labels[i].lower()
    else:
        txt = event_texts[i].upper()
        label = labels[i].upper()

    first_word = label.split()[0]
    cur_q['context'] = txt
    cur_q['qas'] = []
    cur_qas = {}
    cur_qas['question'] = f'What is the {TAG}?'
    cur_qas['answers'] = []
    cur_qas['id'] = str(i)
    if label == 'NONE' or label == 'none':
        cur_qas['is_impossible'] = True
    else:
        cur_qas['is_impossible'] = False
        answer_idx = txt.index(first_word)
        cur_a = {'text': label, 'answer_start': answer_idx}
        cur_qas['answers'].append(cur_a)
    cur_q['qas'].append(cur_qas)
    dev_data.append(cur_q)

print(len(train_data))
print(len(dev_data))


"""# MODEL"""

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

# Configure the model
model_args = QuestionAnsweringArgs(n_best_size=5, max_answer_length=5)
model_args.train_batch_size = 4
model_args.eval_batch_size = 4
model_args.evaluate_during_training = True
model_args.num_train_epochs = 3
model_args.overwrite_output_dir = True

model = QuestionAnsweringModel(
    "roberta", "roberta-base", args=model_args
)

# Train the model
model.train_model(train_data, eval_data=dev_data)

# Evaluate the model
result, texts = model.eval_model(dev_data)

# count = 0
# for example in test_data:
#     print('--------------------------------')
#     answers, probabilities = model.predict([example])

#     print('CONTEXT:', example['context'])
#     print('ANSWER:', answers[0]['answer'][0])
#     print('--------------------------------')
#     if count == 20:
#         break
#     count += 1

example = [
    {
        "context": "Jefferies Virtual Healthcare Conference  Tuesday, June 2, 2020  11:00am EDT Listen to the Webcast",
        "qas": [
            {
                "question": "What is the company?",
                "id": "0",
            }
        ],
    }
]

answers, probabilities = model.predict(example)

print('CONTEXT:', example[0]['context'])
print('ANSWER:', answers[0]['answer'][0])

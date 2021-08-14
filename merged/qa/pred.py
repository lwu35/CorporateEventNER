import pandas as pd
import logging
from simpletransformers.question_answering import QuestionAnsweringModel


def run():

    model = QuestionAnsweringModel(
        "roberta", "best_model"
    )

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


if __name__ == '__main__':
    run()

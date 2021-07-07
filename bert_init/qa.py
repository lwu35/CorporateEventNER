import logging

from simpletransformers.question_answering import QuestionAnsweringModel, QuestionAnsweringArgs


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)


def main():
   train_data = [
    {
        "context": "2021 Astronics Corporation Annual Meeting of Shareholders",
        "qas": [
            {
                "id": "00001",
                "is_impossible": False,
                "question": "What is the event type?",
                "answers": [
                    {
                        "text": "Annual Meeting of Shareholders",
                        "answer_start": 28,
                    }
                ],
            }
        ],
    },
    {
        "context": "The first series, published between 2006 and 2008, consists of The Final Empire,"
                "The Well of Ascension, and The Hero of Ages.",
        "qas": [
            {
                "id": "00002",
                "is_impossible": False,
                "question": "When was the series published?",
                "answers": [
                    {
                        "text": "between 2006 and 2008",
                        "answer_start": 28,
                    }
                ],
            },
        ],
    },
]

eval_data = [
    {
        "context": "The series primarily takes place in a region called the Final Empire "
                "on a world called Scadrial, where the sun and sky are red, vegetation is brown, "
                "and the ground is constantly being covered under black volcanic ashfalls.",
        "qas": [
            {
                "id": "00001",
                "is_impossible": False,
                "question": "Where does the series take place?",
                "answers": [
                    {
                        "text": "region called the Final Empire",
                        "answer_start": 38,
                    },
                    {
                        "text": "world called Scadrial",
                        "answer_start": 74,
                    },
                ],
            }
        ],
    },
    {
        "context": "\"Mistings\" have only one of the many Allomantic powers, while \"Mistborns\" have all the powers.",
        "qas": [
            {
                "id": "00002",
                "is_impossible": False,
                "question": "How many powers does a Misting possess?",
                "answers": [
                    {
                        "text": "one",
                        "answer_start": 21,
                    }
                ],
            },
            {
                "id": "00003",
                "is_impossible": True,
                "question": "What are Allomantic powers?",
                "answers": [],
            },
        ],
    },
]

# Configure the model
model_args = QuestionAnsweringArgs()
model_args.train_batch_size = 16
model_args.evaluate_during_training = True
model_args.overwrite_output_dir = True
#model_args.fp16 = False

model = QuestionAnsweringModel(
    "distilbert", "distilbert-base-uncased", args=model_args
)

# Train the model
model.train_model(train_data, eval_data=eval_data)

# Evaluate the model
result, texts = model.eval_model(eval_data)

    # Make predictions with the model
to_predict = [
        {
            "context": "2021 Astronics Corporation Annual Meeting of Shareholders.",
            "qas": [
                {
                    "question": "What is the event type?",
                    "id": "0",
                }
            ],
        },
                {
            "context": "Fourth Quarter 2020 Earnings.",
            "qas": [
                {
                    "question": "What is the event type?",
                    "id": "1",
                }
            ],
        },
    ]

answers, probabilities = model.predict(to_predict)

print(answers)

    # Configure the model
    model_args = QuestionAnsweringArgs()
    model_args.train_batch_size = 4
    model_args.evaluate_during_training = True
    model_args.dataloader_num_workers = 1
    #model_args.fp16 = False

    model = QuestionAnsweringModel(
        "distilbert", "distilbert-base-uncased", args=model_args
    )

    # Train the model
    model.train_model(train_data, eval_data=eval_data)

    # Evaluate the model
    result, texts = model.eval_model(eval_data)

    # Make predictions with the model
    to_predict = [
        {
            "context": "Vin is a Mistborn of great power and skill.",
            "qas": [
                {
                    "question": "What is Vin's speciality?",
                    "id": "0",
                }
            ],
        }
    ]

    answers, probabilities = model.predict(to_predict)

    print(answers)

if __name__ == "__main__":
    main()

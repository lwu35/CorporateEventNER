import json
import pandas as pd

# Using readline()
file1 = open('job1.json', 'r', encoding="utf8")
count = 0
count_dict = {}
count_judgement = {}

while True:
    count += 1

    # Get next line from file
    line = file1.readline()

    # if line is empty
    # end of file is reached
    # if not line or count == 5:
    #     break
    if not line:
        break

    line_json = json.loads(line)
    #print(json.dumps(line_json, indent=4))
    # print(line_json.keys())
    if line_json['agreement'] in count_dict:
        count_dict[line_json['agreement']] += 1
    else:
        count_dict[line_json['agreement']] = 0

    if line_json['judgments_count'] in count_judgement:
        count_judgement[line_json['judgments_count']] += 1
    else:
        count_judgement[line_json['judgments_count']] = 0

print(count_dict)
print(count_judgement)
file1.close()

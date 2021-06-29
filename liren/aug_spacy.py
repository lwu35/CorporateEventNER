import pandas as pd
import os
from tqdm.auto import tqdm
import spacy
import stanza
import re

from spacy.pipeline import EntityRuler


def main():
    # intialize spacy
    nlp_spacy = spacy.load('en_core_web_lg')

    # nlp_stanza = stanza.Pipeline('en')

    # add custom entity to spacy
    ruler = EntityRuler(nlp_spacy, overwrite_ents=True)

    # patterns = [
    #     {"label": "ORG", "pattern": "astronics"},
    # ]
    # ruler.add_patterns(patterns)

    # load companies list
    print('loading company names')
    file_path = os.path.join('company_names_100k.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')
    companies = list(df['name'])[:100]
    companies.append('astronics')

    # tag companies
    for item in companies:
        ruler.add_patterns([{"label": "ORG", "pattern": item}])

    # tag periods
    periods = ["q1", "q2", "q3", "q4",
               "1q", "2q", "3q", "4q",
               "quarter 1", "quarter 2", "quarter 3", "quarter 4",
               "first quarter", "second quarter", "third quarter", "fourth quarter",
               "full year", "annual", "1S", "2S",
               "S1", "S2", "first half", "second half", ]
    for item in periods:
        ruler.add_patterns([{"label": "FISCAL_PERIOD", "pattern": item}])

    # add custom rules to the pipe
    nlp_spacy.add_pipe(ruler)

    # extract entities

    test_ex = ['2021 Astronics Corporation Annual Meeting of Shareholders', 'May 25, 2021 • 10:00am EDT',
               'Mar 12, 2020', '4Q19 Earnings Call Slides',
               'Fourth Quarter 2020 Earnings', 'Feb 26, 2021 at 8:30 AM EST',
               'Jun 3, 2021 at 10:00 AM CDT', 'Bernstein’s 2021 Strategic Decisions Conference',
               'JUN 2, 2021 4:30 PM EDT', 'Jefferies Virtual Healthcare Conference',
               'May 10, 2021 5:00 PM ET', 'Switch Inc. First Quarter 2021 Earnings Conference Call',
               'MAY 18, 2021 • 9:00AM ET', '2021 Annual Meeting of Stockholders',
               'Jun 01, 2021 01:10 PM ET', 'Cowen 49th Annual Media & Telecom Conference',
               'Cowen 49th Annual Technology Media & Telecom Conference', 'June 1, 2021 09:10 – 9:40 am EDT',
               'The PNC Financial Services Group at the Bernstein Strategic Decisions Conference', 'Thursday, June 03, 2021 10:00 am EDT'
               ]

    for line in test_ex:
        doc = nlp_spacy(line.lower())
        print(line)
        for ent in doc.ents:
            #print('\t<ENT>:', ent.text, '<Label>:', ent.label_)
            if ent.label_ == 'ORG':
                print('\tORG:', ent.text)
            if ent.label_ == 'FISCAL_PERIOD':
                print('\tFISCAL_PERIOD:', ent.text)
            if ent.label_ == 'TIME':
                print('\tTIME:', ent.text)
            if ent.label_ == 'DATE':
                print('\tDATE:', ent.text)

        # doc = nlp_stanza(line.lower())
        # for ent in doc.entities:
        #     if ent.type == 'TIME':
        #         print('\tTIME:', ent.text)
        #     if ent.type == 'DATE':
        #         print('\tDATE:', ent.text)


if __name__ == '__main__':
    main()

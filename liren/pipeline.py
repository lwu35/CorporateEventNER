import pandas as pd
import os
from tqdm.auto import tqdm

import spacy
from spacy.pipeline import EntityRuler

import stanza

from datetime_extractor import DateTimeExtractor
from date_extractor import extract_dates
from date_extractor import extract_date
import datefinder
from dateparser.search import search_dates

import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


def extract_pages(mystr, nlp_spacy, nlp_stanza):

    if len(mystr) > 0:
        soup = BeautifulSoup(mystr, 'html5lib')

        #soup = soup.find("body")

        # remove <script> JS
        for s in soup.select('script'):
            s.extract()

        # remove <button>
        for s in soup.select('button'):
            s.extract()

        # remove <style>
        for s in soup.select('style'):
            s.extract()

        # remove <meta>
        for s in soup.select('meta'):
            s.extract()

        # remove <nav>
        for s in soup.select('nav'):
            s.extract()

        # remove <head>
        for s in soup.select('head'):
            s.extract()

        # remove <header>
        for s in soup.select('header'):
            s.extract()

        # remove <footer>
        for s in soup.select('footer'):
            s.extract()

        # remove <footer>
        for s in soup.select('a href'):
            s.extract()

        try:
            return get_parent_r_text(soup, r'\d{4}', nlp_spacy, nlp_stanza)
            # get_parent_r(soup, r'\d{4}')
        except Exception as e:
            print('Error')


def extract_company(mystr, nlp_spacy, nlp_stanza):
    if len(mystr) > 0:
        soup = BeautifulSoup(mystr, 'html5lib')

        title = soup.find('title')
        title = re.sub("[(]\S+[)]", "", title.string)
        # print(title)  # Prints the tag string content

        spans = re.split("\B\W+\B", title)
        spans = [i for i in spans if i]

        company_name = ''

        for span in spans:
            # Augmented spacy
            # doc = nlp_spacy(span.strip().lower())
            # for ent in doc.ents:
            #     print('\t(Spacy)', ent.text, ':', ent.label_)

            # stanza (stanford ner)
            doc = nlp_stanza(span.strip())
            for ent in doc.entities:
                #print(f'\t(stanza) {ent.text} : {ent.type}')
                company_name = ent.text

        return company_name


def get_page(url):
    # remove cache in url
    url = url.split('?')[0]

    url = url.replace(' ', '')
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        webpage = urlopen(req).read()
        mystr = webpage.decode("utf8")
        return mystr
    except Exception as e:
        print('Error:', url)


def main():

    file_path = os.path.join('60_links.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')
    urls = list(df['Link'])[:20]
    print(len(urls))

    nlp_spacy = spacy.load('en_core_web_lg')
    nlp_stanza = stanza.Pipeline('en')

    # add custom entity to spacy
    ruler = EntityRuler(nlp_spacy, overwrite_ents=True)

    # load companies list
    print('loading company names')
    file_path = os.path.join('company_names_nasdaq.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')
    companies = list(df['name'])

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

    for url in urls:
        page = get_page(url)
        company_name = extract_company(page, nlp_spacy, nlp_stanza)
        print(company_name)
        all_date, all_time = extract_pages(page, nlp_spacy, nlp_stanza)
        print(all_date)
        print(all_time)


def walker(soup):
    page = ''
    for child in soup.recursiveChildGenerator():
        name = getattr(child, 'name', None)
        if name is not None:
            # page += ' <' + name + '> '
            page += ' <DIV> '

        elif not child.isspace():
            blacklist_str = ['widget', 'span',
                             'wrapper', '<', '>', 'row', 'footer']

            if any(x in str(child).lower() for x in blacklist_str) or len(str(child)) < 4:
                pass
                # print(str(child))
            else:
                page += " ".join(child.split())

    t1 = page.encode("ascii", "ignore")
    t2 = t1.decode()
    t3 = t2.split()
    t4 = [t3[i] for i in range(len(t3)) if (i == 0) or t3[i] != t3[i-1]]
    page = " ".join(t4)
    print(len(page))

    return page


def get_root_children(soup):
    soup = soup.html
    root_childs = [e.name for e in soup.children if e.name is not None]
    print('Root Children:', root_childs)


def get_parent_r(soup, pattern):
    print('___________________________________')

    for i, elem in enumerate(soup(text=re.compile(pattern))):
        str_elem = str(elem.parent.get_text())
        str_elem = ' '.join(str_elem.split())
        print(f'{i}-Text: {str_elem}')

        if i > 10:
            break


def get_parent_r_text(soup, pattern, nlp_spacy, nlp_stanza):
    # print('___________________________________')
    stanza_all_date = []
    stanza_all_time = []

    spacy_all_date = []
    spacy_all_time = []
    spacy_all_fp = []

    for i, elem in enumerate(soup(text=re.compile(pattern))):
        str_elem = str(elem.parent.get_text())
        str_elem = ' '.join(str_elem.split())
        stanza_cur_date = []
        stanza_cur_time = []
        spacy_cur_date = []
        spacy_cur_time = []
        spacy_cur_fp = []

        # print(f'{i}---------Text: {str_elem}')

        doc = nlp_spacy(str_elem)
        for ent in doc.ents:
            # print('\t(Spacy) <ENT>:', ent.text, '<Label>:', ent.label_)
            if ent.label_ == 'TIME':
                spacy_cur_time.append(ent.text)
            if ent.label_ == 'DATE':
                spacy_cur_date.append(ent.text)
            if ent.label_ == 'FISCAL_PERIOD':
                spacy_cur_fp.append(ent.text)

        doc = nlp_stanza(str_elem)
        for ent in doc.entities:
            # print(f'\t(stanza) {ent.text}\t{ent.type}')
            if ent.type == 'TIME':
                stanza_cur_time.append(ent.text)
            if ent.type == 'DATE':
                stanza_cur_date.append(ent.text)

        # print('\t(datetime-extractor)', DateTimeExtractor(str_elem))
        # print('\t(date-extractor)', extract_dates(str_elem))
        # print('\t(date-extractor)', extract_date(str_elem))

        # dateFounded = datefinder.find_dates(str_elem)
        # for date in dateFounded:
        #     print('\t(datefinder)', date)

        # print('\t(search_dates)', search_dates(str_elem))

        stanza_all_date.append(stanza_cur_date)
        stanza_all_time.append(' '.join(stanza_cur_time))

        spacy_all_date.append(spacy_cur_date)
        spacy_all_time.append(' '.join(spacy_cur_time))
        spacy_all_fp.append(spacy_cur_fp)
        if i > 5:
            break

    # print('\tstanza dates:', stanza_all_date)
    # print('\tstanza times:', stanza_all_time)

    # print('\tspacy dates:', spacy_all_date)
    # print('\tspacy times:', spacy_all_time)

    return spacy_all_date[:6], stanza_all_time[:6]


if __name__ == '__main__':
    main()

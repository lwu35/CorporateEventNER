import pandas as pd
import os
from tqdm.auto import tqdm
import spacy
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


def download_pages():
    file_path = os.path.join('60_links.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')

    urls = list(df['Link'])
    print(len(urls))

    broken_urls = []

    for url in tqdm(urls):
        url = url.split('?')[0]
        url = url.replace(' ', '')
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            webpage = urlopen(req).read()
            mystr = webpage.decode("utf8")
        except Exception as e:
            broken_urls.append(str(url) + ',' + str(e) + '\n')

        name = url.split('//')[1]
        name = name.replace('www.', '')
        name = name.replace('/', '|')
        name = name.split('.com')[0]

        w_file_path = os.path.join('60_data', name)
        f = open(w_file_path, "w+")
        f.write(mystr)

    output_f = open('broken.csv', 'w')
    output_f.writelines(broken_urls)
    output_f.close()


def extract_pages():
    file_path = os.path.join('60_links.csv')
    df = pd.read_csv(file_path, sep=',', engine='python')
    urls = list(df['Link'])[:10]

    text_file = open("Output.txt", "w")

    nlp_spacy = spacy.load('en_core_web_lg')
    nlp_stanza = stanza.Pipeline('en')

    print(len(urls))

    for url in tqdm(urls):
        url = url.split('?')[0]
        url = url.replace(' ', '')
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            webpage = urlopen(req).read()
            mystr = webpage.decode("utf8")
        except Exception as e:
            print('Error:', url)

        if len(mystr) > 0:
            soup = BeautifulSoup(mystr, 'html5lib')

            title = soup.find('title')

            print(title.string)  # Prints the tag string content
            doc = nlp_spacy(str(title.string).lower())
            for ent in doc.ents:
                print('\t(Spacy) <ENT>:', ent.text, '<Label>:', ent.label_)

            doc = nlp_stanza(title.string)
            for ent in doc.entities:
                print(f'\t(stanza) {ent.text}\t{ent.type}')

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

            # # file output
            # try:
            #     text_file.write(walker(soup) + '\n')
            # except Exception as e:
            #     print(walker(soup))

            # get_root_children(soup)
            # print(soup.prettify())
            # get_parent_r(soup, r'\d{4}')
            try:
                print('<--------------------', url, '-------------------->')
                get_parent_r_text(soup, r'\d{4}', nlp_spacy, nlp_stanza)
            except Exception as e:
                print('Error:')

            # print(soup.get_text())
    # text_file.close()


def main():
    # download html pages
    # download_pages()

    # extract event info (date + time)
    extract_pages()


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
        str_elem = str(elem.parent)
        str_elem = ' '.join(str_elem.split())
        print(f'{i}-Element: {str_elem}')

        if i > 10:
            break


def get_parent_r_text(soup, pattern, nlp_spacy, nlp_stanza):
    print('___________________________________')
    stanza_all_date = []
    stanza_all_time = []

    spacy_all_date = []
    spacy_all_time = []

    for i, elem in enumerate(soup(text=re.compile(pattern))):
        str_elem = str(elem.parent.get_text())
        str_elem = ' '.join(str_elem.split())
        stanza_cur_date = []
        stanza_cur_time = []
        spacy_cur_date = []
        spacy_cur_time = []

        print(f'{i}---------Text: {str_elem}')

        doc = nlp_spacy(str_elem)
        for ent in doc.ents:
            print('\t(Spacy) <ENT>:', ent.text, '<Label>:', ent.label_)
            if ent.label_ == 'TIME':
                spacy_cur_time.append(ent.text)
            if ent.label_ == 'DATE':
                spacy_cur_date.append(ent.text)

        doc = nlp_stanza(str_elem)
        for ent in doc.entities:
            # print(f'\t(stanza) {ent.text}\t{ent.type}')
            if ent.type == 'TIME':
                stanza_cur_time.append(ent.text)
            if ent.type == 'DATE':
                stanza_cur_date.append(ent.text)
        #print('\t(datetime-extractor)', DateTimeExtractor(str_elem))
        #print('\t(date-extractor)', extract_dates(str_elem))
        #print('\t(date-extractor)', extract_date(str_elem))

        # dateFounded = datefinder.find_dates(str_elem)
        # for date in dateFounded:
        #     print('\t(datefinder)', date)

        # print('\t(search_dates)', search_dates(str_elem))

        stanza_all_date.append(stanza_cur_date)
        stanza_all_time.append(' '.join(stanza_cur_time))

        spacy_all_date.append(spacy_cur_date)
        spacy_all_time.append(' '.join(spacy_cur_time))
        if i > 5:
            break

    print('\tstanza dates:', stanza_all_date)
    print('\tstanza times:', stanza_all_time)

    print('\tspacy dates:', spacy_all_date)
    print('\tspacy times:', spacy_all_time)


if __name__ == '__main__':
    main()

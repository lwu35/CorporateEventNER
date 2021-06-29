import pandas as pd
import os
from tqdm.auto import tqdm
import spacy
import stanza

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


def main():
    # download html pages
    # download_pages()

    url = 'https://reelrundown.com/movies/Marvelous-Facts-About-Marvel-Movies'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    mystr = webpage.decode("utf8")

    # soup = BeautifulSoup(mystr, 'html.parser')
    soup = BeautifulSoup(mystr, 'html5lib')
    # soup = BeautifulSoup(mystr, 'lxml')

    # soup.script.decompose()

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

    # walker(soup)
    # get_root_children(soup)
    # print(soup.prettify())
    #get_parent_r(soup, r'\d{4}')
    #get_parent_r_text(soup, r'\d{4}')

    p_tags = soup.find_all('p')

    for each in p_tags:
        print(each.text)
    # print(soup.get_text())


def walker(soup):
    for child in soup.recursiveChildGenerator():
        name = getattr(child, 'name', None)
        if name is not None:
            print('<' + name + '>')
        elif not child.isspace():
            print(child.strip())


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


def get_parent_r_text(soup, pattern):
    print('___________________________________')
    nlp_spacy = spacy.load('en_core_web_sm')
    nlp_stanza = stanza.Pipeline('en')

    for i, elem in enumerate(soup(text=re.compile(pattern))):
        str_elem = str(elem.parent.get_text())
        str_elem = ' '.join(str_elem.split())

        print(f'{i}-Text: {str_elem}')
        doc = nlp_spacy(str_elem)
        for ent in doc.ents:
            # print('\t(Spacy) ENT:', ent.text,
            #       ent.start_char, ent.end_char, ent.label_)
            print('\t(Spacy) <ENT>:', ent.text,
                  '<Label>:', ent.label_)

        doc = nlp_stanza(str_elem)
        print('\t(stanza)', doc.entities)
        print('\t(datetime-extractor)', DateTimeExtractor(str_elem))
        print('\t(date-extractor)', extract_dates(str_elem))
        print('\t(date-extractor)', extract_date(str_elem))

        dateFounded = datefinder.find_dates(str_elem)
        for date in dateFounded:
            print('\t(datefinder)', date)

        print('\t(search_dates)', search_dates(str_elem))
        print('<----------->')


if __name__ == '__main__':
    main()

import pandas as pd
import os
from tqdm.auto import tqdm

import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_pages():
    file_path = os.path.join('appen_urls.csv')
    df = pd.read_csv(file_path, engine='python')

    urls = list(df['url'])
    urls_id = list(df['url_id'])
    print(len(urls))

    broken_urls = []

    for i in tqdm(range(len(urls))):
        # url = url.split('?')[0]
        # url = url.replace(' ', '')
        req = Request(urls[i], headers={'User-Agent': 'Mozilla/5.0'})
        try:
            webpage = urlopen(req).read()
            mystr = webpage.decode("utf8")
        except Exception as e:
            broken_urls.append(f"{str(urls[i])}, {str(urls_id[i])}, {str(e)}\n")

        name = f"{urls_id[i]}.html"
        w_file_path = os.path.join('appen_pages', name)
        f = open(w_file_path, "w+")
        f.write(mystr)

    output_f = open('broken.csv', 'w')
    output_f.writelines(broken_urls)
    output_f.close()

def main():
    # download html pages
    download_pages()


if __name__ == '__main__':
    main()

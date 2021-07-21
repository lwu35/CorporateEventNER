import pandas as pd
import os
from tqdm.auto import tqdm

import re
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from selenium import webdriver
import codecs

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def download_pages():
    file_path = os.path.join('appen_urls.csv')
    df = pd.read_csv(file_path, engine='python')

    urls = list(df['url'])
    urls_id = list(df['url_id'])
    print(len(urls))

    broken_urls = []

    # set chromedriver.exe path
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
    driver.implicitly_wait(0.5)
    # maximize browser
    driver.maximize_window()

    for i in tqdm(range(len(urls))):

        try:
            # launch URL
            driver.get(urls[i])
            # get file path to save page
            name = f"{urls_id[i]}.html"
            n = os.path.join('appen_pages', name)
            # open file in write mode with encoding
            f = codecs.open(n, "w", "utf−8")
            # obtain page source
            h = driver.page_source
            # write page source content to file
            f.write(h)
            # close browser
            driver.quit()
        except Exception as e:
            broken_urls.append(f"{str(urls[i])}, {str(urls_id[i])}, {str(e)}\n")

    output_f = open('broken.csv', 'w')
    output_f.writelines(broken_urls)
    output_f.close()

def main():
    # download html pages
    download_pages()






if __name__ == '__main__':
    main()

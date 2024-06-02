import requests
from bs4 import BeautifulSoup 
import pandas as pd

cbr_link = 'https://www.cbr.com'
url = 'https://www.cbr.com/category/movies/news-movies/'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')

articles = soup.find_all(class_='article')

for article in articles:
    article_title = article.find(class_='display-card-title').text.strip()
    article_author = article.find(class_='article-author').text
    article_tag = article.find(class_='dc-tag-label').text
    article_link = cbr_link+ article.find('a')['href']

    article_request = requests.get(article_link)
    article_soup = BeautifulSoup(article_request.text, 'html.parser')
    article_description = article_soup.find(class_='content-block-regular').find('p').text.strip()

  


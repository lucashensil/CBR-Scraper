import requests
from bs4 import BeautifulSoup 
import pandas as pd

cbr_link = 'https://www.cbr.com'
url = 'https://www.cbr.com/category/movies/news-movies/'
request = requests.get(url)
soup = BeautifulSoup(request.text, 'html.parser')

dic_news = {'Titulo': [], 'Autor': [], 'Tag': [], 'Descricao': [], 'Link': []}

articles = soup.find_all(class_='article')
noticia = 1
for article in articles:
    if noticia == 21:
        break
    article_title = article.find(class_='display-card-title').text.strip()
    article_author = article.find(class_='article-author').text
    article_tag = article.find(class_='dc-tag-label').text
    article_link = cbr_link+ article.find('a')['href']

    article_request = requests.get(article_link)
    article_soup = BeautifulSoup(article_request.text, 'html.parser')
    article_description = article_soup.find(class_='content-block-regular').find('p').text.strip()
    print(f'{noticia}º noticia pega')
    noticia += 1
    dic_news['Titulo'].append(article_title)
    dic_news['Autor'].append(article_author)
    dic_news['Tag'].append(article_tag)
    dic_news['Descricao'].append(article_description)
    dic_news['Link'].append(article_link)


df_news = pd.DataFrame(dic_news)
df_news.to_excel('test.xlsx')









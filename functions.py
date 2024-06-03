import requests
from bs4 import BeautifulSoup 
import pandas as pd
import time


def cbr_scraping(category):
    """Scrapes the latest news from cbr.com in a given category.

    Args:
        category (str): The news category to search for. Must be one of the allowed categories. [Anime, Comics, Game, Movies, Tv].

    Raises:
        ValueError: If the assigned category is not in the list of possibilities.

    Returns:
        dict: A dictionary containing information about the news.
    """
    categories = ['anime', 'comics', 'game', 'movies', 'tv']
    category = category.lower()

    if category not in categories:
        raise ValueError("Invalid category type. Expected one of: %s" % categories)
    
    if category == 'movies' or category == 'tv':
        url = f'https://www.cbr.com/category/{category}/news-{category}/'
    elif category == 'comics':
        url = f'https://www.cbr.com/category/{category}/news/'
    else:
        url = f'https://www.cbr.com/category/{category}-news/'

    cbr_link = 'https://www.cbr.com'

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    dic_news = {'Title': [], 'Author': [], 'Tag': [], 'Description': [], 'Link': []}
    articles = soup.find_all(class_='article')

    print('Starting to add news')
    for i, article in enumerate(articles[:20], 1):
        try:
            article_title = article.find(class_='display-card-title').text.strip()
            article_author = article.find(class_='article-author').text
            article_tag = article.find(class_='dc-tag-label').text
            article_link = cbr_link+ article.find('a')['href']

            article_request = requests.get(article_link)
            article_soup = BeautifulSoup(article_request.text, 'html.parser')
            article_description = article_soup.find(class_='content-block-regular').find('p').text.strip()
            print(f'{i}st {category} news added', end="\r")
            dic_news['Title'].append(article_title)
            dic_news['Author'].append(article_author)
            dic_news['Tag'].append(article_tag)
            dic_news['Description'].append(article_description)
            dic_news['Link'].append(article_link)

            time.sleep(1)
        except AttributeError as e:
            print(f"Error parsing article {i}: {e}")
            continue
        except requests.RequestException as e:
            print(f"Error fetching article {i}: {e}")
            continue
    print(f'All {category} news added')
    return dic_news

def news_to_excel(dic ,file_name):
    """Saves news in an Excel file.

    Args:
        dic (dict): The dictionary containing news information.
        file_name (str): The name of the Excel file to save the news data
    """
    news_df = pd.DataFrame(dic)
    news_df.to_excel(f'{file_name}.xlsx', index=False)

def search_news(category, file_name='news'):
    """Searches for the latest news from cbr.com for a given category and saves it to an Excel file.

    This function scrapes the latest news articles from cbr.com based on the specified category,
    and then saves the collected news data into an Excel file.

    Args:
        category (str): The news category to search for. Must be one of the allowed categories. [Anime, Comics, Game, Movies, Tv].
        file_name (str, optional): The name of the Excel file to save the news data. Defaults to 'news'.

    Raises:
        ValueError: If the assigned category is not in the list of possibilities.
    """
    dic_news = cbr_scraping(category)
    news_to_excel(dic_news, file_name)

# CBR News Scraper

Este projeto faz a raspagem dos artigos de notícias mais recentes do site [CBR.com](https://www.cbr.com/) em uma categoria especificada e salva os dados coletados em um arquivo Excel. Ele utiliza as bibliotecas `requests`, `BeautifulSoup` e `pandas` para buscar, analisar e armazenar os dados das notícias.

## Funcionalidades

- Raspa artigos de notícias do CBR.com nas seguintes categorias: Anime, Comics, Game, Movies, TV.
- Extrai informações como título, autor, tag, descrição e link para o artigo completo.
- Salva os dados das notícias raspadas em um arquivo Excel.

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seuusuario/cbr-news-scraper.git
    cd cbr-news-scraper
    ```

2. Instale as bibliotecas necessárias:
    ```sh
    pip install requests beautifulsoup4 pandas
    ```
    
<br>

## Uso

A principal função a ser utilizada é `search_news`, que raspa os artigos de notícias para uma categoria especificada e os salva em um arquivo Excel.

### Função: `search_news`

```python
from cbr_scraper import search_news

# Raspa as últimas notícias de Anime e salva em 'anime_news.xlsx'
search_news('Anime', 'anime_news')

# Raspa as últimas notícias de Filmes e salva no padrão 'news.xlsx'
search_news('Movies')
```

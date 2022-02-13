import requests
import bs4
from pprint import pprint
base_url = 'https://habr.com/'
url = 'https://habr.com/ru/all/'
KEYWORDS = ['WebMoney']
response = requests.get(url)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    name_article = article.find(class_="tm-article-snippet__title-link").find('span').text
    for keyword in KEYWORDS:
        if keyword in name_article:
            url_article = base_url + article.find(class_="tm-article-snippet__title-link").attrs['href']
            date_article = article.find(class_="tm-article-snippet__datetime-published").find('time').text
            result = f'Статья опубликована {date_article}, Название статьи: {name_article}, ссылка на статью {url_article}'
            print(result)

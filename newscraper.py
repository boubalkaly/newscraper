from bs4 import BeautifulSoup
import urllib.request


quote_page = 'https://techcrunch.com/'

page = urllib.request.urlopen(quote_page)

html = page.read()


soup = BeautifulSoup(html, 'html.parser')

news_feed = soup.find_all('a', class_='post-block__title__link') + soup.find_all(
    'h3', class_='mini-view__item__title') + [soup.find('a', class_='post-block__title__link')]

for news in news_feed:
    print(news.get_text())

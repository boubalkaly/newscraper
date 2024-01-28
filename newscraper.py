from bs4 import BeautifulSoup
import urllib.request
from datetime import date
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' was found... ")


news_categories = ['Latest AI', 'Startups', 'Venture', 'Crypto']

today = date.today()
current_date = today.strftime("%B %d, %Y")


def deliver_ai_news():
    query = "Lastest AI News as of " + current_date
    google_search(query)


def deliver_startup_news():
    pass


def deliver_venture_news():
    pass


def deliver_crypto_news():
    pass


def google_search(query):
    for result in search(query, tld="co.in", num=10, stop=10, pause=2):
        print(result)


while True:  # a loop to see what the choices of the news are
    for i in range(len(news_categories)):  # to display the different options
        print(str(i + 1) + '.', news_categories[i])

    user_news = input('What would you like to learn today? ')
    if not user_news.isdigit() and not int(user_news) in [1, 2, 3, 4]:
        print('Invalid Input, please try again')
        continue
    user_news = int(user_news)
    break


match user_news:
    case 1:
        print('I see you like math a lot')
        deliver_ai_news()
    case 2:
        print("You like money don't you?")
    case 3:
        print("Ah Ah! Okay VC Daddy!")
    case 4:
        print("When you make it please call me")


# quote_page = 'https://techcrunch.com/'

# page = urllib.request.urlopen(quote_page)

# html = page.read()


# soup = BeautifulSoup(html, 'html.parser')

# news_feed = soup.find_all('a', class_='post-block__title__link') + soup.find_all(
#     'h3', class_='mini-view__item__title') + [soup.find('a', class_='post-block__title__link')]

# for news in news_feed:
#     print(news.get_text())

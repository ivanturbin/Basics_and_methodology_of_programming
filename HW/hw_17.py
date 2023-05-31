import requests
import urllib.parse
import random

def season_events(number_of_month, year):
    month_names = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    month_name = month_names[number_of_month - 1]
    url = f'https://ru.wikipedia.org/wiki/{urllib.parse.quote(f"Категория:{month_name.capitalize()}_{year}_года")}'
    response = requests.get(url)
    articles = []
    for line in response.text.split('\n'): 
        if '<a href="/wiki' in line:
            article_title = line.split('title="')[1].split('"')[0]
            articles.append(article_title)
    articles = random.sample(articles, min(len(articles), 5))
    events = ' '.join([f'{i + 1}. {a}' for i, a in enumerate(articles)])
    
    with open('wiki.txt', 'w') as f:
        f.write(f'Вы родились в {month_name} в {year} году. {events}')
season_events(11, 1999) 

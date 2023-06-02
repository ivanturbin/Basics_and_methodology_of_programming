import requests
from urllib.parse import quote
def season_events(number_of_month, year):
    month_names = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                   'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    month_name = month_names[number_of_month-1]
    url = f'https://ru.wikipedia.org/wiki/Категория:{month_name}_{year}_года'
    page = requests.get(url).text
    articles = []
    for line in page.split('\n'):
        if '<a href="/wiki/' in line:
            title_start = line.find('title="') + len('title="')
            title_end = line.find('"', title_start)
            title = line[title_start:title_end]
            articles.append(title)
            if len(articles) == 5:
                break
    with open('wiki.txt', 'w') as f:
        f.write(f'Вы родились в {month_name} в {year} году. ' \
                f'{", ".join(articles)}')
season_events(5, 2004)
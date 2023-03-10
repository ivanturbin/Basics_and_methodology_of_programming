import json

json_data = '''
[
    {
        "name": "Декабрьский Иван",
        "birthday": "01/12/2000"
    },
    {
        "name": "Сергеев Илья",
        "birthday": "25/06/2001"
    },
    {
        "name": "Летняя Мария",
        "birthday": "29.06.1997"
    },
    {
        "name": "Зимний Максим",
        "birthday": "1997-12-05"
    }
]
'''

data = json.loads(json_data)

def calculate_age(birthday):
    if '.' in birthday:
        day, month, year = map(int, birthday.split('.'))
    elif '-' in birthday:
        year, month, day = map(int, birthday.split('-'))
    else:
        day, month, year = map(int, birthday.split('/'))
    today = (2023, 3, 10)
    age = today[0] - year
    if (month, day) > (today[1], today[2]):
        age -= 1
    return age

total_age = sum(calculate_age(person['birthday']) for person in data)
average_age = total_age / len(data)

print("Average age:", average_age)
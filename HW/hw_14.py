import random

# функция для записи результатов в файл
def write_results_to_file(username, attempts):
    with open('game.txt', 'a') as f:
        f.write(f'Имя: {username}, Количество попыток: {attempts}\n')

# Задаем имя пользователя
username = input("Введите ваше имя: ")

# Задаем случайное число
secret_number = random.randint(1, 100)

# Задаем счетчик попыток
attempts = 0

# Игровой цикл
while True:
# Запрашиваем число
    guess = int(input("Угадайте число от 1 до 100: "))
    attempts += 1

# Проверяем, угадал ли пользователь число
    if guess == secret_number:
        print("Вы угадали число!")
        print("Количество попыток:", attempts)
        write_results_to_file(username, attempts)
        break
    elif guess < secret_number:
        print("Задуманное число больше вашего ответа.")
    else:
        print("Задуманное число меньше вашего ответа.")
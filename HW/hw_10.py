secret_list = ["Мавпродош", "Лорнектиф", "Древерол", "Фиригарпиг", "Клодобродыч"]
username = input("Введите свой ник: ")
if username in secret_list:
    print(f"Ты – свой. Приветствую, любезный {username}!")
else:
    print("Тут ничего нет. Еще есть вопросы?")
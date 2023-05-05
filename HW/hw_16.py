import csv
import datetime
import time

# Открываем файл для записи
with open('rows_300.csv', 'w', newline='') as csvfile:
# Задаем разделитель столбцов
    csv_writer = csv.writer(csvfile, delimiter=';')

# Записываем заголовок таблицы
csv_writer.writerow(['№', 'Дата и время', 'Секунда', 'Микросекунда'])

# Записываем 300 строк таблицы
for i in range(1, 301):
# Задаем текущую дату и время
    now = datetime.datetime.now()

# Задаем текущую секунду
second = now.second

# Задаем текущую миллисекунду
microsecond = now.microsecond

# Записываем строку в таблицу
csv_writer.writerow([i, now, second, microsecond])

# Задержка на 0,01 секунды
time.sleep(0.01)
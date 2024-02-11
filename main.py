import requests
import json
from datetime import datetime


# response = requests.get('https://api.github.com')
# print(response)
#
# # преобразование объекта Python в строку JSON
# my_dict = {'name': 'John', 'age': 34, 'city': 'London'}
# json_string = json.dumps(my_dict)
# print(json_string)
#
# # преобразование строки JSON в объект Python
# json_string = '{"name": "Fet", "age": "34", "city": "Novokuznetsk"}'
# my_dict = json.loads(json_string)
# print(my_dict)
#
# # чтение данных из файла и преобразование в объект Python
# with open('data.json', 'r') as f:
#     data = json.load(f)
# print(data)
#
# # запись данных в файл в формате JSON
# with open('data.json', 'w') as f:
#     json.dump(data, f)

def main():
    while True:
        currency = input('Введите название валюты (USD или EUR)')
        if currency not in ('USD', 'EUR'):
            print('Некорректный ввод')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now()

        print(f'Курс {currency} к рублю: {rate}')
        data = {'currency': currency, 'rate': rate, 'timestamp': timestamp}
        save_to_json(data)

        choice = input('Выберите действие: (1 - продолжить, 2 - выйти)')
        if choice == '1':
            continue
        elif choice == '2':
            break
        else:
            print('Нет такого действия')

def get_currency_rate(base):
    pass


def save_to_json(data):
    pass


if __name__ == '__main__':
    main()
import os

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


API_KEY = 'yNVjm1gxJV6KKGEgzFDyYTMxdSmomCfy'
CURRENCY_RATE_FILE = 'currency_rates.json'


def main():
    while True:
        currency = input('Введите название валюты (USD или EUR)')
        if currency not in ('USD', 'EUR'):
            print('Некорректный ввод')
            continue

        rate = get_currency_rate(currency)
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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


def get_currency_rate(base: str) -> float:
    """Получает курс от API и возвращает его в виде float"""

    url = "https://api.apilayer.com/exchangerates_data/latest"
    response = requests.get(url, headers={'apikey': API_KEY}, params={'base': base})
    rate = response.json()['rates']['RUB']
    return rate


def save_to_json(data: dict) -> None:
    """Сохраняет данные в JSON файл"""
    with open(CURRENCY_RATE_FILE, 'a') as f:
        if os.stat(CURRENCY_RATE_FILE).st_size == 0:
            json.dump([data], f)
        else:
            with open(CURRENCY_RATE_FILE) as f:
                data_list = json.load(f)
                data_list.append(data)
            with open(CURRENCY_RATE_FILE, 'w') as f:
                json.dump(data_list, f)


if __name__ == '__main__':
    main()

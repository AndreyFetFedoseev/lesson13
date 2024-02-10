import requests
import json

response = requests.get('https://api.github.com')
print(response)

# преобразование объекта Python в строку JSON
my_dict = {'name': 'John', 'age': 34, 'city': 'London'}
json_string = json.dumps(my_dict)
print(json_string)

# преобразование строки JSON в объект Python
json_string = '{"name": "Fet", "age": "34", "city": "Novokuznetsk"}'
my_dict = json.loads(json_string)
print(my_dict)

# чтение данных из файла и преобразование в объект Python
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)

# запись данных в файл в формате JSON
with open('data.json', 'w') as f:
    json.dump(data, f)

import json


with open('lists.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


if 'lists' in data:
    for item in data['lists']:
        print(f"ID: {item.get('id')}, Name: {item.get('name')}")
else:
    print("No 'lists' key found in the JSON file.")

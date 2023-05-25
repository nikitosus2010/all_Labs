import json
with open('file.json', encoding='utf-8') as f:
    data = json.load(f)
    products=data["products"]
    print(products)
    name = input("Продукт:")
    try:
        price = int(input("Цена:"))
    except ValueError:
        print("неправильна")
    available = input("Наличие:")
    try:
        weight = int(input("Вес:"))
    except ValueError:
        print("неправильна")
    prod ={
        'name': name,
        'price': price,
        'weight': weight,
        'available': available
       }
    products.append(prod)
    print(data)
with open('file.json','w') as f:
    json.dump(data,f)
for prod in products:
    print("Название:",{prod['name']})
    print("Цена:", {prod['price']})
    print("Вес:", {prod['weight']})
    print("Наличие:", {prod['available']})

def z1():

    rus_dict={}
    with open('en-ru.txt', encoding='utf-8') as f:
        d = f.read().strip().split('\n')

        for line in d:
          words = line.split(' - ')
          eng=words[0]
          russ=words[1].split(', ')
          for rus in russ:
             if rus in rus_dict:
                rus_dict[rus].append(eng)
             else:
                rus_dict[rus] = [eng]

    with open('ru-en.txt', 'w') as f:
        for rus in sorted(rus_dict):
            engs = ','.join(sorted(rus_dict[rus]))
            f.write(f"{rus} - {engs}\n")
z1()


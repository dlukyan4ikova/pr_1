import json

def open_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data['products']
    except FileNotFoundError:
        return []

def add_json(file_path, product):
    products = open_json(file_path)
    products.append(product)

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump({"products": products}, file, ensure_ascii=False, indent=4)

def vyivod_products(products):
    if not products:
        print("Нет доступных продуктов.")
        return

    for product in products:
        print(f"Название: {product['name']}")
        print(f"Цена: {product['price']}")
        print(f"Вес: {product['weight']}")
        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")
        print()  # Разделение продуктов

if __name__ == "__main__":
    json_file = 'products.json'
    products = open_json(json_file)

    print("Текущие продукты:")
    vyivod_products(products)

    while True:
        name = input("Добавьте название продукта (или 'выход' для выхода): ")
        if name.lower() == 'выход':
            break

        price = float(input("Введите цену продукта: "))
        weight = float(input("Введите вес продукта: "))
        nalichie = input("В наличии? (да/нет): ").strip().lower()
        available = nalichie == 'да'

        new_product = {
            "name": name,
            "price": price,
            "weight": weight,
            "available": available
        }

        add_json(json_file, new_product)
        print(f"Продукт '{name}' добавлен.\n")

    print("Итоговые продукты:")
    products = open_json(json_file)
    vyivod_products(products)

import json

def open_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data['products']

def vyivod_products(products):
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
    json_file_path = 'products.json'

    products = read_products_from_json(json_file_path)
    display_products(products)

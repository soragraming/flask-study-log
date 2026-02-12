# Dictionary(辞書型)
car = {
    "brand": "Toyota",
    "model": "Corolla",
    "year": 2020
}

print(car.keys())    # dict_keys(['brand', 'model', 'year']
print(car.values())  # dict_values(['Toyota', 'Corolla', 2020]  )
print(car.items())   # dict_items([('brand', 'Toyota'), ('model', 'Corolla'), ('year', 2020)])

print(car["brand"])  # Toyota
print(car.get("bran", "Unknown Brand"))  # Toyota
print(car["model"])  # Corolla
print(car["year"])   # 2020

for k, v in car.items():
    print('key = {}, value = {}'.format(k, v))
# key = brand, value = Toyota
# key = model, value = Corolla
# key = year, value = 2020

if 'brand' in car:
    print('carのブランドは{}'.format(car['brand']))
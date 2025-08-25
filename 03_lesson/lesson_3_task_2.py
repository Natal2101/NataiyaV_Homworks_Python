from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy Z Fold7", "+79112223344"),
    Smartphone("Apple", "iPhone 16", "+79112224455"),
    Smartphone("Xiaomi", "13 Pro", "+7911225566"),
    Smartphone("Honor", "Magic 7 Pro", "+79112226677"),
    Smartphone("Huawei", "Pura 80 Ultra", "+79112227788")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model}. {smartphone.subscriber_number}")

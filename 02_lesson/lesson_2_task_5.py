def month_to_season(mounth):
    if mounth in (1, 2, 12):
        print("Зима")
    elif mounth in (3, 4, 5):
        print("Весна")
    elif mounth in (6, 7, 8):
        print("Лето")
    elif mounth in (9, 10, 11):
        print("Осень")


mounth = int(input("Введите номер месяца: "))

month_to_season(mounth)

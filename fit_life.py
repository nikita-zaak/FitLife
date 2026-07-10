# Проект FitLife - MVP версия 1.0


print("ДОБРО ПОЖАЛОВАТЬ!")
print("-" * 50)
print("Я ваш персональный помощник по здоровью. Давайте знакомиться:)")

user_name = input("Как вас зовут? ", ).strip().title()
print("Красивое имя! А меня зовут — Фитнес.")
print("Буду вам помогать,", user_name, end="!\n")
print("-" * 50)

while True:
    try:
        user_age_str = input("Скажите, сколько вам лет? ")
        user_age_int = int(user_age_str)
        if user_age_int <= 0:
            print("Возраст должен быть больше нуля. Попробуйте ещё раз.")
            continue
        print(user_age_int, "— прекрасный возраст.")
        break
    except ValueError:
        print("Введите только цифры. ")
print()

while True:
    try:
        user_weight_str = input("Введите вес в кг (например, 65): ")
        user_weight = float(user_weight_str)
        if user_weight <= 0:
            print("Введите только положительное число. ")
            continue
        break
    except ValueError:
        print("Введите число")

while True:
    try:
        user_height_str = input("Введите рост в метрах (напр. 1.75, не см): ")
        user_height = float(user_height_str)
        if user_height <= 0:
            print("Введите свой рост")
            continue
        break
    except ValueError:
        print("Введите число с точкой. ")

bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)
status = "норма" if 18.5 <= bmi_rounded < 25 else "не норма"

WATER_PER_KG = 30                  
water_ml = user_weight * WATER_PER_KG 
ML_PER_L = 1000                     
water_l = water_ml / ML_PER_L 
print()
print(f"Ваш ИМТ: {bmi_rounded}, впечатляет?")
print(f"ИМТ: {bmi_rounded} — {status}")

print("-" * 50)
print(f"Отчёт для пользователя: {user_name} ({user_age_int} г.)")
print(f"Ваш Индекс Массы Тела: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print()
print("Расчёт окончен. Будьте здоровы!")

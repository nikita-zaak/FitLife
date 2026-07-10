# Проект FitLife - MVP версия 1.0


from constants import (
    WATER_PER_KG,
    ML_PER_L,
    BMI_LOWER_LIMIT,
    BMI_UPPER_LIMIT,
)

print("ДОБРО ПОЖАЛОВАТЬ!")
print("-" * 50)
print("Я ваш персональный помощник по здоровью. Давайте знакомиться:)")

user_name = input("Как вас зовут? ").strip().title()
print("Красивое имя! А меня зовут — Фитнес.")
print("Буду вам помогать,", user_name, end="!\n")
print("-" * 50)

while True:
    try:
        user_age = int(input("Скажите, сколько вам лет? "))
        if user_age <= 0:
            print("Возраст должен быть больше нуля. Попробуйте ещё раз.")
            continue
        print(user_age, "— прекрасный возраст.")
        break
    except ValueError:
        print("Введите только цифры. ")
print()

while True:
    try:
        user_weight = float(input("Введите вес в кг (например, 65): "))
        if user_weight <= 0:
            print("Введите только положительное число. ")
            continue
        break
    except ValueError:
        print("Введите число")

while True:
    try:
        user_height = float(input("Введите рост в метрах (напр. 1.75): "))
        if user_height <= 0:
            print("Введите свой рост")
            continue
        break
    except ValueError:
        print("Введите число с точкой. ")

bmi = user_weight / (user_height ** 2)
bmi_rounded = round(bmi, 1)
is_normal = BMI_LOWER_LIMIT <= bmi_rounded < BMI_UPPER_LIMIT
status = "норма" if is_normal else "не норма"

water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_L
print()
print(f"Ваш ИМТ: {bmi_rounded}, впечатляет?")
print(f"ИМТ: {bmi_rounded} — {status}")


print("-" * 50)
print(f"Отчёт для пользователя: {user_name} ({user_age} г.)")
print(f"Ваш Индекс Массы Тела: {bmi_rounded}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print()
print("Расчёт окончен. Будьте здоровы!")

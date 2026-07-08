# Проект FitLife - MVP версия 1.0


# 1. Знакомство
print("ДОБРО ПОЖАЛОВАТЬ!")
print("-" * 50)
print("Я ваш персональный помощник по здоровью. Давайте знакомиться :)")

user_name = input("Как вас зовут? ").strip()
user_name = user_name.title()
print("Красивое имя! А меня зовут — Фитнес.")
print("Буду вам помогать,", user_name, end="!\n")
print("-" * 50)


# 2. Сбор данных
input("Давайте приступим к работе, вы готовы? Нажмите Enter...")
user_age_str = input("Скажите, сколько вам лет? ")
user_age_int = int(user_age_str)
print(user_age_int, "— прекрасный возраст.")
print()

user_weight = float(input("Введите вес в кг (например, 65): "))
user_height = float(input("Введите рост в метрах (напр. 1.75, не см): "))


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
print()
input("Я рассчитал ваш ИМТ, хотите узнать его? Нажмите Enter...")
bmi = user_weight / (user_height**2)
print(f"Ваш ИМТ: {round(bmi, 1)}, впечатляет?")
print("-" * 50)


# Подсчет воды: вес * 30 мл
input("А что скажете насчёт нормы воды? Если интересно, нажмите Enter...")
water_ml = user_weight * 30
water_l = water_ml / 1000.0

bmi = round(user_weight / (user_height ** 2), 1)
status = "норма" if 18.5 <= bmi < 25 else "не норма"
print(f"ИМТ: {bmi} — {status}")


# 4. Вывод красивого результата
print("-" * 50)
print(f"Отчёт для пользователя: {user_name} ({user_age_int} г.)")
print(f"Ваш Индекс Массы Тела: {round(bmi, 1)}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л в день")
print()
print("Расчет окончен. Будьте здоровы!")

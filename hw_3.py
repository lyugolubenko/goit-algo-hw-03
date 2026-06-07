import re

def normalize_phone(phone_number):
    # Очищаємо номер телефону від усіх небажаних символів, залишаючи лише цифри
    # Замінюємо всі нецифрові символи на пустий рядок
    clean_number = re.sub(r'\D', '', phone_number)

    # Перевіряємо префікс та додаємо його, якщо потрібно
    if clean_number.startswith('380'):
        sanitized = "+" + clean_number
    elif clean_number.startswith('0'):
        sanitized = "+38" + clean_number
    else:        sanitized = "+" + clean_number

    return sanitized

# Тестування функції на різних форматах номерів телефонів
phone_numbers = ["    +38(050)123-32-34",
                 "     0503451234",
                 "(050)8889900",
                 "38050-111-22-22",
                 "38050 111 22 11   "]
normalized_numbers= [normalize_phone(num) for num in phone_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", normalized_numbers)
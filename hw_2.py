import random

def get_numbers_ticket(min, max, quantity):
    """
    Параметри:
        min (int): Мінімальне число (>= 1)
        max (int): Максимальне число (<= 1000)
        quantity (int): Кількість чисел для вибору
    """

    # Валідація даних. 
    # Повертаємо пустий список, якщо дані некоректні
    if min < 1 or max > 1000 or min >= max or quantity < 1 or quantity > (max - min + 1):
        return []

    # Створюємо діапазон чисел (наприклад, від 1 до 49)
    all_numbers = range(min, max + 1)

    # Отримуємо потрібну кількість унікальних чисел
    result = random.sample(all_numbers, quantity)

    # Сортуємо їх в списку за зростанням і повертаємо
    return sorted(list(result))


# Тестування функції з неправильними даними
print(get_numbers_ticket(-1, 1200, 10))
print(get_numbers_ticket(-10, 10, 5))
print(get_numbers_ticket(1000, 1200, 10))
print(get_numbers_ticket(10, 4, 5))
print(get_numbers_ticket(10, 14, 6))

# Тестування функції з правильними даними
print(get_numbers_ticket(1, 49, 6))
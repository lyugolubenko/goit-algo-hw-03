from datetime import datetime


def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у формат 'РРРР-ММ-ДД' в об'єкт datetime
        date_obj = datetime.strptime(date, "%Y-%m-%d")

        # Отримуємо поточну дату (без часу)
        current_date = datetime.today()

        # Обчислюємо різницю між поточною датою та вказаною датою
        difference = current_date - date_obj

         # Розраховуємо різницю днів
        return difference.days
    except ValueError:
        return (
            "Некоректний формат дати. Введіть дату у форматі 'РРРР-ММ-ДД'."
        )


# Тестуємо функцію з різними датами
print(get_days_from_today("2023-10-03"))
print(get_days_from_today("2025-12-31"))
print(get_days_from_today("2021-10-09"))
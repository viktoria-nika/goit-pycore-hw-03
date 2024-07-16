# Імпортуйте модуль datetime.
from datetime import datetime
# Створюємо функцію, яка розраховує кількість днів між заданою датою і поточною датою.
def get_days_from_today( date : str) -> int:
        # Функція приймає один параметр date, який перетворюємо у ціле число.
        # Враховуємо можливість введення даних у неправильному форматі.
        try:
            date = datetime.strptime (date, "%Y-%m-%d").date()
            # Вказуємо, що введена дата повинна приймати фoрмат 'РРРР-ММ-ДД' та виводити лише дні.
        
        except ValueError:
              return 0
    
        today = datetime.today().date()
        # Отримайте поточну дату, використовуючи datetime.today()

        return (date - today).days
        # Розраховуємо різницю між поточною датою та заданою датою
  
print(get_days_from_today( "2024-10-19"))
# Виводимо результат у днях як ціле число



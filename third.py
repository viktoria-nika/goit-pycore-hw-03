# імпортуємо  модуль re для регулярних виразів для видалення непотрібних символів.
import re
# створюємо функцію для нормальзації телефонного номера, яка приймає один аргумен - це номер телефону. 
def phone_number(number):
#тимчасово її блокуємо для написання коду послідовно
    pass
#маємо телефонній номер для реалізації написання коду
number = "    +38(050)123-32-34"

#за допомогою методу sub у модулі re видаляємо усі відразу символи, окрім циф
pattern = r"\D"
replacement = ""
new_number = re.sub(pattern, replacement, number)

#за допомогою методу removeprefix видаляємо фіксовану частину міжнародного коду.

res = (new_number.removeprefix("38"))

# до телефонного номера додаємо + та код 38 і виводимо результат за домомогою команди print

for nomber in res.split():
    print("Нормалізовані номери телефонів для SMS-розсилки:"f"+38{nomber}")


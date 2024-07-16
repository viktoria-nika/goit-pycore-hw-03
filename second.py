import random
# імпортуемо модуль random для розвязування завдання
# створюємо функцію яка приймає три аргументи min, max, quantity, де всі цілі числа
# створюємо пустий список
# за допомогою циклу if(якщо) прописуємо умови для вибору лотерейних номерів
# використовуємо метод random.randint для отримання випадкових цілих чисел в заданих межах
# за допомогою медота append додаємо до нашого списку лотерейні номери
# використовуючи метод sorted робимо іх унікальні
# викликаємо створену функцію 

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    my_list = []
    if min >=1 and max <=1000 and min < quantity  and quantity < max and max > min :
        while len(my_list) < quantity:
            lottery_numbers = random.randint(min, max)
            if lottery_numbers not in my_list: 
                my_list.append(lottery_numbers)
        return sorted(my_list)
    return my_list

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)



from datetime import datetime, timedelta, date
#імпортуємо всі потрібні нам модулі

def get_users_b(users: list[dict]) -> list[dict]:
#сторюємо функцію, яка приймає список у вигляді словника    
#перевіряємо чи пустий список
    if not users:
        return []
    #дізнаємося який сюгодні день
    to_date = date.today()
    #print(to_date)
    #створюємо пустий список
    res = []
    #проходимось по списку і щукаємо дні народження, переводячи день у потрібний формат, та перетворюючи на поточний рік

    for user in users:
        #print(user["birthday"])

        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").replace(year=to_date.year).date()
        #print() 
        # перевіряємо чи дата народження пройшла 
        if birthday < to_date:
            birthday = birthday.replace(year=to_date.year+1)
        if to_date <= birthday<=to_date+timedelta(days=7):
            #print(user)
            #перевіряємо на який день тижня прийшов день народження, та якщо на вихідні то додаємо у список перетворюючи на потрібний нам формат
            dete_week = birthday.weekday()
            #print(dete_week)
            if dete_week == 5:
                birthday = birthday+timedelta(days=2)
            if dete_week == 6:
                birthday = birthday+timedelta(days=1)
            #print(user["name"],birthday)
            res.append({"name":user["name"],"congratulation_date":birthday.strftime("%Y.%m.%d")})
    return res

users = [
    {"name": "John Doe", "birthday": "1985.07.20"},
    {"name": "Jane Smith", "birthday": "1990.07.21"},
    {"name": "Janna Smith", "birthday": "1990.07.14"},
]

r=get_users_b(users=users)
print(r)


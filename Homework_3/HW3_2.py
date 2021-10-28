def personal(name, lastname, birth, city, email, phone):
    return print(f'Имя: {name} Фамилия: {lastname} Год рождения: {birth} '
                 f'Город: {city} Email: {email} Телефон: {phone}')

personal(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    birth=input('Год Рождения: '),
    city=input('Город: '),
    email=input('email: '),
    phone=input('phone: ')
       )



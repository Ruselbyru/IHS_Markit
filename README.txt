Тестовое задание!

Для создания БД было использована модель Django
Таблица (Blog) из app IHS_Markit.
Поля :
id - создается автоматически моделью (свойсва: NOT NULL AUTO INCREMENT) он же PRIMARY KEY
author - тип CHAR(30) где 30 макс. длина
text - тип TEXT
pud_date - тип DATE

Заполнение таблицы:
Исользовали библиотеку "faker" для генерации случайных величин, таких как имя, текст, дата.
Изпользовали оболочку Python для взаимодействи с API Django:

$ python manage.py shell

>>> from IHS_Markit.models import Blog
>>> from faker import Faker

>>> fake = Faker()

>>> for _ in range (100):
...     name = fake.first_name()
...     date = fake.date_between(start_date='-2y', end_date='now')
...     text = fake.text()
...     note = Blog(author=name, text=text, pub_date=date)
...     note.save()
>>> ^Z
now exiting InteractiveConsole...

API :

Отправляем GET запрос по адресу "http://localhost/api/top10"
Получаем JSON формат [{имя_автора:количество его записей},]

Docker:

1. docker build -t ihs_markit .  создание образа
2. docker run --name ihs -p 8000:8000 -d ihs_markit  запуск контейнера на основе образа

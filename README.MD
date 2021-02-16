# Тестовое задание

## Задача 
Cпроектировать и разработать API для системы опросов пользователей.

## Функционал для администратора системы
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

## Функционал для пользователей системы:
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

## Технологии
Django 2.2.10, Django REST framework.

## Информация
Ссылка на Postman коллекцию для тестирования - https://www.getpostman.com/collections/27c19d2b8e969c8c7d0a

Swagger - http://localhost:8000/swagger/

## Установка для тестирования и разработки
Создать PostgreSQL базу:
SQL_DATABASE=polls_master
SQL_USER=polls_master_user
SQL_PASSWORD=polls_master_321
SQL_HOST=localhost

В корне проекта сделать .env файл, в котором прописать:
DEBUG=True
SECRET_KEY="SOME_SECRET"
DJANGO_ALLOWED_HOSTS="localhost 127.0.0.1"
SQL_DATABASE=polls_master
SQL_USER=polls_master_user
SQL_PASSWORD=polls_master_321
SQL_HOST=localhost
SQL_PORT=5432
DATABASE=postgres

Выполнинть pip install -r requirements.txt

Запустить проект python manage.py runserver 8080
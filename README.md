# Интернет магазин электроники "Megano"

## Структура сайта
* Главная страница.
  * Каталог с фильтром и сортировкой:
  * Сам каталог товаров.
  * Детальная страница товара, с отзывами.
* Оформление заказа:
  * Корзина.
  * Оформление заказа.
  * Оплата.
* Личный кабинет:
  * Профиль.
  * История заказов.
* Административный раздел:
  * Просмотр и редактирование товаров.
  * Просмотр и редактирование заказов.
  * Просмотр и редактирование категорий каталога.
>Примечание: Письма для сброса пароля находятся в папке sent_emails
## Разворачивание проекта
1. `git clone https://gitlab.skillbox.ru/nikita_gorodov/python_django_diploma.git`
2. Активировать виртуальное окружение .env
3. Установить зависимости `pip install -r requirements.txt`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`
6. При необходимости загрузить fixtures `python manage.py loaddata */fixtures/*.json`
> Примечание: при загрузке fixtures создавать superuser (5 пункт) не нужно!

## Запуск сервера

1. Запуск брокера сообщений `redis-server`
2. Запуск очереди задач `celery -A megano worker -l INFO -P solo`
3. Запуск сервера `python manage.py runserver`
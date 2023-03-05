# Интерактивная карта Москвы

---

Посмотреть сайт можно [тут](http://polya.pythonanywhere.com/).
Развернут на pythonanywhere. 
Админка находится по [адресу](http://polya.pythonanywhere.com/admin).

--- 

## Как пользоваться 

Данные на сайт добавляются через админ-панель. В ней есть встроенный текстовый редактор, чтобы не приходилось оформлять данные в виде html-разметки, также можно добавлять картинки (есть возможность перетаскивать их мышкой, чтобы менять порядок добавления). Нужно указать координаты, короткое и длинное описание, приложить картинки - тогда локация появится на сайте.

Кроме  того, локации можно добавлять в формате json, вида:

'''
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://kudago.com/media/images/place/d0/f6/d0f665a80d1d8d110826ba797569df02.jpg",
        "https://kudago.com/media/images/place/66/23/6623e6c8e93727c9b0bb198972d9e9fa.jpg",
        "https://kudago.com/media/images/place/64/82/64827b20010de8430bfc4fb14e786c19.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты птичьего полёта?",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии ...</p>",
    "coordinates": {
        "lat": 55.753676,
        "lng": 37.64
    }
}
'''

Добавление новых локаций через json-файл:

'''python manage.py load_place http://адрес/файла.json'''

---

## Как развернуть

На компьютере уже должен стоять python версии 3. 

Чтобы все заработало, нужно настроить переменные окружения в .env файле. 

```
DEBUG=False #установить True, если не планируете деплоить
SECRET_KEY= # ваш секретный ключ Django
DATABASE_URL= # ссылка на базу данных
ALLOWED_HOSTS='.pythonanywhere.com' # можно указать свой
#STATIC_ROOT= # последние два аргумента необязательные
#MEDIA_ROOT=
```

Скачать проект себе на машину:

```git clone https://github.com/jiezzzzzzz/Moscow-entertainment-map```

Установить зависимости: 

```pip install -r requirements.txt```

Накатить миграций:

```python manage.py migrate```

Создать суперюзера для админки:

```python manage.py createsuperuser```




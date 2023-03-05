# Интерактивная карта Москвы

---

Посмотреть сайт можно [тут](http://polya.pythonanywhere.com/).
Развернут на pythonanywhere. 
Админка находится по [адресу](http://polya.pythonanywhere.com/admin).

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
<span><code>git clone https://github.com/jiezzzzzzz/Moscow-entertainment-map</span></code>

Установить зависимости: 
<span><code>pip install -r requirements.txt</span></code>

Накатить миграций (для этого нужно перейти в папку с проектом):
<span><code>python manage.py migrate</span></code>

Создать суперюзера для админки:
<span><code>python manage.py migrate</span></code>




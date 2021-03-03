# SStest
Test task SunriseStudio
### FAQ
#### Начальная настройка

1. Скачать Репозиторий
2. Установить [Docker](https://docs.docker.com/engine/install/) и [Docker-compose](https://docs.docker.com/compose/install/)
3. Перейти в папку репозитория (файл docker-compose.yml)
4. Создать файл ".env"
5. задать в нем переменные для settings.py:
  
```
DEBUG=True 
SECRET_KEY=foo
DJANGO_ALLOWED_HOSTS="127.0.0.1 [::1],
                     '*',"
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
  
6. Выполнить команду в териманале ```docker-compose up --build```. После для запуска проекта нужна будет только команда ```docker-compose up```
7. Следющие запуски после первичной сборки для запуска: ```docker-compose up``` и  для остановки:```docker-compose down```.
8. Создать администратора ```docker exec -it shop python manage.py createsuperuser```
9. Обращаться к джанго можно через ```docker exec -it shop python manage.py```

#### Письма отправляються в терминал 
Для показа терминала выполните команду в терминле: ```docker-compose logs -f ```

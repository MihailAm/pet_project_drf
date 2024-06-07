После запуска докера установить все миграции
Создать суперюзера
Для работы cron после запуска контейнеров надо выполнить две команды, первая добавляет задачу в крон, вторая запускает крон на выполнение 
docker exec -it testproject-web-1 python manage.py crontab add,
docker exec -it testproject-web-1 service cron start

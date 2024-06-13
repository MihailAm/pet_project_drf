Что необходимо чтоб запустить проект

- Git
- Docker
- Postman (для проверки работоспособности)

Запуск проекта

1. Склонируйте репозиторий:
git clone https://github.com/MihailAm/test_task.git
2. Перейдите в директорию проекта:
cd test_task
3. Соберите и запустите контейнеры:
docker-compose up —build
4. Остановите контейнеры:
docker-compose down
5. Выполните миграции:
docker-compose run web python manage.py migrate
6. Заново запустите все контейнеры:
docker-compose up -d
7. Добавьте cron задачи:
docker exec -it web python manage.py crontab add
8. Запустите cron задачи:
docker exec -it web service cron start

Проверка работоспособности API:

1. Создаем новый запрос в Postman по адресу(метод запроса POST):
http://localhost:8000/api/v1/auth/users/ 
Формат данных: 
{ 
 "username": "user", 
 "email": "user@example.com", 
 "password": "string", 
 "date_of_birth": "2024-06-13" 
} 
2. Создаем второго пользователя на которого будем подписываться, дату рождения ставим завтрашний день(год любой) 
3. Авторизируемся под первым пользователем которого создали, по адресу (метод запроса POST): 
http://localhost:8000/api/v1/auth/token/ 
Копируем access token 
4. Теперь подпишемся на второго созданного пользователя (метод POST). Так же необходимо перейти на вкладку authorization, выбирать тип токена Bearer Token и вставить наш скопированный токен 
http://localhost:8000/api/v1/subscribe/ 
Формат данных: 
{ 
 "subscribed_to": number 
} 
На этом всё

5.Но стоит удостоверится что cron работает

Для этого в консоли стоит написать
docker exec -it web service cron status 
Если ответ failed стоит его перезапустить 
docker exec -it web service cron restart

Теперь проверяем письмо на почте

6.Так же доступен и метод для отписки по адресу: 
http://localhost:8000/api/v1/unsubscribe/<int:subscribed_to_id>'

Так же можно настроить за сколько дней, надо чтоб приходило оповещение о дне рождении для этого при подписки надо указать еще один параметр 
{
"notification_time": number 
}
По дефолту он равен единице, это значит что сообщение придет за один день до дня рождения


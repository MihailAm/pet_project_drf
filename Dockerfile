FROM python:3.12

RUN apt-get update && apt-get install -y cron
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:8000"]
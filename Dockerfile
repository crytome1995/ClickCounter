FROM python:3.9.6-slim

ENV FLASK_APP=app.py \
    FLASK_ENV=production

WORKDIR /application

COPY click_counter/* .
COPY requirements.txt .

RUN pip3 install -r requirements.txt

ENTRYPOINT  gunicorn --workers 2 --bind 0.0.0.0:5000  app:app
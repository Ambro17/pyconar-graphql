FROM python:3.11.4-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV PORT=8080

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENV MUTATIONS_ENABLED=1
CMD gunicorn -w 4 "pyconar.app:create_app()" -b 0.0.0.0:$PORT


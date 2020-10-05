FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV PORT=5050

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app


CMD gunicorn -w 4 "strawapp.flask_app:app" -b 0.0.0.0:$PORT
# [gunicorn", "--bind",  "0.0.0.0:8000", "strawapp.flask_app:app"]

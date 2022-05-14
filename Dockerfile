# pull official base image
FROM python:3.10-slim-buster

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean

# install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# run gunicorn
CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT
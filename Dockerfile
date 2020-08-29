FROM python:3.7.9-alpine3.12
MAINTAINER Enargit Ltd.

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D djangouser
USER djangouser

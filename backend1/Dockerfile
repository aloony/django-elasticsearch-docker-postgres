FROM python:3.7

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y \
    unzip wget sudo less curl gosu build-essential software-properties-common \
    libpq-dev postgresql-client 
    # apt-get clean all && rm /var/apt/lists/* && rm -rf /var/cache/apt/*

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install pipenv
RUN pip install -r requirements.txt
# RUN pipenv install --system





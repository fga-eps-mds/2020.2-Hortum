FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD . /code/

RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /code/src

FROM python:3.9-alpine

LABEL maintainer="luciennajev@hotmail.com"

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

RUN apk update \
  && apk add postgresql-dev \
  && apk add gcc \
  && apk add python3-dev \
  && apk add musl-dev \
  && apk add jpeg-dev \
  && apk add zlib-dev

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .

COPY . .

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]

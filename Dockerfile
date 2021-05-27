FROM python:3.8-alpine AS builder
WORKDIR /app
COPY . /app
RUN apk update
RUN apk add gcc musl-dev git
RUN pip install pipenv

FROM builder AS development
RUN pipenv install --dev

FROM builder AS production
RUN pipenv install

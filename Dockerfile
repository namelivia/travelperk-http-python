FROM python:3.8-alpine AS builder
WORKDIR /app
COPY . /app
RUN apk update
RUN apk add gcc musl-dev git
RUN pip install -I pipenv==2018.11.26

FROM builder AS development
RUN pipenv install --dev
EXPOSE 4444

FROM builder AS production
RUN pipenv install

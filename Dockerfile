FROM python:3.8

# Install pipenv
RUN pip install pipenv

# Copy contents
WORKDIR /app
COPY . /app

# Install dependencies
RUN pipenv install --dev

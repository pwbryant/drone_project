# Pull base image
FROM python:3.7-slim

# Set environmental vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHON UNBUFFERED 1

# Set work dir
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

COPY . /code/

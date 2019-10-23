FROM python:3.8-alpine

#RUN apt-get update && apt-get install -y \
#    gcc \
#    libc-dev \
#    libffi-dev

WORKDIR /app

RUN python -m pip -q --no-cache-dir install poetry && \
    python -m poetry config settings.virtualenvs.create false

COPY pyproject.toml .
COPY poetry.lock .
RUN python -m poetry install -q --no-interaction --no-dev && \
    python -m poetry cache:clear -n --no-interaction pypi --all

COPY . .


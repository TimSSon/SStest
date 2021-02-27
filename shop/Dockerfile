FROM python:3.8.5 as build
ARG RUN_DB_MIGRATIONS_ARG=value
ENV RUN_DB_MIGRATIONS=$RUN_DB_MIGRATIONS_ARG
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY entrypoint.sh /code/
RUN apt-get update && apt-get install --no-install-recommends -y netcat -V \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN chmod +x  /code/entrypoint.sh
COPY . /code/
ENTRYPOINT ["/code/entrypoint.sh"]
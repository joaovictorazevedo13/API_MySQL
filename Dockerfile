FROM mysql:latest

COPY CreateDataBase.sql /docker-entrypoint-initdb.d/
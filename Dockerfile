FROM python:3.8

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

ENV FLASK_APP=appFile.py
ENV FLASK_RUN_HOST=0.0.0.0

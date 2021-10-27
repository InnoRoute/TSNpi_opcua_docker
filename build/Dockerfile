# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
RUN apt update && apt install -y build-essential libxml2-dev libxslt1-dev  python3-wheel libz-dev
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]


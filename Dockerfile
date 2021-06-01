FROM python:3-alpine

RUN python -m pip install --upgrade pip

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN apk add build-base

RUN apk add alpine-sdk

WORKDIR /Probe-Management-System

COPY . /Probe-Management-System

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]

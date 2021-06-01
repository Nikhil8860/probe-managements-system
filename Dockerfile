FROM python:3-alpine

RUN python -m pip install --upgrade pip

WORKDIR /Probe-Management-System

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]
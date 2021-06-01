FROM python:3-alpine

RUN python -m pip install --upgrade pip

WORKDIR /Probe-Management-System

COPY . /Probe-Management-System

RUN pip install --ignore-installed six watson-developer-cloud

RUN pip install Flask==1.1.2 && pip install flask_restful && pip install flask-sqlalchemy==2.3.0 && pip install psycopg2

EXPOSE 5000

ENTRYPOINT  ["python3"]

CMD ["app.py"]
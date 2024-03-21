FROM python:3.8-slim

WORKDIR /api

COPY requirements_flask.txt .

RUN pip3 install -r requirements_flask.txt

COPY app.py .

COPY entrypoint.sh .

CMD [ "python3", "app.py", "runserver" ]
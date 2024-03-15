FROM python:3.8-alpine

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY api.py .

CMD [ "python3", "api.py" ]
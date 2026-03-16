FROM python:3.11-slim

WORKDIR /app

COPY service_a/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY shards/ ./shards/

COPY service_a/ .

CMD ["python","main.py"]
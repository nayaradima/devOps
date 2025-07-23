FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y gcc build-essential netcat-traditional && \
    pip install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]
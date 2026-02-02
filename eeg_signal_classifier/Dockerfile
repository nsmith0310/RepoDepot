FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

COPY data /app/data

ENV TF_CPP_MIN_LOG_LEVEL=3

EXPOSE 8080

CMD ["python", "/app/src/demo.py"]  

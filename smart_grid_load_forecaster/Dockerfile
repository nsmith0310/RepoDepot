FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src /app/src

COPY data /app/data

EXPOSE 8080

CMD ["python", "/app/src/demo.py"]  

FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/app.py src/
COPY src/db.py src/
COPY html/ html/
COPY text/ text/
COPY db/ db/

EXPOSE 5000

CMD ["python", "src/app.py"]

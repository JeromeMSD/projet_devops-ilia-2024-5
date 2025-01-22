FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./src /app/src
EXPOSE 5000

CMD ["python", "src/main.py"]

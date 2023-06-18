FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

COPY . .

FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6

COPY requirements.txt requirements.txt
RUN pip3 install --upgrade --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

COPY . .

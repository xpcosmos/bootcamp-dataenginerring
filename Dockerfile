FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
COPY pipeline.py pipeline.py

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install wget

ENTRYPOINT [ "python", "pipeline.py" ]
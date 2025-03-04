FROM python:latest

WORKDIR /app

COPY requirements.txt requirements.txt
COPY pipeline.py pipeline.py

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get install wget
RUN apt-get install gzip
RUN wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-10.csv.gz
RUN wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
RUN gzip -d green_tripdata_2019-10.csv.gz

ENTRYPOINT [ "python", "pipeline.py" ]
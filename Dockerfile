
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install numpy
RUN command python -m nltk.downloader punkt
RUN python -m nltk.downloader vader_lexicon


COPY . /app/
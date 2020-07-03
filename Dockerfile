FROM python:3.7-slim
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN apt-get update && apt-get install -y \
    sudo \
    g++
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN python3 -m nltk.downloader stopwords
COPY . /app
EXPOSE 5000
CMD exec gunicorn --workers 1 --threads 8 app:app -b :5000
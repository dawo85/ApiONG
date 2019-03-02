FROM python:3.6
ENV PYTHONBUFFERED 1

RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
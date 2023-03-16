FROM python:3.10.9-bullseye

ARG USER=app
ARG USER_ID=1000

ENV APP_USER=$USER

RUN useradd $USER -u $USER_ID -m -r

RUN apt-get update;
RUN apt-get install -y git vim gettext;
RUN apt-get clean;

RUN pip3 install --upgrade pip wheel setuptools supervisor

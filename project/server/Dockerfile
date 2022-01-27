FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install python3 python3-pip python3-opencv
RUN pip install opencv-python numpy hug
RUN groupadd -r hug && useradd -r -g hug hug

ADD main.py /app/main.py
WORKDIR /home/hug
EXPOSE 8585
CMD hug -f /app/main.py -p 8585


FROM ubuntu:20.04
MAINTAINER Ethan

RUN apt update -y
RUN apt upgrade -y

RUN apt install python3 -y
RUN apt install python3-pip -y
RUN 

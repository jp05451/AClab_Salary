FROM ubuntu:20.04
MAINTAINER Ethan

RUN apt update -y
RUN apt upgrade -y

RUN apt install python3 -y
RUN apt install python3-pip -y
RUN apt install git -y
RUN pip3 install pipenv
RUN git clone https://github.com/jp05451/AClab_Salary.git

WORKDIR AClab_Salary
RUN pipenv install

#CMD [ "pipenv run python3 getCurriculum.py" ]
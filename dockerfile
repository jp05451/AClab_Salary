FROM ubuntu:20.04
MAINTAINER Ethan

RUN apt update -y
RUN apt upgrade -y

RUN apt install python3,python3-pip,git -y
RUN pip3 install pipenv
RUN git clone https://github.com/jp05451/Salary.git

RUN cd Salary
RUN pipenv install

CMD [ "pipenv run python3 getCurriculum.py" ]
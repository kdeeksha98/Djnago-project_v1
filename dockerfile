FROM ubuntu:20.04
WORKDIR /book_store
RUN apt-get -qq update
RUN apt-get update
COPY requirement.txt .
RUN apt-get --no-install-recommends -y install python3-dev python3-pip
RUN pip install -r requirement.txt
#RUN sudo apt-get -y install python3 pip3
COPY . .
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000


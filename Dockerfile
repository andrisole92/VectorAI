FROM python:3

ADD ./src /usr/vector/writer/src
ADD ./requirements.txt /usr/vector/writer
ADD ./setup.py /usr/vector/writer
WORKDIR /usr/vector/writer

RUN pip install -e .
RUN ls
RUN pip install -r requirements.txt
WORKDIR /usr/vector/writer/src

CMD [ "python", "./consumer.py" ]
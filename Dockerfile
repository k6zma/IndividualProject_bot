FROM python:3.9.7

WORKDIR /home/k6zma/docker
RUN pip3 install --upgrade setuptools
RUN pip3 install pyTelegramBotAPI==4.10.0
RUN chmod 755 . .
COPY . .

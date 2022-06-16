FROM python:3.8
LABEL maintainer="s446394@sinyi.com.tw"

RUN apt-get update \
        && apt-get upgrade -y \
        && apt-get install -y build-essential python3-dev default-libmysqlclient-dev

# Install project package
WORKDIR /home/to-website

COPY . .

ENV DJANGO_SETTINGS_MODULE towebsite.settings

RUN pip3 install --upgrade pip \
        && pip3 install -r ./config/requirements.txt \
        && mkdir logs \
        && chmod u+x ./config/init.sh

EXPOSE 8000

CMD  ["bash","-c","/home/to-website/config/init.sh"]

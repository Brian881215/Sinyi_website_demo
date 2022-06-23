FROM python:3.8
LABEL maintainer="s446394@sinyi.com.tw"

RUN apt-get update \
        && apt-get upgrade -y \
        && apt-get install -y build-essential python3-dev default-libmysqlclient-dev nginx

# Install odbc 17
RUN apt-get install -y apt-transport-https gnupg2 unixodbc unixodbc-dev \
        && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
        && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
        && apt-get update \
        && ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools \
        && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc \
        && . ~/.bashrc

# Install project package
WORKDIR /home/to-website

COPY . .

RUN pip3 install --upgrade pip \
        && pip3 install -r ./config/requirements.txt \
        && mkdir logs \
        && chmod u+x ./config/init.sh

EXPOSE 80

CMD  ["bash","-c","/home/to-website/config/init.sh"]

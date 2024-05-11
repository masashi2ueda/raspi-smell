FROM nikolaik/python-nodejs:python3.10-nodejs21

RUN apt-get update

RUN yarn global add @vue/cli

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install flask flask-cors

USER pn
WORKDIR /src
FROM --platform=linux/amd64 python:3.11.7-alpine

RUN apt-get update -y
RUN python -m pip install --upgrade pip
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get -y install curl
RUN apt-get install libgomp1

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

WORKDIR /new_vision/bnviit-vision/FastAPI

CMD ["/bin/bash"]
FROM --platform=linux/amd64 python:3.11.7-alpine

# apk를 사용하여 패키지 업데이트 및 설치
RUN apk update && apk add --no-cache \
    curl \
    libgomp \
    bash \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev

# pip 업그레이드
RUN python -m pip install --upgrade pip

# requirements.txt 복사 및 Python 패키지 설치
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# 작업 디렉토리 설정
WORKDIR /app/

# bash를 기본 쉘로 설정
CMD ["/bin/bash"]

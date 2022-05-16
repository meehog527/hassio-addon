ARG BUILD_FROM=ghcr.io/hassio-addons/debian-base/amd64:5.3.0
FROM ${BUILD_FROM}

ARG ARCH=arm64
ARG NODE_VERSION=8.17.0

RUN  \
    apk add --no-cache --virtual .build-dependencies \
        g++=10.3.1_git20211027-r0 \
        gcc=10.3.1_git20211027-r0 \
        libc-dev=0.7.2-r3 \
        linux-headers=5.10.41-r0 \
        make=4.3-r0 \
        py3-pip=20.3.4-r1 \
        python3-dev=3.9.7-r4 \
    \
    && apk add --no-cache \
        git=2.34.2-r0 \
        nodejs=16.14.2-r0 \
        nodejs-dev \
        npm=8.1.3-r0 \
        patch=2.7.6-r7 \
        python3=3.9.7-r4 \
        bluez \
        bluez-lib \
        bluez-dev \
        eudev \ 
        eudev-lib \
        eudev-dev \
        mosquitto-clients \
        ca-certificates \
    \
    && npm config set unsafe-perm true \
    \
    && pip install --no-cache-dir -r /opt/requirements.txt \
    \
    && npm install \
        --no-audit \
        --no-optional \
        --no-update-notifier \
        --only=production \
        --unsafe-perm \
    \
    && npm cache clear --force \
    \

RUN update-ca-certificates --fresh

ADD / /EspruinoHub

WORKDIR /EspruinoHub

RUN npm install \
 && npm cache clean --force

VOLUME ["/EspruinoHub/log"]

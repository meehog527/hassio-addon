ARG BUILD_FROM=ghcr.io/hassio-addons/debian-base/amd64:5.3.0
FROM ${BUILD_FROM}

# Copy root filesystem
COPY rootfs /

WORKDIR /etc/espruinohub

RUN  \
    apk add --no-cache --virtual .build-dependencies \
        g++ \
        gcc \
        libc-dev \
        linux-headers \
        make \
        py3-pip \
        python3\
    \
    && apk add --no-cache \
        nodejs \
        nodejs-dev \
        npm\
        patch \
        python3 \
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

RUN npm install \
 && npm cache clean --force

VOLUME ["etc/espruinohub/log"]

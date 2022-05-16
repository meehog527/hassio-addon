ARG BUILD_FROM=ghcr.io/hassio-addons/debian-base/amd64:5.3.0
FROM ${BUILD_FROM}

ARG ARCH=arm64
ARG NODE_VERSION=8.17.0

# Copy Node-RED package.json
COPY package.json requirements.txt /opt/

# Set workdir
WORKDIR /opt

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

# Copy root filesystem
COPY rootfs /

WORKDIR /etc/espruinohub

RUN npm install \
 && npm cache clean --force

VOLUME ["etc/espruinohub/log"]



# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_DESCRIPTION
ARG BUILD_NAME
ARG BUILD_REF
ARG BUILD_REPOSITORY
ARG BUILD_VERSION

# Labels
LABEL \
    io.hass.name="${BUILD_NAME}" \
    io.hass.description="${BUILD_DESCRIPTION}" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Matt Meehan" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="Home Assistant Community Add-ons" \
    org.opencontainers.image.authors="Matt Meehan" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://addons.community" \
    org.opencontainers.image.source="https://github.com/${BUILD_REPOSITORY}" \
    org.opencontainers.image.documentation="https://github.com/${BUILD_REPOSITORY}/blob/main/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \

ARG BUILD_FROM=ghcr.io/hassio-addons/debian-base/amd64:5.3.0
FROM ${BUILD_FROM}

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Setup base system
ARG BUILD_ARCH=amd64

RUN apk update
RUN apk add --no-cache nodejs
RUN apk add --no-cache npm
RUN apk add --no-cache --virtual .build-dependencies python=2.7.16-r1
RUN apk add --no-cache --virtual .build-dependencies build-base=0.5-r1
RUN apk add --no-cache --virtual .build-dependencies bluez=5.50-r3
RUN apk add --no-cache --virtual .build-dependencies linux-headers=4.19.36-r0
RUN apk add --no-cache --virtual .build-dependencies eudev-dev=3.2.8-r0
RUN apk add --no-cache --virtual .build-dependencies git=2.24.2-r0

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$ARCH.tar.gz" \
 && tar -xzf "node-v$NODE_VERSION-linux-$ARCH.tar.gz" -C /usr/local --strip-components=1 \
 && rm "node-v$NODE_VERSION-linux-$ARCH.tar.gz"

# Copy root file system
# COPY rootfs /

# Build arguments
ARG BUILD_ARCH
ARG BUILD_DATE
ARG BUILD_REF
ARG BUILD_VERSION

WORKDIR /var/espruinohub

COPY run.sh /var/espruinohub/run.sh
RUN chmod +x /var/espruinohub/run.sh

CMD /var/espruinohub/run.sh

# Labels
LABEL \
    io.hass.name="EspruinoHub" \
    io.hass.description="BLE MQTT bridge" \
    io.hass.arch="${BUILD_ARCH}" \
    io.hass.type="addon" \
    io.hass.version=${BUILD_VERSION} \
    maintainer="Matias Käkelä" \
    org.label-schema.description="BLE MQTT bridge" \
    org.label-schema.build-date=${BUILD_DATE} \
    org.label-schema.name="EspruinoHub" \
    org.label-schema.schema-version="0.4.0" \
    org.label-schema.usage="https://github.com/massive/hassio-espruinohub/blob/master/README.md" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/massive/hassio-espruinohub.git" \
    org.label-schema.vendor="Community Hass.io Addons"

ARG BUILD_FROM=hassioaddons/base:7.1.0
FROM ${BUILD_FROM}

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

ENV LANG C.UTF-8

USER root

ARG BUILD_ARCH

RUN apt-get update \
 && apt-get install -y bluetooth \
                       bluez \
                       libbluetooth-dev \
                       libudev-dev \
                       mosquitto-clients \
                       build-essential \
                       python3 \
                       ca-certificates \
 && apt-get clean

RUN update-ca-certificates --fresh

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
    org.label-schema.usage="https://github.com/meehog527/hassio-espruinohub/blob/master/README.md" \
    org.label-schema.vcs-ref=${BUILD_REF} \
    org.label-schema.vcs-url="https://github.com/meehog527/hassio-espruinohub.git" \
    org.label-schema.vendor="Community Hass.io Addons"

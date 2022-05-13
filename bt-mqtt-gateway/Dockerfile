ARG BUILD_FROM=ghcr.io/hassio-addons/base/amd64:11.1.0
FROM ${BUILD_FROM}

# Setup base
ARG BUILD_ARCH=amd64

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# Install requirements for add-on
RUN \
  apk add --no-cache \
    git \
    python3 \
    py3-pip \
    python3-dev \
    py3-setuptools \
    bluez \
    glib \
    glib-dev

#RUN git clone https://github.com/meehog527/bt-mqtt-gateway.git

# Copy root filesystem
COPY rootfs /

# Copy data for add-on
#COPY run.sh /
#RUN chmod a+x /run.sh
#CMD [ "/run.sh" ]

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
    org.opencontainers.image.version=${BUILD_VERSION}

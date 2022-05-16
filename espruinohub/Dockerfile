ARG BUILD_FROM=ghcr.io/hassio-addons/base/aarch64:11.1.2
FROM ${BUILD_FROM}

# Setup base
ARG BUILD_ARCH=aarch64

# Copy Node-RED package.json
COPY package.json requirements.txt /opt/

# Set workdir
WORKDIR /opt

# Set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

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
        bluez-libs \
        bluez-dev \
        eudev \ 
        eudev-libs \
        eudev-dev \
        mosquitto-clients \
        ca-certificates \
        util-linux \
        libcap \
        dbus \
        openrc \
    \
    && npm config set unsafe-perm true \
    \
  #  && pip install --no-cache-dir -r /etc/requirements.txt \
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

# Environment variables
ENV NODE_ICU_DATA=/opt/node_modules/full-icu

# Copy root filesystem
COPY rootfs /

# openrc changes
RUN \
    # Tell openrc its running inside a container, till now that has meant LXC
        sed -i 's/#rc_sys=""/rc_sys="lxc"/g' /etc/rc.conf &&\
    # Tell openrc no need for cgroups signal kill
        sed -i 's/#rc_send_sigkill="YES"/rc_send_sigkill="NO"/g' /etc/rc.conf &&\
    # Tell openrc loopback and net are already there, since docker handles the networking
        echo 'rc_provide="loopback net"' >> /etc/rc.conf &&\
    # no need for loggers
        sed -i 's/^#\(rc_logger="YES"\)$/\1/' /etc/rc.conf &&\
    # can't get ttys unless you run the container in privileged mode
        sed -i '/tty/d' /etc/inittab &&\
    # can't set hostname since docker sets it
        sed -i 's/hostname $opts/# hostname $opts/g' /etc/init.d/hostname &&\
    # can't mount tmpfs since not privileged
        sed -i 's/mount -t tmpfs/# mount -t tmpfs/g' /lib/rc/sh/init.sh &&\
    # can't do cgroups
        sed -i 's/cgroup_add_service /# cgroup_add_service /g' /lib/rc/sh/openrc-run.sh

RUN rc-status

# Set workdir
WORKDIR /etc/espurinohub

RUN npm install \
 && npm cache clean --force

VOLUME ["/etc/espruinohub/log"]

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
    maintainer="Franck Nijhof <frenck@addons.community>" \
    org.opencontainers.image.title="${BUILD_NAME}" \
    org.opencontainers.image.description="${BUILD_DESCRIPTION}" \
    org.opencontainers.image.vendor="Home Assistant Community Add-ons" \
    org.opencontainers.image.authors="Franck Nijhof <frenck@addons.community>" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://addons.community" \
    org.opencontainers.image.source="https://github.com/${BUILD_REPOSITORY}" \
    org.opencontainers.image.documentation="https://github.com/${BUILD_REPOSITORY}/blob/main/README.md" \
    org.opencontainers.image.created=${BUILD_DATE} \
    org.opencontainers.image.revision=${BUILD_REF} \
    org.opencontainers.image.version=${BUILD_VERSION}

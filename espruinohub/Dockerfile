ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

ADD package.json /


RUN \ 
    apk add --no-cache \
        nodejs \
        npm \ 
    && cd / && npm install --unsafe-perm \
    && VERSION="76753003df534b32d2e9dad9fa74aeb0e93876a1" \
    && NODE_PATH="/usr/lib/node_modules" \
    && npm -g i "git+https://github.com/espruino/EspruinoHub.git#${VERSION}" \
    && apk add --no-cache --virtual .build-dependencies \
        python3 \
        bluez \
        linux-headers \
        eudev-dev \
        git 
   
# Copy data for add-on
COPY run.sh /
COPY index.js /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

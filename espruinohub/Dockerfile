ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

ADD package.json /


RUN \ 
    apk add --no-cache \
        nodejs \
        npm \ 
    && git clone "https://github.com/espruino/EspruinoHub.git" \
    && cd EspruinoHub \
    && npm install 
    
    && apk add --no-cache --virtual .build-dependencies \
        python3 \
        bluez \
        linux-headers \
        eudev-dev \
        git 
     && cd / && npm install --unsafe-perm \

#   && npm -g i espruino 
    
# Copy data for add-on
COPY run.sh /
COPY index.js /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]

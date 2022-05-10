ARG BUILD_FROM

FROM ${BUILD_FROM}
ARG ARCH=arm64
ARG NODE_VERSION=8.17.0

RUN apt-get update \
 && apt-get install -y bluetooth \
                       bluez \
                       libbluetooth-dev \
                       libudev-dev \
                       mosquitto-clients \
                       build-essential \
                       python3 \
                       ca-certificates \
                       curl \
 && apt-get clean

RUN update-ca-certificates --fresh

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-$BUILD_FROM.tar.gz" \
 && tar -xzf "node-v$NODE_VERSION-linux-$BUILD_FROM.tar.gz" -C /usr/local --strip-components=1 \
 && rm "node-v$NODE_VERSION-linux-$BUILD_FROM.tar.gz"

ADD / /EspruinoHub

WORKDIR /EspruinoHub

RUN npm install \
 && npm cache clean --force

VOLUME ["/EspruinoHub/log"]

ENTRYPOINT ["node", "index.js"]

COPY run.sh /var/espruinohub/run.sh
RUN chmod +x /var/espruinohub/run.sh

CMD /var/espruinohub/run.sh 

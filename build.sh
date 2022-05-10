docker run --rm --privileged \
    -v ~/.docker:/root/.docker \
    homeassistant/amd64-builder \
    --all \
    -r https://github.com/meehog527/hassio-espruinohub.git \
    -b master \
    -t espruinohub

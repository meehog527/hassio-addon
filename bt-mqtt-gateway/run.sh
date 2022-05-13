#!/usr/bin/with-contenv bashio
# ==============================================================================
# Home Assistant Community Add-on: BT-MQTT Gateway
# Runs BT-MQTT Gateway
# ==============================================================================

bashio::log.info "Starting BT-MQTT Gateway..."
bashio::log.info "Installing python packages..."
pip3 install -r ./requirements.txt
apt-get remove git -y
apt-get clean

bashio::log.info "Initilizing BT-MQTT Gateway..."
python3 gateway.py

#!/bin/bash
set -e

CONFIG_PATH=/data/options.json
CONNECTION_STRING="$(jq --raw-output '.connectionString' $CONFIG_PATH)"

echo Hello!
node -v
npm -v
npm install
node index.js


#!/bin/bash

function log_info {
	echo -e $(date '+%Y-%m-%d %T')"\e[1;32m $@\e[0m"
}

function start_espruino_hub {
	log_info "Starting EspruinoHub"
	BLENO_ADVERTISING_INTERVAL=300 NOBLE_MULTI_ROLE=1 node /usr/lib/node_modules/EspruinoHub/index.js
}

function terminate_container {
  kill ${spid}
  if [ $pid -ne 0 ]; then
    kill -SIGTERM "$pid"
    wait "$pid"
  fi
  log_info "EspruinoHub stopped"
  exit 0 # finally exit main handler script
}

trap "terminate_container" SIGTERM

log_info "Initializing Container"

cp -v /data/options.json config.json

while true
do
	start_espruino_hub
	export pid=${!}	
	sleep 1s &
	export spid=${!}
	wait $spid
done

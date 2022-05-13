from mqtt import MqttMessage
from workers.base import BaseWorker
import bluetooth
import json

REQUIREMENTS = ["bluepy"]

class TestWorker(BaseWorker):
  def _setup(self):
    self._some = 'variable'

  def status_update(self):
    found_devices = bluetooth.discover_devices(lookup_names = True, lookup_class = True)
    reported_devices = []
    for addr, name, device_class in found_devices:
      device = {
            "name": name,
            "address": address,
            "device_class": device_class
          }
      reported_devices.append(device)
    json_devices = json.dumps(reported_devices)
    return [MqttMessage(topic=self.format_topic('number'), payload=str(found_devices))]

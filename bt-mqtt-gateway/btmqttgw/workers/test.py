from mqtt import MqttMessage
from workers.base import BaseWorker

REQUIREMENTS = ["bluepy"]

class TestWorker(BaseWorker):
  def _setup(self):
    self._some = 'variable'

  def status_update(self):
    return [MqttMessage(topic=self.format_topic('time'), payload="test")]

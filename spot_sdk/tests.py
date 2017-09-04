import random
import unittest
from datetime import datetime

from spot_sdk import Feed, Message

class TestMessage(unittest.TestCase):

  raw_message = {
    "@clientUnixTime": "0",
    "id": 823677113,
    "messengerId": "0-3049668",
    "messengerName": "svcatsaway",
    "unixTime": 1504560201,
    "messageType": "UNLIMITED-TRACK",
    "latitude": 44.26225,
    "longitude": -76.37656,
    "modelId": "SPOT3",
    "showCustomMsg": "Y",
    "dateTime": "2017-09-04T21:23:21+0000",
    "batteryState": "GOOD",
    "hidden": 0,
    "altitude": 74
  }

  def test_creating_message(self):
    message = Message(self.raw_message)

    self.assertTrue(message.type == "UNLIMITED-TRACK")
    self.assertTrue(message.battery_state == "GOOD")
    self.assertTrue(message.latitude == 44.26225)
    self.assertTrue(message.longitude == -76.37656)
    self.assertTrue(message.datetime == datetime(2017, 9, 4, 21, 23, 21))
    self.assertTrue(message.content == Message.NO_MESSAGE_CONTENT)
    self.assertTrue(message.raw == self.raw_message)

if __name__ == '__main__':
    unittest.main()

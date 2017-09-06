import random
import unittest
from unittest.mock import patch, mock_open
from datetime import datetime

from spot_sdk import Feed, Message, SpotSDKError

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

    self.assertTrue(message.id == 823677113)
    self.assertTrue(message.type == "UNLIMITED-TRACK")
    self.assertTrue(message.battery_state == "GOOD")
    self.assertTrue(message.latitude == 44.26225)
    self.assertTrue(message.longitude == -76.37656)
    self.assertTrue(message.datetime == datetime(2017, 9, 4, 21, 23, 21))
    self.assertTrue(message.content == Message.NO_MESSAGE_CONTENT)
    self.assertTrue(message.raw == self.raw_message)

  def test_with_content(self):
    raw_message = self.raw_message
    content = "The cats are purring"
    raw_message['messageContent'] = content
    message = Message(raw_message)

    self.assertTrue(message.content == content)


class TestFeed(unittest.TestCase):
  success_json_reponse = open('spot_sdk/sample_success_response.json', 'r').read()
  mock_success_urlopen = mock_open(read_data=success_json_reponse)
  @patch('urllib.request.urlopen', mock_success_urlopen)
  def test_creating_feed(self):
    feed = Feed('ValidApiKey')
    feed.collect()
    self.assertTrue(feed.count() == 2)
    self.assertTrue(feed.first().id == 823675096)
    self.assertTrue(feed.last().id == 823674967)
    self.assertTrue(isinstance(feed.messages, list))

  error_json_reponse = open('spot_sdk/sample_error_response.json', 'r').read()
  mock_error_urlopen = mock_open(read_data=error_json_reponse)
  @patch('urllib.request.urlopen', mock_error_urlopen)
  def test_incorrect_api_key(self):
    with self.assertRaises(SpotSDKError):
      Feed('InvalidApiKey').collect()

if __name__ == '__main__':
    unittest.main()

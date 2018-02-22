import urllib.request
import json
from datetime import datetime


class SpotSDKError(Exception):
    pass


class Message(object):
  def __init__(self, raw_message):
    if not isinstance(raw_message, dict):
      raise SpotSDKError('message should be dictionary')

    self.id =            raw_message['id']
    self.type =          raw_message['messageType']
    self.battery_state = raw_message['batteryState']
    self.latitude =      raw_message['latitude']
    self.longitude =     raw_message['longitude']
    self.datetime =      datetime.utcfromtimestamp(raw_message['unixTime'])
    self.content =       self.__content(raw_message)
    self.raw =           raw_message

  NO_MESSAGE_CONTENT = 'No message content'

  def __content(self, raw_message):
    if 'messageContent' in raw_message:
      return raw_message['messageContent']
    else:
      return self.NO_MESSAGE_CONTENT


class Feed(object):
  def __init__(self, key):
    if not isinstance(key, str):
      raise SpotSDKError('key should be string')
    self.key      = key
    self.messages = []

  BASE_URL = 'https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/'

  def __request_url(self):
    return self.BASE_URL + self.key + '/message.json'

  def first(self):
      return self.messages[0]

  def last(self):
      return self.messages[-1]

  def count(self):
      return len(self.messages)

  def collect(self):
    self.collected_at = datetime.now()

    url          = self.__request_url()
    raw_response = urllib.request.urlopen(url).read().decode('utf8')
    response     = json.loads(raw_response)['response']

    if 'errors' in response.keys():
      raise SpotSDKError(response['errors']['error']['text'])

    raw_messages = response['feedMessageResponse']['messages']['message']
    self.__create_messages(raw_messages)

  def __create_messages(self, raw_messages):
    for raw_message in raw_messages:
        self.messages.append(Message(raw_message))

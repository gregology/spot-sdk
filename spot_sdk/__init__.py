import urllib.request
import json
from datetime import datetime


class SpotSDKError(Exception):
    pass

class SpotMessage(object):
  def __init__(self, raw_message):
    if not isinstance(raw_message, dict):
      raise SpotSDKError('message should be dictionary')
    self.__dict__.update(raw_message)
    self.raw_message = raw_message
    self.fields      = raw_message.keys()

class SpotFeed(object):

  BASE_URL = 'https://api.findmespot.com/spot-main-web/consumer/rest-api/2.0/public/feed/'

  def __init__(self, key):
    if not isinstance(key, str):
      raise SpotSDKError('key should be string')
    self.key = key
    self.collect_messages()

  def __request_url(self):
    return self.BASE_URL + self.key + '/message.json'

  def collect_messages(self):
    self.messages     = []
    self.collected_at = datetime.now()

    url          = self.__request_url()
    raw_response = urllib.request.urlopen(url).read()
    response     = json.loads(raw_response)['response']

    if 'errors' in response.keys():
      raise SpotSDKError(response['errors']['error']['text'])

    self.__dict__.update(response['feedMessageResponse']['feed'])
    self.__create_spot_messages(response['feedMessageResponse']['messages']['message'])

  def __create_spot_messages(self, raw_messages):
    for raw_message in raw_messages:
        self.messages.append(SpotMessage(raw_message))

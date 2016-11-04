"""
    @Author Gustavo García

    This class communicates with the Yandex API.
    In order to use the translate servicem you need
    to give your key in https://tech.yandex.com/keys/get/?service=trnsl
    and paste it into KEY constant.

    Do not touch the constants A and B unless that Yandex 
    will update their API (The current version is 1.6).
"""

import requests
import json
import collections
from providers.yandex import YandexProvider
from providers.google import GoogleProvider
from providers.microsoft import MicrosoftProvider


class Translator:

    def set_provider(self, name):
        if name == "yandex":
            self.provider = YandexProvider()
        elif name == "google":
            self.provider = GoogleProvider()
        elif name == "microsoft":
            self.provider = MicrosoftProvider() 

    def get_langs(self):
        return self.provider.get_langs()

    def translate(self, text, _from, _to):
        return self.provider.translate(text, _from, _to)
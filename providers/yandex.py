"""
    @Author Gustavo García

    This is the Yandex provider. Implements the abstract methods
    of AbstractProvider.
    The constants LANGS, KEYS and TRANSLATE stored the Yandex
    API's data to be used.
"""

from providers.abstract import AbstractProvider
import collections


LANGS_URL = "https://translate.yandex.net/api/v1.5/tr.json/getLangs"
KEY = "trnsl.1.1.20161101T171829Z.5dea93ff6b9a868a.014e82c30d19754abdc1d471af2891ea274572a8"
TRANSLATE_URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"

class YandexProvider(AbstractProvider):

    def parse_langs(self, res):
        langs = res.get("langs")
        ordered_langs = collections.OrderedDict(sorted(
                            langs.items(),
                            key=lambda t: t[1]))
        return ordered_langs

    def parse_translation(self, res):
        return "".join(res.get("text"))


    def build_langs_url(self):
        return "{url}?ui=en&key={key}" \
                .format(url = LANGS_URL, key = KEY)
    
    def build_translate_url(self, text, _from, _to):
        return "{url}?key={key}&lang={lang}&text={text}" \
                .format(url = TRANSLATE_URL, key = KEY, text = text, 
                        lang = "".join((_from, "-", _to)))
    
    def check_langs_status(self, code):
        if code == 401:
            raise Exception("Your API key is invalid")
        elif code == 402:
            raise Exception("Your API key was blocked")

    def check_translation_status(self, code):
        if code == 401:
            raise Exception("Your API key is invalid")
        elif code == 402:
            raise Exception("Your API key was blocked")
        elif code == 404:
            raise Exception("You have exceeded the daily limit of translated text")
        elif code == 413:
            raise Exception("You have exceeded the maximum text size")
        elif code == 422:
            raise Exception("Text cannot be translated")
        elif code == 501:
            raise Exception("The specified translation direction is not supported")
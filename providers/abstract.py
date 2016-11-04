"""
    @Author Gustavo García

    This is an abstract class that abstract the most part
    of the translation process.
    The concrete implementations must be override the
    abstract methods.
"""

from abc import ABCMeta, abstractmethod
import requests


class AbstractProvider(metaclass = ABCMeta):

    def get_langs(self):
        LANGS_URL = self.build_langs_url()
        req = requests.post(LANGS_URL)
        res = req.json()
        status_code = res.get("code")
        try:
            self.check_langs_status(status_code)
            langs = self.parse_langs(res)
            return langs
        except Exception as e:
            raise e

    def translate(self, text, _from, _to):
        TRANSLATE_URL = self.build_translate_url(text, _from, _to)
        req = requests.post(TRANSLATE_URL)
        res = req.json()
        status_code = res.get("code")
        try:
            self.check_translation_status(status_code)
            trans_text = self.parse_translation(res)
            return trans_text
        except Exception as e:
            raise e

    """
        Get the languages from the response and sort them.

        @param res response object
        @return the ordered langs
    """
    @abstractmethod
    def parse_langs(self, res):
        pass

    """
        Get the translated text from the response.

        @param res response object
        @return the translated text
    """
    @abstractmethod
    def parse_langs(self, res):
        pass

    """
        Build the lang discovery URL of the provider.

        @return the built URL
    """
    @abstractmethod
    def build_langs_url(self):
        pass

    """
        Build the translate URL of the provider.

        @param text text to translate
        @param _from origin lang
        @param _to target lang
        @return the build URL
    """
    @abstractmethod
    def build_translate_url(self, text, _from, _to):
        pass

    """
        Check the status code of the langs discovery response.
        Each provider has a specified status of the response
        with it meaning.
        If there are problems, a Exception is raised.
    """
    @abstractmethod
    def check_langs_status(self, code):
        pass

    """
        Check the status code of the translation response.
        Each provider has a specified status of the response
        with it meaning.
        If there are problems, a Exception is raised.
    """
    @abstractmethod
    def check_translation_status(self, code):
        pass

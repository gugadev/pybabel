# [Pybabel](https://github.com/guzgarcia/pybabel)

Translate text using the most popular available providers.

<p align="center">
    <img src="https://cdn.rawgit.com/guzgarcia/pybabel/master/extra/screenshot.jpg"/>
</p>

## Run from source

You need to install Python 3.x and PyQt5 to run the application.

## Extend

This application is designed to be extensible, all provider-specific behaviour is inyected inside application extending the `AbstractProvider` class. This class only show to `Translator` class two methods: `get_langs` and `translate`. The provider-specific methods must be implemented by him. So, if you want add new providers then you must create a class extending `AbstractProvider` and implement the abstract methods as show the following class diagram:

<p align="center">
    <img src="https://cdn.rawgit.com/guzgarcia/pybabel/master/extra/class-diagram.jpg"/>
</p>

**Methods that providers must implement:**
- `build_langs_url`: build the URL to fetch the langs using this povider parameters.
- `build_translate_url`: build the URL to translate text using the provider parameters
- `parse_langs`: read the response object, extract, sort the languages and return them.
- `parse_translation`: read the response object, extract the processed text and return it.
- `check_langs_status`: check the status of the langs request.
- `check_translation_status`: check the status of the translation request.

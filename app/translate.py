import json
import requests
from flask_babel import _
from flask import current_app


def translate(text, source_language, dest_language):
    # Use below when registered with Microsoft Translate.
    """if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {
        'Ocp-Apim-Subscription-Key': current_app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'westus2'}
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com'
        '/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language), headers=auth, json=[
                {'Text': text}])
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()[0]['translations'][0]['text']"""

    # Test config for LibreTranslate.
    headers = {"Content-Type": "application/json"}  # Not sure how to use this.
    r = requests.post(
        'https://libretranslate.com/translate',
        json={'q': text, 'source': source_language, 'target': dest_language})
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return r.json()['translatedText']

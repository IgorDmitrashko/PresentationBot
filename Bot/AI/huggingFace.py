import requests


from deep_translator import GoogleTranslator
from Bot.Model.config import API_KEY_AI

class HuggingFace:
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    HEADERS = {"Authorization": f"Bearer {API_KEY_AI}"}
    def __init__(self):
        None

    def geterate_answer(self, prompt):
        try:
            text = self.__translate_large_text(prompt)
            payload = {"inputs": text, "parameters": {"max_length": 150, "temperature": 0.7}}
            response = requests.post(self.API_URL, headers=self.HEADERS, json=payload)

            return self.__translate_large_text(response.json()[0]['generated_text'], source='en', target='uk')
        except Exception as ex:
            return f"О{ex}"


    def __translate_large_text(self, text, source='uk', target='en'):
        return GoogleTranslator(source=source, target=target).translate(text)




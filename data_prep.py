import pandas as pd
import requests

API_KEY = 'KEY'
TRANSLATE_URL = f"https://translation.googleapis.com/language/translate/v2?key={API_KEY}"
TRANSLITERATE_URL = "https://translate.googleapis.com/translate_a/single"


def get_translation(word):
    data = {
        'q': word,
        'source': 'he',
        'target': 'en'
    }
    try:
        response = requests.post(TRANSLATE_URL, data=data)
        response.raise_for_status()
        return response.json()['data']['translations'][0]['translatedText']
    except requests.exceptions.RequestException:
        return None


def get_pronunciation(word):
    params = {
        'client': 'gtx',
        'sl': 'he',
        'tl': 'en',
        'dt': 'rm',
        'q': word
    }
    try:
        response = requests.get(TRANSLITERATE_URL, params=params)
        response.raise_for_status()
        result = response.json()

        for item in result[0]:
            if item and len(item) > 1 and isinstance(item[1], str) and item[1].isascii():
                return item[1]

        return word
    except Exception:
        return word


def build_dataset(txt_file_path, csv_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]

    data = []

    for word in words:
        english_word = get_translation(word)

        if english_word:
            pronunciation = get_pronunciation(word)

            data.append({
                "Hebrew": word,
                "English": english_word,
                "Pronunciation": pronunciation
            })

    df = pd.DataFrame(data)

    df.to_csv(csv_file_path, index=False, encoding='utf-8-sig')

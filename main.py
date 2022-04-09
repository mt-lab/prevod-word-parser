from bs4 import BeautifulSoup
import requests


def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


def get_word(query_word):
    target_url = "https://en.wiktionary.org/wiki/" + query_word + "#Russian"
    page_text = requests.get(target_url)
    parsed_html = BeautifulSoup(page_text.text, features="html.parser")
    for nominal_noun_form in parsed_html.select('span[class*="Cyrl form-of lang-ru nom|s-form-of origin"]'):
        return nominal_noun_form.text.strip()


print(get_word("сабля"))

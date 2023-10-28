import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """Fungsi ini digunakan untuk mengambil data dari Wikipedia"""
    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki


def search_wiki(name):
    """Mencari halaman Wikipedia dengan nama tertentu"""
    results = wikipedia.search(name)
    return results


def phrase(name):
    """Mengembalikan frasa-frasa dari Wikipedia"""
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases

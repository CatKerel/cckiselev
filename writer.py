from html_parser import get_soup
from bs4 import BeautifulSoup, element
from googletrans import Translator


def replace_tag_with_child(tag, translated):

    print([type(cont) for cont in tag.find_all(text=True)])
    for subtag in tag.find_all(text=True):
        if isinstance(subtag, element.NavigableString):
            print(subtag)
            print(subtag.parent)
            substring = str(subtag)
            for en, hi in translated:
                substring = substring.replace(en, hi)
            print(substring)
            subtag.replace_with(substring)


def replace(filename, translated):
    soup = get_soup(filename)
    tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'li', 'p', 'a', 'strong', 'span', 'button', 'i'])
    for tag in tags:
        if not len(tag.find_all()):
            for en, hi in translated:
                tag.string = tag.text.replace(en, hi)
    for tag in tags:
        if len(tag.text) and len(tag.find_all()):
            replace_tag_with_child(tag, translated)
    return soup


def write(filename, text):
    with open('hindi/' + filename, 'w', encoding='utf-8') as html:
        html.write(str(replace(filename, text)))
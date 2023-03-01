from html_parser import get_soup
from bs4 import element


def replace_tag_with_child(tag, translated):
    for subtag in tag.find_all(text=True):
        if isinstance(subtag, element.NavigableString):
            substring = str(subtag)
            for en, hi in translated:
                substring = substring.replace(en, hi)
            subtag.replace_with(substring)


def replace(filename, translated):
    soup = get_soup(filename)
    tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'li', 'p', 'a', 'strong', 'span', 'button', 'i', 'label', 'option', 'input'])
    for tag in tags:
        if not len(tag.find_all()):
            for en, hi in translated:
                tag.string = tag.text.replace(en, hi)
    for tag in tags:
        if tag.name == 'input':
            if 'placeholder' in list(tag.attrs.keys()):
                string = str(tag.attrs['placeholder'])
                for en, hi in translated:
                    string = string.replace(en, hi)
                tag.attrs['placeholder'] = string
    for tag in tags:
        if len(tag.text) and len(tag.find_all()):
            replace_tag_with_child(tag, translated)
    return soup


def write(filename, text):
    with open('hindi/' + filename, 'w', encoding='utf-8') as html:
        html.write(str(replace(filename, text)))
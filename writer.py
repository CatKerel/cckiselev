from html_parser import get_soup


def replace(filename, text):
    soup = get_soup(filename)
    tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'li', 'p', 'a', 'strong', 'span', 'button', 'i'])
    for tag in tags:
        if not len(tag.find_all()):
            for en, hi in text:
                tag.string = tag.text.replace(en, hi)
    for tag in tags:
        if len(tag.text) and len(tag.find_all()):
            print(type(tag))
            print(type(tag.text))
            print(str(tag))
            print(str(tag).replace('>', '<').split('<')) # split by < and >x  even numbers
    return soup


def write(filename, text):
    with open('hindi/' + filename, 'w', encoding='utf-8') as html:
        html.write(str(replace(filename, text)))
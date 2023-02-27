from bs4 import BeautifulSoup


def get_soup(filename):
    with open(filename, 'r', encoding='utf-8') as html:
        html_text = html.read()
        soup = BeautifulSoup(html_text, 'html.parser')
        return soup


def get_text(filename):
    soup = get_soup(filename)
    elems = soup.find_all(['h1', 'h2', 'h3', 'h4', 'li', 'p', 'a', 'strong', 'span', 'button', 'i'])
    texts = list()
    for elem in elems:
        elem_text = str(elem).replace('>', '<').split('<')
        text = [elem_text[i].strip() for i in range(len(elem_text)) if not i % 2 and elem_text[i] not in ['', '\n']]
        #lines = (line.strip() for line in elem.text.splitlines())
        #chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        #text = '\n'.join(chunk for chunk in chunks if chunk)
        #texts.extend(text.split(' ')) #разбивает на слова, лучше переводить фразами и отсортировать словарь по длине по убыванию
        #texts.extend(text.split('\n'))
        texts.extend(text)
    texts = [i for i in texts if i != '']
    texts.sort(key=len)
    texts = texts[::-1]
    return list(dict.fromkeys(texts))
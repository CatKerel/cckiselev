from translator import translate
from html_parser import get_text
from writer import write

filenames = ['www.classcentral.com/index.html']
for filename in filenames:
    text = get_text(filename)
    text = translate(text)
    write(filename, text)
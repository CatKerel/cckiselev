from translator import translate
from html_parser import get_text
from writer import write
from html_searcher import search_htmls_1
import sys
import time


exclude = ['www.classcentral.com/institutions.html',
        'www.classcentral.com/index.html',
        'www.classcentral.com/about.html',
        'www.classcentral.com/contact.html',
        'www.classcentral.com/collections.html'
        'www.classcentral.com/help.html',
        'www.classcentral.com/providers.html',
        'www.classcentral.com/rankings.html',
        'www.classcentral.com/signup.html',
        'www.classcentral.com/subjects.html',
        'www.classcentral.com/lists.html']

#filenames = [i for i in search_htmls() if i not in exclude]
#filenames = ['www.classcentral.com/index.html']
filenames = search_htmls_1()[int(sys.argv[1]):int(sys.argv[2])]
print(len(filenames))
i = 0
for filename in filenames:
    i = i + 1
    print(filename, i)
    text = get_text(filename)
    try:
        text = translate(text)
    except:
        try:
            time.sleep(5)
            text = translate(text)
        except:
            time.sleep(5)
            text = translate(text)
    write(filename, text)
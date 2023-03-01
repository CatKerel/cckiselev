from os import walk
import requests
from selenium import webdriver
import time


htmls = []
for (dirpath, dirnames, filenames) in walk(r'C:\Users\gibbo\class\www.classcentral.com\subject\wrong'):
    for filename in filenames:
        if len(filename.split('.')) == 2 and filename.split('.')[1] == 'html' and 'hindi' not in dirpath.split('\\'):
            htmls.append('/'.join(str(dirpath + '\\' + filename).replace('\\', '/').split('/')[4:]))

print(htmls)
wb = webdriver.Chrome()
for html in htmls:
    url = html.replace('/wrong', '').replace('.html', '')
    wb.get(f'https://{url}')
    time.sleep(5)
    with open(html, 'w', encoding='utf-8') as html_file:
        print(html)
        html_file.write(wb.page_source)
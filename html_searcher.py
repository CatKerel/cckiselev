from os import walk, getcwd

def search_htmls():
    htmls = []
    for (dirpath, dirnames, filenames) in walk(getcwd()):
        for filename in filenames:
            if len(filename.split('.')) == 2 and filename.split('.')[1] == 'html' and 'hindi' not in dirpath.split('\\'):
                htmls.append('/'.join(str(dirpath + '\\' + filename).replace('\\', '/').split('/')[4:]))
    return htmls


def search_htmls_1():
    htmls = []
    for (dirpath, dirnames, filenames) in walk(r'C:\Users\gibbo\class\www.classcentral.com\subject\wrong'):
        for filename in filenames:
            if len(filename.split('.')) == 2 and filename.split('.')[1] == 'html' and 'hindi' not in dirpath.split('\\'):
                htmls.append('/'.join(str(dirpath + '\\' + filename).replace('\\', '/').split('/')[4:]))
    return htmls
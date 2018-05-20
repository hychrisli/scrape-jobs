from os.path import dirname, realpath 
from lxml import html, etree

fileDir = realpath(__file__)
rootDir = dirname(dirname(fileDir))
dataFile = rootDir + '/pages/data/138222.html'

root = html.parse(dataFile)
find_text = etree.XPath("//h1/a/text()");
title = find_text(root)
print(title)



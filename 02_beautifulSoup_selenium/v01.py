# BeautifulSoup4的基本操作
# 搜索文档对象
# 遍历文档

from bs4 import BeautifulSoup
from  urllib import request

url = "http://www.baidu.com"
rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

content = soup.prettify()
# print(content)

print("=="*12)
print(soup.title)
print("=="*12)
print(soup.title.attrs)
print("=="*12)
print(soup.title.string)
print("=="*12)
print(soup.title.name)
print("=="*12)
print(soup.name)
print("=="*12)


# 遍历文档
for node in soup.head.contents:
    if node.name == "meta":
        print(node)

    if node.name == "title":
        print(node.string)

print("=="*12)


# find_all
import re
tags = soup.find_all(re.compile("^me"),content="IE=Edge") # content="always"
for tag in tags:
    print(tag)
print("=="*12)


import re

pattern = re.compile(r'\d+')

s = pattern.search("i am 18 year old and 176 heigh",20)
print(s.group())
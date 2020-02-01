import re

pattern = re.compile(r'\d+')

s = pattern.findall("i am 123123124 dsh 455")
print(s)

s = pattern.finditer("i am 123123124 dsh 455")
for i in s:
    print(i.group())


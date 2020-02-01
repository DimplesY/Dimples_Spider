import re

s = r"([a-z]+) ([a-z]+)"

pattern = re.compile(s,re.I)

m = pattern.match("hello world wide web")


s = m.group(0)
print(s)

s = m.span(0)
print(s)

s = m.group(1)
print(s)

s = m.span(1)
print(s)

s = m.groups()
print(s)

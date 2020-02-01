from lxml import html

etree = html.etree

text = '''

    <div>
        <ul>
            <li><a href="1.html">item1</a></li>
            <li><a href="2.html">item2</a></li>
            <li><a href="3.html">item3</a>
        </ul>
    </div>
'''
html = etree.HTML(text)
print(etree.tostring(html))

html = etree.parse("./test.xml")
cst = etree.tostring(html,pretty_print=True)
print(cst)

# 查找所有book的节点
rst = html.xpath("//book")
print(type(rst))
print(rst)

rst = html.xpath("//book[@lang='en']")
print(rst[0].text)
print(rst[0].tag)
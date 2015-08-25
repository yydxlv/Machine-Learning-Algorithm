# coding=utf_8
# 内建函数str()和repr() (representation，表达，表示)或反引号操作符（``）可以方便地以字符串的方式获取对象的内容、类型、数值属性等信息。
#  str()函数得到的字符串可读性好（故被print调用），而repr()函数得到的字符串通常可以用来重新获得该对象，
# 通常情况下 obj==eval(repr(obj)) 这个等式是成立的。这两个函数接受一个对象作为其参数，返回适当的字符串。
__author__ = 'xilin'
# class D(object):
#     def __str__(self):
#         return "a __str__"
#
#     def __repr__(self):
#         return "a __repr__"
import html
import re
line='asdf fjdk; afed, fjek,asdf    foo'
fields=re.split(r'(;|,|\s)\s*', line)
values=fields[::2]
delimiters=fields[1::2]+['']
text="Today is 11/27/2012. PyCon starts 3/13/2013."
def make_element(name,value,**attrs):
    keyvals=['%s="%s"'% item for item in attrs.items()]
    keyval=[item for item in attrs.items()]
    print(['%s=%s'%("yyd", "xl")])
    print(keyval)
    print(keyvals)
    attr_str=''.join(keyvals)
    element='<{name}{attrs}>{value}</{name}>'.format(name=name,attrs=attr_str,value=html.escape(value))
    return element
if __name__=="__main__":
    # dr = D()
    # print(dr)
    # print("%s" % dr)
    # print("%r" % dr)

    # print(re.split(r'[;,\s]\s*', line))
    # print(fields)
    # print(values)
    # print(delimiters)
    # print(''.join(v+d for v,d in zip(values,delimiters)))   #  asdf fjdk;afed,fjek,asdf foo
    # print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
    print(make_element('item','Albatross', size='large', quantity=6))
#!/usr/bin/python
#encoding=utf-8

def contains(text, key):
    if key in text:
        return True
    else:
        return False

def find(text, key):
    return text.find(key)


import re

def re_find(text, key):
    # 查找
    return re.search(key, text)

def re_match(text, key):
    # 匹配(完全匹配)
    return re.match(key, text)

if __name__ == '__main__':

    print "abcd cantains abc:", contains('abcd', 'abc')

    print "abcd find bcd:", find('abcd', 'bcd')

    print "[TID=100 re_find TID=([\d]+)", re_find('[TID=100', r'TID=([\d]+)').group(1)

    print "[TID=100 re_find TID=([\d]+)", re_match('[TID=100', r'TID=([\d]+)')

    print "TID=100 re_find TID=([\d]+)", re_match('TID=100', r'TID=([\d]+)').group(1)
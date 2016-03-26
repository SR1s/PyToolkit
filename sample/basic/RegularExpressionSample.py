#!/usr/bin/python
#encoding=utf-8

import re

def multi_expression(text, key1, key2):
	# (key1)|(key2)
	# 正则表达式支持多重规则，但对于重合的部分无效
	key = '(' + key1 + ')|(' + key2 + ')'
	return re.search(key, text)

if __name__ == '__main__':

	param = ("abcdefg", r'bc', r'cd')
	print "test: %s, key1: %s, key2: %s\n result:" % param
	groups = multi_expression(param[0], param[2], param[1]).groups()
	for group in groups:
		print group
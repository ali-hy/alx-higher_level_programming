#!/usr/bin/python3
def no_c(my_string:str):
	res = ""
	for c in my_string:
		if c != 'c' and c != 'C':
			res += c
	return res

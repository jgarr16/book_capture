#!/usr/bin/env python
# -*- coding: utf-8 -*-
# John Garrigues Feb 2019
# 
# Python script that takes in text from the clipboard (i.e., text that has been highlighted and copied from a web page, or pdf, etc.) and converts it to a format that Scrivener can ingest and transform into an epub file.


import pyperclip
import re


findTable = re.findall(' Open table as spreadsheet 5')


# Import clipboard text with pyperclip
text = str(pyperclip.paste())
for tableSign in findTable.findall(text):
	print(tableSign)

# for record in text:
# 	if " Open table as spreadsheet 5" in record:
# 		print(record)
# print(text)
# with open('/Users/jrgarrigues/book_copy/6c.txt', 'r') as text:
# 	for line in text:
# 		if " Open table as spreadsheet 5" in line:
# 			print(line)
		# else: print('it didn\'t work!!!')


# print(findTable)
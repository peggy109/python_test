#!/usr/bin/python

rows=5; # 4 * 4
for row in range(0,rows):
	for column in range(0,rows):
		if row != 0 and row != rows-1 and column != 0 and column != rows -1:
 			print " ",
 		else:
 			print "*",
	else:
		print
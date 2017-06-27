#!/usr/bin/python

for row in range(1,8):
	if row in range(1,5):
		space_number = 4 - row;
	else:
		space_number = row - 4;
	for column in range(1, 8):
		if column > space_number and column < 8 - space_number:
			print "*",
		else:
			print " ",
	else:
		print
		
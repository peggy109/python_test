#!/usr/bin/python
for i in range(10, 20):
	for j in range(2, i):
		if i % j == 0:
			b = i / j;
			print i," = ",j," * ",b
			break;
	else:
		print "*******prime number"
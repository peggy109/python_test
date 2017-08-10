#!/usr/bin/python
import color
color.print_color("apple");
#invalid
#print_color("apple");
from color import print_color
print_color("apple");

#invalid
#print_name("orange");

from color import *
print_color("apple");
print_name("orange");


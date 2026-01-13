#!/usr/bin/env python3
import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if c == math.sqrt(a**2 + b**2):
	print(a, b, "und", c,"sind ein pythagotärisches  Triplet!")
else:
	print(a, b, "und", c,"sind kein pythagotärisches  Triplet!")

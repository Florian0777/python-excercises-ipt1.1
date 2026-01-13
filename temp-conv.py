#!/usr/bin/env python3
import sys
import math

a = float(sys.argv[1])
b = sys.argv[2]
x = 0

if b == 'c' or b == 'C':
	x = a * (9 / 5) + 32
	print(f"{a:.2f}°{b} = {x:.2f} F")

elif b == 'f' or b == 'F':
	x = (a -32) * (5 / 9)
	print(f"{a:.2f}°{b} = {x:.2f} C")


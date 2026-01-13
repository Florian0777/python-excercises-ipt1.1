#!/usr/bin/env python3
import sys
import math


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = b**2 - (4 * (a * c))

if d > 0:
	x1 = (-b + math.sqrt(d)) / (2 * a)
	x2 = (-b - math.sqrt(d)) / (2 * a)

	print(f"x1={x1:.1f}, x2={x2:.2f}")

elif d == 0:
	x = -b / 2 * a
	print(f"x={x:.1}")

elif d < 0:
	print("Keine Lösung")




#!/usr/bin/env python3
import math
import sys

r = float(sys.argv[1])

U = 2 * math.pi * r
A = math.pi * r * r

print(f"A={A:.2f}\nU={U:.2f}")

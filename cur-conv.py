#!/usr/bin/env python3
import sys

a = float(sys.argv[1])
b = sys.argv[2]
x = 0

if b == 'USD':
	x = a / 100 * 80
	print(f"CHF {x:.2f}")
elif b == 'EUR':
    x = a / 100 * 93
    print(f"CHF {x:.2f}")
elif b == 'GBP':
    x = a / 100 * 107
    print(f"CHF {x:.2f}")

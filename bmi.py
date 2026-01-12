#!/usr/bin/env python3

height_cm = float(input("Körpergrösse in cm: "))
weight = float(input("Körpergewicht in kg: "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

print(f"Dein Body-Mass-Index: {bmi:.2f}")

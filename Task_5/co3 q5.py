import time
import sys
readings = [4, 5, 60, -55, 1, 9, 7, 52, -50, 2]
valid1 = []
fahrenheit1 = []
for c in readings:
    if -50 <= c <= 50:
        valid1.append(c)
        fahrenheit1.append(round(c * 9/5 + 32, 2))
print("Method 1 - For Loop")
print("Valid readings:", valid1)
print("Fahrenheit:", fahrenheit1)
valid2 = [c for c in readings if -50 <= c <= 50]
fahrenheit2 = [
    round(c * 9/5 + 32, 2)
    for c in readings if -50 <= c <= 50
]
print("\nMethod 2 - List Comprehension")
print("Valid readings:", valid2)
print("Fahrenheit:", fahrenheit2)
valid3 = list(filter(lambda c: -50 <= c <= 50, readings))
fahrenheit3 = list(
    map(lambda c: round(c * 9/5 + 32, 2), valid3)
)
print("\nMethod 3 - Map and Filter")
print("Valid readings:", valid3)
print("Fahrenheit:", fahrenheit3)
alarm = [
    (minute, temp)
    for minute, temp in enumerate(readings, start=1)
    if -50 <= temp <= 50 and (temp < 2 or temp > 8)
]
print("\nAlarm Minutes:", alarm)
print("\nResults Identical:",
      valid1 == valid2 == valid3 and
      fahrenheit1 == fahrenheit2 == fahrenheit3)

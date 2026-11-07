import random
import time
readings = [random.randint(0, 100) for _ in range(365)]
weekly_totals = []
for i in range(0, len(readings), 7):
    weekly_totals.append(sum(readings[i:i+7]))
print("Weekly Totals:", weekly_totals)
maximum = max(readings)
minimum = min(readings)
print("Maximum Rainfall:", maximum)
print("Maximum Position (Day):", readings.index(maximum) + 1)
print("Minimum Rainfall:", minimum)
print("Minimum Position (Day):", readings.index(minimum) + 1)
moving_average = []
for i in range(len(readings) - 6):
    avg = sum(readings[i:i+7]) / 7
    moving_average.append(avg)
print("7-Day Moving Average:", moving_average)
dry_days = []
for i in range(len(readings)):
    if readings[i] == 0:
        dry_days.append(i + 1)
print("Dry Days:", dry_days)

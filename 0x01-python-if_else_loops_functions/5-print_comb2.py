#!/usr/bin/python3
# Print numbers from 0 to 99 in two-digit format
for i in range(100):
    if i < 99:
        print(f"{i:02d}", end=", ")
    else:
        print(f"{i:02d}")
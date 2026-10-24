#!/usr/bin/python3
import sys

n = int(sys.argv[1]) if len(sys.argv) > 1 else 15

result = []

for i in range(1, n + 1):
    if i % 15 == 0:
        result.append("FizzBuzz")
    elif i % 3 == 0:
        result.append("Fizz")
    elif i % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(i))

print(" ".join(result))

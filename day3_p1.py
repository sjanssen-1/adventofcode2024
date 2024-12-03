import sys
import re

if len(sys.argv) > 1 and sys.argv[1] == '-sample':
    file = open("day3_sample.in", "r")
else:
    file = open("day3.in", "r")

result = 0
for line in file:
    matches = re.findall(r"mul\((\d*),(\d*)\)", line)
    for match in matches:
        result += int(match[0]) * int(match[1])

print(result)
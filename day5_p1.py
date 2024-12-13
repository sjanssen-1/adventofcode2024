import sys
from typing import List, Dict

if len(sys.argv) > 1 and sys.argv[1] == '-sample':
    file = open("day5_sample.in", "r")
else:
    file = open("day5.in", "r")

parsingRules = True
rules: List[Dict[str, str]] = []
updates: List[List[int]] = []

for line in file.readlines():
    if line == "\n":
        parsingRules = False
        continue

    if parsingRules:
        parts = line.split("|")
        rules.append({'page': int(parts[0]), 'before': int(parts[1])})
    else:
        updates.append([int(x) for x in line.split(',') if x.strip().isdigit()])

valid_updates: List[List[int]] = []
valid_sum = 0
for update in updates:
    updateValid = True
    for rule in rules:
        try:
            pageIndex = update.index(rule["page"])
            beforeIndex = update.index(rule["before"])
            if pageIndex >= beforeIndex:
                updateValid = False
                break
        except ValueError:
            continue
    
    if updateValid:
        valid_updates.append(update)

for update in valid_updates:
    l = len(update)
    valid_sum += update[int(l/2)]

print("valid sum: " + str(valid_sum))
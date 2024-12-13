import sys
from typing import List, Dict
import itertools

if len(sys.argv) > 1 and sys.argv[1] == '-sample':
    file = open("day5_sample.in", "r")
else:
    file = open("day5.in", "r")

def isUpdateValid(update: List[int], rules: List[Dict[str, str]]) -> bool:
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
    return updateValid

def checkRule(update: List[int], rule: Dict[str, str]) -> bool:
    try:
        pageIndex = update.index(rule["page"])
        beforeIndex = update.index(rule["before"])
        return not pageIndex >= beforeIndex
    except ValueError:
        return True
    
def checkRules(update: List[int], rules: List[Dict[str, str]]) -> bool:
    for rule in rules:
        if not checkRule(update, rule):
            return False
    return True


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

invalid_updates: List[List[int]] = []
valid_sum = 0
for update in updates:    
    if not isUpdateValid(update, rules):
        invalid_updates.append(update)

for update in invalid_updates:
    update_corrected = update
    
    while not checkRules(update_corrected, rules):
        for rule in rules:
            while not checkRule(update_corrected, rule):
                pageIndex = update.index(rule["page"])
                beforeIndex = update.index(rule["before"])
                update_corrected[beforeIndex] = rule["page"]
                update_corrected[pageIndex] = rule["before"]
    
    l = len(update_corrected)
    valid_sum += update_corrected[int(l/2)]

print("valid sum: " + str(valid_sum))
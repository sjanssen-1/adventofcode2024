import sys

def all_increasing_or_decreasing(report: list[int]):
    if report[0] == report[1]:
        return False

    isIncreasing = report[0] > report[1]
    for i,level in enumerate(report):
        if i == len(report)-1:
            return True
    
        if isIncreasing and report[i] <= report[i+1]:
            return False
        elif not isIncreasing and report[i] >= report[i+1]:
            return False
        
def check_safe_difference(report: list[int]):
    for i, level in enumerate(report):
        if i == len(report)-1:
            return True
        
        diff = abs(level - report[i+1])
        if diff < 1 or diff > 3:
            return False


def problem_dampener(report: list[int]):
    for i in range(0, len(report)):
        dampened_report = report.copy()
        del dampened_report[i]
        if all_increasing_or_decreasing(dampened_report) and check_safe_difference(dampened_report):
            return True
    return False

if len(sys.argv) > 1 and sys.argv[1] == '-sample':
    file = open("day2_sample.in", "r")
else:
    file = open("day2.in", "r")

safe = 0

for line in file:
    report = [int(x) for x in line.split(" ")]
    if all_increasing_or_decreasing(report) and check_safe_difference(report):
        safe+=1
    elif problem_dampener(report):
        safe+=1

print(str(safe) + ' reports are safe')
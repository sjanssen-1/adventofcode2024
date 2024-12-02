import sys

if len(sys.argv) > 1 and sys.argv[1] == '-sample':
    file = open("day1_sample.in", "r")
else:
    file = open("day1.in", "r")


left_arr = []
right_arr = []

total = 0

for line in file:
    # print(line)
    split = line.split("   ")
    left_arr.append(int(split[0]))
    right_arr.append(int(split[1]))

left_arr.sort()
right_arr.sort()

for i,x in enumerate(left_arr):
    difference = left_arr[i] - right_arr[i]
    total+=abs(difference)

print('total is: ' + str(total))
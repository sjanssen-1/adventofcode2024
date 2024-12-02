import sys

if len(sys.argv) > 1 and sys.argv[1] == '-sample':
    file = open("day1_sample.in", "r")
else:
    file = open("day1.in", "r")

left_arr = []
right_arr = []


for line in file:
    # print(line)
    split = line.split("   ")
    left_arr.append(int(split[0]))
    right_arr.append(int(split[1]))

similarity_score = 0
for x in left_arr:
    similarity_score+= x * right_arr.count(x)

print('similarity score: ' + str(similarity_score))
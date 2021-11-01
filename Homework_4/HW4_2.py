import random

list1 = random.sample(range(1, 300), 10)
print(list1)

new_list = []

for i in range(len(list1) - 1):
    if list1[i] < list1[i+1]:
        new_list.append(list1[i+1])

print(new_list)
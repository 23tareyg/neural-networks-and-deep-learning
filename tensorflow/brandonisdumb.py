total = 0

try:
    my_list = []

    while True:
        my_list.append(int(input()))

except:
    print("hi")

for num in range(0, len(my_list)):
    total = total + my_list[num]

print("Average: ", total/len(my_list))
print("sum equals: ", total)

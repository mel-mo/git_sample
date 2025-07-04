data = [1,9,2,8,3,7,4,6,5]

max = data[0]
for i in range(len(data)):
    if max < data[i]:
        max = data[i]
print(max)

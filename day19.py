num_data = \
        [
            [0, 12],
            [3, 5],
            [8, 15],
            [17, 25],
            [9, 10],
            [13, 22],
            [22, 12],
            [14, 2],
            [17, 0]
        ]
count = 0
array = []
max_idx = 0
for i in range(9):
    count = count + num_data[i][1] - num_data[i][0]
    array.append(count)

    for j in range(1, len(array)):
        if (array[max_idx] > array[j]):
            max_idx = j
        else:
            pass

print(array)
print(array[max_idx])

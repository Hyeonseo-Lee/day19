
def sort(array) :
	n = len(array)
	for i in range(0, n-1) :
		min = i
		for k in range(i+1, n) :
			if (array[min] > array[k]) :
				min = k
		tmp = array[i]
		array[i] = array[min]
		array[min] = tmp

	return array

ary2 = [[55, 33, 250, 44],
		 [88,  1,  67, 23],
		 [199,222, 38, 47],
		 [155,145, 20, 99]]
narray = []


for i in range(len(ary2)) :
	for k in range(len(ary2[i])) :
		narray.append(ary2[i][k])

print('1차원 변경 후, 정렬 전 -->', narray)
narray = sort(narray)
print('1차원 변경 후, 정렬 후 -->', narray)
print('중앙값 --> ', narray[len(narray) // 2])

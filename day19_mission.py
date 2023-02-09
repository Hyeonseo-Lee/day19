import random
import time

def sort(array) :
	n = len(array)
	for i in range(0, n-1) :
		minIdx = i
		for k in range(i+1, n) :
			if (array[minIdx] > array[k]) :
				minIdx = k
		temp = array[i]
		array[i] = array[minIdx]
		array[minIdx] = temp

	return array

def q_sort(array, start, end) :
	if end <= start :
		return

	low = start
	high = end

	pivot = array[(low + high) // 2]
	while low <= high:
		while array[low] < pivot :
			low += 1
		while array[high] > pivot :
			high -= 1
		if low <= high :
			array[low], array[high] = array[high], array[low]
			low, high = low + 1, high - 1

	mid = low

	q_sort(array, start, mid - 1)
	q_sort(array, mid, end)

def quick_sort(ary) :
	q_sort(ary, 0, len(ary) - 1)


count_array = [1000, 10000, 12000, 15000]

for count in count_array :
	temp_array = [random.randint(10000, 99999) for _ in range(count)]
	select_array = temp_array[:]
	quick_array = temp_array[:]

	print("## 데이터 수 : ", count, "개")
	start = time.time()
	sort(select_array)
	end = time.time()
	print("	선택 정렬 --> %10.3f 초" % (end-start))
	start = time.time()
	quick_sort(select_array)
	end = time.time()
	print("	퀵 정렬  --> %10.3f 초" % (end-start))
	print()

	count *= 5


import random
import time


def bubble(array) :
	n = len(array)
	for end in range(n-1, 0, -1) :
		changeYN = False
		for cur in range(0, end) :
			if (array[cur] > array[cur + 1]) :
				array[cur], array[cur + 1] = array[cur + 1], array[cur]
				changeYN = True
		if not changeYN :
			break
	return array

def q_sort(array, start, end) :
	if end <= start :
		return

	low = start
	high = end

	pivot = array[(low + high) // 2]
	while low <= high :
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

def quickSort(ary) :
	q_sort(ary, 0, len(ary) - 1)


tarray = [random.randint(10000, 99999) for _ in range(1000000)]
tarray.sort()

rnd_p = random.randint(0, len(tarray) - 1)
print("# 데이터 개수 --> ", len(tarray))
print("# 끼어든 위치 --> ", rnd_p)
tarray.insert(rnd_p, tarray[-1])

bubble_array = tarray[:]
quick_array = tarray[:]

start = time.time()
bubble(bubble_array)
end = time.time()
print("다시 정렬 시간(버블 정렬) --> %10.3f 초" % (end-start))

start = time.time()
quickSort(quick_array)
end = time.time()
print("다시 정렬 시간(퀵 정렬)   --> %10.3f 초" % (end-start))

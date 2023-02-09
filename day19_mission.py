
def scorest(array) :
	n = len(array)
	for end in range(1, n) :
		for current in range(end, 0, -1) :
			if ( array[current - 1][1] > array[current][1]) :
				array[current - 1], array[current] = array[current], array[current - 1]
	return array


score_array = [['수호', 88], ['시우민', 99], ['디오', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]

print('정렬 전 -->', score_array)
score_array = scorest(score_array)
print('정렬 후 -->', score_array)

print('## 성적별 조 편성표 ##')
for i in range(len(score_array) // 2) :
	print(score_array[i][0], ':', score_array[len(score_array) - 1 - i][0])

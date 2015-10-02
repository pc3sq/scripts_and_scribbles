def insertionSort (array): 

	sortedArr = []
	sortedArr.append(array[0])

	j = 1

	while j < len(array):
		currentCard = array[j]
		
		i = 0
		embed()
		
		while currentCard < sortedArr[i]:
			sortedArr[i + 1] = sortedArr[i]
			sortedArr[i] = currentCard
			i = i + 1

	j = j + 1

	return sortedArr

print insertionSort([10, 3, 2, 4, 101, 55])
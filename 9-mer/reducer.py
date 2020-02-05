import sys
import copy
kMer = None
currentKMer = None
countOfKMer = 0
total9Mer=0
outputText=9

for line in sys.stdin:
	line = line.strip()
	word = line.split('\t')
	if currentKMer == word[0]:
		countOfKMer = countOfKMer + int(word[1])
	elif currentKMer==None:
		currentKMer=word[0]
		countOfKMer=int(word[1])
	elif len(word)==2:
		total9Mer+=1
		print("{0}\t{1}".format(currentKMer,countOfKMer))
		currentKMer=word[0]
		countOfKMer=int(word[1])
	else:
		total9Mer+=1
		print("{0}\t{1}".format(currentKMer,countOfKMer))
print("{0}\t{1}".format(outputText,total9Mer))

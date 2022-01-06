import os.path
from os import path

def main():
	while(True): #loop through to keep asking for filename
		filename = input("Enter a filename: ") #get filename through user input
		if(path.exists(filename)):
			print("\nSummary of file {}:".format(filename))
			wordProcessing(filename) #if there is a file pass the filename to wordProcessing and run it
		elif(filename == "quit"):
			quit() #quits program
		else: #we know the file wont open because it doesnt exist so print the exception
			try:
				open(filename)
			except Exception as e:
				print (e) 
				

def wordProcessing(filename):
	dictionary = {}
	totalWords = 0
	totalUniqueWords = 0
	uniqueWords = {}
	uniqueWordCount = 0
	counter = 0
	
	fh = open(filename, 'r') #got exceptions when getting filename unless on linux and dont have read permissions
	for line in fh.readlines():
		counter += 1 #counter for line number
		line = line.lower() #lowercase string so all
		words = line.split() #make array of words in the string
		wordCount = len(words) #get word count
		totalWords += wordCount
		for word in words: #iterate through the array
			if(word not in uniqueWords): #if word hasnt showed up in the line
				uniqueWords[word] = 1
			
			if(word in dictionary): #if word has showed up in document
				dictionary[word] += 1
			else:
				dictionary[word] = 1
		uniqueWordCount = len(uniqueWords) #get unique word count of the line
		print("Line {}: {} words\t {} unique words".format(counter, wordCount, uniqueWordCount))
		uniqueWords = {}
	totalUniqueWords = len(dictionary) #get unique word count of document
	print("Total number of words found in the file: {}".format(totalWords))
	print("Total number of unique words found in the file: {} and they are:\n".format(totalUniqueWords))

	index = 0
	for key in sorted(dictionary.keys()): #iterate through list of sorted keys 
		if(index % 5 == 0): #every values printed go to new line
			print("\n", end = "")
		print("{:>15}: {:<5}".format(key, dictionary[key]), end = "")
		index += 1
	print("\n", end = "")
	fh.close()

if(__name__ == "__main__"): main()
#Counting words in a string

def wordCount():
    lst = list()
    count = dict()
    textToProcess = input('Please provide text or file: ')
    try:
        fhand = open(textToProcess)
        for line in fhand:
            line = line.rstrip()
            lst = line.split()
        for word in lst:
            count[word] = count.get(word, 0) + 1

    except:
        textToStr = textToProcess.split()
        return len(textToStr)
    return count
print(wordCount())

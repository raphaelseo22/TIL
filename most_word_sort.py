import operator
try :
    file_name = input('Enter the file name : ')
    file_open = open(file_name)

    counts = dict()
    for line in file_open :
        words = line.lower().split()
        for word in words :
            counts[word] = counts.get(word,0) + 1
            bigcount = None
            bigword = None
            for word,count in counts.items() :
                if bigcount is None or count > bigcount:
                    bigword = word
                    bigcount = count
    print(bigword,bigcount)
    counts = sorted(counts.items(), key = operator.itemgetter(1), reverse = True)
    print(counts)
except Exception as e :
        print(e)

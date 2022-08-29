# find max word in a file
try:
    file = open(input('Enter file name: '))

except:
    exit('Please check if the file name is correct and in the py4e folder')

Counts = dict()
for line in file:
    words = line.split()
    for word in words:
        Counts[word]=Counts.get(word,0)+1

bigcount = 0
bigword = 0

for word,count in Counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print (bigword,bigcount)

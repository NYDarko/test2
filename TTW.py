#Top ten words that appeared the most in a text file
try:
    fhand = open(input ("Enter the file name: " ))
except:
    exit('Sorry, the file cannot be found')


d = dict()
for line in fhand :
 words = line.split()
 for word in words:
  d[word]=d.get(word, 0) +1

lst = list()
for key,value in d.items():
  newtuple = (value,key)
  lst.append(newtuple)

lst = sorted(lst, reverse=True)

for val,key in lst[:10]:
  print (key,val)

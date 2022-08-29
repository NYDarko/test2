#regex to find max value of a specific item in a word file
import re

data = 'mbox-short.txt'
file = open(data)
numlist = list()
for line in file:
  line = line.strip()
  stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
  if len(stuff)!=1 : continue
  num = float(stuff[0])
  numlist.append(num)
print('Max:', max(numlist))
print(num)

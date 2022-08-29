#Using re.search() like startswith
import re

hand =  open ('networks.txt')
for line in hand :
  line = line.rstrip()
  line = line.lower()
  if re.search('^from',line):
      print (line)

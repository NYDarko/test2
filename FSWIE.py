#loop through a file and find text
fhand = open('networks.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'): continue
    words = line.split()
    print (words[1])

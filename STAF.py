#skipping lines in text

fhand = open('networks.txt')
for line in fhand:
    line = line.strip()
    if line.startswith('From:'):
        print (line)

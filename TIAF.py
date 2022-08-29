#typing in a file to analyze strings and trapping errors

fname = input ('Enter file name: ' )
try:
    fhand = open(fname)

except:
    print(fname, 'cannot be found')
    quit()

count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        count = count + 1
print ('There are',count,'lines that start with from:')

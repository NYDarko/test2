#Parsing and Extracting data

data = 'From stephen.marquad@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
sspos = data.find(' ',atpos)
host = data[atpos + 1:sspos]
print (host)

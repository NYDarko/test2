#counting in dictionaries
count = dict ()
names = ['Kwe','Cwe','Darry','Saul','Cwe','Kwe','Cwe']
for name in names:
    if name not in count:
        count [name] = 1
    else:
        count [name] = count [name] +1
print(count)

#Sorting tuples by values instead of keys

d = {'a':20,'b':1,'c':5}
tmp = list()

for k,v in d.items():
  tmp.append((v,k))
print (tmp)

tmp = sorted(tmp, reverse=True)
print (tmp)

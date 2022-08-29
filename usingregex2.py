#using regex cont
import re

x = 'from nydarko@ecobank.com Sat Jan 5 09:23:16 2022'
y = re.findall('^from .*@([^ ]*)',x)
print (y)

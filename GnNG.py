#Greedy Matching
import re

#x = "response: He hit her hard, ask: madam"
#y = re.findall('^r.+:',x)
#print (y)


#Non Greedy Matching
x = "response: He hit her hard, ask: madam"
y = re.findall('^r.+?:',x)
print (y)

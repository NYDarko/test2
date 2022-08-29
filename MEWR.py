#Matching and Extracting with regex
import re

inp = " My 4 fav numbers are 16 , 17, 24 and 90"
outp = re.findall ('[0-9]+', inp')
print (outp)

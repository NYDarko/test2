#loopacceptinginput

Word = input ('Type in your longest word: ' )
index = 0
while index < len(Word):
    letter = Word[index]
    print (index,letter)
    index = index + 1
print (len(Word))

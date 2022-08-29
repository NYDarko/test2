#DefiniteLoop
smallest_so_far = None
print ('before:')
for num in [21,20,4,9,2,-1,4]:
    if smallest_so_far is None :
        smallest_so_far = num
    elif num < smallest_so_far:
        smallest_so_far = num
    print (num, smallest_so_far)
print('After:',smallest_so_far)

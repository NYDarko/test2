#running_count_and_sum_and_average
sum = 0
count = 0
print ('Before:', sum , count)
for val in [10,21,8,81,5,99,1290,28]:
  count = count + 1
  sum = sum + val
  print (val, count, sum)
print ('After:', count, sum, sum/count)

 1

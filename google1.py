#Addition
# Given an array of integers that represents an integer, create a function that adds a number N to the array A
# e.g A = [1,2,3], N = 1, your result should be 124 in the following format: [1,2,4]

arr = [9,9,9,9,9,9]
num = 183
def add(A,N):
  counter = len(A) - 1
  newArr = [0] * len(A)
  index = len(A) - 1
  over = 0
 
  for i in range(0,len(A)):
    x = N + A[index - i]
    if(x > 9):
      remainder = x % 10
      quotient_ = x - remainder
      over = 1
      while(quotient_ > 10):
        over = over + 1
        quotient_ = quotient_ - 10
      N = over
      newArr[counter]= remainder
    else:
      over = 0
      N = 0
      newArr[counter] = x
    counter = counter - 1
  if over != 0:
    newArr_ = [0]*(len(newArr)+1)
    newArr_[0] = 1
    for i in range(1,len(newArr_)):
      newArr_[i] = newArr[i-1]
    return newArr_
  else:
    return newArr
print(add(arr,num))


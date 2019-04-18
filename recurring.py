#This file finds the first recurring character in a given string
#If no recurring character is found, then the function returns 0



#Initiate a loop for the given string
#Initialize a variable to hold current char
#Initialize a variable to hold value of array after current char
#Check if current char in new array, if so then exit and return char, else continue until i + 1 >= len(string_)
def rec(string_):
  for i in range(len(string_)):
      temp = string_[i]
      if i + 1 >= len(string_):
        break
      tempa = string_[i+1:]
      if temp in tempa:
        return temp
   return 0

# In olden days finding square roots seemed to be difficult but nowadays it can be easily done using in-built functions available across many languages .
# Assume that you happen to hear the above words and you want to give a try in finding the square root of any given integer using in-built functions.

T = int(input("Enter number of test cases: "))
while T > 0:
   n = int(input("Enter number: "))
   sqrt = n ** 0.5
   sqrt_root = round(sqrt)
   print(sqrt_root)
   T = T - 1
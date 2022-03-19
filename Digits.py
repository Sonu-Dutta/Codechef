# Write a program to obtain a number (N) from the user and display whether the number is a one digit number, 2 digit number, 3 digit number or more than 3 digit number

# Input:
# First line will contain the number N,
# Output:
# Print "1" if N is a 1 digit number.

# Print "2" if N is a 2 digit number.

# Print "3" if N is a 3 digit number.

# Print "More than 3 digits" if N has more than 3 digits.

# Sample Input:
# 9
# Sample Output:
# 1
# Author

n=int(input("Enter a number: "))
count=0
while(n>0):
    res=n%10
    count=count+1
    n=n//10
if(count==1):
    print("1")
elif(count==2):
    print("2")
elif(count==3):
    print("3")
elif(count>3):
    print("More than 3 digits")
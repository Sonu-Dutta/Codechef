# Write a program to take a character (C) as input and check whether the given character is a vowel or a consonant.
# Vowels are 'A', 'E', 'I', 'O', 'U'. Rest all alphabets are called consonants.

# Input:
# First line will contain the character C.
# Output:
# Print "Vowel" if the given character is a vowel, otherwise print "Consonant".

# Sample Input:
# Z
# Sample Output:
# Consonant

a=input("Enter a letter: ")
if a in ["A", "E", "I", "O", "U"]:
    print("Vowel")
else:
    print("Consonant")
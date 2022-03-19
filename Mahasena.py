# Kattapa, as you all know was one of the greatest warriors of his time. The kingdom of Maahishmati had never lost a battle under him (as army-chief), 
# and the reason for that was their really powerful army, also called as Mahasena.
# Kattapa was known to be a very superstitious person. He believed that a soldier is "lucky" if the soldier is holding an even number of weapons, and "unlucky" otherwise.
# He considered the army as "READY FOR BATTLE" if the count of "lucky" soldiers is strictly greater than the count of "unlucky" soldiers, and "NOT READY" otherwise.

# Given the number of weapons each soldier is holding, your task is to determine whether the army formed by all these soldiers is "READY FOR BATTLE" or "NOT READY".
# Note: You can find the definition of an even number here.

# Input
# The first line of input consists of a single integer N denoting the number of soldiers. 
# The second line of input consists of N space separated integers A1, A2, ..., AN, where Ai denotes the number of weapons that the ith soldier is holding.

# Output
# Generate one line output saying "READY FOR BATTLE", if the army satisfies the conditions that Kattapa requires or "NOT READY" otherwise (quotes for clarity).

# Example 1
# Input:
# 1
# 1
# Output:
# NOT READY

# Example 2
# Input:
# 1
# 2
# Output:
# READY FOR BATTLE

# Example 3
# Input:
# 4
# 11 12 13 14
# Output:
# NOT READY

# Example 4
# Input:
# 3
# 2 3 4
# Output:
# READY FOR BATTLE

# Example 5
# Input:
# 5
# 1 2 3 4 5
# Output:
# NOT READY

a = int(input("Enter number of soldiers: "))
l = list(map(int , input("Enter the numbers of weapons: ").split()))

x=y=0
for i in l:
    if i % 2 == 0:
        x = x + 1
    else:
        y = y + 1
if x > y:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
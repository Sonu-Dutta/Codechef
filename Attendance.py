# Chef is teaching a cooking course. There are N students attending the course, numbered 1 through N.
# Before each lesson, Chef has to take attendance, i.e. call out the names of students one by one and mark which students are present. 
# Each student has a first name and a last name. In order to save time, Chef wants to call out only the first names of students. 
# However, whenever there are multiple students with the same first name, Chef has to call out the full names (both first and last names) of all these students. 
# For each student that does not share the first name with any other student, Chef may still call out only this student's first name.
# Help Chef decide, for each student, whether he will call out this student's full name or only the first name.

# Input
# The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first line of each test case contains a single integer N.
# N lines follow. For each valid i, the i-th of the following N lines contains two space-separated strings denoting the first and last name of student i.
# Output
# For each test case, print N lines. For each valid i, the i-th of these lines should describe how Chef calls out the i-th student's name ― it should contain either the first name or the first and last name separated by a space.

# Sample Input 1 
# 1
# 4
# hasan jaddouh
# farhod khakimiyon
# kerim kochekov
# hasan khateeb
# Sample Output 1 
# hasan jaddouh
# farhod
# kerim
# hasan khateeb

for i in range(int(input("Enter number of test cases: "))):
    name1=[]
    name2=[]
    for j in range(int(input("How many names? "))):
        h=input("Enter name: ").split()
        name1.append(h[0])
        name2.append(h[1])
    for k in range(len(name1)):
        if name1.count(name1[k])==1:
            print(name1[k])
        else:
            print(name1[k],'',name2[k])
        
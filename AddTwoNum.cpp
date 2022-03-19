
// Shivam is the youngest programmer in the world, he is just 12 years old. 
// Shivam is learning programming and today he is writing his first program.

// The task is very simple: given two integers A and B, write a program to add these two numbers and output it.

// bits/stdc++.h
// It loads most of the libraries of C++ required.
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    printf("How many times you want to perform addition ? \n");
    scanf("%d", &T);
    int i = 0;
    while (i < T)
    {
        int a, b;
        printf("Enter first number: \n");
        scanf("%d", &a);
        printf("Enter second number: \n");
        scanf("%d", &b);
        int ans = a + b;
        printf("%d + %d = %d\n", a,b,ans);
        i++;
    }

    return 0;
}
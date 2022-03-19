
// You're given an integer N. Write a program to calculate the sum of all the digits of N.

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cout<<"Enter number of test cases: ";
    cin>>n;
    while(n--)
    {
     int num,m,sum=0;
     cout<<"Enter a number: ";
     cin>>num;
     while(num>0)
     {
      m=num%10;
      sum+=m;
      num/=10;
     }
     cout<<sum<<"\n";
    }
    return 0;
}

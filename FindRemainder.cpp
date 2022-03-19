// Write a program to find the remainder when an integer A is divided by an integer B.

#include <iostream>
using namespace std;

int main() {
    int a,b,t,r;
    cout<<"How many times you want to perform this test ?\n ";
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cout<<"Enter 2 numbers : ";
        cin>>a>>b;
        r=a%b;
         cout<<r<<endl;
    }
   
 return 0;
}
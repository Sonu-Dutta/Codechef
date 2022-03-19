//  Write a program to obtain a number N and increment its value by 1 if the number is divisible by 4 otherwise decrement its value by 1.

//  Input:
//  First line will contain a number N.
//  Output:
//  Output a single line, the new value of the number.

//  Sample Input:
//  5
//  Sample Output:
//  4
//  EXPLANATION:
//  Since 5 is not divisible by 4 hence, its value is decreased by 1.
#include <iostream>
using namespace std;

int main() {
	int n;
	cout<<"Enter Number: ";
	cin>>n;
	if(n%4==0){
	    n++;
	    cout<<n<<endl;
	}
	else{
	    n--;
	    cout<<n<<endl;
	}
	return 0;
}

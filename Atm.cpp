/*
Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, 
and Poojas account balance has enough cash to perform the withdrawal transaction (including bank charges). 
For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.

Input
Positive integer 0 < X <= 2000 - the amount of cash which Pooja wishes to withdraw.

Nonnegative number 0<= Y <= 2000 with two digits of precision - Pooja's initial account balance.

Output
Output the account balance after the attempted transaction, given as a number with two digits of precision. 
If there is not enough money in the account to complete the transaction, output the current bank balance.*/

#include <iostream>
#include <iomanip>
using namespace std;
int main() {
    int a;
    float b;
    cout<<"First enter the amount you want to withdraw, followed by the total amount present:";
    cin >> a >> b;
    if (a % 5 == 0 && a<=b -0.5) {
    b = b-a-0.50;
    }
    cout << fixed <<setprecision(2) <<b;
    return 0;
}
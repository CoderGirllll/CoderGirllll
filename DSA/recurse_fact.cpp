#include <iostream>
using namespace std;

int fact(int n);

int main(){
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Factorial of " << n << " is " << fact(n) << endl;
}

int fact(int n){
    if (n == 1){
        return 1;
    }
    else{
        return n * fact(n-1);
    }
}
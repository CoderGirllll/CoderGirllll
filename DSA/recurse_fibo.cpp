#include <iostream>
using namespace std;

int fibo(int n);

int main(){
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Finbonacci of " << n << " is: " << fibo(n) << endl;
}

int fibo(int n){
    if (n == 0){
        return 0;
    }
    else if (n == 1){
        return 1;
    }
    else{
        return fibo(n-1) + fibo(n-2);
    }
}
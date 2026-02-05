#include <iostream>
using namespace std;

int pow(int a, int b);

int main(){
    int a, b;
    cout << "Enter a and b: ";
    cin >> a >> b;
    cout << a << " raised to the power of " << b << " is: " << pow(a, b) << endl;
}

int pow(int a, int b){
    if (b == 0) return 1;
    if (b == 1) return a;
    return a * pow(a, b - 1);
}
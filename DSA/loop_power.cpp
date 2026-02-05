#include <iostream>
using namespace std;

int main(){
    int a, b;
    cout << "Enter a and b: ";
    cin >> a >> b;

    int pow = 1;

    for (int i = 0; i < b; i++){
        pow *= a;
    }
    cout << a << " raised to the power of " << b << " is: " << pow << endl;
}
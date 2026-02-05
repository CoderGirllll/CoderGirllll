#include <iostream>
using namespace std;

int main(){
    int x = 5;
    int y = 8;
    cout << "Before swap: x = " << x << ", y = " << y << endl;

    x = x + y;
    y = x - y;
    x = x - y;

    cout << "After swap: x = " << x << ", y = " << y << endl;
}
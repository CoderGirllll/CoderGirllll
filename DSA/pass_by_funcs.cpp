#include <iostream>
using namespace std;

void ref(int &x, int &y){
    x += 10;
    y += 10;
    cout << "Inside ref function: x = " << x << ", y = " << y << endl;
};

void val(int x, int y){
    x += 10;
    y += 10;
    cout << "Inside val function: x = " << x << ", y = " << y << endl;
}
int main(){
    int x, y;
    cout << "Enter two integers: ";
    cin >> x >> y;

    ref(x, y);
    cout << "Pass by reference: x = " << x << ", y = " << y << endl;
    val(x, y);
    cout << "Pass by value: x = " << x << ", y = " << y << endl;
}
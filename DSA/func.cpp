#include <iostream>
using namespace std;

int sum(int x, int y);
int mul(int x, int y);
int sub(int x, int y);
int divide(int x, int y);

int main(){
    int x,y;
    cout << "Enter two integers: ";
    cin >> x >> y;
    cout << "The sum is: " << sum(x,y) << endl;
    cout << "The product is: : " << mul(x,y) << endl;
    cout << "The difference is: " << sub(x,y) << endl;
    cout << "The quotient is: " << divide(x,y) << endl;
}

int sum(int x, int y){
    return x+y;
};

int mul(int x, int y){
    return x*y;
};

int sub(int x, int y){
    return x-y;
};

int divide(int x, int y){
    return x/y;
};
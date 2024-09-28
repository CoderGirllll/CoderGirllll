#include <iostream>
using namespace std;
int main(void){
    int l,b,h;
    cout<<"Enter length: ";
    cin>>l;
    cout<<"Enter breadth: ";
    cin>>b;
    cout<<"Enter height: ";
    cin>>h;
    cout<<"Area: "<<(l*(b+h) + b*(l+h) + h*(l+b))<<endl;
    cout<<"Volume: "<<l*b*h<<endl;
}
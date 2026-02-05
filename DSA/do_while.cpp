#include <iostream>
using namespace std;

int main(){
    //trying while loop
    int n = 2;
    while (n > 0){
        cout << "In while: " << n << endl;
        n--;
    }

    //trying do while loop
    do{
        cout << "In do-while: " << n << endl;
    } while ( n < 0);
}
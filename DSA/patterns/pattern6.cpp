#include <iostream>
using namespace std;

int main(){
    for (int i = 0; i < 5; i++){
        for (int j = 5; j > i; j--){
            cout << " ";
        }
        for (int k = 0; k < i; k++){
            cout << "*";
        }
        cout << "*";
        for (int l = 0; l < i; l++){
            cout << "*";
        }
        cout << endl;
    }

    //Alternate
    for (int i = 0; i < 5; i++){
        for (int j = 5; j > i; j--){
            cout << " ";
        }
        for (int k = 0; k < 2*i+1; k++){
            cout << "*";
        }
        cout << endl;
    }
}
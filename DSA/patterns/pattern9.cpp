#include <iostream>
using namespace std;
int j = 1;

int main(){
    for (int i = 1; i < 10; i = i + 2){
        for (j = 1; j < i; j = j + 2){
            cout << j;
        }
        for (int k = j; k > 0; k = k - 2){
            cout << k;
        }
        cout << endl;
    }
}
#include <iostream>
using namespace std;

int main(){
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    cout << "Original array: ";
    for (int i = 0; i < 10; i++){
        cout << arr[i] << ' ';
    }
    cout << endl;

    cout << "Reversed array: ";
    for (int i = 9; i >= 0; i--){
        cout << arr[i] << ' ';
    }
    cout << endl;
    
    cout << "Original array after reversal: ";
    for (int i = 0; i < 10; i++){
        cout << arr[i] << ' ';
    }
    cout << endl;

    cout << "Skipped array (every other element): ";
    for (int i = 0; i < 10; i += 2){
        cout << arr[i] << ' ';
    }
    cout << endl;

    cout << "Array in reverse order (every other element): ";
    for (int i = 9; i >= 0; i -= 2){
        cout << arr[i] << ' ';
    }
    cout << endl;
}
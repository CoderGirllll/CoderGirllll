#include <iostream>
using namespace std;

int main(){
    int arr[5] = {3, 1, 4, 1, 5};
    int sum = 0;
    for (int i = 0; i < 5; i++){
        cout << arr[i] << ' ';
        sum += arr[i];
    }
    cout << endl << "Sum: " << sum << endl;
}
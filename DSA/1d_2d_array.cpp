#include <iostream>
using namespace std;

int main(){
    int arr1D[5] = {1, 2, 3, 4, 5};
    cout << "1D Array: " << endl;
    for(int i = 0; i < 5; i++){
        cout << arr1D[i] << ' ';
    }
    cout << endl;

    int arr2D[2][3] = {{1,2,3}, {4,5,6}};
    cout << "2D Array: " << endl;
    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 3; j++){
            cout << arr2D[i][j] << ' ';
        }
        cout << endl;
    }
    cout << endl;
    return 0;
}
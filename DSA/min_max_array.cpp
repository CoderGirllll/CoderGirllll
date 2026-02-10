#include <iostream>
using namespace std;

int main(){
    int arr[10] = {56, 23, 78, 12, 34, 90, 45, 67, 89, 10};
    int min = arr[0], max = arr[0];
    for (int i = 0; i < 10; i++){
        if (arr[i] > max){
            max = arr[i];
        }
        if (arr[i] < min){
            min = arr[i];
        }
        cout << arr[i] << " ";
    }
    cout << endl;
    cout << "Min: " << min << endl;
    cout << "Max: " << max << endl;
}
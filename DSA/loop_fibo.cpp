#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int prev = 0, curr = 1;
    for (int i = 0; i < n; i++){
        cout << curr << ' ';
        int next = prev + curr;
        prev = curr;
        curr = next;
    }
}
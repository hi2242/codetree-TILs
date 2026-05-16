#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int numbers[N];
    for (int i = 0; i < N; i++)
        cin >> numbers[i];
    for (int i = N - 1; i >= 0; i--) {
        if (numbers[i] % 2 == 0)
            cout << numbers[i] << ' ';
    }
        
    return 0;
}
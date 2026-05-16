#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    for (int i = 1; i <= N; i++) {
        if (i % 2 == 0) {
            for (int j = N; j >= 1; j--) {
                cout << j;
            }
        } else {
            for (int j = 1; j <= N; j++) {
                cout << j;
            }
        }
        cout << endl;
    }
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < 2 * r + 1; c++) {
            cout << '*';
        }
        cout << endl;
    }
    return 0;
}
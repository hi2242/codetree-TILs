#include <iostream>
using namespace std;

int main() {
    int N, curr = 1;
    cin >> N;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c <= r; c++) {
            cout << curr << ' ';
            curr++;
        }
        cout << endl;
    }
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    for (int r = 0; r < N; r++) {
        for (int c = r; c < N; c++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
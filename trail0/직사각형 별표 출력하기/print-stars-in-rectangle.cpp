#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            cout << "* ";
        }
        cout << endl;
    }
    return 0;
}
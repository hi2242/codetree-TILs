#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    int grid[N][N];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            grid[j][i] = i % 2 != 0 ? N - j : j + 1;
        }
    }
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cout << grid[r][c];
        }
        cout << endl;
    }
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int grid[3][3];
    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            cin >> grid[r][c];
        }
    }

    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            cout << grid[r][c] * 3 << ' ';
        }
        cout << endl;
    }
    return 0;
}
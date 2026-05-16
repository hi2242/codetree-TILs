#include <iostream>
using namespace std;

int main() {
    int grid[4][4];
    int acc;
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            cin >> grid[r][c];
        }
    }
    for (int r = 0; r < 4; r++) {
        acc = 0;
        for (int c = 0; c < 4; c++) {
            acc += grid[r][c];
        }
        cout << acc << endl;
    }
    return 0;
}
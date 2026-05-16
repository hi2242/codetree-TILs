#include <iostream>
using namespace std;

int main() {
    int grid[4][4], count = 0;
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            cin >> grid[r][c];
        }
    }
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            if (grid[r][c] % 5 == 0) {
                count++;
            }
        }
    }
    cout << count;
    return 0;
}
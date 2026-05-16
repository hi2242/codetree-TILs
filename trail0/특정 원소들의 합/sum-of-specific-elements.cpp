#include <iostream>
using namespace std;

int main() {
    int grid[4][4], result = 0;
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c < 4; c++) {
            cin >> grid[r][c];
        }
    }
    for (int r = 0; r < 4; r++) {
        for (int c = 0; c <= r; c++) {
            result += grid[r][c];
        }
    }
    cout << result;
    return 0;
}
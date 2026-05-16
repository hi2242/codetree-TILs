#include <iostream>
using namespace std;

int main() {
    int first_grid[3][3], second_grid[3][3];
    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            cin >> first_grid[r][c];
        }
    }
    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            cin >> second_grid[r][c];
        }
    }
    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            cout << first_grid[r][c] * second_grid[r][c] << ' ';
        }
        cout << endl;
    }
    return 0;
}
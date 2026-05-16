#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    int first_grid[N][M], second_grid[N][M], new_grid[N][M];
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            cin >> first_grid[r][c];
        }
    }
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            cin >> second_grid[r][c];
        }
    }
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            if (first_grid[r][c] == second_grid[r][c]) {
                new_grid[r][c] = 0;
            } else {
                new_grid[r][c] = 1;
            }
        }
    }
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            cout << new_grid[r][c] << ' ';
        }
        cout << endl;
    }
    return 0;
}
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

void print_grid(vector<vector<int>>& grid);
int solve(vector<vector<int>>& grid, int N, int M);
bool validate(int r, int c, int N, int M);

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<int>> grid(N, vector<int>(M, 0));
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < M; c++) {
            cin >> grid[r][c];
        }
    }
    cout << solve(grid, N, M);
    return 0;
}

void print_grid(vector<vector<int>>& grid) {
    for (vector<int>& row : grid) {
        for (int elem : row) {
            cout << elem << ' ';
        }
        cout << endl;
    }
    cout << endl;
}

bool validate(int r, int c, int N, int M) {
    return 0 <= r && r < N && 0 <= c && c < M;
}

int solve(vector<vector<int>>& grid, int N, int M) {
    int dr[4] = {-1, 0, 1, 0}, dc[4] = {0, 1, 0, -1};
    vector<vector<int>> visited(N, vector<int>(M, 0));
    queue<pair<int, int>> d;
    d.push({0, 0});
    visited[0][0] = 1;
    while(!d.empty()) {
        auto [cr, cc] = d.front();
        if (cr == N - 1 && cc == M - 1) {
            return 1;
        }
        d.pop();
        for (int i = 0; i < 4; i++) {
            int nr = cr + dr[i], nc = cc + dc[i];
            if (validate(nr, nc, N, M) && grid[nr][nc] && !visited[nr][nc]) {
                d.push({nr, nc});
                visited[nr][nc] = 1;
            }
        }
    }
    return 0;
}
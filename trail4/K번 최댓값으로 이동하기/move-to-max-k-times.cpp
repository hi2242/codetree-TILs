#include <iostream>
#include <queue>
#include <utility>
using namespace std;

const int MAX_N = 100;
int N, K;
int grid[MAX_N][MAX_N];
int visited[MAX_N][MAX_N];
int sr, sc;

void print_grid();
void solve();
bool validate(int r, int c);
bool can_go(int r, int c);

int main() {
    cin >> N >> K;
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cin >> grid[r][c];
            visited[r][c] = 0;
        }
    }
    cin >> sr >> sc;
    solve();
    return 0;
}

void print_grid() {
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cout << visited[r][c] << ' ';
        }
        cout << endl;
    }
    cout << endl;
}

bool validate(int r, int c) {
    return 0 <= r && r < N && 0 <= c && c < N;
}

bool can_go(int s_value, int nr, int nc) {
    return validate(nr, nc) && s_value > grid[nr][nc] && !visited[nr][nc];
}

bool can_update(int m, int mr, int mc, int nr, int nc) {
    return m < grid[nr][nc] || (m == grid[nr][nc] && (mr > nr || (mr == nr && mc > nc)));
}

void solve() {
    int dr[4] = {-1, 0, 1, 0}, dc[4] = {0, 1, 0, -1};
    int mr = sr - 1, mc = sc - 1, m = 0;
    queue<pair<int, int>> q;
    q.push({mr, mc});
    visited[mr][mc] = 1;

    for (int k = 0; k < K; k++) {
        int s_value = grid[mr][mc];
        while (!q.empty()) {
            auto [cr, cc] = q.front();
            q.pop();
            for (int i = 0; i < 4; i++) {
                int nr = cr + dr[i], nc = cc + dc[i];
                if (can_go(s_value, nr, nc)) {
                    q.push({nr, nc});
                    visited[nr][nc] = 1;
                    if (can_update(m, mr, mc, nr, nc)) {
                        mr = nr, mc = nc;
                        m = grid[nr][nc];
                    }
                }
            }
        }
        q.push({mr, mc});
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                visited[r][c] = 0;
            }
        }
        visited[mr][mc] = 1;
        m = 0;
    }
    cout << mr + 1 << ' ' << mc + 1;
}
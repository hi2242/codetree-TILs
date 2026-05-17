#include <iostream>
#include <queue>
#include <utility>
using namespace std;

const int MAX_N = 100;
int N, K;
int grid[MAX_N][MAX_N], visited[MAX_N][MAX_N];

void print_grid(int arr[][MAX_N]);
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
    solve();
    return 0;
}

void print_grid(int arr[][MAX_N]) {
    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            cout << arr[r][c] << ' ';
        }
        cout << endl;
    }
}

bool validate(int r, int c) {
    return 0 <= r && r < N && 0 <= c && c < N;
}

bool can_go(int r, int c) {
    return validate(r, c) && !grid[r][c] && !visited[r][c];
}

void solve() {
    int dr[4] = {-1, 0, 1, 0}, dc[4] = {0, 1, 0, -1};
    int sr, sc, count;
    queue<pair<int, int>> q;
    for (int i = 0; i < K; i++) {
        cin >> sr >> sc;
        q.push({sr - 1, sc - 1});
        visited[sr - 1][sc - 1] = 1;
        count += 1;
    }
    while (!q.empty()) {
        auto [cr, cc] = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nr = cr + dr[i], nc = cc + dc[i];
            if (can_go(nr, nc)) {
                q.push({nr, nc});
                visited[nr][nc] = true;
                count += 1;
            }
        }
    }
    cout << count;
}
#include <iostream>
#include <cmath>
using namespace std;

bool check(int a, int b);
void solve(int n, int a, int b, int c);

int main() {
    int N, a, b, c;
    cin >> N >> a >> b >> c;
    solve(N, a, b, c);
    return 0;
}

bool check(int a, int b) {
    return 0 <= abs(a - b) && abs(a - b) <= 2;
}

void solve(int n, int a, int b, int c) {
    int count = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                if (check(a, i) || check(b, j) || check(c, k)) {
                    count++;
                }
            }
        }
    }
    cout << count;
}
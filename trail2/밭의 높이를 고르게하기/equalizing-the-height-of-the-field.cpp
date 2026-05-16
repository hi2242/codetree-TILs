#include <iostream>
#include <cmath>
using namespace std;

void solve(int n, int h, int t, int numbers[]);

int main() {
    int N, H, T;
    cin >> N >> H >> T;
    int numbers[N];
    for (int i = 0; i < N; i++) {
        cin >> numbers[i];
    }
    solve(N, H, T, numbers);
    return 0;
}

void solve(int n, int h, int t, int numbers[]) {
    int result = 1e9;
    for (int i = 0; i <= n - t; i++) {
        int temp = 0;
        for (int j = 0; j < t; j++) {
            temp += abs(numbers[i + j] - h);
        }
        result = min(result, temp);
    }
    cout << result;
}
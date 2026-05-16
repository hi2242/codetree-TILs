#include <iostream>
#include <algorithm>

using namespace std;

void solve(int k, int line[]);

int main() {
    int N, K;
    cin >> N >> K;
    int position, count;
    int line[101];
    for (int i = 0; i < 101; i++) {
        line[i] = 0;
    }
    for (int i = 0; i < N; i++) {
        cin >> count >> position;
        line[position] += count;
    }

    solve(K, line);
    return 0;
}

void solve(int k, int line[]) {
    int result = 0, temp;
    if (k >= 50) {
        for (int i = 0; i < 101; i++) {
            result += line[i];
        }
        cout << result;
        return;
    }
    for (int c = k; c <= 101 - k; c++) {
        temp = 0;

        for (int i = -k; i <= k; i++) {
            temp += line[c + i];
        }
        result = max(result, temp);
    }
    cout << result;
}
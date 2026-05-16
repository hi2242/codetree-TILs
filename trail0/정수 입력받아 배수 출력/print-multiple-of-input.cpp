#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    for (int i = N; i <= 5 * N; i += N)
        cout << i << ' ';
    return 0;
}
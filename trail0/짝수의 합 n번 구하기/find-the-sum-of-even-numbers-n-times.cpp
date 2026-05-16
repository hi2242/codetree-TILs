#include <iostream>
using namespace std;

int main() {
    int N, a, b, acc;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> a >> b;
        acc = 0;
        for (int j = a; j <= b; j++) {
            if (j % 2 == 0) {
                acc += j;
            }
        }
        cout << acc << endl;
    }
    return 0;
}
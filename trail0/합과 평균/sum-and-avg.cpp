#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    int total = A + B;
    double avg = (double)total / 2;
    cout << fixed;
    cout.precision(1);
    cout << total << ' ' << avg;
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    int total = a + b + c, avg = total / 3;
    cout << total << endl << avg << endl << total - avg;
    return 0;
}
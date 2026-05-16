#include <iostream>
using namespace std;

int main() {
    int A, B, C;
    cin >> A >> B >> C;
    if ((A > B and B > C) or (C > B and B > A))
        cout << B;
    else if ((B > C and C > A) or (A > C and C > B))
        cout << C;
    else
        cout << A;
    return 0;
}
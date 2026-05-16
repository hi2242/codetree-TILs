#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    cout << (A >= B ? 1 : 0) << endl;
    cout << (A > B ? 1 : 0) << endl;
    cout << (B >= A ? 1 : 0) << endl;
    cout << (B > A ? 1 : 0) << endl;
    cout << (A == B ? 1 : 0) << endl;
    cout << (A != B ? 1 : 0) << endl;
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    if (N >= 80) {
        cout << "pass" << endl;
    } else {
        cout << 80 - N << " more score" << endl;
    }
    return 0;
}
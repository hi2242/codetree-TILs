#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    cout << (N >= 3000 ? "book" : (N >= 1000 ? "mask" : "no"));
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;
    cout << ((N % 2 == 0 && N % 5 == 0) || (N % 2 != 0 && N % 3 == 0) ? "true" : "false");
    return 0;
}
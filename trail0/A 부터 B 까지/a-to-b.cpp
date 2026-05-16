#include <iostream>
using namespace std;

int main() {
    int A, B;
    cin >> A >> B;
    int temp = A;
    while (true) {
        cout << temp << ' ';
        if (temp % 2 != 0)
            temp *= 2;
        else
            temp += 3;
        if (temp > B)
            break;
    }
    return 0;
}
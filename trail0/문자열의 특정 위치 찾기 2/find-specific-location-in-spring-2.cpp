#include <iostream>
using namespace std;

int main() {
    string words[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char c;
    int count = 0;
    cin >> c;
    for (auto w : words) {
        if (w[2] == c || w[3] == c) {
            cout << w << endl;
            count++;
        }
    }
    cout << count;
    return 0;
}
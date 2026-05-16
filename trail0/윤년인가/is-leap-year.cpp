#include <iostream>
using namespace std;

int main() {
    int Y;
    string result = "true";
    cin >> Y;
    if (Y % 100 == 0 && Y % 400 != 0 || Y % 4 != 0) {
        result = "false";
    }
    cout << result;
    return 0;
}
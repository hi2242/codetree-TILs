#include <iostream>
using namespace std;

int main() {
    int gender, age;
    string result;
    cin >> gender >> age;
    if (gender == 0) {
        result = age >= 19 ? "MAN" : "BOY";
    } else {
        result = age >= 19 ? "WOMAN" : "GIRL";
    }
    cout << result;
    return 0;
}
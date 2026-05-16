#include <iostream>
using namespace std;

int main() {
    string first, second, result;
    cin >> first >> second;
    if (first.length() > second.length())
        result = first;
    else if (second.length() > first.length())
        result = second;
    else
        result = "same";
    cout << result << ' ';
    if (result != "same")
        cout << result.length();
    return 0;
}
#include <iostream>
using namespace std;

int main() {
    string word;
    cin >> word;
    word[1] = 'a';
    word[word.length() - 2] = 'a';
    cout << word;
    return 0;
}
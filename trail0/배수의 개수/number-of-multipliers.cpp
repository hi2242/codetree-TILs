#include <iostream>
using namespace std;

int main() {
    int numbers[10];
    int multiple_3 = 0, multiple_5 = 0;
    for (int i = 0; i < 10; i++)
        cin >> numbers[i];
    for (auto i : numbers) {
        if (i % 3 == 0)
            multiple_3++;
        if (i % 5 == 0)
            multiple_5++;
    }
    cout << multiple_3 << ' ' << multiple_5;
    return 0;
}
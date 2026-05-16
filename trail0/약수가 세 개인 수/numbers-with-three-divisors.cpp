#include <iostream>
using namespace std;

int main() {
    int start, end, count = 0, temp;
    cin >> start >> end;
    for (int i = start; i <= end; i++) {
        temp = 0;
        for (int j = 1; j <= i; j++) {
            if (i % j == 0) {
                temp++;
            }
        }
        if (temp == 3) {
            count++;
        }
    }
    cout << count;
    
    return 0;
}
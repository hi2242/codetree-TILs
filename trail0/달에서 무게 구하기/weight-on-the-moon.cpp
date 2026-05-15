#include <iostream>
using namespace std;

int main() {
    int weight = 13;
    double gravitation = 0.165;
    cout << fixed;
    cout.precision(6);
    cout << weight << " * " << gravitation << " = " << weight * gravitation;
    return 0;
}
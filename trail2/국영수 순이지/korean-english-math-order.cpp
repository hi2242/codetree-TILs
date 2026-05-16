#include <iostream>
#include <algorithm>
using namespace std;

const int MAX_N = 10;

class Student {
    public:
        string name;
        int kor;
        int eng;
        int math;
    
    Student(string name, int kor, int eng, int math) {
        this->name = name;
        this->kor = kor;
        this->eng = eng;
        this->math = math;
    }
    Student() = default;
};

bool cmp(Student& a, Student& b);

int main() {
    int n;
    Student students[MAX_N];
    cin >> n;
    for (int i = 0; i < n; i++) {
        string name;
        int kor, eng, math;
        cin >> name >> kor >> eng >> math;
        students[i] = Student(name, kor, eng, math);
    }
    sort(students, students + n, cmp);
    for (int i = 0; i < n; i++) {
        cout << students[i].name << ' ' << students[i].kor << ' ' << students[i].eng << ' ' << students[i].math << endl;
    }
    return 0;
}

bool cmp(Student& a, Student& b) {
    if (a.kor != b.kor) {
        return a.kor > b.kor;
    } else if (a.eng != b.eng) {
        return a.eng > b.eng;
    }
    return a.math > b.math;
}
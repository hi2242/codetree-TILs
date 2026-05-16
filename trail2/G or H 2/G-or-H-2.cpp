#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

void solve(vector<pair<int, int>>& people, int n);

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> people;
    int start = 1e9, end = -1e9;
    for (int i = 0; i < N; i++) {
        int position;
        char alpha;
        cin >> position >> alpha;
        people.push_back(alpha == 'G' ? pair<int, int>{position, 1} : pair<int, int>{position, 2});
    }
    sort(people.begin(), people.end());
    solve(people, N);
    return 0;
}

void solve(vector<pair<int, int>>& people, int n) {
    int result = 0;
    for (int i = 0; i < n; i++) {
        int count_1 = 0, count_2 = 0, temp = 0;
        for (int j = i; j < n; j++) {
            if (people[j].second == 1) {
                count_1++;
            } else if (people[j].second == 2) {
                count_2++;
            }
            if ((count_1 != 0 && count_2 == 0) || (count_1 == 0 && count_2 != 0) || (count_1 != 0 && count_1 == count_2)) {
                result = max(result, people[j].first - people[i].first);            }
        }
    }
    cout << result;
}
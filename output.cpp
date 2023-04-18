#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    string s;
    cin >> s;

    for (int i = 0; i < s.length(); ++i) {
        if (s[i] == 'A' || s[i] == 'O' || s[i] == 'Y' || s[i] == 'E' || s[i] == 'U' || s[i] == 'I' || s[i] == 'a' || s[i] == 'o' || s[i] == 'y' || s[i] == 'e' || s[i] == 'u' || s[i] == 'i') {
            s.erase(i, 1);
            --i;
        }
        else {
            s.insert(i, 1, '.');
            s[i + 1] = tolower(s[i + 1]);
            ++i;
        }
    }

    cout << s;
    return 0;
}
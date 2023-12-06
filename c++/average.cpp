//find the average of the foo array

#include <iostream>
#include <cstring>

using namespace std;
int ans = 0;
int out;

int main() {
    int foo [5] = { 16, 2, 77, 40, 5 };

    for (int i : foo) {

        ans += i;

    }
    out = ans / 5;

    std::cout << out << std::endl;

    return 0;
}

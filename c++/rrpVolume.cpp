//Write a C++ program that calculates the volume of a right rectangle pyramid.

#include <iostream>
#include <cmath>


using namespace std;


void rrp(int l, int w, int h) {

    double ans = (l * w * h) / 3;


    std::cout << ans << std::endl;

}

int main() {

    rrp(3,3,5);

    return 0;
}

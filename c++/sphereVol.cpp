//Write a C++ program that calculates the volume of a sphere.

#include <iostream>
#include <cmath>


using namespace std;


void sphere(int rad) {

    double ans = pow(rad,3) * M_PI * (4.0 / 3.0);


    std::cout << ans << std::endl;

}

int main() {

    sphere(5);

    return 0;
}

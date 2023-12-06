//Write a C++ program that calculates the volume of a cube.

#include <iostream>
#include <cmath>


using namespace std;


void cube(int edge) {

    double ans = pow(edge,3);


    std::cout << ans << std::endl;

}

int main() {

    cube(5);

    return 0;
}

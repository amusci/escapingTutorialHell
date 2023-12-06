//Similarly, converting temperature to another unit of measurement is a helpful program to build.
// See if you can create a program that takes inputted
// temperature in Celsius and returns the same temperature in Fahrenheit.
// (0°C × 9/5) + 32 = 32°F

#include <iostream>

int main() {
    double cel;
    double fah;

    std::cout << "Enter your temperature in Celsius: "; // Type a number and press enter
    std::cin >> cel; // Get user input from the keyboard

    fah = (cel * 9/5) + 32;

    std::cout << cel << " converted to Fahrenehit is " << fah << std::endl;

    return 0;
}

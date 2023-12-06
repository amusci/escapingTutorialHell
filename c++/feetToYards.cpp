#include <iostream>

int main() {
    double inp;
    double out;

    std::cout << "Type a number: "; // Type a number and press enter
    std::cin >> inp; // Get user input from the keyboard

    std::cout << "Your number is: " << inp << std::endl; // Display the input value with a newline

    out = inp / 3;

    std::cout << inp << " converted to yards is " << out << std::endl;

    return 0;
}

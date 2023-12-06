//string lowercase to uppercase

#include <iostream>
#include <cstring>

using namespace std;


int main() {
    char str[6] = "geeks";

    for (int i = 0; i <strlen(str); i++)
        putchar(toupper(str[i]));


    return 0;
}

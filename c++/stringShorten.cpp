//Can you construct a function that accepts a string as input
// and returns a shortened version of 10


#include <iostream>
#include <string>

using namespace std;

void myFunction(string s) {

    int len = s.length();
    if (len > 10) {

        len = 10;
    }



    for (int i = 0; i < len; i++) {
        cout << s[i] << endl;

    }
}



int main() {
    myFunction("oaooaooaoaooaooaoaaooaoaoaoa2123213132");
    return 0;
}

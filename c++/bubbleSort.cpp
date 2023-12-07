//sort a god damn array

#include <bits/stdc++.h>


using namespace std;
int temp;


void b_sort(int arr[], int length) {

    bool swapped;

    for (int i = 0; i < length; i++) { // outer loop: this pases the array through length amount of times

        swapped = false; // initalize swap = false early
        for (int j = 0; j < length - 1 ; j++) { // inner loop: iterates through each array element

            if (arr[j] > arr[j+1]) { // this checks if the element is greater than the next one

                //swap(arr[j], arr[j+1]); // if so, swap them

                swapped = true; // make sure program continues
                temp = arr[j+1];
                arr[j+1] = arr[j];
                arr[j] = temp;
            }

        }

        if (!swapped) { // if no more swaps
            break;  // break
        }
    }

}


void print_array(int arr[], int size) {

    int i;
    for (i = 0; i < size; i++)
        cout << " " << arr[i];

}

int main() {

    int unsorted_array[10] = {51,44,32,20,92,81,172,46,143,110};
    int n = sizeof(unsorted_array) / sizeof(unsorted_array[0]); // size of index = 4, size of entire array is 4 * whatever
    b_sort(unsorted_array,n);
    print_array(unsorted_array, 10);

    return 0;

}

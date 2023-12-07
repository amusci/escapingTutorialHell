//sort a god damn array

#include <bits/stdc++.h>


using namespace std;


void b_sort(int arr[], int length) {

    bool swapped;

    for (int i = 0; i < length; i++) {
        swapped = false;
        for (int j = 0; j < length - 1; j++) {

            if (arr[j] > arr [j+1]) {
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }
}

void print_array(int arr[], int size) {

    int i;
    for (i = 0; i < size; i++)
        cout << " " << arr[i];

}

int main() {
    int unsorted_array[10] = {5,4,3,2,9,8,7,6,1,0};
    int n = sizeof(unsorted_array) / sizeof(unsorted_array[0]);
    b_sort(unsorted_array,n);
    print_array(unsorted_array, 10);

    return 0;

}

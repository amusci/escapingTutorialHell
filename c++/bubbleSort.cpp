//sort a god damn array

#include <bits/stdc++.h>


using namespace std;


void b_sort(int arr[]) {

    bool swapped;

    for (int i = 0; i < 10; i++) {
        swapped = false;
        for (int j = 0; j < 10 - 1; j++) {

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
    b_sort(unsorted_array);
    print_array(unsorted_array, 10);

    return 0;
}

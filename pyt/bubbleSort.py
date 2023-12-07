def b_sort(arr, len):
    for i in range(len - 1):
        swapped = False
        for j in range(0, len - 1):

            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            return


if __name__ == '__main__':
    arr = [3, 213321, 3312, 43242, 5, 323, 435237627, 2121, 1223, 1]
    n = len(arr)
    b_sort(arr, n)
    print(arr)

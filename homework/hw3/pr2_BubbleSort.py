def main():
    arr = [10, 80, 23, 1, 78, 9]
    bubbleSort(arr)
    print(arr)


def bubbleSort(arr):
    l = len(arr)
    # Traverse through all array elements
    for i in range(l-1):
        # Last elements are already in place
        # Traverse array from 0 to l-i-1
        for j in range(l-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


main()

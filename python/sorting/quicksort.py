def quicksort(array):
    """
    Works by always taking the last point in the array and reorganizing it so
    all smaller elements go before it and all larger elements go after it
    """

    # set up bounds
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[-1]

    for item in array: # O(n) 
        if item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
        elif item < pivot:
            low.append(item)
    result = quicksort(low) + same + quicksort(high) # split up into nlogn in best case... 
    return result

print(quicksort([1, 4, 2, 5, 2, 55, 33, 43, 2]))



#   1   4   2   5   2   55  33  43  2

#   1   [2  2]  4   5   33  43  55                                   

# 4   5   33  43  55   
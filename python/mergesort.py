"""
Merge sort implementation from 

DIVIDE AND CONQUER METHOD: 
    https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python

Important steps: 
#1 separate list into individuals and left and right nodes
    and set up recursively

#2 merge two (sorted) arrays... return one
    MAKE SURE to include the tail ends of the arrays incase they are very different in shape! 
    Properly set up base cases! 

Thanks to its runtime complexity of O(n log2n), merge sort is a very efficient algorithm that scales well as the size of the input array grows. It’s also straightforward to parallelize because it breaks the input array into chunks that can be distributed and processed in parallel if necessary.

That said, for small lists, the time cost of the recursion allows algorithms such as bubble sort and insertion sort to be faster. For example, running an experiment with a list of ten elements results in the following times:

"""

def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2

    # breaks everything down to 0 or 1 point all the way down.... 
    # divide and conquer method
    left=merge_sort(array[:midpoint])
    right=merge_sort(array[midpoint:])

    return merge(left, right)


def merge(left, right):
    """
    Args:
        left (list)
        right (list)
    Returns: 
        merged (list)
    """
    # print(left, right)
    # base cases:
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    # initialize left and right pointers
    merged = []
    l_idx = 0
    r_idx = 0    
    
    # [8, 3, 1, 7, 0, 10, 2]
    #   8   3   1   
    #   7   0   10  2

    #   7   0   8   3   1   
    # l: 2
    # r: 3

    while len(merged) < len(left) + len(right): 
        print(f'len: {len(merged)}')
        if left[l_idx] <= right[r_idx]:
            merged.append(left[l_idx])
            l_idx+=1
        else:
            merged.append(right[r_idx])
            r_idx+=1

        if r_idx == len(right):
            merged += left[l_idx:]
            break

        if l_idx == len(left):
            merged += right[r_idx:]
            break

    return merged
    


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
# print('{} to {}'.format(test_list_1, merge_sort(test_list_1)))
# print('{} to {}'.format(test_list_2, merge_sort(test_list_2)))
# print('{} to {}'.format(test_list_3, merge_sort(test_list_3)))

print('answer', merge_sort(test_list_1) )
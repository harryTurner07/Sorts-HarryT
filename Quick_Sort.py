def quick_sort(items):
    """
    A quick sort is a sorting algorithm that uses pivots to order the items in a list
    """
    length = len(items) # Im not writing this over and over
    # Base Case
    if length <= 1:
        return items
    else:
        pivot_value = items[0]
        small_values = []
        large_values = []
        # Recursive Case
        for i in range(length):
            if items[i] < pivot_value:
                small_values.append(i)
            else:
                large_values.append(i)
            return quick_sort(small_values) + [pivot_value] + quick_sort(large_values)

list_of_items = [9,6,3,8,1,5,4,2,7,10]

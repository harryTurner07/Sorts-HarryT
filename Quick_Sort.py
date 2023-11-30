def quick_sort(items):
    """
    A quick sort is a sorting algorithm that uses pivots to order the items in a list
    """
    # Base Case
    if len(items) <= 1:
        return items
    else:
        pivot_value = items[0]
        small_values = []
        large_values = []
        # Recursive Case
        for i in range(1,len(items)):
            if items[i] < pivot_value:
                small_values.append(items[i])
            else:
                large_values.append(items[i])
        return quick_sort(small_values) + [pivot_value] + quick_sort(large_values)

list_of_items = [2,5,1,6,4,3]
print(quick_sort(list_of_items))
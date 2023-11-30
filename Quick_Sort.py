def quick_sort(items):
    """
    A quick sort is a sorting algorithm that uses pivots to order the items in a list
    """
    # Base Case
    if len(items) <= 1:
        return items
    else:
        # Just sets the variables to be used - here because if the length is 1 or less, not needed
        pivot_value = items[0]
        small_values = []
        large_values = []
        # Recursive Case
        for i in range(1,len(items)):
            if items[i] < pivot_value:
                small_values.append(items[i]) # If the selected item is smaller than the pivot, add the INDEX OF I to the list of small values
            else:
                large_values.append(items[i]) # Same as small but this time, add/append to the big item list
        return quick_sort(small_values) + [pivot_value] + quick_sort(large_values)
        # Return the small list, the original pivot item, and the large list all as one big big list

list_of_items = [2,5,1,6,4,3]
print(quick_sort(list_of_items))

# Bug(s)
# Items being appended wrong
# ^ Fixed - lines were the value and not index
# ^ e.g. append(i) when it should have been append(items[i])
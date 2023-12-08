def merge_sort(item_list):
    """
    A merge sort works by essentially splitting the list into single values, then ordering
    them into one single list - re-ordering them if needed.
    """
    if len(item_list) > 1:
        middle_point = len(item_list) // 2
        left = item_list[:middle_point]
        right = item_list[middle_point:]
        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        half_a = 0
        half_b = 0
        
        # Iterator for the main list
        main_list = 0
        
        while half_a < len(left) and half_b < len(right):
            if left[half_a] <= right[half_b]:
              # The value from the left half has been used
              item_list[main_list] = left[half_a]
              # Move the iterator forward
              half_a += 1
            else:
                item_list[main_list] = right[half_b]
                half_b += 1
            # Move to the next slot
            main_list += 1

        # For all the remaining values
        while half_a < len(left):
            item_list[main_list] = left[half_a]
            half_a += 1
            main_list += 1
        while half_b < len(right):
            item_list[main_list]=right[half_b]
            half_b += 1
            main_list += 1
        return item_list

list_of_items = [5,7,2,6,1,4,3]
print(merge_sort(list_of_items))

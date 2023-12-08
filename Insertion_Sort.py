def insertion_sort(items):
    """
    An insertion sort is similar to a bubble sort, but it works one item at a time
    With every new item in a list, it sorts it ready for the next item -
    it doesn't move on until the past item and the current list is sorted
    """
    for i in range(len(items)):
        current_item = items[i]
        new_index = i
        while (new_index > 0) and (items[new_index - 1] > current_item): # correct position not found
            items[new_index] = items[new_index - 1] # shuffle item accross
            new_index -= 1
        items[new_index] = current_item # Places item to new position
    return items

list_of_items = [1,9,2,8,3,7,4,6,5]
print(insertion_sort(list_of_items))
def bubble_sort(items):
    """
    A sorting algorithm using bubbles, it goes through the list bubbling the highest numbers to the top.
    """
    length = len(items) # Set length to be the length of the list
    swapped = True # Set swapped to be True for the loop
    while swapped:
        swapped = False # Reset at the start of each iteration
        for i in range(length - 1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                # ^ if the items before is greater than the item next to it, swap them
                swapped = True
        length -= 1 # Should hopefully decrease the length everytime the swap is made
    return items

item_list = [5,7,2,7,1,4,3] # Items
print(bubble_sort(item_list))
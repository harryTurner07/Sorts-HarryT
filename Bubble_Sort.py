def bubble_sort(items):
    """
    A sorting algorithm using bubbles, it goes through the list bubbling the highest numbers to the top.
    """
    l = len(items) # Set l to be the length of the list
    swapped = True # Set swapped to be True for the loop
    l = int(l) - 1 # For some reason this line is needed to keep it in range :/
    while swapped:
        swapped = False # Reset at the start of each iteration
        for i in range(l):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
    return items

item_list = [5,7,2,7,1,4,3]
print(bubble_sort(item_list))
def swap(lst):
    if len(lst) < 2:
        # If the list has 0 or 1 element, it cannot be swapped.
        return lst

    # Swapping the first and last elements using tuple unpacking.
    lst[0], lst[-1] = lst[-1], lst[0]

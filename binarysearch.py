def binary_search(lst: list, n) -> int:
    if not lst:
        raise ValueError("List is None.")

    if len(lst) == 0:
        raise ValueError("Can't sort a zero length list.")

    low = 0
    hi = len(lst) - 1

    while low <= hi:
        mid = int((low + hi) / 2)

        if n == lst[mid]:
            return mid

        if n > lst[mid]:
            low = mid + 1
        else:
            hi = mid - 1

    raise ValueError("Item not found.")

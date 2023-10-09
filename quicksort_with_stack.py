def quick_sort(arr):
    range_stack = [(0, len(arr) - 1)]
    while range_stack:
        start, end = range_stack.pop()
        pivot = arr[start]
        index = start
        exchange_index = start
        while index < end:
            index += 1
            if arr[index] < pivot:
                exchange_index += 1
                arr[index], arr[exchange_index] = arr[exchange_index] ,arr[index]
        arr[start], arr[exchange_index] = arr[exchange_index] ,arr[start]
        if start < exchange_index - 1:
            range_stack.append((start, exchange_index -1))
        if exchange_index + 1 < end:
            range_stack.append((exchange_index+1, end))
    return arr


def test():
    arr = [5,2,7,34,6,8,0,45,234,64,2,1,3]
    print(quick_sort(arr))


if __name__ == "__main__":
    test()
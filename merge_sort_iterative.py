# This is an iterative implementation of merge sort algorithm

def merge_sort(arr):
    another_arr = []
    slice_size = 1
    while slice_size < len(arr):  
        for i in range(0, len(arr), slice_size*2): 
            first_start = i
            first_end = i + slice_size - 1
            second_start = i + slice_size
            second_end = min(i + slice_size*2 - 1, len(arr) - 1)
            another_arr.extend(_sort_slices(arr, first_start, first_end, second_start, second_end))
        arr = another_arr
        another_arr = []
        slice_size *= 2 # <-- ** logn
    return arr


def _sort_slices(arr, first_start, first_end, second_start, second_end):
    result = []
    while first_start <= first_end and second_start <= second_end:
        if arr[first_start] < arr[second_start]:
            result.append(arr[first_start])
            first_start += 1
        else:
            result.append(arr[second_start])
            second_start += 1
    if first_start <= first_end:
        result.extend(arr[first_start:first_end+1])
    elif second_start <= second_end:
        result.extend(arr[second_start:second_end+1])
    return result



if __name__ == '__main__':
    arr = [3, 5, 1, 2, 4, 6, 8, 7]
    print(merge_sort(arr))

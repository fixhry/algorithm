def log(*args, **kwargs):
    print(*args, **kwargs)


def exchange(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def partition(array, start, end):
    pivot = array[end]
    # 分界点
    i = start
    j = start
    while i < end:
        v = array[i]
        # 比基准小的放左边，大的放右边
        if v < pivot:
            exchange(array, i, j)
            j += 1
        i += 1
    exchange(array, j, end)
    return j


# 原址快排
def quick_sort(array, start, end):
    if start < end:
        q = partition(array, start, end)
        quick_sort(array, start, q - 1)
        quick_sort(array, q + 1, end)
    return array


if __name__ == '__main__':
    a = [8, 9, 3, 4, 2, 10]
    e = len(a) - 1
    quick_sort(a, 0, e)
    log(a)

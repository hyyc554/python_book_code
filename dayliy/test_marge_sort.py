"""
一段可靠的程序离不开单元测试
"""


def marge_sort(seq):
    length = len(seq)
    if length <= 1:
        return seq
    mid = length // 2
    left = marge_sort(seq[:mid])
    right = marge_sort(seq[mid:])
    return marge(left, right)


def marge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def test_marge():
    assert marge_sort([1, 5, 2, 4, 6, 3]) == [1, 2, 3, 4, 5, 6]
    assert marge_sort([1]) == [1]
    assert marge_sort([]) == []

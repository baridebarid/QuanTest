# -*- coding: utf-8
"""
Дан массив из n целых чисел. Написать программу, которая находит
количество способов разбить все элементы массива на три подмассива так,
чтобы сумма элементов в каждом массиве была одинаковой.

1 <= n <= 500000, где n - количество элементов в массиве
abs(a[i]) <= 1000000000, где a[i] - элементы входного массива

Пример

Input:
5
1 2 3 0 3
Output:
2

Существует два способа разбить массив на три подмассива с одинаковой суммой:
[1, 2], [3], [0, 3] и [1, 2], [3, 0], [3].

Требование к задаче

1. Работать со стаднартным вводом и выводом.
2. Оценить ассимптотическую сложность построенного алгоритма.
 """

import sys

ARRAY_LEN = 5 * 10 ** 5
RANGE = 10 ** 9


def read_array_length():
    print "Enter array length: "
    raw_array_len = sys.stdin.readline()
    array_len = int(raw_array_len)
    if array_len > ARRAY_LEN:
        print "Array cannot be longer than 500000."
        array_len = ARRAY_LEN
    return array_len


def read_array(array_len):
    print "Enter array elements: "
    raw_array = sys.stdin.readline()
    array = [int(elem) for elem in raw_array.split()]

    if len(array) < array_len:
        print "Entered array is too small for its length."
    elif len(array) > array_len:
        print "Entered array is cropped to its length."
        array = array[:array_len]
    return array


def clean_input_array():
    array = read_array(read_array_length())
    for ind, el in enumerate(array):
        if el > RANGE:
            print "Elements cannot be bigger than 1000000000."
            array.pop(ind)
            array.insert(ind, RANGE)
        elif el < -RANGE:
            print "Elements cannot be less than -1000000000."
            array.pop(ind)
            array.insert(ind, -RANGE)
    print array
    return array


def count_ways(array):
    """ Counting number of  ways to break input array to subarrays of equal sum """

    print "\narray", array
    total_sum = sum(array)
    result = 0

    if total_sum % 3 == 0:  # Checking is it possible to get equal sums
        array_len = len(array)
        count = [0] * array_len
        sub_sum = 0
        third_of_sum = total_sum / 3

        for i in range(array_len - 1, -1, -1):
            sub_sum += array[i]
            if sub_sum == third_of_sum:
                count[i] = 1

        for i in range(array_len - 2, -1, -1):
            count[i] += count[i + 1]

        sub_sum = 0
        for i in range(array_len - 2):
            sub_sum += array[i]
            if sub_sum == third_of_sum:
                result += count[i + 2]
    else:
        print "Sum will never be equal. Just give up."

    print result, "way(s)"
    return result


def test_count_ways():
    assert count_ways([1, 2, 3, 0, 3]) == 2
    assert count_ways([0, 1, -1, 0]) == 1
    assert count_ways([0, 0, 0, 0, 0, 0, 0, 0, 0]) == 28
    assert count_ways([1, 1, 1, 1, 1, 1]) == 1
    assert count_ways([3, 3, -3, 3, 3]) == 3

if __name__ == '__main__':

    test_count_ways()
    array = clean_input_array()
    count_ways(array)
    raw_input("Press <ENTER> to exit.")



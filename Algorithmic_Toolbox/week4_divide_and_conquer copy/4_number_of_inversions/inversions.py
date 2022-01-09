# Uses python3
import sys

def my_sort(a):
    num_inversions = 0
    if len(a) < 2:
        return a, 0
    i = -1
    while i <len(a)-1:
        i += 1
        for j in range(i, len(a)):
            if i != j:
                if a[i] > a[j]:
                    a[i], a[j] = a[j], a[i]
                    print(a)
                    num_inversions += 1
                    i = -1
                    break

    return a, num_inversions

def merge_sort(a, left, right):
    num_inversions = 0
    if right - left < 2:
        return a, 0
    if right - left == 2:
        return my_sort(a)
    
    ave = (left + right) // 2

    a, left_invs = merge_sort(a, left, ave)
    
    a, right_invs = merge_sort(a, ave, right)

    num_inversions += left_invs + right_invs

    a, more_invs = my_sort(a)

    return a, num_inversions + more_invs

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # a = [2, 4, 3, 6, 1]
    
    # print(a)

    a, num_inversions = merge_sort(a, 0, len(a))

    print(f'there were {num_inversions} inversion(s).  The sorted array is {a}.')

    print(num_inversions)

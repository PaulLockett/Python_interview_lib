# https://www.geeksforgeeks.org/merge-sort/
# Python program for implementation of
# MergeSort (Alternative) Try it on a linked list


def merge_sort(values):
    if len(values) > 1:
        m = len(values) // 2  # Finding the mid of the array
        left = values[:m]  # Dividing the array elements
        right = values[m:]  # into 2 halves
        left = merge_sort(left)  # Sorting the first half
        right = merge_sort(right)  # Sorting the second half

        values = []

        # Copy data to temp array values[]
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                values.append(left[0])
                left.pop(0)
            else:
                values.append(right[0])
                right.pop(0)

        # Checking if any element was left
        for i in left:
            values.append(i)
        for i in right:
            values.append(i)

    return values


# Input list
a = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(*a)

a = merge_sort(a)

# Print output
print("Sorted array is : ")
print(*a)

# This code is contributed by Marco Lam

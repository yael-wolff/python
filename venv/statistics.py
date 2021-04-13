values = [1, 7, 5, 7, 3, 3]

def happy(values):
    return 0


def mean(values):
    """
    This function finds the mean of given values.
    :parameters: values
    :type: float[]
    :returns: sum
    :type: float
    """
    sum = 0
    count = 0
    for i in values:
        sum += i
        count = count + 1
    return(count)
    return(sum/count)


def median(values):
    count = 0
    med_val = 0
    for i in values:
        count = count + 1
    if count % 2 == 0 :
        place = int(count / 2)
        mid_val = ((values[place]) + (values[place-1]))/2
    if count % 2 == 1 :
        mid_val = values[(count/2) + 1]
    return(mid_val)
# need to add docstring

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)



n = len(values)
print("Given array is")
for i in range(n):
    print("%d" % values[i]),

mergeSort(values, 0, n - 1)


my_sum(values)
mean(values)
median(values)

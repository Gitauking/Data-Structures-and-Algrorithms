#first algorithm bubble sort
#compare if left > than right swap them

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j+1], arr[j]
    return arr

numbers = [30,56,89,43,66,12,75,33,73,93,17,57]
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)


#second sorting algorithm selection sort
#looks for the smallest index and swaps to the right


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i #assumes the smallest index

        for j in range(i + 1, n): #look for smaller index
            if arr[j] < arr[min_index]:
                min_index = j #update the smallest found

        #swap the smallest with the current
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

numbers = [30,56,89,43,66,12,75,33,73,93,17,57]

sort_number = selection_sort(numbers)

print(sort_number)


#third sorting algorithm merge sort
#divide and conquer. split the array in half over and over again and put the back in the right order

def merge_sort(arr):
    if len(arr) <=1: #base case
        return arr
    
    #step 1: divide
    mid  = len(arr) // 2

    left = merge_sort(arr[:mid])#sorts in the left half
    right = merge_sort(arr[mid:])#sorts in the right half
    #conquer

    return merge(left,right)

def merge(left, right):
    result = []
    i=j=0

    #compare elements from both halves and merge them

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    #add any leftover elements

    result.extend(left[i:])
    result.extend(right[j:])

    return result

numbers = [30, 56, 89, 43, 66, 12, 75, 33, 73, 93, 17, 57]
sorted_numbers = merge_sort(numbers)
print("Sorted:", sorted_numbers)

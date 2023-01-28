#1: Please write a function in python using break and continue
def process_list(numbers): # it takes a list as argument
    for num in numbers: # iterating the list
        if num < 0: # if number is lessthan
            continue # skip the number
        if num > 100: # if greater than 100
            break # breaking the loop
        print(num) # if both condition met wrong it print the number

nums = [1, -2, 50, 200, 25]
process_list(nums)


my_list = [[10,20,30],[40,50,60],[70,80,90]]

# In the above list, create a function to swap 1st and 3rd element in all the sublists.

def swap(my_list): # taking the list
    for i in my_list: # iterating the list
        li = i # access the list 
        li[0], li[-1] = li[-1], li[0] # swapping using the index 0-->first and -1 -->last
    return my_list # returning the list
print(swap(my_list))


# Merge sort is fast it has a time complexity of O(n log n), 
# which means that the time it takes to sort an array grows logarithmically with the size of the array. 
# This makes it very efficient for large arrays. It works by dividing the array into two halves, sorting each half, and then merging the sorted halves back together.
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

arr = [3,4,5,3,3,5,4,6,7,4,3,2,1,5,7,8,9]
print(merge_sort(arr))
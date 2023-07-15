"""
Question : Given an array, make it so that you the sum of array elements to its positions (Σ i*A[i]) is maximum possible. 
Provided, you are able to swap two adjacent elements of the array. 
Note: You are not allowed to swap elements that you have already swapped previously. 
"""

arr = [2,1,5,100,7,3]
dyn_arr = arr.copy()
positions = []
for i in range(len(arr)):
    m = max(dyn_arr)
    p = dyn_arr.index(m)
    dyn_arr[p] = 0
    if (p+1 < len(arr)) and (p not in positions):
        if (p+1 not in positions):
            positions.append(p)
            positions.append(p+1)
            arr[p+1],arr[p] = arr[p], arr[p+1]
print(arr) 

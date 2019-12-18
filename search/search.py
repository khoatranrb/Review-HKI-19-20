def linear_search(arr, key):
    for i in len(arr):
        if arr[i]==key:
            return i
    return None

#################################################################
def binary_search(arr,lo,hi,key):
    mid = int(lo + (hi-lo)/2)
    if arr[mid]==key:
        return mid
    elif arr[mid]<key:
        binary_search(arr,mid,lo,key)
    else:
        binary_search(arr, lo, mid, key)


def interpolation_search(arr,lo,hi,key):
    mid = int(lo + ((hi - lo) / (arr[hi]-arr[lo]))*(key-arr[lo]))
    if arr[mid] == key:
        return mid
    elif arr[mid] < key:
        interpolation_search(arr, mid, lo, key)
    else:
        interpolation_search(arr, lo, mid, key)

################################################################

def selection_search(arr,k):
    l = len(arr)
    for i in range(k):
        p = i
        for j in range(i, l):
            if arr[j] < arr[p]:
                p = j
        arr[i], arr[p] = arr[p], arr[i]
        
    return arr[k-1]




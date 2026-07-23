def binarySearch(arr, left, right, key):
  mid = left + right - 1 // 2
  if key == arr[mid]:
    return mid
  elif key > arr[mid] and mid != right:
    return binarySearch(arr, mid + 1, right, key)
  elif key < arr[mid] and mid != left:
    return binarySearch(arr, left, mid - 1, key)
  else:
    return -1

arr = [0, 1, 2, 5, 7, 8]
n = len(arr)
key = 2
position = binarySearch(arr, 0, n-1, key)
print("found ", key, " at index ", position)
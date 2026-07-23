def linearSearch(arr, n, key):
  for i in range(n):
    if arr[i] == key: 
      return i

arr = [1, 5, 2, 7, 8, 0]
n = len(arr)
key = 5
position = linearSearch(arr,  n, key)
print("found ", key, " at index ", position)
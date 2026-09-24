arr = [5, 2, 7, 3, 1, 9]
n = len(arr)

# bubble sort
def bubbleSort(arr, n):
  for i in range(1, n):
    for j in range(1, n):
      if arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
  return arr
print(bubbleSort(arr, n))

# insertion sort
def insertionSort(arr, n):
  for i in range(n):
    j = i
    k = arr[i]
    while arr[j-1] > k and j-1 >= 0:
      arr[j] = arr[j-1]
      j -= 1
    arr[j] = k
  return arr
print(insertionSort(arr, n))

# selection sort
def selectionSort(arr, n):
  for i in range(n):
    minIdx = i
    for j in range(i, n):
      if arr[j] < arr[minIdx]:
        minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
  return arr
print(selectionSort(arr, n))

# merge sort
def mergeSort(arr, n):
  def merge(arr, low, mid, high):
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]
    n1 = len(left)
    n2 = len(right)
    i, j, k = 0, 0, low
    while(i < n1 and j < n2):
      if(left[i] < right[j]):
        arr[k] = left[i]
        i+=1
      else:
        arr[k] = right[j]
        j+=1
      k+=1
    while(i < n1):
      arr[k] = left[i]
      i+=1
      k+=1
    while(j < n2):
      arr[k] = right[j]
      j+=1
      k+=1
  def mS(arr, low, high):
    if low < high:
      mid = (low + high) // 2
      mS(arr, low, mid)
      mS(arr, mid+1, high)
      merge(arr, low, mid, high)
  mS(arr, 0, n-1)
  return arr
print(mergeSort(arr, n))

# quick sort
def quickSort(arr, n):
  def partition(arr, left, right):
    i = left - 1
    p = arr[right]
    for j in range(left, right):
      if arr[j] <= p:
        i+=1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return i+1
  def qs(arr, left, right):
    if left < right:
      pi = partition(arr, left, right)
      qs(arr, left, pi-1)
      qs(arr, pi+1, right)
  qs(arr, 0, n-1)
  return arr
print(quickSort(arr, n))

# shell sort
def shellSort(arr, n):
  gap = n // 2
  while gap > 0:
    for i in range(gap, n):
      temp = arr[i]
      j = i
      while j >= gap and arr[j - gap] > temp:
        arr[j] = arr[j - gap]
        j -= gap
      arr[j] = temp
    gap //= 2
  return arr
print(shellSort(arr, n))

def heapSort(arr):
  def heapify(arr, n, i):
      largest = i
      left = 2 * i + 1
      right = 2 * i + 2
      if left < n and arr[left] > arr[largest]:
          largest = left
      if right < n and arr[right] > arr[largest]:
          largest = right
      if largest != i:
          arr[i], arr[largest] = arr[largest], arr[i]
          heapify(arr, n, largest)
  def heap_sort(arr):
      n = len(arr)
      for i in range(n // 2 - 1, -1, -1):
          heapify(arr, n, i)
      for i in range(n - 1, 0, -1):
          arr[0], arr[i] = arr[i], arr[0] 
          heapify(arr, i, 0)
      return arr
  return heap_sort(arr)
print(heapSort(arr))
#include<iostream>

void mergeSort(int arr[], int left, int right);
void merge(int arr[], int left, int mid, int right);

void mergeSort(int arr[], int left, int right) {
  if (left < right) {
    int mid = (left + right) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
  }
}

void merge(int arr[], int left, int mid, int right) {
  int n1 = mid - left + 1;
  int n2 = right - mid;
  int L[n1], R[n2];
  for (int i = 0; i < n1; i++) {
    L[i] = arr[left + i];
  }
  for (int i = 0; i < n2; i++) {
    R[i] = arr[mid + 1 + i];
  }
  int i = 0, j = 0, k = left;
  while (i < n1 && j < n2) {
    if (L[i] < R[j]) {
      arr[k++] = L[i++];
    } else {
      arr[k++] = R[j++];
    }
  }
  while(i < n1) {
    arr[k++] = L[i++];
  }
  while(j < n2) {
    arr[k++] = R[j++];
  }
}

int main() {
  int arr[100];
  int n;
  std::cin >> n;
  for (int i = 0; i < n; i++) {
    std::cin >> arr[i];
  }

  int mid = n / 2;
  mergeSort(arr, 0, n - 1);
  
  for (int i = 0; i < n; i++) {
    std::cout << arr[i] << " ";
  }
   
  return 0;
}

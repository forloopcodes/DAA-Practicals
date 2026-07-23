#include<iostream>

int main() {
  int arr[100];
  int n;
  std::cin >> n;
  for (int i = 0; i < n; i++) {
    std::cin >> arr[i];
  }

  for (int i = 1; i < n; i++) {
    int value = arr[i];
    int j = i - 1;
    while (arr[j] > value && j >= 0) {
      arr[j + 1] = arr[j];
      j--;
    };
    arr[j + 1] = value;
  }

  for (int i = 0; i < n; i++) {
    std::cout << arr[i] << " ";
  }

  return 0;
}

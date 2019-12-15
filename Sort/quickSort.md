##### <span style="color:blue">**Mục tiêu:**</span> Sắp xếp một mảng chưa được sắp xếp

##### <span style="color:blue">**Giải thuật:**</span>

- Chọn phần tử cuối mảng làm $pivot$
- Duyệt một lượt trả về mảng có $pivot$ trên ở giữa, mảng bên trái gồm các giá trị nhỏ hơn $pivot$ và phần bên phải ngược lại
- Sắp xếp đệ quy mảng trái và mảng phải $pivot$

##### <span style="color:blue">**Code Python:**</span>

```python
def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi+1, high)
```

- **Độ phức tạp:**
  - Best: $\Omega (n)=nlog(n)$
  - Average: $\Theta (n) = nlog(n)$
  - Worst: $\Omicron(n) = n^2$

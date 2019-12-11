##### <span style="color:blue">**Mục tiêu:**</span> Sắp xếp một mảng chưa được sắp xếp

##### <span style="color:blue">**Giải thuật:**</span>

- <span style="color:red">*Bước 1:*</span> Duyệt từ phần tử thứ 2 đến cuối mảng (duyệt n-1 lần):
  - Sau mỗi lần duyệt, phần mảng từ $arr[0]$ đến $arr[i]$ được sắp xếp
  - Nếu phần tử được duyệt nhỏ hơn *phần tử trước* nó, dịch dần về phía trái cho đến khi nó **lớn hơn** *phần tử trước*

##### <span style="color:blue">**Code Python:**</span>

```python
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

- **Độ phức tạp:**
  - Best: $\Omega (n)=n$
  - Average: $\Theta (n) = n^2$
  - Worst: $\Omicron(n) = n^2$

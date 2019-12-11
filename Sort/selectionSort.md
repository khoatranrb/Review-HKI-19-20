##### <span style="color:blue">**Mục tiêu:**</span> Sắp xếp một mảng chưa được sắp xếp

##### <span style="color:blue">**Giải thuật:**</span>

- <span style="color:red">*Bước 1:*</span> Duyệt phần tử từ đầu đến cuối mảng:
  - Sau mỗi lần duyệt, phần mảng từ $arr[0]$ đến $arr[i]$ được sắp xếp
  - So sánh phần tử đó với các phần tử bên phải nó
  - Đổi chỗ phần tử đó với phần tử nhỏ hơn nó gần cuối dãy nhất

##### <span style="color:blue">**Code Python:**</span>

```python
def selectionSort(arr):
    l = len(arr)
    for i in range(l):
        p = i
        for j in range(i,l):
            if arr[j]<arr[i]:
                p = j
        arr[i], arr[p] = arr[p], arr[i]
```

- **Độ phức tạp:**
  - Best: $\Omega (n)=n^2$
  - Average: $\Theta (n) = n^2$
  - Worst: $\Omicron(n) = n^2$


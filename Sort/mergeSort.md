##### <span style="color:blue">**Mục tiêu:**</span> Sắp xếp một mảng chưa được sắp xếp

##### <span style="color:blue">**Giải thuật:**</span>

- <span style="color:red">*Bước 1:*</span> Chia đôi mảng một cách đệ quy
- *Bước 2:* Ghép các mảng conarr lại với nhau để được một mảng con sắp xếp

##### <span style="color:blue">**Code Python:**</span>

```python
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

- **Độ phức tạp:**
  - Best: $\Omega (n)=nlog(n)$
  - Average: $\Theta (n) = nlog(n)$
  - Worst: $\Omicron(n) = nlog(n)$

##### <span style="color:blue">**Mục tiêu:**</span> Sắp xếp một mảng chưa được sắp xếp

##### <span style="color:blue">**Giải thuật:**</span>

- <span style="color:red">*Bước 1:*</span> Duyệt từ đầu đến cuối mảng:
  - Nếu *phần tử sau* lớn hơn *phần tử trước*, đổi chỗ chúng
- <span style="color:red">*Bước 2:*</span> Nếu duyệt toàn bộ mảng mà không phải đổi chỗ bất kì phần tử nào, kết thúc thuật toán. Nếu không, lặp lại *bước 1*.

##### <span style="color:blue">**Code Python:**</span>

```python
def bubbleSort(arr):
    n = len(arr) #0
    for i in range(n): #1
        swap = False #2
        for j in range(n-1): #3
            if arr[j]>arr[j+1]: #4
                arr[j], arr[j+1] = arr[j+1], arr[j] #5
                swap = True #6
        if swap == False: #7
            return None #8
```



##### Phân tích độ phức tạp:

- Hàm trên có 2 phần con:
  - #0 : $O(n)= n$
  - #1 : $O(n)=n$
    - #2 : $O(n)=1$
    - #3 : $O(n)=n-1$
      - #4 : $O(n)=1$
        - #5 : $O(n)=2$
        - #6 : $O(n)=1$
    - #7 : $O(n)=1$
      - #8 : $O(n)= 1$
- Độ phức tạp:
  - Best: $\Omega (n)=n$
  - Average: $\Theta (n) = n^2$
  - Worst: $$\Omicron(n) = n^2$$

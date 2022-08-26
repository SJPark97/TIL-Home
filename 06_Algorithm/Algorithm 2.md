### 배열

1. 배열 : 2차원 배열
2. 부분집합 생성
3. 바이너리 서치 (Binary Search)
4. 셀렉션 알고리즘 (Selection Algorithm)
5. 선택 정렬 (Selection Sort)

---

### 2차원 배열

- 행 우선 순회

```python
# i 행의 좌표
# j 행의 좌표
for i in range(n):
    for j in range(m):
        Array[i][j] #필요한 연산 수행
```

- 열 우선 순회

```python
# i 행의 좌표
# j 행의 좌표

for j in range(m):
    for i in range(n):
        Array[i][j] #필요한 연산 수행
```

- 지그재그 순회

```python
# i 행의 좌표
# j 열의 좌표

for i in range(n):
    for j in range(m):
        Array[i][j + (m-1-2*j) * (i%2)]
        # 필요한 연산 수행
```

- 전치 행렬

```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3*3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

- 델타를 이용한 배열 접근

```python
arr[0...N-1][0...N-1]
di[] = [0, 0, -1, 1]
dj[] = [-1, 1, 0, 0]
for i : 1 -> N-1:
    for j : 1 -> N-1:
        for k in range(4):
            ni <- i + di[k]
            nj <- j + dj[k]
            if 0<=ni<N and 0<=nj<N:    #유효한 인덱스면
                test(arr[ni][nj])            
```

- 




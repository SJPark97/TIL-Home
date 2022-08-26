# 교수님 노트

- 정렬 : 따로 뭔가 특별한 것이 아니라 (for, if)문의 배치 차이에 따라 달라진다.
  
  - 버블 정렬
    
    - ```python
      sample = [55, 7, 78, 12, 42]
      
      def bubble_sort(a): #정렬
          for i in range(len(a) - 1, 0, -1):
              for j in range(0, i):
                  if a[j] > a[j + 1]:
                      a[j], a[j+1] = a[j+1], a[j]
          return a
      
      print(bubble_sort(sample)
      ```
    
    - ```python
      sample = [("철수", 55), ("영희", 7), ("민수", 78), 
      ("기영", 12), ("유리", 32]
      
      def bubble_sort(a): #정렬
          for i in range(len(a) - 1, 0, -1):
              for j in range(0, i):
                  if a[j] > a[j + 1]:
                      a[j], a[j+1] = a[j+1], a[j]
          return a
      
      print(bubble_sort(sample)
      ```
  
  - 카운팅 정렬
    
    - ```python
      def counting_sort(original, k):
          counter = [0] * (k + 1)
      
          # 1. counter에 original 원소의 빈도수 담기
          for i in original:
              counter[i] += 1
      
          # 2. 누적(counter 업데이트)
          for i in range(1, len(counter)
              counter[i] += counter[i + 1]
      
          # 3. result 생성
          result = [-1] * len(original)
      
          # 4. result에 정렬하기(counter를 참조)
          for i in range(len(original)) - 1, -1, -1):
              counter[original[i]] -= 1
              result[counter[original[i]] = original[i]
      
          return result
      
      a= [0, 4, 1, 3, 1, 2, 4, 1]
      print(counting_sort(a, 5))  #[0, 1, 1, 1, 2, 3, 4, 4]   
      ```
    
    - stable정렬 : 입력한 수의 순서를 그대로 순서대로 출력
    
    - unstable정렬 : 입력한 수의 순서와 상관없이 출력

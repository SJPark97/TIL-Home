## Python 

##### 교수님 강의 노트

- map으로 입력 받는 과정 

- a, b = map(int, input().split())
  - [Quiz 1]  a, b, c = map(int,input())
  - input() = 123
  - print(a + b + c)
  - answer = 6
  
- a, b = map(int, input().split())
  - [Quiz 1]  a, b, c = map(int,input().split())
  - input() = 1 2 3
  - print(a + b + c)
  - answer = 6
  
- end, sep 옵션을 사용하여 출력 조작하기
  - print(a, end='@')
  - print(b)
  - --> a@b
  - print(a, b, sep='\n')
  - --> a
  - --> b

- 재귀란 함수가 자기 자신을 계속 호출하며 문제를 해결하는 것을 말한다.

  - 팩토리얼 문제를 통해 재귀 이해하기

    - 문제 4! = 4 x 3 x 2 x 1

    - 4! = 4 x 3! = 4 x 3 x 2! = 4 x 3 x 2 x 1! = 4 x 3 x 2 x 1 = 4 x 3 x 2 = 4 x 6 = 24

    - ```python
      def factorial(n):
          if n <= 1:
              return 1
          return n * factorial(n-1)
      
      
      print(factorial(4))
      >>> 24
      ```

  - 모든 재귀 함수는 반복문으로 표현이 가능하다.

  - 그럼 재귀 함수를 사용하는 이유는?

    - 반복문보다 대체적으로 더 직관적이고 코드가 간결하다.
    - 시간적/공간적 효율이 떨어진다.
    - 적절한 함수를 이용하는게 키 포인트

  - 재귀 함수 작성 가이드

    - [1] 종료 조건 (Base Case)
      - 가장 하위 문제에 도달 시 재귀를 종료할 수 있는 조건문(if)
    - [2] 점화식
      - 무조건 범위가 줄어들어야함.
    - 재귀 함수는 깊이가 1000번으로 파이썬에서 정해져 있다.

---

# 가상 환경

- 가상환경 설정 방법
  - python -m venv venv
  - source venv/Scripts/activate

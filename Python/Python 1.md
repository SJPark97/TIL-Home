## Python

###### Python 기초

- 프로그래밍 용어 정리
  - 프로그래밍 : 컴퓨터에게 일을 시키기 위해서 프로그램을 만드는 행위
  - 프로그램 : 컴퓨터가 해야 할 일들의 모음
  - 프로그래머 : 프로그램을 만드는 사람 (소프트웨어 개발자)
  - 소프트웨어 : 엄밀히 따지면 다르지만. 프로그램과 유사한 의미로 사용
  - 코딩 : 엄밀히 따지면 다르지만. 프로그래밍과 유사한 의미로 사용
- Python을 배워야 하는 이유
  - 알고리즘 코딩 테스트에서 Python이 2위를 기록
  - 코딩 테스트의 유형이 다양해지면서, 변칙적인 유형에 대응하기 쉬운 Python이 코딩 테스트에 유리
  - 입사를 위한 코딩 테스트는 Python 추천
- Jupyter Notebook
  - 문법 학습을 위한 최적의 도구로, 소스코드와 함께 실행 결과와 마크다운 저장 가능
  - 웹 플랫폼 킻 어플리케이션으로, 파이썬을 비롯한 다양한 프로그래밍 언어를 지원하며 셀 단위의 실행이 가능한 것이 특징
- 주석
  - 코드를 보다 이해하기 쉽게 만드는 것
  - 요즘은 코드를 다는 것 보다는 클린코드를 사용하는 것을 추천함.
- 연산자
  - ![image-20220718215849324](Python 1.assets/image-20220718215849324.png)
- 자료형(Datatype) 분류
  - 수치형 (Numeric Type)
    - int (정수, integer)
    - float (부동소수점, 실수, floating point number)
    - complex (복소수, complex number)
  - 문자열 (String Type)
  - 불린형 (Boolean Type)
  - None
- 진수 표현
  - 2진수 : 0b
  - 8진수 : 0o
  - 16진수 : 0x
- Escape sequence
  - ![image-20220718220200675](Python 1.assets/image-20220718220200675.png)
- 비교 연산자
  - ![image-20220718220234449-16581493553861](Python 1.assets/image-20220718220234449-16581493553861.png)
  - ![image-20220718220301262](Python 1.assets/image-20220718220301262.png)
- 리스트
  - 리스트는 대괄호([]) 혹은 list()를 통해 생성
    - 파이썬에서는 어떠한 자료형도 저장할 수 있으며, 리스트 안에 리스트도 넣을 수 있음
    - 생성된 이후 내용 변경이 가능 -> 가변 자료형
  - 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
    - 값에 대한 접근은 list[i]![image-20220718220512983](C:\Users\SJPark97\Desktop\싸피\TIL\README.assets\image-20220718220512983.png)
- 튜플
  - 항상 소괄호 형태로 사용
    - 소괄호 (()) 혹은 tuple()을 통해 생성
    - 값에 대한 접근은 tuple[i]
    - 리스트와의 차이점은 생성 후, 담고 있는 값 변경이 불가 -> 불변 자료형![image-20220718222156773](Python 1.assets/image-20220718222156773.png)
- Range의 정의
  - 숫자의 시퀀스를 나타내기 위해 사용
  - 주로 반복문과 함께 사용됨![image-20220718222404181](Python 1.assets/image-20220718222404181-16582431258511.png)
  - range(n)
    - 0부터 n-1까지의 숫자의 시퀀스
  - range(n, m)
    - n부터 m-1까지의 숫자의 시퀀스
  - range(n, m, s)
    - n부터 m-1까지 s만큼 증가시키는 숫자의 시퀀스
- 슬라이싱 연산자
  - 예제
  - ![image-20220718224043125](Python 1.assets/image-20220718224043125.png)
  - ![image-20220718224052926](Python 1.assets/image-20220718224052926.png)
  - ![image-20220718224101086](Python 1.assets/image-20220718224101086.png)
  - ![image-20220718224113771](Python 1.assets/image-20220718224113771.png)
- 셋(set)
  - Set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
    - 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있다면 하나만 저장
    - 순서가 없기 때문에 인덱스를 이용한 접근 불가능
  - 수학에서의 집합을 표현한 컨테이너
    - 집합 연산이 가능 (여집합을 표현하는 연산자는 별도로 존재 X)
    - 중복된 값이 존재하지 않음
  - 담고 있는 요소를 삽입 변경, 삭제 가능 -> 가변 자료형
  - 중괄호({}) 혹은 set()을 통해 생성
    - 빈 Set을 만들기 위해서는 set()을 반드시 활용해야 함
  - 순서가 없어 별도의 값에 접근할 수 없음
  - ![image-20220718224543410](Python 1.assets/image-20220718224543410.png)
- 딕셔너리
  - ![image-20220718224951436](Python 1.assets/image-20220718224951436.png)
  - 중괄호({}) 혹은 dict()을 통해 생성
  - key를 통해 value에 접근![image-20220718225027702](Python 1.assets/image-20220718225027702.png)
- 형 변환
  - 파이썬에서는 데이터 형태는 서로 변환할 수 있음
  - 암시적 형 변환
    - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
    - ![image-20220718225121557](Python 1.assets/image-20220718225121557.png)
  - 명시적 형 변환
    - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우
    - ![image-20220718225130723](Python 1.assets/image-20220718225130723.png)
    - ![image-20220718225234825](Python 1.assets/image-20220718225234825.png)
    - ![image-20220718225242579](Python 1.assets/image-20220718225242579.png)
    - ![image-20220718225251569](Python 1.assets/image-20220718225251569.png)

---

- 필기
  - 공학, 기술 -> 문제해결 -> 요구사항 ++ ->프로그램++ -> 개발자 (따라서 확장성이 중요함)
  - 확장성을 위해서는 style guide가 중요함
    - 따라서 black이란 프로그램을 많이 사용함 (저장시 자동으로 style guide가 적용됨)
  - 프로그래밍
    - 저장
      - 변수
      - 컨테이너
      - 자료구조
    - 처리
      - 연산자
      - if, while, for (조건, 반복문)
      - 알고리즘
  - 컨테이너
    - 시퀀스형 (순서가 있는 데이터)
      - 리스트 (가변형 mutable)
      - 튜플 (불변형 immutable)
      - 레인지 (불변형 immutable)
    - 비시퀀스형 (순서가 없는 데이터)
      - 세트 (가변형 mutable)
      - 딕셔너리 (가변형 mutable)

![image-20220719104024922](Python 1.assets/image-20220719104024922.png)
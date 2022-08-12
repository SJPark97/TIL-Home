### String 교수님 강의 (금요일)

- 컴퓨터의 문자 발전 과정
  
  - 지역마다 통일 - 미국에서 통일 (ASCII) - 전세게에서 통일 (유니코드)

- 유니코드 인코딩 (UTF : Unicode Tranasformation Format)
  
  - UTF-8 (in web) (파이썬) (많이 쓰임) (공간적으로 효율적) (8bit을 고정으로 차지)
    
    - MIN : 8bit, MAX: 32bit(1 Byte * 4*)
  
  - UTF-16 (in windows, java) (16bit을 고정으로 차지)
    
    - MIN : 16bit, MAX: 32bit(2 Byte * 2*)
  
  - UTF-32 (in unix) (32bit을 고정으로 차지)
    
    - MIN : 32bit, MAX: 32bit(4 Byte * 1*)

---

- 문자열
  
  - 컨테이너 -> 시퀀스 -> 변경 X 
  
  - indexing, slicing 가능 (slicing이 신의 축복)
  
  - 다양한 method

- 문자열을 뒤집는 방법
  
  - 반복문 (뒤에서부터 하나씩 반복해서 출력하기)
  
  - reverse (리스트로 변경 -> 리버스를 사용해서 거꾸로 -> 문자열 (''.join() method)
  
  - slicing (string[::-1])

---

### 패턴 매칭에 사용되는 알고리즘들

- 고지식한 패턴 검색 알고리즘

- 카프-라빈 알고리즘 (코테에 나오면 제보바람)

- KMP 알고리즘 (코테에 나오면 제보바람)

- 보이어-무어 알고리즘 (코테에 나오면 제보바람)



# 교수님 노트

### Flexbox

- Flex Container (부모) : 수직 수평축을 이용해서 깔끔하게 정렬할때 사용
  - main axis(메인축) : 수직일수도 수평일수도 있음 (items이 쌓이는 방향에 따라 다름) 
    - flex-direction : row일때는 가로 (좌->우) row-reverse (우->좌) (row가 기본)
    - flex-direction : column일때는 세로 (상->하) column-reverse (하->상)
    - flex-wrap : wrap (상->하) wrap-reverse (하->상)
      - nowrap : 크기가 넘어가도 줄여서 한 줄에 채움 (nowrap이 기본)
      - wrap : 크기가 넘어가면 다음 줄에 채움
    - flex-flow : flex-direction과 flex-wrap을 동시에 쓸 수 있음 
  - justify-content : 메인축을 따라다니는 메인축을 기준으로 여러개 정렬
    - flex-start : 앞으로 붙이기
    - flex-end : 뒤로 붙이기
    - center : 가운데로 붙이기
    - space-between : 좌우를 붙이고 빈공간 크기를 똑같이 배치
    - space-evenly : 좌우를 붙이지 않고 빈공간 박스 빈공간 박스 배치 (빈공간끼리 크기가 같음)
    - space-around : 빈공간-박스-빈공간 순으로 빈공간 크기가 같음
    - flex-graw : 1, 2 (1:1 비율로 공백을 먹는다, 1:2비율로 공백을 먹는다) (0이 기준)
  - cross axis(교차축) : 메인축이 에 수평인 축
  - align-items : 교차축을 따라다니는 교차축을 기준으로 하나 정렬 (사용 안함)
    - flex-start : 위로 붙이기
    - flex-end : 아래로 붙이기
    - center : 가운데로 붙이기
  - align-content : 교차축을 기준으로 여러개 정렬
  - 부모 -> 자식 : 바로 하나의 자식까지만 효과를 줌 (자손 x)
  - 부모 Container에 적용하는 것과 자식 item에 적용하는 것으로 나뉨
    - 부모 Cpntainer (display : flex;)
- align-self (자식) : 자식에 적용해서 각각의 item에 교차축을 기준으로 정렬
- order (자식) : order : 숫자 (숫자의 순서로 바꿈) (눈으로 보는것만 바뀜)



### Bootstrap Grid System

- framework(공구함) : 추상화 (만드어진걸 그대로 가져와서 사용)
- container -> row -> col(최대 12개)

#### Vscord 

###### 자율학습

- git - branch
  - 나무의 가지로 비유
  - 작업이 분기되는 현상 (branch를 만든다)
  - git branch (현재 branch 확인)
  - git branch 이름 (branch를 만든다)
  - git check out 이름 (해당하는 branch로 바꾼다)
    - ![image-20220717221534404](C:\Users\SJPark97\Desktop\싸피\TIL\README.assets\image-20220717221534404.png)
  - git log --branches -- decorate --graph --oneline
    - ![image-20220717222703815](C:\Users\SJPark97\Desktop\싸피\TIL\README.assets\image-20220717222703815.png)
  - git log master...exp (master에는 없고 exp에는 있는 것)
    - ![image-20220717223006555](C:\Users\SJPark97\Desktop\싸피\TIL\README.assets\image-20220717223006555.png)
  - git log exp..master (exp에는 없고 master에는 있는 것)
    - ![image-20220717223057780](C:\Users\SJPark97\Desktop\싸피\TIL\README.assets\image-20220717223057780.png)
  - git log -p exp..master (exp에는 없고 master에는 있는 것과 변경 내용)
    - ![image-20220717223313552](C:\Users\SJPark97\Desktop\싸피\TIL\README.assets\image-20220717223313552.png)
  - Git - branch에서 학습 종료
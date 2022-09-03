#### Vscord

- 누구(한번) -> 초기화(폴더마다) -> 3공간 -> 버전
  - 누구 : git config --global user.name SJPark97
  - 이메일 : git config --global user.email tjwlsdud33@naver.com
  - 초기화 : git init
  - 3 공간 
    - working directory : 작업 폴더
    - stage area : 스테이지 (git add)
    - commit : 커밋 (git commit -m "Why")
    - git status : Git 상태 확인 (제일 중요)
    - git log : 버전 확인
      - git log --oneline : 한 줄로 버전 확인 (간편하게)
    - git checkout (version ID) : 버전 불러오기
    - git reset --hard (version ID) : 버전 돌아가기
    - git commit -am "Why" (add와 commit를 동시에 하는 법)
- git clone : 다운로드 (Remote에 있는 내용을 그대로 다운로드)
  - 폴더 생성
  - git init
  - git remote add origin (URL)
  - 버전, 파일 생성
  - 위 4 단계가 자동으로 됨
- git pull : 업데이트 (git clone로 다운로드 후 변경사항 업데이트)
  - git pull origin master

- README.md : 내 github에 대한 설명 (자동으로 인식하여 출력함)
  - *무조건 맨 처음에 만들어야 함
- .gitignore
  - 남에게 보여주면 안되는 보안 파일 관리 (ignore.txt)
  - 굳이 올리지 않아도 되는 파일
  - *무조건 맨 처음에 만들어야 함 (한 번 버전관리가 된 파일은 무시가 불가능)
  - .gitignore 파일 만든 후 gitignore.io에 접속 후 프로그램 언어, 개발환경, 사용 프로그램, 입력 후 내용 복붙
- 협업하는 사람이 많아지면
  - branch, merge를 이용 (DAY 4에 구글링으로 확인 후 학습 예정)
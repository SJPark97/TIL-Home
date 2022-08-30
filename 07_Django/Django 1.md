### Django

##### 교수님노트

- Django Intro

- Django 구조 이해하기 (MTV Design Pattern)

- Django Quick start

- Django Template

- Sending and Retrieving form data

- Django URLs

---

1. Framework 이해하기
- 누군가 만들어 놓은 코드를 재사용 하는 것은 이미 익숙한 개발 문화

- 그렇다면 '웹 서비스'도 누군가 개발해 놓은 코드를 재사용하면 된다!

- 전 세계의 수많은 개발자들이 이미 수없이 많이 개발해 봤고, 그 과정에서 자주 사용되는 부분들을 재사용 할 수 있게 좋은 구조의 코드를 만들어 두었음

- 그러한 코드들을 모아 놓은 것, 즉 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것 = 프레임워크(Framework)

- Frame(뼈대) + Work(일하다)
  
  - 일정한 뼈대, 틀을 가지고 일하다
  
  - 제공받은 도구들과 뼈대, 규약을 가지고 무언가를 만드는 일
  
  - 특정 프로그램을 개발하기 위한 여러 도구들과 규약을 제공하는 것

- "소프트웨어 프레임워크"는 복잡한 문제를 해결하거나 서술하는 데 사용되는 기본 개념 구조

- 따라서, Framework를 잘 사용하기만 하면 웹 서비스 개발에 있어서 모든 것들을 하나부터 열까지 직접 개발할 필요 없이, 내가 만들고자 하는본질(로직)에 집중해 개발할 수 있음

- 소프트웨어의 생산성과  품질을 높임
2. Django를 배워야하는 이유
- Python으로 작성된 프레임워크
  
  - Python이라는 언어의 강력함과 거대한 커뮤니티

- 수많은 여러 유용한 기능들

- 검증된 웹 프레임워크
  
  - 화해, Toss, 두나무, 당근 마켓, 요기요 등
  
  - 유명한 많은 서비스들이 사용한다는 것 == 안정적으로 서비스 할 수 있다는 검증
3. 클라이언트-서버 구조
- 오늘날 우리가 사용하는 대부분의 웹 서비스는 클라이언트-서버 구조를 기반으로 동작

- 클라이언트와 서버 역시 하나의 컴퓨터이며 이들이 어떻게 상호작용하는지에 대한 간소화된 다이어그램은 다음과 같음
  ![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-08-30-09-25-03-image.png)

- 클라이언트
  
  - 웹 사용자의 인터넷에 연결된 장치 (예를 들어 wi-fi에 연결된 컴퓨터 또는 모바일)
  
  - Chrome 또는 Firefox와 같은 웹 브라우저
  
  - 서비스를 요청하는 주체

- 서버
  
  - 웹 페이지, 사이트 또는 앱을 저장하는 컴퓨터
  
  - 클라이언트가 웹 페이지에 접근하려고 할 때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라이저에 표시됨
  
  - 요청에 대해 서비스를 응답하는 주체

- 상호작용 예시
  
  - 예를 들어, 우리가 Google 홈페이지에 접속한다는 것은 무엇을 뜻하는지 알아보자
  1. 결론적으로 인터넷에 연결된 전세계 어딘가에 있는 구글 컴퓨터에게 'Google 홈페이지.html' 파일을 달라고 요청하는 것
  
  2. 그러면 구글 컴퓨터는 우리의 요청을 받고 'Google 홈페이지.html' 파일을 인터넷을 통해서 우리 컴퓨터에게 응답해줌
  
  3. 그렇게 전달받은 Google 홈페이지.html 파일을 웹 브라우저가 우리가 볼 수 있도록 해석해주는 것
1. 정적 웹 페이지
- Static Web page

- 있는 그대로를 제공하는 것(served as-is)을 의미

- 우리가 지금까지 작성한 웹 페이지이며 한 번 작성된 HTML 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것
  
  - == 서버에 미리 저장된 HTML 파일 그대로 전달된 웹 페이지
  
  - == 같은 상황에서 모든 사용자에게 동일한 정보를 표시
2. 동적 웹 페이지
- Dynamic Web page

- 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지

- 웹 페이지의 내용을 바꿔주는 주체 == 서버
  
  - 서버에서 동작하고 있는 프로그램이 웹 페이지를 변경해줌 이렇게 사용자의 요청을 받아서 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크가 바로 우리가 배울 Django

- 다양한 서버 사이드 프로그래밍언어 사용 가능. 파일을 처리하고 데이터베이스와의 상호작용이 이루어짐

- 이 중에서 Python을 이용해서 개발할 수 있는 프레임워크인 Django를 학습하는 것

#### 정리

- 우리가 사용하는 웹은 클라이언트-서버 구조로 이루어져 있음

- 앞으로 우리가 배우는 것도 이 클라이언트-서버 구조를 만드는 방법을 배우는 것

- 이 중에서 Django는 서버를 구현하는 웹 프레임워크

---

### MTV 패턴

##### MTV 패턴은 MVC 디자인 패턴을 기반으로 조금 변형된 패턴이다.

1. MVC 소프트웨어 디자인 패턴
- MVC는 Model - View - Controller의 준말 데이터 및 논리 제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴

- 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
  
  - Model : 데이터와 관련된 로직을 관리
  
  - View : 레이아웃과 화면을 처리
  
  - Controller : 명령을 model과 view 부분으로 연결
2. Django에서의 디자인 패턴
- Django는 MVC 패턴을 기반으로 한 MTV 패턴을 사용 두 패턴은 서로 크게 다른 점은 없으며 일부 역할에 대해 부르는 이름이 다름

MVC : Model, View, Controller

MTV : Model, Template, View

3. MTV 디자인 패턴
- Model
  
  - MVC 패턴에서 Model의 역할에 해당
  
  - 데이터와 관련된 로직을 관리
  
  - 응용프로그램의 데이터 구조를 정의하고 데이터베이스의 기록을 관리

- Template
  
  - 레이아웃과 화면을 처리
  
  - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
  
  - MVC 패턴에서 View의 역할에 해당

- View
  
  - Model & Template과 관련한 로직을 처리해서 응답을 반환
  
  - 클라이언트의 요청에 대해 처리를 분기하는 역할
  
  - 동작 예시
    
    - 데이터가 필요하다면 model에 접근해서 데이터를 가져오고 가져온 데이터를 template로 보내 화면을 구성하고 구성된 화면을 응답으로 만들어 클라이언트에게 반환
  
  - MVC 패턴에서 Controller의 역할에 해당

![](C:\Users\multicampus\AppData\Roaming\marktext\images\2022-08-30-09-47-44-image.png)

#### 정리

- Django는 MTV 디자인 패턴을 가지고 있음
  
  - Model : 데이터 관련
  
  - Template : 화면 관련
  
  - View : Model & Template 중간 처리 및 응답 반환

---

1. 가상환경 만들기
   
   $ python -m venv venv

2. 가상환경 활성화
   
   $ source venv/Scripts/activate
   
   $ source venv/bin/activate (MAC)

3. 가상환경 비활성화
   
   $deactivate

4. django 설치하기
   
   $ pip install django==3.2.13

5. 가상환경 패키지 목록 조회
   
   $pip list

6. requirements.txt 생성
   
   $ pip freeze > requirements.txt

7. requirements.txt 목록 설치
   
   $ pip install -r requirements.txt

8. django 프로젝트 생성
   
   $django-admin startproject firstpjt .

9. django 서버 실행
   
   $ python manage.py runserver

10. django 애플리케이션 생성
    
    $ python manage.py startapp articles

11. INSTALLED_APPS에 앱을 등록
    
    (반드시 앱을 먼저 생성 후 등록)

12. urls.py에 path 등록

13. views.py에 함수 생성

14. template 생성

---

### DTS Syntax

1. Variable

2. Filters

3. Tags

4. Comments

---

#### 템플릿 상속

상속에 관련된 태그 

1. {% extends '' %}

2. {% block content %}{% endblock content %}

HTTP 메서드

GET : 조회

POST : 생성

PUT : 변경

DELETE : 삭제

---

#### Django URLs

웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함

#### Variable routing

템플릿의 많은 부분이 중복되고, 일부분만 변경되는 상황에서 비슷한 URL과 템플릿을 계속해서 만들어야 할까?

path('show/<str:name >/', views.show),

path('show/<name>/', views.show),

path('show/<int:number >/', views.show),



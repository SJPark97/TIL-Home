# Javascript 2

- INDEX
  - DOM
  - Event
  - this


- DOM
  - 문서 객체 모델 (Document Object Model)
  - 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    - 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있게 도움
    - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음
  - HTML 문서를 구조화하여 있으며 각 요소는 객체로 취급
  - 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
  - DOM은 문서를 논리 트리로 표현
  - DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경할 수 있음
  - 웹 페이지는 일종의 문서
  - 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
  - DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
  - DOM은 웹 페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음
  - DOM을 사용하기 위해 특별히 해야 할 일은 없음
  - 모든 웹 브라우저는 스크립트 언어가 접근할 수 있는 웹페이지를 만들기 위해 DOM을 항상 사용함
  - DOM의 주요 객체들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음
  - DOM의 주요 객체
    - window object
      - DOM을 표현하는 창
      - 가장 최상위 객체
      - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄
      - 새 탭 열기 (window.open())
      - 인쇄 대화 상자 표시 (window.print())
      - 경고 대화 상자 표시 (window.alert())
    - document object
      - 브라우저가 불러온 웹 페이지
      - 페이지 컨텐츠의 진입점 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함하고 있음
      - 구문 분석, 해석
      - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
  - DOM 조작 순서
    - 선택 (select)
      - 한개 선택 : document.querySelector(selector) : CSS selector를 만족하는 첫 번째 element 객체를 반환 (없으면 null 반환)
      - 여러개 선택 : document.querySelectorAll(selector) : CSS selector를 만족하는 여러 element를 선택
        - nodelist를 반환
          - index로만 각 항목에 접근 가능
          - 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
          - querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음
    - 조작 (manipulation)
      - 생성, 추가, 삭제 등
      - 생성 : document.createElement(tagName) : 작성한 tagName의 HTML 요소를 생성하여 반환
      - 입력 : Node.innerText
        - Node 객체와 그 자손의 텍스트 컨텐츠를 표현
        - 사람이 읽을 수 있는 요소만 남김
        - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
      - 추가 : Node.appendChild()
        - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
        - 한번에 오직 하나의 Node만 추가할 수 있음
        - 추가된 Node 객체를 반환
        - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동
        - 삭제 : Node.removeChild()
          - DOM에서 자식 Node 제거
          - 제거된 Node를 반환
    - 속성 조회 및 설정 메서드
      - Element.getAttribute(attributeName)
        - 해당 요소의 지정된 값을 반환
        - 인자는 값을 얻고자 하는 속성의 이름
      - Element.setAttribute(name, value)
        - 지정된 요소의 값을 설정
        - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가


- Event
  - Event란 프로그래밍하고 있는 시스템에서 일어나는 사건 혹은 발생으로, 각 이벤트에 대해 조작할 수 있도록 특정 시점을 시스템이 알려주는 것
    - 예를 들어 사용자가 웹 페이지의 버튼을 클릭한다면 우리는 클릭이라는 사건에 대한 결과를 응답 받기를 원할 수 있음
  - 클릭 말고도 웹에서는 각양각색의 Event가 존재
    - 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등
  - Event object
    - 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
    - Event 발생
      - 마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고
      - 특정 메서드를 호출하여 프로그래밍적으로도 만들어 낼 수 있음
    - DOM 요소는 Event를 받고("수신")
    - 받은 Event를 "처리"할 수 있음
      - Event 처리는 주로 addEventListener()라는 Event 처리기를 다양한 html 요소에 "부착"해서 처리함
      - EventTarget.addEventListener(type, listener)
        - listener : 콜백함수
        - 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
        - Event를 지원하는 모든 객체를 대상으로 지정 가능
        - type
          - 반응 할 Event 유형을 나타내는 대소문자 구분 문자열
          - 대표 이벤트
            - input, click, submit
    - Event 취소 : event.preventDefault() 
      - 현재 Event의 기본 동작을 중단
      - HTML 요소의 기본 동작을 작동하지 않게 막음
      - HTML 요소의 기본 동작 예시
        - a 태그 : 클릭 시 특정 주소로 이동
        - form 태그 : form 데이터 전송
  - this
    - 어떠한 object를 가리키는 키워드
      - java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴
    - JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
    - JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
    - JavaScript는 해당 함수 호출 방식에 따라 this에 바인딩 되는 객체가 달라짐
    - 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 함수가 어떻게 호출 되었는지에 따라 동적으로 결정됨
    - this INDEX
      - 전역 문맥에서의 this
      - 함수 문맥에서의 this
        - 단순 호출
        - Metiod (객체의 메서드로서)
        - Nested
      - 함수 문맥에서의 this
        - 함수의 this 키워드는 다른 언어와 조금 다르게 동작
          - this의 값은 함수를 호출한 방법에 의해 결정됨
          - 함수 내부에서 this의 값은 함수를 호출한 방법에 의해 좌우됨
        - 단순 호출
          - 전역 객체를 가리킴
          - 전역은 브라우저에서는 window, Node.js는 global을 의미함
        - Method (Function in Object, 객체의 메서드로서)
          - 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩
        - Nested (Function 키워드)
          - forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
          - 단순 호출 방식으로 사용되었기 때문
          - 이를 해결하기 위해 등장한 함수 표현식이 바로 "화살표 함수"
          - 이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴
          - 화살표 함수에서 this는 자신을 감싼 정적 범위
          - 자동으로 한 단계 상위의 scope의 context를 바인딩
      - 화살표 함수
        - 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킴
        - Lexical scope
          - 함수를 어디서 호출하는지가 아니라 어디에 선언하였는지에 따라 결정
          - Static scope 라고도하며 대부분의 프로그래밍 언어에서 따르는 방식
        - 따라서 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장
      - 화살표 함수와 addEventListener
        - addEventListener에서 화살표 함수로 선언하면 this가 window를 가리킴
        - 고로 addEventListener에서는 function 키워드로 선언해야 함

1
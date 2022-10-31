# Vue 1

- Front-end Development
  - Front-end 개발이란? : 사용자에게 보여주는 화면 만들기
  - Web App을 만들 때 사용하는 도구 : SPA - Single Page Application
    - SSR
      - 기존의 요청 처리 방식
      - Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
      - 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행
    - SPA 
      - Web App과 함께 자주 등장할 용어
      - 이전까지는 사용자의 요청에 적절한 페이지 별 template을 반환
      - SPA는 서버에서 최초 1장의HTML만 전달받아 모든 요청에 대응하는 방식을 의미
        - 어떻게 한 페이지로 모든 요청에 대응 할 수 있을까?
        - CSR 방식으로 요청을 처리하기 때문
        - 최초 한 장의 HTML을 받아오는 것은 동일
          - 단, server로부터 최초로 받아오는 문서는 빈 html문서
        - 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
          1. 필요한 페이지를 서버에 AJAX로 요청
          2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
          3. JSON 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링)
        - CSR 방식의 장점
          - 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨
            - 클라이언트 - 서버간 통신 즉, 트래픽 감소
            - 트래픽이 감소한다 => 응답 속도가 빨라진다
          - 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
            - SNS에서 추천을 누를 때마다 첫 페이지로 돌아간다 = 끔찍한 App!
            - 요청이 자연스럽게 진행이 된다 = UX 향상
          - BE와 FE의 작업 영역을 명확히 분리 할 수 있음
            - 각자 맡은 역할을 명확히 분리한다 = 협업이 용이해짐
        - CSR 방식의 단점
          - 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
          - Naver, Netfixm Disney+ 등 모바일에 설치된 Web-App을 실행 하게 되면 잠깐의 로딩 시간이 필요
          - 검색 엔진 최적화가 어려움
            - 서버가 제공하는 것은 텅 빈 HTML
            - 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트가 진행
          - 대체적으로 THML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움
        - CSR vs SSR
          - CSR과 SSR은 흑과 백이 아님
            - 내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 함
          - SPA 서비스에서도 SSR을 지원하는 Framework이 발전하고 있음
            - Vue의 Nuxt.js
            - React의 Next.js
            - Angular Universal 등
  - Vue는 정말 쉬울까?
    - Vue 구조는 매우 직관적임
    - FE Framework를 빠르고 쉽게 학습하고 활용 가능
    - 추후 필요하다면, 다른 FEFramework 학습 시 빠르게 적응 가능
  - Vue CDN
    - Vue로 작업을 시작하기 위하여 CDN을 가져와야 함
    - Django == Python Web Framework
      - pip install
    - Vue === JS Front-end Framework
      - Bootstrap에서 사용하였던 CDN 방식 제공
      - npm 활용은 추후에 진행 예정
  - Vue2 vs Vue3
    - 여전히 Vue2가 많이 사용됨
    - 사용된 기간이 긴 만큼 상대적으로 많은 문서의 양, 참고자료, 질문/답변
    - 안정적인 측면에서는 아직 Vue2가 우세한 편


### Vue

- M/V/VM Pattern
  - 소프트웨어 아키텍처 패턴의 일종
  - 마크업 언어로 구현하는 그래픽 사용자 인터페이스(view)의 개발을 Back-end(model)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
- Model : 실제 데이터 = JSON
- View : 우리 눈에 보이는 부분 = DOM
- View Model
  - View를 위한 Model
  - View와 연결(binding)되어 Action을 주고 받음
  - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경
  - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고, 바인딩된 다른 View도 변경됨
- el
  - Vue instance와 DOM을 mount(연결)하는 옵션
    - View와 Model을 연결하는 역할
    - HTML id 혹은 class와 마운트 가능
  - Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음
    - Vue 속성 및 메서드 사용 불가
- Template Syntax
  - 렌더링 된 DOM을 기본 Vue instance의 data에 선언적으로 바인딩 할 수 있는 HTML 기반 template syntax를 사용
    - 렌더링 된 DOM - 브라우저에 의해 보기 좋게 그려질 HTML 코드
    - HTML 기반 template syntax - HTML 코드에 직접 작성할 수 있는 문법 제공
    - 선언적으로 바인딩 - Vue instance와 DOM을 연결
- Directives
  - v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음
    - 값에는 JS 표현식을 작성 할 수 있음
  - directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
- v-show vs v-if
  - v-show
    - 표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 v-if보다 높을 수 있음
    - display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
  - v-if
    - 표현식 결과가 false인 경우 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show 보다 낮을 수 있음
    - 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가
- computed
  - Vue instance가 가진 options 중 하나
  - computed 객체에 정의한 함수를  페이지가 최초로 렌더링 될 때 호출하여 계산
    - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반환
  - method vs computed
    - method
      - 호출 될 때마다 함수를 실행
      - 같은 결과여도 매번 새롭게 계산
    - computed
      - 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
      - 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환
# API vs Json

- API :**A**pplication **P**rograming **I**nterface

- 브라우저 : --요청(reques, API) --> 서버
  
  - Client <-- 응답(respond, Json)-- Server

- source : mnd, agify.io

- requests module
  
  - GET : 조회하는 것
  - POST : 수정할때(만능) *ex) 댓글 생성, 수정*
  - PUT : 변경하는 것
  - DELETE : 지우는 것

### URL

프로토콜 : https: *(기본 프로토콜)*

- Base url : www.blabla.com/api/v1 *기본 웹사이트*
- path : movie/now_playing *그 중에서도 현재 재생되고 있는 영화*
- params : ?'key'='value'&'key'='value'&'key'='value' *처음 'key'는 정보에 접근이 허가 되는 'value'*

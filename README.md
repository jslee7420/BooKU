# BooKU
BooKU는 선후배간에 전공책을 쉽게 교환하고 거래할 수 있도록 도와주는 플랫폼입니다. 기존의 중고거래 사이트와의 차별성을 위해 유저들이 학과에 소속된사람들끼리 교환/거래 할 수 있도록 만들었습니다.동아리에서 팀프로젝트로 진행하였으며 기획부터 개발까지 모두 참여하였습니다.

사용자 계정 모델을 생성하였고 CRUD를 구현했으며, 회원가입 시 이메일 인증 기능을 Gmail 계정과 연동하여 SMTP를 활용하여 구현했습니다. 
사용자 계정으로부터 토큰을 생성하여 암호화하여 이메일로 URL을 생성하여 전송하였습니다. 모든 웹페이지를 반응형으로 제작하였습니다.
AWS EC2 서비스를 활용하여 Ubuntu 환경에서 웹서버는 Nginx, WSGI server는 Gunicorn을 사용해 서비스를 배포했습니다. 

Site Url: http://booku.club

## System Architecture
![그림1](https://user-images.githubusercontent.com/46511190/118897354-0902ea00-b945-11eb-8054-527d7c6ba729.jpg)

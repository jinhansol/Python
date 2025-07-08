<h3 id="thymeleaf-학습학기">Thymeleaf 학습학기</h3>
<h4 id="thymeleaf란">Thymeleaf란?</h4>
<p>타임리프는 JSP, Freemarker와 같은 템플릿 엔진의 일종으로 스프링에서 권장하고 있습니다.</p>
<h4 id="1-컨트롤러-생성">1. 컨트롤러 생성</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/05249a1c-09d4-4c01-83d0-61e728bb0bc5/image.png" /></p>
<p>클라이언트의 요청에 대해서 어떤 컨트롤러가 처리할지 매핑하는 어노테이션입니다. url에 &quot;/thymeleaf&quot; 경로로 오는 요청을 ThymeleafExController가 처리하도록 합니다.</p>
<h4 id="1-1-thymeleaf-layout-dialect-dependency-추가하기">1-1. Thymeleaf Layout Dialect dependency 추가하기</h4>
<p>Thymeleaf Layout Dialect를 이용하면 하나의 레이아웃을 여러 페이지에 똑같이 적용할 수 있습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/f030a02c-989d-46e5-b9d9-7bb3488e51e1/image.png" /></p>
<p>라이브러리 설치가 완료되었다면 templates 아래에 fragments 폴더 생성 후 footer / header 파일을 생성하고 layouts 폴더를 만들어서 layout1 파일을 생성합니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/3ac98772-e499-4255-b018-0cdd772f2cb8/image.png" /></p>
<h4 id="1-2-footer--header-layout1-예제-만들기">1-2. footer / header, layout1 예제 만들기</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/101bfa28-fd9a-4aa2-8fe6-1e679145efbe/image.png" /></p>
<p>footer 영역 생성</p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/d88815d5-bc18-4479-a155-11c793c09717/image.png" /></p>
<p>header 영역 생성</p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/1def8a33-e3f7-4735-8879-198745dc030c/image.png" /></p>
<p>layout1 영역 생성</p>
<h4 id="1-3-thymeleaf-파일-만들기">1-3. Thymeleaf 파일 만들기</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/2f637338-d50d-4996-9b39-e88d8bd18f77/image.png" /></p>
<p>layout1.html을 적용하기 위해서 네임스페이스를 추가합니다.</p>
<p>부트스트랩으로 header와 footer의 영역수정을 할겁니다.</p>
<p>서버 개발자로서 애플리케이션을 만들 때 힘든 점은 웹 페이지의 디자인 및 웹 퍼블리싱인데 오픈소스인 부트스트랩을 통하여 웹사이트 디자인을 쉽게 만들 수 있습니다.</p>
<p>bootstrap을 통해 사용할 코드 예제를 가져와서 만들고 있는 쇼핑몰에 맞게 수정을 해서 사용을 했을 때 나오는 최종 결과물 입니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/d3a2df63-c332-41da-8746-1729ed763289/image.png" /></p>
<h3 id="마치며">마치며</h3>
<p>이번에는 Thymeleaf와 bootstrap을 통하여 화면에 보여지는 페이지의 디자인을 구성해보았습니다.</p>
<p>다음 시간에는 코딩하는데 오랜시간을 잡아먹었던 Spring Security에 대해 포스팅해보겠습니다.</p>
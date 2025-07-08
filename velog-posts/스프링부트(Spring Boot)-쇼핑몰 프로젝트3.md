<h3 id="프로젝트-안내사항">프로젝트 안내사항</h3>
<p>•빌드 툴 - 메이븐
•언어 - JAVA 17
•스트링 부트 버전 : 3.3.1
•패키징 : Jar
•의존성 : Spring Web</p>
<p>이번 시간은 쿼리 메소드부터 시작합니다!</p>
<h3 id="1쿼리-메소드">1.쿼리 메소드</h3>
<p>쿼리 메소드를 이용할 때 가장 많이 사용하는 문법으로 find를 사용합니다. 엔티티의 이름은 생략이 가능하며, By 뒤에는 검색할 때 사용할 변수의 이름을 적어줍니다.</p>
<h4 id="find--엔티티-이름--by--변수이름">find + (엔티티 이름) + By + 변수이름</h4>
<p>기존에 작성했던 ItemRepository에 findByItemNm 메소드를 추가합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/11e07d26-cc87-45e8-bca6-3b8d2c2a3027/image.png" /></p>
<p>itemNm(상품명)으로 데이터를 조회하기 위해서 By 뒤에 필드명인 ItemNm을 메소드의 이름에 붙여줍니다.</p>
<p>기존에 작성했던 ItemRepositoryTest 클래스에 테스트 코드를 추가합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/6a6f3833-fe99-47cb-994f-bfac8bdb2bde/image.png" /></p>
<p>테스트 코드를 실행하면 콘솔창에 Select 쿼리문이 실행되는 것을 볼 수 있습니다. Where 조검누에는 item_nm이 조건으로 걸려있으며 binding parameter 로 &quot;테스트 상품1&quot;이 지정됐습니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/7791f4ac-efc4-48d5-868c-05cd80d96461/image.png" /></p>
<p>상품을 상품명과 상품 상세 설명을 OR 조건을 이용하여 조회하는 쿼리 메소드입니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/d49d59e4-44dc-45ae-b04c-dcb67aa597d5/image.png" /></p>
<p>기존에 만들었던 테스트 상품을 만드는 메소드를 실행하여 조회할 대상을 만들어주겠습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/46f412a9-229c-4b77-baa6-74683ea6d623/image.png" /></p>
<p>파라미터로 넘어온 price 변수보다 값이 작은 상품 데이터를 조회하는 쿼리 메소드입니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/5e91ca34-9585-4a56-89aa-24542602b23c/image.png" /></p>
<p>현재 데이터베이스에 저장된 가격은 10001~10004입니다. 테스트 코드 실행 시 10개의 상품을 저장하는 로그가 콘솔에 나타나고 맨 마지막에 가격이 10005보다 작은 4개의 상품을 출력해주는 것을 확인할 수 있습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/9005c1de-7b59-4c5c-9c80-0bef481fe91f/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/2e0f74af-4a58-4230-bbae-7eef3ff9a722/image.png" /></p>
<p>출력된 결과를 OrderBy 키워드를 이용한다면 오름차순 또는 내림차순으로 조회할 수 있다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/ba5f72d5-1100-49c3-b501-2cf8b30be399/image.png" /></p>
<p>가격을 내림차순으로 조회가 가능한지 테스트하기 위한 코드를 작성합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/ba7d43fa-18ab-4455-af3f-39ada95a9c72/image.png" /></p>
<p>출력 결과를 살펴보면 가격이 높은 순으로 출력되는 것을 확인할 수 있습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/386a7459-6453-4fd1-a11a-23eea349bed1/image.png" /></p>
<h4 id="마치며">마치며</h4>
<p>이번시간은 쿼리 메소드와 관련한 내용을 알아보았습니다. 다음 시간에는 Spring DATA JPA 어노테이션에 대해서 알아보겠습니다.</p>
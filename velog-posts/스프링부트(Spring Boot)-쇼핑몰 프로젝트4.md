<h3 id="1-query-어노테이션">1. @Query 어노테이션</h3>
<p>Spring Data JPA에서 제공하는 @Query 어노테이션을 이용하면 SQL과 유사한 JPQL이라는 객체지향 쿼리 언어를 통해 복합한 쿼리도 처리가 가능하다.</p>
<h4 id="1-1-query를-이용한-검색-처리하기">1-1 @Query를 이용한 검색 처리하기</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/7611a65e-c2f2-4f15-8489-a1475dcd268b/image.png" />
Query 어노테이션 안에 JPQL로 작성한 쿼리문을 넣어줍니다. from 뒤에는 엔티티 클래스로 작성한 Item을 지정해주고, Item으로부터 데이터를 select 하겠다는 것을 의미합니다.</p>
<h4 id="1-2-상품조회-테스트">1-2 상품조회 테스트</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/e5f71c7f-ab1b-4c73-b676-a90d6891dd18/image.png" /></p>
<p>테스트 코드 실행 결과 상품 상세 설명에 '테스트 상품 상세 설명'을 포함하고 있는 상품 데이터 10개가 가격이 높은 순부터 조회되는 것을 확인할 수 있습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/b481b104-a662-4026-bfa8-e4b35744e9c9/image.png" /></p>
<h3 id="2querydsl">2.Querydsl</h3>
<p>Queyrydsl은 JPQL을 코드로 작성할 수 있도록 도와주는 빌더 API입니다. 소스 작성시 오타가 발생하면 개발자에게 오타가 있음을 바로 알려줍니다.</p>
<h2 id="장점">장점</h2>
<p>•고정된 SQL문이 아닌 조건에 맞게 동적으로 쿼리를 생성할 수 있다.
•비슷한 쿼리를 재사용할 수 있으며 제약 조건 조립 및 가독성을 향상시킬 수 있다.
•문자열이 아닌 자바 소스코드로 작성하기 때문에 컴파일 시점에 오류를 발견할 수 있다.
•IDE의 도움을 받아서 자동완성 기능을 이용할 수 있기에 생산성을 향상시킬 수 있다.</p>
<p>Querydsl을 사용하기 위해서는 몇가지 설정을 추가해야합니다. pom.xml 파일에 다음의 의존성을 추가합니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/48b46954-8d86-4544-a7a1-d762b3754d4f/image.png" />
&lt;교제에 있던 내용의 버전은 20년도 버전이라 신규 버전으로 변경되었습니다.&gt;</p>
<p>다음으로 pom.xml에 Qdomain이라는 자바 코드를 생성하는 플러그인을 추가합니다. 엔티티를 기반으로 접두사(prefix)로 'Q'가 붙는 클래스들을 자동으로 생성해주는 플러그인 입니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/8837ea5d-bd2a-4ab1-ae59-dd04cfe956b4/image.png" />
&lt;버전 호완성 문제로 최신버전으로 검색하여 수정하였습니다.&gt;</p>
<p>Maven -&gt; Reload All Maven Projects 버튼 클릭 -&gt; complile(클릭)
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/0db8a2ee-b7bf-40cc-a895-55732430d67a/image.png" />
target/generated-sources 폴더에 QItem 클래스가 생성됨을 확인</p>
<h4 id="2-1-jpaqueryfactory를-이용한-상품-조회-예제">2-1 JPAQueryFactory를 이용한 상품 조회 예제</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/ecbec962-929f-408d-a875-80b4db5eff37/image.png" />
•영속성 컨텍스트를 사용하기 위해 @PersistenceContext 어노테이션을 이용해 EntityManager 빈을 주입
•JPAQueryFactory를 이용하여 쿼리를 동적으로 생성
•Querydsl을 통해 쿼리를 생성하기 우해 플러그인을 통해 자동으로 생성된 QItem 객체 이용</p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/7a369d6c-54e2-4eec-8edb-1fecc72c0f5a/image.png" />
쿼리를 실행해보면 JPAQuery에 추가한 판매상태 코드와 상품 상세 설명이 where 조건에 추가돼 있고, 상품의 가경이 내림차순으로 정렬돼 데이터를 조회합니다.</p>
<p>다음은 QuerydslPredicateExecutor 를 이용한 상품 조회 예제입니다. Predicate란 '이 조건이 맞다'고 판단하는 근거를 함수로 제공하는 것입니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/c7b907ab-20c2-4e7d-a2f3-a0fd493ecf1f/image.png" />
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/9866b1f0-4aa4-4a87-bddc-a9b2c6aeff86/image.png" /></p>
<p>실행결과
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/ab72a7cd-c2b0-464a-b4bc-13443a4b579c/image.png" /></p>
<h3 id="마무리">마무리</h3>
<p>다음은 Thymeleaf에 대해서 공부하고 직접 실행해보는 시간을 가져보도록 하겠습니당.</p>
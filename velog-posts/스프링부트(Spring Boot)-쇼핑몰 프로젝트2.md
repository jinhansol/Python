<p>이번 시간부터는 본격적으로 프로젝트를 진행해보도록 하겠습니다.</p>
<h4 id="스프링부트-쇼핑몰-프로젝트-with-jpa">스프링부트 쇼핑몰 프로젝트 with JPA</h4>
<p>라는 교제를 통하여 하나씩 공부하면서 진행하는 것이라 진행속도가 느릴 수도 있지만 천천히 해보도록 하겠습니당.</p>
<h3 id="프로젝트-안내사항">프로젝트 안내사항</h3>
<p>•빌드 툴 - 메이븐
•언어 - JAVA 17
•스트링 부트 버전 : 3.3.1
•패키징 : Jar
•의존성 : Spring Web</p>
<h3 id="1-applicationproperties-설정하기">1. application.properties 설정하기</h3>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/760d8013-8172-477d-9ae1-640c53081dca/image.png" /></p>
<h4 id="maria-db-연결-설정하기">Maria DB 연결 설정하기</h4>
<ol>
<li>데이터 베이스에 연결하기 위해 Maria jdbc driver를 설정합니다.</li>
<li>연결할 데이터베이스의 URL, 포트 번호, 데이터베이스의 이름을 입력합니다.
3,4. 앞쪽에서 데이터베이스를 설치할 때 입력했던 아이디와 비밀번호를 입력합니다.</li>
</ol>
<h3 id="2상품-엔티티-설계하기">2.상품 엔티티 설계하기</h3>
<p>쇼핑몰 페이지에 나오는 상품들을 설정하기 위해 상품 등록 및 조회, 수정 삭제가 가능하도록 엔티티 설계를 진행하겠습니다.</p>
<p>엔티티란 데이터베이스의 테이블에 대응하는 클래스라고 생각하면 됩니다. 상품 엔티티를 만들기 위해서는 상품 테이블에 어떤 데이터가 저장되어야 할지 설계해야 하며, LOMBOK의 어노테이션을 이용한다면 getter, setter, toString 등 을 자동으로 만들어 주기 때문에 코드를 깔끔하게 짤 수 있습니다.</p>
<h4 id="2-1-프로젝트-패키지-추가">2-1. 프로젝트 패키지 추가</h4>
<p>com.shop 패키지에서 마우스 오른쪽 버튼을 눌러 나오는 메뉴 [New]-[Package]를 선택합니다. 패키지 이름을 입력하는 창에서 com.shop. 뒤에 entity를 입력하여 entity 패키지를 생성합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/c4d1a38a-7854-488b-b6ab-1f8264175bea/image.png" /></p>
<p>생성한 entity 패키지에 동일하게 마우스 오른쪽 버튼을 누르고 [New]-[Java Class]를 선택합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/f62eb826-4388-4d0d-9713-d97653f0897c/image.png" /></p>
<p>상품 클래스 이름은 Item으로 만들겠습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/cac8fe9e-3b0b-4635-8c9c-34086d93aaa3/image.png" /></p>
<p>com.shop 패키지 아래에 constant 패키지를 하나 생성하고 enum 타입을 모아둡니다.
상품이 현재 판매중인지 품절 상태인지를 나타내는 enum 타입의 클래스입니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/85ccc128-2777-435b-8804-ff813680aa42/image.png" /></p>
<p>이제 Item 클래스가 가지고 있어야할 멤버 변수들을 선언해 주겠습니다.
동시에 상품 클래스 엔티티 매핑도 함께 진행합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/b8292bcf-566d-4129-9722-dda188c714ed/image.png" />
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/dadb96d2-f808-45f4-913c-6d104c90a567/image.png" /></p>
<p>상품 정보로 상품코드, 가격, 상품명, 상품 상세 설명, 판매 상태를 만들어줍니다.
판매 상태의 경우 재고가 없거나, 상품을 미리 등록해 놓고 나중에 '판매 중' 상태로 바꾸거나 재고가 없을 때는 프론트에 노출시키지 않기 위해서 판매 상태로 코드로 갖고 있습니다.</p>
<p>Item 클래스를 엔티티로 매핑하기 위해서 관련된 어노테이션들을 알아보겠습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/3d33ad88-c0cc-4e15-ba2d-4ac16a326918/image.png" /></p>
<p>Item 엔티티 클래스 작성 완료 후 애플리케이션을 실행하면 item 테이블이 생성되는 쿼리문을 하단 콘솔창에서 볼 수 있습니다.</p>
<h3 id="3repository-설계하기">3.Repository 설계하기</h3>
<p>Spring Data JPA에서는 엔티티 매니저를 직접 이용해 코드를 작성하지 않아도 됩니다. 그 대신에 Data Access Object의 역할을 하는 Repository 인터페이스를 설계한 후 사용하는 것만으로 충분합니다.</p>
<p>com.shop 패키지 아래에 repository 패키지를 만든 후 ItemRepository 인터페이스를 만듭니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/ca149a38-c75e-4bc2-8044-6b06ce81fe91/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/d5eecd37-ba16-42a5-97cc-cd05e504a66b/image.png" /></p>
<p>JpaRepository를 상속받는 ItemRepository를 작성했습니다. JpaRepository는 2개의 제네릭 타입을 사용하는데 첫 번째에는 엔티티 타입 클래스를 넣어주고, 두 번째는 기본 키 타입을 넣어줍니다.</p>
<h4 id="jparepository에서-지원하는-메소드-예시">JpaRepository에서 지원하는 메소드 예시</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/c6db2366-d19b-41a5-b880-11fe9f82d128/image.png" /></p>
<p>테스트 환경의 경우 h2 데이터베이스를 사용하도록  resources 아래에 applicaiton-test.properties 파일을 만들겠습니다. 테스트 환경을 위한 별도의 Properties를 만드는 것입니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/b59be24a-868f-421a-833d-122ba278aa49/image.png" /></p>
<p>테스트 코드를 작성하기 위해 ItemRepository 인터페이스에서 마우스 오른쪽 버튼을 눌러[Go TO] - [Test] 버튼을 클릭합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/bec73185-b26f-4f2e-8dab-45419aa7a2a1/image.png" /></p>
<p>[Creaete New Test]를 클릭합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/0acf46b3-5906-4c38-b5ba-cb7607eb5bec/image.png" /></p>
<p>테스트를 위한 Junit 버전을 선택할 수 있으며, 테스트할 패키지와 테스트 클래스 이름을 자동으로 설정해줍니다. junit5 버전을 이용하여 테스트를 하겠습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/46b2d8ea-e0c7-40fb-9a26-b28d9d198321/image.png" /></p>
<p> 버튼을 누르면 test 폴더에 ItemRepositoryTest.java 파일이 생성된 것을 볼 수 있습니다. ItemRepository를 테스트하는 코드는 이 클래스에 작성하겠습니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/0831144f-b2d5-4650-bb31-a6dfe28a813e/image.png" /></p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/9f9f0e36-f1e2-454a-a139-5e0d1ff87abb/image.png" /></p>
<p>테스트 코드를 작성이 완료되었으니 이제 테스트 코드를 실행해 보겠습니다. 테스트할 메소드에서 마우스 오른쪽 버튼을 클리한 후 Run 'createItemTest()'을 클릭합니다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/816cdf74-2c57-401b-a931-a621a8f387ef/image.png" /></p>
<p>테스트 코드가 실행되면 콘솔창에 실행되는 쿼리문을 볼 수 있습니다. hibernate_sequence라는 키 생성 전용 테이블로부터 다음에 저장할 상품의 기본키(PK)를 가져와서 item 테이블의 기본키 값으로 넣어줍니다.</p>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/f3db12cc-47eb-494e-9e9f-19fab3de69bd/image.png" /></p>
<h4 id="마치며">마치며</h4>
<p>오늘은 Repository를 설계하고 1차 테스트하는 것까지 작성해보았습니다.
다음 시간에는 쿼리 메소드를 설정하는 것부터 시작해보도록 하겠습니다.</p>
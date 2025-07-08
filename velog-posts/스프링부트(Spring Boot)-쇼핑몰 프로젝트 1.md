<p>지난 시간에 이어서 이번엔 프로젝트를 Improt하고 db까지 연결을 해보도록 하겠습니다.</p>
<h3 id="1-프로젝트-improt-하기">1. 프로젝트 Improt 하기</h3>
<p>생성한 프로젝트를 인텔리제이에 Improt를 해보려고 합니다.</p>
<h4 id="1-1cdevelopworkspace에-shopzip의-압축을-풀고-경로를-맞춰주도록-합시다">1-1.C:\develop\workspace에 Shop.zip의 압축을 풀고, 경로를 맞춰주도록 합시다.</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/3479a5b4-8a1a-419c-bd9e-135595d6ec6f/image.png" /></p>
<h4 id="1-2-인텔리제이-projects-탭의-open을-클릭합니다">1-2. 인텔리제이 Projects 탭의 Open을 클릭합니다.</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/478afc40-0748-4074-83c7-02ab567a55e3/image.png" /></p>
<h4 id="1-3-프로젝트의-경로를-선택하고-ok를-클릭합니다">1-3. 프로젝트의 경로를 선택하고 OK를 클릭합니다.</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/9aa5599f-1283-47f8-9717-143ce85104f0/image.png" /></p>
<h4 id="1-4-컨펌창이-열리면-trust-project를-클릭합니다">1-4. 컨펌창이 열리면 Trust Project를 클릭합니다.</h4>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/b6b98712-796f-4dd7-b79b-040931ec25d8/image.png" /></p>
<h4 id="1-5-인텔리제이에서-구동에-필요한-일들을-자동으로-실행해줍니다-실행-완료까지-23분-정도의-시간이-소요될-예정입니다">1-5. 인텔리제이에서 구동에 필요한 일들을 자동으로 실행해줍니다. 실행 완료까지 2~3분 정도의 시간이 소요될 예정입니다.</h4>
<h3 id="2mariadb란">2.MariaDB란?</h3>
<p>마리아DB는 오픈 소스 관계형 데이터베이스 관리 시스템(RDBMS)으로, MySQL의 포크(Fork)이다. MySQL은 오픈 소스 RDBMS로서 가장 많이 사용되는 데이터베이스 시스템 중 하나였으며, 그 인기로 인해 여러 포크 버전들이 등장하게 되었다.</p>
<h4 id="2-1mariadb의-장점">2-1.MariaDB의 장점</h4>
<p> •<strong>2-1-1. 호환성</strong>
  마리아DB는 MySQL과 완벽하게 호환되며, 기존에 MySQL을 사용하던 프로젝트들이 쉽게 이전가능하다.
 •<strong>2-2-2. 성능</strong>
  몇몇 상황에서 MySQL보다 더 빠른 성능을 제공할 수 있다. 특히 일부 쿼리와 작업에 최적화가 되어있다.
 •<strong>2-2-3. 보안</strong>
  데이터 보안을 강화하기 위해 다양한 기능을 제공한다.
 •<strong>2-2-4. 오픈소스</strong>
  오픈 소스를 무료로 사용 가능하며, 비용 절감과 라이선스 문제에 대한 걱정이 없다.</p>
<h4 id="2-2mariadb의-단점">2-2.MariaDB의 단점</h4>
<p> •<strong>2-2-1. 특정기능의 부재</strong>
  MySQL과 비교했을 때, 마리아DB는 일부 특정 기능들이 부재할 수 있다. 이는 미세한 차이일 수 있으며, 대부분의 경우에는 문제가 없다. 하지만 특정한 기능이 필요할 때는 MySQL 의 기능 지원을 확인하는 것이 좋다.
 •<strong>2-2-2. 지원 서비스</strong>
  MySQL은 Oracle Corporation이 후훤하고 있으며, 상용 라이선스와 기술 지원을 제공한다. 하지만 마리아DB는 오픈 소스 프로젝트이기 때문에 공식적인 기술 지원이 상대적으로 제한적일 수 있다.</p>
<h4 id="2-3mariadb-다운로드하기">2-3.MariaDB 다운로드하기</h4>
<p>마리아DB 홈페이지에 들어가면 다음과 같은 화면을 볼수 있다.
지금은 10버전을 기준으로 10.6.18버전을 다운로드 해보려고 한다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/dd62307a-d58a-4569-9bba-fff38e78756f/image.png" /></p>
<h3 id="3db설치install하기">3.DB설치(Install)하기</h3>
<p>본격적으로 MariaDB 설치를 진행해보려고 한다.
3-1.Setup 파일을 실행하여 Next를 클릭 한다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/e5eedff8-bfca-48df-8892-371ea58e9c41/image.png" /></p>
<p>3-2.하단에 나와있는 체크박스를 선택한 후 Next를 클릭 한다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/436683b1-4162-46cd-891d-1b67c210918c/image.png" /></p>
<p>3-3.설치 경로는 Setup에 설정된 기본 경로로 진행한다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/060d00a1-6385-45da-9b3d-60552105dbdc/image.png" /></p>
<p>3-4.다음에는 데이터베이스의 마스터 계정인 root 계정의 비밀번호를 입력하고, Use UTF8 옵션을 체크한 후 Next를 클릭한다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/a51aff8e-b903-492d-b1a8-172db44795af/image.png" /></p>
<p>3-5.다음에도 기본 옵션 그대로 선택하고 Next 클릭하기!
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/247778fb-863d-48d1-885f-cf9c2dbf8aa7/image.png" /></p>
<p>3-6.마지막으로 Install을 클릭하면 설치가 완료된다.!
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/9b253a35-feb1-4268-8350-787ff15fcb6d/image.png" /></p>
<p>이제 시작 메뉴로 들어가 보면 HeidiSQL 과 MariaDB가 설치된 것을 확인해 볼 수 있다.
저는 HeidiSQL보다 다양한 DBMS를 지원해 주는 디비버(DBeaver)라는 툴을 사용하는 것이 더 편해서 디비버를 사용하고 있다.</p>
<h3 id="4데이터베이스-접속하기">4.데이터베이스 접속하기</h3>
<p>4-1.Database Navigator 영역에서 마우스를 우클릭한 후 Create - Connection을 클릭한다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/80232d55-b786-41f5-9512-444d8c7d73f8/image.png" /></p>
<p>4-2.DB선택 창에서, MariaDB를 선택하고 다음을 클릭한다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/09847eb1-fa79-4c1c-bc1b-c4a5b4b1e611/image.png" /></p>
<p>4-3.이제 DB 접속 정보를 입력하는 창이 나오고 모든 정보를 입력한 후 좌측 하단의 Test Connection을 통해 DB와 정상적으로 연결되었는지 확인이 가능하다.
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/0fbcdbba-9beb-4c9d-a32a-dbc6f0529171/image.png" /></p>
<h3 id="마무리">마무리</h3>
<p>이번시간에는 데이터베이스를 접속하는 방법까지 진행해 보았습니다.
다음 시간에는 생성한 프로젝트를 본격적으로 한걸음씩 진행해보는 시간을 가지도록 하겠습니다.</p>
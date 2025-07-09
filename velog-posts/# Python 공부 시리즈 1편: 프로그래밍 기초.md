<h2 id="1-프로그램의-정의">1. 프로그램의 정의</h2>
<p>&quot;프로그램&quot;이란 <strong>컴퓨터를 실행하기 위해 작성한 순차적인 명령어의 모음</strong>입니다.
사람의 수작업으로 처리하기 어려운 문제를 <strong>자동화 수행</strong>을 통해, 처리 방법과 순서를 명확하게 기술한 <strong>명령문의 집합체</strong>라고 할 수 있습니다.</p>
<hr />
<h2 id="2프로그래밍-과정">2.프로그래밍 과정</h2>
<p>프로그매이은 &quot;프로그래밍 언어를 사용하여 프로그램을 만드는 전체 과정&quot;을 의미합니다. 보통 다음 5단계를 거쳐 진행합니다.</p>
<ol>
<li><p><strong>요구사항 분석 (Planning)</strong></p>
<ul>
<li>해결하려는 문제 정의</li>
<li>사용자 요구사항, 기능 범위 정리</li>
</ul>
</li>
<li><p><strong>설계 (Design)</strong></p>
<ul>
<li><strong>흐름도(flowchart)</strong> 또는 <strong>의사코드(pseudocode)</strong> 로 전체 흐름 설계</li>
<li>주요 모듈, 데이터 구조, 입출력 인터페이스 결정</li>
</ul>
</li>
<li><p><strong>구현 (Coding)</strong></p>
<ul>
<li>설계 문서를 바탕으로 코드 작성</li>
<li>변수,함수,클래스 정의, 로직 구현</li>
</ul>
</li>
<li><p><strong>테스트 &amp; 디버깅 (Test &amp; Debugging)</strong></p>
<ul>
<li><strong>단위 테스트</strong> : 각 기능별 입력, 출력 검증</li>
<li><strong>통합 테스트</strong> : 모듈 간 연동 확인</li>
<li><strong>예외 처리</strong> : 경계값, 오류 상황 처리</li>
</ul>
</li>
<li><p><strong>배포 &amp; 유지보수 (Deployment &amp; Maintenance)</strong></p>
<ul>
<li>배포 환경(서버, 클라우드 등)에 프로그램 설치</li>
<li>사용자 피드백 반영, 버그 수정 및 기능 개선</li>
</ul>
</li>
</ol>
<hr />
<h2 id="3-프로그래밍-언어-분류">3. 프로그래밍 언어 분류</h2>
<p>프로그래밍 언어는 <strong>하드웨어와의 근접 정도</strong>에 따라 크게 두 그룹으로 나눌 수 있습니다.</p>
<hr />
<h3 id="31-저급언어-low-level-language">3.1 저급언어 (Low-level Language)</h3>
<ul>
<li><strong>기계어(Machine code)</strong><ul>
<li>바이너리(0과 1)의 명령어</li>
<li>CPU가 직접 해석,실행 가능</li>
</ul>
</li>
<li><strong>어셈블리어(Assembly)</strong><ul>
<li>기계어에 대응하는 간단한 텍스트 명령어</li>
<li>기계어 매핑이 1 : 1</li>
</ul>
</li>
<li><strong>특징</strong><ul>
<li>하드웨어 제어에 최적화</li>
<li>코드 가독성, 이식성은 매우 낮음</li>
</ul>
</li>
</ul>
<h3 id="32-고급언어-high-level-language">3.2 고급언어 (High-level Language)</h3>
<ul>
<li>대표 언어: Python, Java, C++, JavaScript 등</li>
<li>특징<ul>
<li>사람 친화적 문법 -&gt; 가독성, 생산성 우수</li>
<li>컴파일러/인터프리터가 기계어로 변환</li>
<li>플랫폼 독립성(한 번 작성하면 여러 OS에서 실행 가능)</li>
</ul>
</li>
</ul>
<pre><code>print(&quot;Hello, World!&quot;)</code></pre><h4 id="4-마무리">4. 마무리</h4>
<p>1편에서는 &quot;프로그램이란 무엇인가&quot;, 프로그래밍의 전체 흐름, 언어 분류에 대해서 다루었습니다.
다음 2편에서는 개발 환경 세팅에 대해서 알아봅니다.</p>
<h1 id="1-프로젝트-소개">1. 프로젝트 소개</h1>
<p>이 프로젝트는 <strong>실시간 뉴스 요약과 음성 AI(STT/TTS)</strong> 기능이 통합된 웹 서비스입니다.<br />사용자는 최신 뉴스를 핵심적으로 요약된 텍스트 및 음성으로 빠르게 접하고,<br />음성으로도 질문하여 뉴스 정보를 받을 수 있습니다.</p>
<blockquote>
<p>📢 <strong>네이버 뉴스 → AI 요약 → 음성 변환까지 단 5초!</strong></p>
</blockquote>
<hr />
<h2 id="전체-목차">전체 목차</h2>
<ol>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%86%8C%EA%B0%9C">프로젝트 소개</a><br />1.1 <a href="https://api.velog.io/rss/@hanyeon#%EA%B0%9C%EB%B0%9C-%EB%B0%B0%EA%B2%BD-%EB%B0%8F-%ED%95%84%EC%9A%94%EC%84%B1">개발 배경 및 필요성</a><br />1.2 <a href="https://api.velog.io/rss/@hanyeon#%ED%95%B5%EC%8B%AC-%EA%B8%B0%EB%8A%A5-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EC%9E%90-%EC%8B%9C%EB%82%98%EB%A6%AC%EC%98%A4">핵심 기능 및 사용자 시나리오</a><br />1.3 <a href="https://api.velog.io/rss/@hanyeon#%EA%B8%B0%EC%88%A0-%EC%8A%A4%ED%83%9D-%EB%B0%8F-%EC%97%AD%ED%95%A0">기술 스택 및 역할</a><br />1.4 <a href="https://api.velog.io/rss/@hanyeon#%EB%B3%B4%EC%95%88-%EB%B0%8F-%EC%9A%B4%EC%98%81-%EA%B3%A0%EB%A0%A4%EC%82%AC%ED%95%AD">보안 및 운영 고려사항</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%EA%B0%9C%EB%B0%9C-%ED%99%98%EA%B2%BD-%EC%A4%80%EB%B9%84">개발 환경 준비</a><br />2.1 <a href="https://api.velog.io/rss/@hanyeon#python-310-%EC%84%A4%EC%B9%98">Python 3.10 설치</a><br />2.2 <a href="https://api.velog.io/rss/@hanyeon#pycharm-%EC%84%A4%EC%B9%98-%EB%B0%8F-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%83%9D%EC%84%B1">PyCharm 설치 및 프로젝트 생성</a><br />2.3 <a href="https://api.velog.io/rss/@hanyeon#git%EA%B3%BC-pycharm-%EC%97%B0%EB%8F%99-%EB%B2%84%EC%A0%84%EA%B4%80%EB%A6%AC">Git과 PyCharm 연동 (버전관리)</a><br />2.4 <a href="https://api.velog.io/rss/@hanyeon#%ED%95%84%EC%88%98-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EC%84%A4%EC%B9%98-%EB%B0%8F-api-%ED%82%A4-%EA%B4%80%EB%A6%AC">필수 라이브러리 설치 및 API 키 관리</a><br />2.5 <a href="https://api.velog.io/rss/@hanyeon#%EC%9E%90%EC%A3%BC-%EB%B0%9C%EC%83%9D%ED%95%98%EB%8A%94-%EB%AC%B8%EC%A0%9C-%EB%B0%8F-%ED%95%B4%EA%B2%B0-%ED%8C%81">자주 발생하는 문제 및 해결 팁</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%A1%B0-%EC%9D%B4%ED%95%B4">프로젝트 구조 이해</a><br />3.1 <a href="https://api.velog.io/rss/@hanyeon#%ED%8F%B4%EB%8D%94-%EB%B0%8F-%ED%8C%8C%EC%9D%BC-%EA%B5%AC%EC%A1%B0">폴더 및 파일 구조</a><br />3.2 <a href="https://api.velog.io/rss/@hanyeon#%EB%B0%B1%EC%97%94%EB%93%9C%C2%B7%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EC%97%AD%ED%95%A0-%EB%B0%8F-api-%EC%97%B0%EB%8F%99">백엔드·프론트엔드 역할 및 API 연동</a><br />3.3 <a href="https://api.velog.io/rss/@hanyeon#%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%9D%90%EB%A6%84-%EA%B0%9C%EB%85%90%EB%8F%84">데이터 흐름 개념도</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%EC%BD%94%EB%93%9C-%EB%A6%AC%EB%B7%B0-1-%EB%84%A4%EC%9D%B4%EB%B2%84-%EB%89%B4%EC%8A%A4-api-%EC%97%B0%EB%8F%99-%EB%B0%8F-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%A7%91">코드 리뷰 1: 네이버 뉴스 API 연동 및 데이터 수집</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%EC%BD%94%EB%93%9C-%EB%A6%AC%EB%B7%B0-2-%ED%85%8D%EC%8A%A4%ED%8A%B8-%ED%81%AC%EB%A1%A4%EB%A7%81-%EB%B0%8F-%EC%A0%95%EC%A0%9C">코드 리뷰 2: 텍스트 크롤링 및 정제</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%EC%BD%94%EB%93%9C-%EB%A6%AC%EB%B7%B0-3-langchain%EA%B3%BC-openai-gpt%EB%A5%BC-%ED%99%9C%EC%9A%A9%ED%95%9C-%EB%89%B4%EC%8A%A4-%EC%9A%94%EC%95%BD">코드 리뷰 3: LangChain과 OpenAI GPT를 활용한 뉴스 요약</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%EC%BD%94%EB%93%9C-%EB%A6%AC%EB%B7%B0-4-sttts-%EA%B8%B0%EB%8A%A5-%EA%B5%AC%ED%98%84">코드 리뷰 4: STT/TTS 기능 구현</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%EC%BD%94%EB%93%9C-%EB%A6%AC%EB%B7%B0-5-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C-%EC%A3%BC%EC%9A%94-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8-%EB%B0%8F-api-%EC%97%B0%EB%8F%99">코드 리뷰 5: 프론트엔드 주요 컴포넌트 및 API 연동</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%EC%BD%94%EB%93%9C-%EB%A6%AC%EB%B7%B0-6-%EC%97%90%EB%9F%AC-%EC%B2%98%EB%A6%AC-%EB%B3%B4%EC%95%88-%EA%B0%95%ED%99%94-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94">코드 리뷰 6: 에러 처리, 보안 강화, 성능 최적화</a>  </p>
</li>
<li><p><a href="https://api.velog.io/rss/@hanyeon#%ED%99%95%EC%9E%A5-%EC%95%84%EC%9D%B4%EB%94%94%EC%96%B4-%EB%B0%8F-%EB%A7%88%EB%AC%B4%EB%A6%AC">확장 아이디어 및 마무리</a>  </p>
</li>
</ol>
<hr />
<h2 id="11-개발-배경-및-필요성">1.1 개발 배경 및 필요성</h2>
<ul>
<li>방대한 뉴스 속 중요 정보 선별의 어려움 해소  </li>
<li>바쁜 직장인, 시각장애인, 운전 중 사용자 대상 음성 뉴스 서비스 필요  </li>
<li>뉴스 소비 시간 단축 및 접근성 개선 목표</li>
</ul>
<hr />
<h2 id="12-핵심-기능-및-사용자-시나리오">1.2 핵심 기능 및 사용자 시나리오</h2>
<ul>
<li>네이버 뉴스 API + 웹 크롤링으로 최신 뉴스 확보 &amp; OpenAI GPT로 요약  </li>
<li>네이버 데이터랩 검색어 트렌드 API로 인기 키워드 실시간 제공  </li>
<li>OpenAI Whisper(STT), TTS로 음성 인터랙션 지원  </li>
<li>React.js UI로 텍스트·음성 결과 표시 및 음성 질문 기능 제공</li>
</ul>
<blockquote>
<p>예시: 출퇴근길 “오늘 경제 뉴스 알려줘” 음성 질문 → 요약 음성 답변</p>
</blockquote>
<hr />
<h2 id="13-기술-스택-및-역할">1.3 기술 스택 및 역할</h2>
<table>
<thead>
<tr>
<th>기술 분야</th>
<th>사용 기술 및 도구</th>
</tr>
</thead>
<tbody><tr>
<td>프로그래밍 언어</td>
<td>Python, JavaScript</td>
</tr>
<tr>
<td>프레임워크 및 라이브러리</td>
<td>FastAPI, React.js, LangChain, BeautifulSoup</td>
</tr>
<tr>
<td>AI 및 머신러닝 도구</td>
<td>OpenAI GPT, Whisper(STT), TTS API</td>
</tr>
<tr>
<td>API</td>
<td>네이버 뉴스 API, 네이버 데이터랩 검색어 트렌드 API</td>
</tr>
<tr>
<td>개발 도구</td>
<td>PyCharm, Git</td>
</tr>
<tr>
<td>기타</td>
<td>RESTful API 설계, 환경변수 관리 (.env), 버전관리 (Git)</td>
</tr>
</tbody></table>
<hr />
<h2 id="14-보안-및-운영-고려사항">1.4 보안 및 운영 고려사항</h2>
<ul>
<li>API 키 <code>.env</code> 또는 환경변수로 안전하게 관리 (코드 내 하드코딩 금지)  </li>
<li><code>.env</code> 파일은 <code>.gitignore</code>에 추가해 GitHub 공개 방지  </li>
<li>사용자 입력에 대한 백엔드 검증 필수 (보안 공격 예방)  </li>
<li>프로덕션 환경에서는 HTTPS 적용 권장  </li>
<li>필요 시 API 요청 제한 및 인증 체계 도입 고려</li>
</ul>
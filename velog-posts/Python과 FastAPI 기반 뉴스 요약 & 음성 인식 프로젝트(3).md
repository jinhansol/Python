<h1 id="3-프로젝트-구조-이해">3. 프로젝트 구조 이해</h1>
<p>이 장에서는 프로젝트의 전체 폴더와 주요 파일 구조를 살펴보고,<br />백엔드와 프론트엔드 각각의 역할과 책임, 그리고<br />핵심적으로 네이버 뉴스 API 및 네이버 데이터랩 트렌드 API가 어디에서 어떻게 활용되는지를 자세히 설명합니다.</p>
<p>초보자라도 쉽게 이해할 수 있도록 프로젝트 데이터 흐름과 개념도를 함께 제공합니다.</p>
<hr />
<h2 id="31-프로젝트-폴더-및-파일-구조">3.1 프로젝트 폴더 및 파일 구조</h2>
<h4 id="📁-프로젝트-구조">📁 프로젝트 구조</h4>
<table>
<thead>
<tr>
<th>구분</th>
<th>경로 및 파일명</th>
<th>역할 및 설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong>백엔드</strong></td>
<td><code>backend/</code></td>
<td>FastAPI 기반 서버 코드 전체 폴더</td>
</tr>
<tr>
<td></td>
<td>├─ <code>main.py</code></td>
<td>서버 메인 진입점, API 엔드포인트(뉴스 요약, 트렌드 등) 정의</td>
</tr>
<tr>
<td></td>
<td>├─ <code>voice_chat.py</code></td>
<td>음성 인식(STT) 및 음성 합성(TTS) 기능 구현 (OpenAI API 연동)</td>
</tr>
<tr>
<td></td>
<td>├─ <code>patched_cleanre.py</code></td>
<td>뉴스 본문에서 불필요한 문자 및 태그 제거 텍스트 정제 모듈</td>
</tr>
<tr>
<td></td>
<td>├─ <code>requirements.txt</code></td>
<td>백엔드 파이썬 패키지 의존성 목록</td>
</tr>
<tr>
<td></td>
<td>└─ 기타 파일</td>
<td>추가적인 백엔드 모듈 및 라이브러리</td>
</tr>
<tr>
<td><strong>프론트엔드</strong></td>
<td><code>frontend/</code></td>
<td>React.js 기반 웹 UI 전체 코드 폴더</td>
</tr>
<tr>
<td></td>
<td>├─ <code>src/</code></td>
<td>React 소스코드 폴더</td>
</tr>
<tr>
<td></td>
<td>│  ├─ <code>App.js</code></td>
<td>메인 컴포넌트, 화면 구성과 백엔드 API 호출 및 응답 처리</td>
</tr>
<tr>
<td></td>
<td>│  ├─ <code>components/</code></td>
<td>UI 재사용 컴포넌트 모음 폴더</td>
</tr>
<tr>
<td></td>
<td>│  │  ├─ <code>PopularKeywords.js</code></td>
<td>인기 키워드 리스트 UI 컴포넌트</td>
</tr>
<tr>
<td></td>
<td>│  │  ├─ <code>ChatBox.js</code></td>
<td>사용자 질의/응답 채팅 UI 컴포넌트</td>
</tr>
<tr>
<td></td>
<td>│  │  └─ 기타 컴포넌트</td>
<td>추가 UI 컴포넌트</td>
</tr>
<tr>
<td></td>
<td>├─ <code>public/</code></td>
<td>정적 파일(html, 이미지 등)</td>
</tr>
<tr>
<td></td>
<td>├─ <code>package.json</code></td>
<td>프론트엔드 패키지 및 빌드 설정</td>
</tr>
<tr>
<td></td>
<td>└─ 기타 설정 파일</td>
<td>예: <code>.env</code>, <code>babel.config.js</code> 등</td>
</tr>
<tr>
<td><strong>기타</strong></td>
<td><code>.env.example</code></td>
<td>환경변수 예시 (API 키 등 비밀정보는 실제로 넣지 않음)</td>
</tr>
<tr>
<td></td>
<td><code>README.md</code></td>
<td>프로젝트 설명 및 사용법 문서</td>
</tr>
</tbody></table>
<hr />
<h2 id="32-백엔드와-프론트엔드-역할-및-네이버-api-연동-위치">3.2 백엔드와 프론트엔드 역할 및 네이버 API 연동 위치</h2>
<h3 id="백엔드-fastapi">백엔드 (FastAPI)</h3>
<ul>
<li>네이버 뉴스 API 호출로 최신 뉴스 목록(JSON)을 수집하고,  </li>
<li>네이버 데이터랩 검색어 트렌드 API를 통해 인기 키워드 데이터를 받아옴  </li>
<li>웹 크롤링(BeautifulSoup)으로 각 뉴스 기사의 본문을 수집 및 정제  </li>
<li>LangChain과 OpenAI GPT API를 활용해 기사 본문을 핵심적으로 요약  </li>
<li>OpenAI Whisper(STT) 및 TTS API 호출로 음성 인식과 음성 합성 처리  </li>
<li>주요 API 엔드포인트 (<code>/news_trend/</code>, <code>/generate-tts/</code>, <code>/generate-stt/</code>)를 제공하여 프론트엔드와 소통</li>
</ul>
<h3 id="프론트엔드-reactjs">프론트엔드 (React.js)</h3>
<ul>
<li>인기 키워드 UI를 제공하고 사용자의 키워드 클릭 및 음성 입력을 통해 질의 수집  </li>
<li>백엔드 API를 호출하여 뉴스 요약 결과를 텍스트와 음성(mp3)으로 받아서 화면에 표시  </li>
<li>사용자에게 직관적인 뉴스 검색 및 음성 인터랙션 환경 제공</li>
</ul>
<hr />
<h2 id="33-프로젝트-데이터-흐름-개념도">3.3 프로젝트 데이터 흐름 개념도</h2>
<pre><code>[ User ] 
   │
   ▼
[ Frontend (React.js) ]  
   - 키워드 클릭, 음성 입력, UI 표시
   - 백엔드 API 호출 및 결과 표시
   │
   ▼
[ Backend (FastAPI) ]  
   - API 엔드포인트 제공
   - 네이버 뉴스 API 호출 (뉴스 목록 수집)
   - 네이버 데이터랩 트렌드 API 호출 (인기 키워드 수집)
   - 웹 크롤링 (BeautifulSoup, 기사 본문 수집)
   - LangChain + OpenAI GPT (뉴스 요약)
   - OpenAI Whisper / TTS (음성 인식 및 변환)
   │
   ▼
[ External APIs &amp; AI Models ]
   - 네이버 뉴스 API
   - 네이버 데이터랩 검색어 트렌드 API
   - OpenAI GPT, Whisper, TTS API</code></pre><hr />
<h2 id="34-추가-설명-및-실무-팁">3.4 추가 설명 및 실무 팁</h2>
<ul>
<li>주요 백엔드 파일(<code>main.py</code>, <code>voice_chat.py</code>)는 API 요청/응답과 음성 처리 핵심 로직이 집중되어 있어, 이후 코드 리뷰에서 중점적으로 다룹니다.  </li>
<li><code>patched_cleanre.py</code>는 뉴스 본문에서 광고, 특수문자 등 노이즈 제거에 중요한 역할을 하므로 텍스트 전처리 이해에 필수적입니다.  </li>
<li>프론트엔드 컴포넌트(<code>PopularKeywords.js</code>, <code>ChatBox.js</code>)는 사용자 경험(UX) 개선과 통신 로직을 동시에 처리하여, 인터렉티브한 서비스 구현의 근간입니다.  </li>
<li>API 키 등 민감 정보는 <code>.env</code> 파일과 환경변수를 통해 철저히 분리해 다루는 것을 권장합니다.  </li>
<li>데이터 흐름 개념도를 참고하면, 서비스 전반의 요청부터 처리, 결과 전달까지 어떤 단계로 진행되는지 한눈에 이해할 수 있어 유지보수 및 확장에 큰 도움이 됩니다.</li>
</ul>
<hr />
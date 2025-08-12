<h1 id="6장-코드-리뷰-3-ai-요약-모델-연동-및-결과-생산">6장 코드 리뷰 3: AI 요약 모델 연동 및 결과 생산</h1>
<p>5장에서 우리는 뉴스 기사 URL에서 본문을 크롤링하고 텍스트를 정제하는 과정을 구현했습니다.<br />이번 6장에서는 그 결과물을 <strong>LangChain</strong>과 <strong>OpenAI GPT</strong>를 활용해 목적 기반 뉴스 요약문으로 변환하고, API 응답으로 제공하는 방법을 다룹니다.</p>
<hr />
<h2 id="61-구현-목적">6.1 구현 목적</h2>
<ul>
<li>기사에서 <strong>핵심 정보만 간결하게 제공</strong> (3~5줄 요약)</li>
<li>분야별·키워드별 <strong>목적 기반 요약</strong> 가능</li>
<li>API로 제공하여 <strong>프론트엔드·TTS 기능과 연동</strong> 가능</li>
<li>사용자에게 <strong>읽기 쉽고 듣기 좋은 뉴스 콘텐츠</strong> 제공</li>
</ul>
<hr />
<h2 id="62-전체-데이터-처리-흐름">6.2 전체 데이터 처리 흐름</h2>
<pre><code>flowchart TD
    A[정제된 뉴스 본문 (5장 결과)] --&gt; B[LangChain PromptTemplate - 목적 포함]
    B --&gt; C[LLMChain(OpenAI GPT-4o)]
    C --&gt; D[뉴스별 요약문 생성]
    D --&gt; E[다수 요약문 → 전체 트렌드 분석]
    E --&gt; F[FastAPI API로 응답 반환]
    F --&gt; G[프론트엔드 화면 출력 및 TTS 음성 재생]</code></pre><hr />
<h2 id="63-사용-라이브러리-및-역할">6.3 사용 라이브러리 및 역할</h2>
<table>
<thead>
<tr>
<th>라이브러리/도구</th>
<th>역할</th>
</tr>
</thead>
<tbody><tr>
<td>fastapi</td>
<td>API 서버 구현</td>
</tr>
<tr>
<td>langchain</td>
<td>프롬프트 템플릿 + LLM 체인 관리</td>
</tr>
<tr>
<td>openai</td>
<td>GPT-4o 모델 호출, 요약 생성</td>
</tr>
<tr>
<td>pydantic</td>
<td>요청 스키마 검증</td>
</tr>
<tr>
<td>requests, BeautifulSoup</td>
<td>(5장에서) 뉴스 본문 크롤링, HTML 파싱</td>
</tr>
<tr>
<td>dotenv</td>
<td>환경 변수 로드</td>
</tr>
<tr>
<td>react + fetch API</td>
<td>프론트엔드 연동, 응답 표시, 음성 재생</td>
</tr>
</tbody></table>
<hr />
<h2 id="64-핵심-코드">6.4 핵심 코드</h2>
<h3 id="641뉴스-본문-크롤링-및-텍스트-정제-함수-5장-결과-재사용">6.4.1뉴스 본문 크롤링 및 텍스트 정제 함수 (5장 결과 재사용)</h3>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/ef6e8ea3-21b7-4ffa-a167-a270961d5adf/image.png" />
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/58482b49-67a1-4938-ae10-a734aea0c0a0/image.png" /></p>
<h3 id="642-langchain--openai-gpt-요약-모델-연동">6.4.2 LangChain + OpenAI GPT 요약 모델 연동</h3>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/007b3357-65fd-4f49-98d4-081dfdfa7746/image.png" />
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/c33ccf3c-c369-45d5-9472-dc0268537e32/image.png" /></p>
<hr />
<h2 id="64-코드-설명">6.4 코드 설명</h2>
<ul>
<li><strong>LangChain LLM 설정</strong>: GPT-4o 모델을 <code>ChatOpenAI</code>로 호출하며, <code>temperature=0.7</code>로 자연스러운 요약 지원  </li>
<li><strong>summary_chain</strong>: 뉴스 기사별 3~5줄 요약 생성용 프롬프트 및 실행 체인  </li>
<li><strong>trend_chain</strong>: 여러 개 기사 요약을 모아 전반적인 트렌드 3~5줄 설명 생성용 체인  </li>
<li><code>/news_trend/</code> API  <ul>
<li>키워드를 목적에 맞게 매핑  </li>
<li>네이버 뉴스 API로 상위 3개 뉴스 검색  </li>
<li>각 뉴스 URL에 대해 본문 크롤링 및 텍스트 정제 후 individual summary 생성  </li>
<li>다수 요약을 합쳐 트렌드 분석 결과 생성  </li>
<li>최종 JSON 응답으로 핵심 뉴스 요약 및 트렌드 정보를 포함  </li>
</ul>
</li>
</ul>
<hr />
<h2 id="65-전체-서비스-연계">6.5 전체 서비스 연계</h2>
<ul>
<li>프론트엔드에서 키워드를 입력하거나 음성 인식 결과를 받아 <code>/news_trend/</code> API 호출  </li>
<li>응답받은 뉴스 요약 및 트렌드 정보를 화면에 렌더링하고,  </li>
<li>주요 트렌드 텍스트를 TTS로 변환해 음성으로 사용자에게 전달  </li>
</ul>
<hr />
<h2 id="66-api-요청-및-응답-예시">6.6 API 요청 및 응답 예시</h2>
<h3 id="요청-예시">요청 예시</h3>
<pre><code>{
&quot;keyword&quot;: &quot;AI&quot;
}</code></pre><h3 id="응답-예시">응답 예시</h3>
<pre><code>### 응답 예시

{
&quot;keyword&quot;: &quot;AI&quot;,
&quot;purpose&quot;: &quot;인공지능 트렌드 요약&quot;,
&quot;trend_digest&quot;: &quot;최근 인공지능 업계에서는 생성형 AI 기술을 중심으로 다양한 산업에서 활용이 급속도로 증가하고 있습니다...&quot;,
&quot;trend_articles&quot;: [
{
&quot;title&quot;: &quot;인공지능 기술혁신 동향&quot;,
&quot;url&quot;: &quot;https://news.example.com/ai1&quot;,
&quot;summary&quot;: &quot;인공지능 기술은 빠른 속도로 발전하며 여러 산업 분야에 적용되고 있습니다...&quot;
},
{
&quot;title&quot;: &quot;AI 스타트업 투자 증가&quot;,
&quot;url&quot;: &quot;https://news.example.com/ai2&quot;,
&quot;summary&quot;: &quot;최근 AI 스타트업에 대한 투자 붐이 일고 있으며 혁신적인 서비스가 등장하고 있습니다...&quot;
}
]
}</code></pre><hr />
<h2 id="67-고도화-제안-및-유의-사항">6.7 고도화 제안 및 유의 사항</h2>
<ul>
<li><strong>긴 기사 처리</strong>: GPT 토큰 제한에 맞춰 기사 본문을 여러 조각으로 분할한 후 각각 요약하고 병합하는 chunking 기법 적용  </li>
<li><strong>프롬프트 최적화</strong>: 일관된 문체 유지와 사용자 맞춤형 요약을 위한 프롬프트 튜닝  </li>
<li><strong>오류 관리</strong>: API 호출 실패, 네트워크 오류 등 발생 시 재시도 로직 및 세밀한 예외처리 필요  </li>
<li><strong>다양한 목적 지원</strong>: 금융, 부동산, IT 등 키워드 특화 요약 템플릿 확장 가능  </li>
<li><strong>API 보안 및 제한</strong>: 인증과 호출 횟수 제한 설정으로 서비스 안정성 확보  </li>
</ul>
<hr />
<p>이상으로 6장은 정제된 뉴스 본문을 AI 요약 모델에 연동하여, 목적에 맞는 뉴스 요약과 트렌드 분석 결과를 생성하는 핵심 구현 과정을 다뤘습니다.<br />이를 통해 사용자에게 직관적이고 빠른 뉴스 이해 경험을 제공하며, 프론트엔드 및 TTS 서비스를 연계한 완성도 높은 뉴스 요약 서비스를 구축하게 됩니다.</p>
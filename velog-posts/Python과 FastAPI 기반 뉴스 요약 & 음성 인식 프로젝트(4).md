<h1 id="4-코드-리뷰-1-네이버-api-데이터-수집-뉴스--트렌드-키워드">4. 코드 리뷰 1: 네이버 API 데이터 수집 (뉴스 + 트렌드 키워드)</h1>
<p>이 장에서는 프로젝트의 핵심 데이터 수집 부분인<br />네이버 뉴스 API와 네이버 데이터랩 트렌드 API를 연동하는 기능을 상세히 살펴봅니다.</p>
<hr />
<h2 id="41-네이버-뉴스-api-연동-뉴스-목록-수집">4.1 네이버 뉴스 API 연동 (뉴스 목록 수집)</h2>
<p><strong>이 코드가 필요한 이유</strong>  </p>
<ul>
<li><code>/news_trend/</code> 엔드포인트에서 최신 뉴스 기사를 수집하기 위해,<br />지정된 키워드로 네이버 뉴스 API를 호출하는 역할을 담당합니다.  </li>
<li>뉴스 본문 크롤링과 AI 요약을 진행하기 전, <strong>데이터 수집의 첫 단계</strong>입니다.</li>
</ul>
<h3 id="412-뉴스-검색-api-호출-함수-코드">4.1.2 뉴스 검색 API 호출 함수 코드</h3>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/1b20e4fe-623c-4841-81f2-b079f5acd636/image.png" /></p>
<h3 id="413-코드-라인별-상세-해설">4.1.3 코드 라인별 상세 해설</h3>
<ul>
<li><p><code>url = ...</code><br />네이버 뉴스 검색 API의 공식 주소입니다.</p>
</li>
<li><p><code>headers = {...}</code><br />API 호출에 필요한 <strong>인증 정보</strong>(Client ID, Client Secret)를 환경변수에서 꺼내 HTTP 헤더에 넣습니다.<br /><em>직접 코드에 키를 쓰지 않고 관리해 보안을 유지합니다.</em></p>
</li>
<li><p><code>params = {...}</code><br />API 요청에 필요한 파라미터:  </p>
<ul>
<li><code>query</code>: 사용자 검색어  </li>
<li><code>display</code>: 한번에 받을 뉴스 기사 개수 (최대 100 개)  </li>
<li><code>start</code>: 검색 시작 위치(1부터)  </li>
<li><code>sort</code>: 결과 정렬 방식 (<code>date</code>는 최신순)</li>
</ul>
</li>
<li><p><code>res = requests.get(...)</code><br />위 URL과 헤더, 파라미터로 GET 요청을 보내며, <strong>5초 타임아웃</strong> 설정해 서버 응답 지연에 대비합니다.</p>
</li>
<li><p><code>res.raise_for_status()</code><br />요청 실패 시 HTTP 오류 코드를 감지하고 예외를 자동 발생시켜 안정성을 높입니다.</p>
</li>
<li><p><code>items = res.json().get(&quot;items&quot;, [])</code><br />정상 응답 시 JSON 데이터에서 뉴스 목록 배열 <code>items</code>를 추출합니다. 없으면 빈 리스트 기본값.</p>
</li>
<li><p><code>if not items:</code><br />뉴스 기사가 없으면 HTTP 404 에러를 발생시켜 호출자에게 알립니다.</p>
</li>
<li><p><code>return ...</code><br />실제 사용할 뉴스 제목과 링크만 추려서 깔끔한 리스트로 반환합니다.</p>
</li>
</ul>
<p><strong>연계 구조</strong>  </p>
<ul>
<li><code>/news_trend/</code> API 내에서 호출 → 기사 URL 목록을 후속 본문 추출(<code>extract_article_text</code>) 단계로 전달</li>
</ul>
<hr />
<h2 id="42-네이버-데이터랩-트렌드-api-연동-인기-키워드-수집">4.2 네이버 데이터랩 트렌드 API 연동 (인기 키워드 수집)</h2>
<p><strong>이 코드가 필요한 이유</strong>  </p>
<ul>
<li>사용자가 요청한 키워드에 대해, 기사별 요약과 전체 트렌드 요약을 만들어주는 <strong>핵심 API</strong>입니다.  </li>
<li>뉴스 검색 → 본문 추출 → 텍스트 정제 → AI 요약 → 트렌드 종합 과정을 모두 아우릅니다.</li>
</ul>
<h3 id="422-트렌드-api-호출-함수-코드">4.2.2 트렌드 API 호출 함수 코드</h3>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/61cda3b8-b96f-415d-a4ee-3b2b8e18f24b/image.png" /></p>
<h3 id="425-코드-라인별-상세-해설-news_trend-엔드포인트">4.2.5 코드 라인별 상세 해설 (<code>/news_trend/</code> 엔드포인트)</h3>
<ul>
<li><p><code>@app.post(&quot;/news_trend/&quot;)</code><br />→ 클라이언트에서 키워드를 POST 요청으로 전송하면 처리하는 <strong>FastAPI 엔드포인트</strong>입니다.</p>
</li>
<li><p><code>purpose = map_keyword_to_purpose(req.keyword)</code><br />→ 사용자가 입력한 키워드를 “뉴스 요약 목적” 문자열로 변환합니다.<br />  예) <code>AI</code> → &quot;인공지능 트렌드 요약&quot;<br />  이 목적은 AI 요약 프롬프트를 더 구체적이고 문맥에 맞게 만들기 위해 사용됩니다.</p>
</li>
<li><p><code>links = search_naver_news(req.keyword, max_articles=3)</code><br />→ 앞서 본 <code>search_naver_news()</code> 함수를 호출해, 해당 키워드의 최신 뉴스 3건을 가져옵니다.</p>
</li>
<li><p><code>summaries = []</code>, <code>details = []</code><br />→ 뉴스 기사별 요약문(<code>summaries</code>)과 기사 상세 정보(<code>details</code>)를 담을 빈 리스트 생성.</p>
</li>
<li><p><code>for link in links:</code><br />→ 가져온 각 뉴스 기사 링크에 대해 다음 처리를 반복합니다.</p>
<ol>
<li><code>art = extract_article_text(link[&quot;url&quot;])</code><br />→ 기사 페이지에서 HTML 본문을 추출합니다.</li>
<li><code>clean = clean_text(art, &quot;KR&quot;)</code><br />→ 노이즈(광고·HTML 태그·특수문자 등)를 제거해 뉴스 본문만 깔끔하게 남깁니다.</li>
<li><code>summ = summary_chain.invoke({&quot;purpose&quot;: purpose, &quot;article&quot;: clean}).content</code><br />→ 정제된 본문을 LLM(LangChain+OpenAI)에게 전달해 목적에 맞는 요약을 생성합니다.</li>
<li><code>summaries.append(summ)</code><br />→ 전체 요약문 리스트에 추가.</li>
<li><code>details.append({...})</code><br />→ 기사 제목, URL, 요약을 포함한 딕셔너리를 기사별 상세 리스트에 추가.</li>
</ol>
</li>
<li><p><code>trend = trend_chain.invoke({&quot;purpose&quot;: purpose, &quot;summaries&quot;: &quot;\n&quot;.join(summaries)}).content</code><br />→ 기사별 요약들을 모두 합쳐 전체 트렌드 요약문을 생성합니다.<br />  예: “AI 산업은 최근 3개월간…”과 같은 종합 분석 형태.</p>
</li>
<li><p><code>return {...}</code><br />→ 클라이언트에 반환되는 JSON 구조:</p>
<ul>
<li><code>keyword</code> : 검색 키워드</li>
<li><code>purpose</code> : 요약 목적</li>
<li><code>trend_digest</code> : 전체 트렌드 요약문</li>
<li><code>trend_articles</code> : 기사별 제목/URL/요약 리스트</li>
</ul>
</li>
</ul>
<hr />
<p><strong>연계 구조</strong>  </p>
<ul>
<li>프론트엔드에서 키워드 클릭/검색 시 <code>/news_trend/</code>를 호출  </li>
<li>내부에서 <code>search_naver_news</code>로 기사 수집 → <code>extract_article_text</code>로 본문 추출 → <code>clean_text</code>로 정제 → LLM으로 기사별 요약 &amp; 트렌드 요약  </li>
<li>결과 JSON은 React(프론트) 컴포넌트에서 받아 UI에 표시</li>
</ul>
<hr />
<h2 id="43-코드-라인별-상세-해설-popular_keywords-엔드포인트">4.3 코드 라인별 상세 해설 (<code>/popular_keywords/</code> 엔드포인트)</h2>
<p><strong>이 코드가 필요한 이유</strong>  </p>
<ul>
<li>프론트엔드 메인 화면(또는 홈 화면)에서 <strong>사용자가 가장 먼저 보게 될 인기 키워드 목록</strong>을 제공하는 API입니다.  </li>
<li>사용자가 인기 키워드를 클릭하면 해당 키워드로 <code>/news_trend/</code> API를 호출하여 관련 뉴스 요약을 확인할 수 있습니다.  </li>
<li>즉, 뉴스 검색 API의 시작점을 만들어 주는 <strong>진입점 기능</strong>을 합니다.</li>
</ul>
<hr />
<h3 id="431-popular_keywords-엔드포인트-코드">4.3.1 <code>/popular_keywords/</code> 엔드포인트 코드</h3>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/8c4c5951-3e49-43b8-bb6f-d193c5a072dc/image.png" /></p>
<hr />
<h3 id="432-코드-라인별-상세-해설-popular_keywords">4.3.2 코드 라인별 상세 해설 (<code>/popular_keywords/</code>)</h3>
<ul>
<li><p><code>@app.get(&quot;/popular_keywords&quot;)</code> / <code>@app.get(&quot;/popular_keywords/&quot;)</code><br />→ 같은 함수를 두 개의 경로 데코레이터에 등록하여, 끝에 <code>/</code>가 있든 없든 요청을 처리할 수 있도록 합니다.<br />  예) <code>/popular_keywords</code> 와 <code>/popular_keywords/</code> 모두 접근 가능.</p>
</li>
<li><p><code>def popular_keywords():</code><br />→ 인기 키워드 목록과 각 키워드별 뉴스 개수를 반환하는 함수입니다.</p>
</li>
<li><p><code>return [ {...}, {...}, ... ]</code><br />→ 리스트 형태로 키워드 정보들을 반환합니다. 각 항목은 다음과 같습니다.</p>
<ul>
<li><code>keyword</code>: 인기 검색어(예: <code>&quot;코인&quot;</code>, <code>&quot;부동산&quot;</code>, <code>&quot;AI&quot;</code>)  </li>
<li><code>news_count</code>: 해당 키워드와 관련된 뉴스 기사 수</li>
</ul>
</li>
</ul>
<hr />
<p><strong>연계 구조</strong>  </p>
<ul>
<li>프론트엔드(React)의 <strong>PopularKeywords</strong> 컴포넌트에서 이 API를 호출 → 인기 키워드 목록 표시  </li>
<li>사용자가 목록 중 하나를 클릭하면 <code>/news_trend/</code>로 키워드가 전달되어 해당 키워드 관련 뉴스 목록과 요약이 표시됨  </li>
</ul>
<hr />
<h2 id="44-전체-데이터-흐름-다이어그램">4.4 전체 데이터 흐름 다이어그램</h2>
<p>[사용자]
    │
    ▼
GET /popular_keywords → 인기 키워드 목록
    │
    ▼ (인기 키워드 클릭)
POST /news_trend (keyword)
    ├─ search_naver_news() → 최신 뉴스 목록
    ├─ extract_article_text() → 본문 추출
    ├─ clean_text() → 텍스트 정제
    ├─ summary_chain → 기사별 요약
    └─ trend_chain → 전체 트렌드 요약
        │
        ▼
JSON 응답 → 프론트엔드 표시</p>
<hr />
<h2 id="45-마무리">4.5 마무리</h2>
<p>이번 4장에서는 main.py 안에서 구현된<br /><strong>네이버 뉴스 검색 API 함수</strong>, <strong>뉴스 트렌드 요약 API</strong>, <strong>인기 키워드 API</strong>를 실제 코드와 함께 분석했습니다.</p>
<ul>
<li><p><strong>search_naver_news()</strong><br />→ 키워드 기반으로 최신 뉴스 기사 목록을 네이버 뉴스 API에서 수집하는 <strong>데이터 수집 1단계</strong><br />→ 이후 본문 추출, 텍스트 정제, AI 요약을 위한 기반 데이터 생성</p>
</li>
<li><p><strong>/news_trend/</strong><br />→ 뉴스 검색 → 본문 추출 → 정제 → 기사별 요약 → 전체 트렌드 요약까지<br />   하나의 데이터 파이프라인을 구성하는 <strong>핵심 API 엔드포인트</strong></p>
</li>
<li><p><strong>/popular_keywords/</strong><br />→ 메인 화면에서 인기 키워드를 제공하는 <strong>사용자 진입점</strong> API<br />   클릭 시 자동으로 <code>/news_trend/</code> 호출로 이어짐</p>
</li>
</ul>
<p>이번 장을 통해,  </p>
<ul>
<li>뉴스 데이터 수집과 가공 과정이 어떻게 백엔드에서 이루어지는지  </li>
<li>각 API가 상호 연계되어 전체 서비스 플로우를 완성하는 방법을<br />명확히 이해할 수 있었습니다.</li>
</ul>
<hr />
<p>다음 5장에서는<br /><strong>본문 크롤링과 텍스트 정제 로직</strong>(<code>extract_article_text</code>, <code>clean_text</code>)을 심층 분석하고,<br />AI 요약기(<code>summary_chain</code>, <code>trend_chain</code>)와 결합하는 방법을 살펴봅니다.</p>
<p>이 과정을 거치면 뉴스 데이터가<br />'원시 HTML'에서 '사용자 친화적 요약 데이터'로 변환되는 전체 흐름이 완성됩니다.</p>
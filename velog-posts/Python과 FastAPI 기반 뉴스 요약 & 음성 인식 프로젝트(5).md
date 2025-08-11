<h1 id="5-코드-리뷰-2-본문-크롤링-및-텍스트-정제">5. 코드 리뷰 2: 본문 크롤링 및 텍스트 정제</h1>
<p>이번 5장에서는 4장에서 수집한 뉴스 기사 URL의 각 뉴스 페이지에서<br />웹 크롤링으로 실제 본문을 추출하고,<br />불필요한 광고·HTML 태그·특수문자를 제거해 텍스트를 정제하는 과정을 다룹니다.</p>
<hr />
<h2 id="51-본문-크롤링-및-정제-함수의-필요성">5.1 본문 크롤링 및 정제 함수의 필요성</h2>
<ul>
<li>뉴스 기사 URL만 가지고선 사용자가 읽거나, AI가 요약할 <em>실질 데이터</em>가 없습니다.</li>
<li>웹 크롤링을 통해 <strong>기사의 실제 본문</strong>을 추출하고, 노이즈와 광고를 제거해 <strong>깨끗하고 분석 가능한 텍스트</strong>로 만들어야 요약, 분석, DB 저장, UI 렌더링에 활용할 수 있습니다.</li>
</ul>
<hr />
<h2 id="52-크롤링-및-정제-주요-코드">5.2 크롤링 및 정제 주요 코드</h2>
<h3 id="521-기사-본문-크롤링-함수">5.2.1 기사 본문 크롤링 함수</h3>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/7da1a038-1104-424b-9149-2434d0d37b96/image.png" /></p>
<h3 id="522-본문-크롤링-함수-extract_article_text">5.2.2 본문 크롤링 함수 (<code>extract_article_text</code>)</h3>
<ul>
<li><code>headers = {&quot;User-Agent&quot;: &quot;Mozilla/5.0&quot;}</code><br />사람이 브라우저로 접근하는 듯한 요청임을 서버에 알림(봇 차단 우회).</li>
<li><code>res = requests.get(url, headers=headers, timeout=5)</code><br />지정 URL의 HTML 페이지 다운로드(5초 타임아웃).</li>
<li><code>res.raise_for_status()</code><br />HTTP 오류 코드 감지시 즉시 예외 발생.</li>
<li><code>soup = BeautifulSoup(res.content, &quot;html.parser&quot;)</code><br />HTML 파싱 후 DOM 트리 생성.</li>
<li><code>node = soup.select_one(...)</code><br />주요 뉴스 사이트별 기사 본문 CSS 선택자 모음(확장 용이).</li>
<li><code>if node:</code><br />본문이 있으면 아래 과정 반복:<ul>
<li><code>for bad in node.select(&quot;script, .ad_banner, .advertisement&quot;):</code><br />본문 내 광고, 스크립트 등 불필요 태그 탐색 및 제거.</li>
<li><code>bad.decompose()</code><br />해당 태그를 완전히 삭제.</li>
<li><code>return node.get_text(separator=&quot; &quot;, strip=True)</code><br />최종적으로 남은 순수 본문 텍스트 반환.</li>
</ul>
</li>
<li><code>paras = [...]</code><br />본문 영역 존재하지 않을 경우, <code>&lt;p&gt;</code> 태그 내 긴 문단(50자 이상)만 따로 추출 후 합침.</li>
<li><code>if paras:</code><br />추출된 문단이 있으면 줄바꿈으로 연결해 반환.</li>
<li><code>raise HTTPException(...)</code><br />어느 방법으로도 본문 추출 실패시 500 에러 발생.</li>
</ul>
<hr />
<h3 id="523-텍스트-정제-함수">5.2.3 텍스트 정제 함수</h3>
<p><img alt="" src="https://velog.velcdn.com/images/hanyeon/post/c03e6a0e-d564-49a8-bfd5-384e00dcb018/image.png" /></p>
<hr />
<h3 id="524-텍스트-정제-함수-clean_text">5.2.4 텍스트 정제 함수 (<code>clean_text</code>)</h3>
<ul>
<li><code>if language == 'KR':</code><br />한글 뉴스 기사에만 특화된 정제 진행.</li>
<li><code>re.sub(r&quot;\s+&quot;, &quot; &quot;, text)</code><br />여러 줄, 과도한 공백을 하나로 축소.</li>
<li><code>re.sub(r&quot;[^...]&quot;, &quot;&quot;, text)</code><br />한글, 숫자, 영어, 일부 구두점 외 모든 특수문자 제거.</li>
<li><code>re.sub(r&quot;[\■▲◆▶]&quot;, &quot;&quot;, text)</code><br />뉴스 광고에 주로 쓰이는 특수기호 완전 제거.</li>
<li><code>text.strip()</code><br />앞뒤 불필요한 공백까지 정리해서 반환.</li>
<li><code>else: raise ValueError(...)</code><br />한국어 뉴스에 쓰지 않을 경우 명확하게 오류 안내.</li>
</ul>
<hr />
<h2 id="54-연계-구조">5.4 연계 구조</h2>
<ul>
<li><code>/news_trend/</code> 엔드포인트 내 기사 URL 리스트가 생성됨</li>
<li>각 URL → <code>extract_article_text()</code>로 본문 HTML 크롤링</li>
<li>추출된 본문 텍스트 → <code>clean_text()</code>로 광고·노이즈 제거</li>
<li>정제한 텍스트는 AI 요약체인(<code>summary_chain</code>)에 전달돼 최종 요약문으로 생성/분석됨</li>
</ul>
<hr />
<h2 id="55-시각적-데이터-처리-흐름">5.5 시각적 데이터 처리 흐름</h2>
<p>[뉴스 기사 URL 리스트]
        ↓
[이미지1 : extract_article_text() - 본문 크롤링]
        ↓
[이미지2 : clean_text() - 텍스트 정제]
        ↓
[AI 요약기(summary_chain) - 뉴스 요약 생성]
        ↓
[최종 뉴스 요약 결과]</p>
<hr />
<h2 id="56-마무리">5.6 마무리</h2>
<p>본문 크롤링과 정제 단계는 <em>뉴스 데이터 품질과 AI 요약 결과의 핵심!</em><br />사이트·광고 구조가 자주 바뀌므로 코드 유지보수와 선택자 전략도 중요합니다.<br />이 과정을 거치면 사용자가 읽기 좋은, 그리고 AI가 정확히 요약하는 뉴스 데이터 파이프라인의 기반이 완성됩니다.</p>
<p>다음 6장에서는<br />이 정제된 본문을 바탕으로 AI 요약 모델(LangChain+OpenAI GPT) 연동 로직 및 결과 생산 과정을 상세히 리뷰하겠습니다.</p>
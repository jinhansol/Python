<h2 id="31예약어-목록-키워드">3.1예약어 목록 (키워드)</h2>
<p>Python 언어 구문을 정의하는 예약어(keyword)는 변수명·함수명·클래스명 등 식별자로 사용할 수 없습니다. 주요 키워드는 다음과 같습니다:  </p>
<pre><code>| False | await | else | import | pass |
| None | break | except | in | raise |
| True | class | finally | is | return |
| and | continue | for | lambda | try |
| as | def | from | nonlocal | while |
| assert | del | global | not | with |
| async | elif | if | or | yield |</code></pre><p>위 키워드 전체 목록과 설명은 공식 문서 및 Programiz 키워드 리스트에서 확인할 수 있습니다.</p>
<hr />
<h2 id="32-식별자-네이밍-규칙">3.2 식별자 네이밍 규칙</h2>
<p>식별자(identifier)는 변수, 함수, 클래스 등 프로그래머가 정의하는 이름입니다. 다음 규칙을 따라야 합니다:</p>
<ul>
<li><strong>허용 문자</strong>: 영문 대·소문자, 숫자, 밑줄(<code>_</code>) 조합 가능 (대소문자 구분)  </li>
<li><strong>시작 문자</strong>: 숫자로 시작 불가 (예: <code>1var</code> ❌ vs <code>var1</code> ✅)  </li>
<li><strong>키워드 사용 금지</strong>: <code>global = 10</code> ❌  </li>
<li><strong>특수문자 금지</strong>: <code>!</code>, <code>@</code>, <code>#</code>, <code>$</code>, <code>%</code> 등 ❌  </li>
<li><strong>길이 제한 없음</strong>: 길이가 길어도 무방하나, 가독성을 위해 적당한 길이 권장  </li>
</ul>
<h3 id="스타일-가이드-pep-8">스타일 가이드 (PEP 8)</h3>
<ul>
<li><strong>변수·함수</strong>: <code>snake_case</code> (e.g. <code>user_name</code>, <code>print_value</code>)  </li>
<li><strong>클래스</strong>: <code>CamelCase</code> (e.g. <code>MyClass</code>)  </li>
<li><strong>상수</strong>: <code>ALL_CAPS</code> (e.g. <code>MAX_RETRY</code>)  </li>
</ul>
<pre><code class="language-python"># 올바른 예
user_age = 30
calculate_area()
MAX_CONNECTIONS = 5

# 잘못된 예
1st_value = 10      # 숫자로 시작
for = 5             # 키워드 사용
total-value = 100   # 하이픈 사용</code></pre>
<hr />
<h2 id="33-명령문statement--여러-문장-표현-방식">3.3 명령문(statement) &amp; 여러 문장 표현 방식</h2>
<p>Python에서 명령문(statement) 은 한 줄에 실행 가능한 코드 단위를 의미합니다.</p>
<pre><code>a = 1          # 할당문 (assignment statement)
print(a)       # 함수 호출문</code></pre><h3 id="여러-줄-명령문-multi-line">여러 줄 명령문 (Multi-line)</h3>
<ol>
<li>역슬래시( \ ) 사용<pre><code>total = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9</code></pre></li>
<li>괄호 사용<pre><code>total = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)</code></pre></li>
<li>대괄호 / 중괄호 내에서 자동으로 연결<pre><code>data = [
&quot;apple&quot;, &quot;banana&quot;, &quot;cherry&quot;,
&quot;date&quot;, &quot;elderberry&quot;
]</code></pre></li>
<li>세미콜론(;) 으로 한줄에 여러 문장<pre><code>x = 1; y = 2; print(x + y)</code></pre></li>
</ol>
<hr />
<h2 id="34-들여쓰기indentation--주석comments">3.4 들여쓰기(indentation) &amp; 주석(comments)</h2>
<h3 id="들여쓰기indentation">들여쓰기(Indentation)</h3>
<ul>
<li>중괄호 대신 들여쓰기로 코드 블록을 구분합니다.</li>
<li>스페이스 4칸 사용 권장 (탭 대신 스페이스).</li>
<li>잘못된 예:<pre><code>if True:
print(&quot;Hello&quot;)    # IndentationError</code></pre></li>
<li>올바른 예:<pre><code>if True:
  print(&quot;Hello&quot;)
  x = 5
  if x &gt; 0:
      print(&quot;Positive&quot;)</code></pre></li>
</ul>
<h3 id="주석comments">주석(Comments)</h3>
<ul>
<li>한 줄 주석 : # 뒤에 설명<pre><code># 사용자 이름 입력 받기
name = input(&quot;Name: &quot;)</code></pre></li>
</ul>
<ul>
<li>블록 주석 : 여러 줄 # 또는 멀티라인 문자열
```
&quot;&quot;&quot;
이 함수는 주어진 값을 두 배로 만들어 반환합니다.</li>
<li>입력: num (int 또는 float)</li>
<li>반환: num * 2
&quot;&quot;&quot;
```</li>
<li>주석 주의점 : <ul>
<li>코드 변경 시 주석도 함께 업데이트</li>
<li>과도한 주석은 오히려 가독성을 해칠 수 있음</li>
</ul>
</li>
</ul>
<hr />
<h2 id="35-docstring-활용">3.5 Docstring 활용</h2>
<p>Docstring은 함수·클래스·모듈 정의 바로 아래에 위치한 문서화 문자열입니다. <strong>doc</strong> 속성과 연결되어 자동 문서화 도구에서 활용됩니다.</p>
<pre><code>def greet(name: str) -&gt; None:
    &quot;&quot;&quot;
    주어진 이름으로 인사 메시지를 출력합니다.

    Args:
        name (str): 사용자 이름

    Returns:
        None
    &quot;&quot;&quot;
    print(f&quot;Hello, {name}!&quot;)</code></pre><ul>
<li>첫 줄: 간단 요약(한 문장)</li>
<li>빈 줄: 요약과 본문 구분</li>
<li>본문:<ul>
<li>Args: 파라미터 설명</li>
<li>Returns: 반환값 설명</li>
<li>Raises: 발생 가능한 예외 설명</li>
</ul>
</li>
<li>접근:<pre><code>print(greet.__doc__)</code></pre></li>
<li>PEP 257 권장 형식 준수</li>
</ul>
<hr />
<p>다음은 4편 변수,상수,리터럴에 대해서 적어보겠습니다!</p>
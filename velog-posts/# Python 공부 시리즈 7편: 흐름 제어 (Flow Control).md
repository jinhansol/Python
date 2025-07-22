<h2 id="71-조건문-if-if-else--if-elif-else--중첩-if">7.1 조건문: if/ if-else / if-elif-else / 중첩 if</h2>
<p>Python의 조건문은 <strong>코드 흐름을 분기</strong> 시키는 기본 도구입니다. 들여쓰기를 통해 조건에 따라 실행 블록을 구분합니다.</p>
<h3 id="기본구조">기본구조</h3>
<pre><code>Python

if 조건식:
    실행문</code></pre><hr />
<h4 id="if-else">if-else</h4>
<pre><code>python

score = 85

if score &gt;= 60:
    print(&quot;합격입니다&quot;)
else :
    print(&quot;불합격입니다.&quot;)</code></pre><hr />
<h4 id="if---elif---else여러-조건-처리">if - elif - else(여러 조건 처리)</h4>
<pre><code>python

score = 75

if score &gt;= 90:
    print(&quot;A등급&quot;)
elif score &gt;= 80:
    print(&quot;B등급&quot;)
elif score &gt;= 70:
    print(&quot;C등급&quot;)
else:
    print(&quot;D등급&quot;)</code></pre><ul>
<li>elif는 필요에 따라 여러 번 사용 가능합니다.</li>
<li>else는 모든 조건이 False일 때 실행됩니다.</li>
</ul>
<hr />
<h4 id="중첩ifnested-if">중첩if(Nested if)</h4>
<pre><code> python

 num = 10

 if num &gt; 0:
     if num % 2 == 0:
        print(&quot;양수이며 짝수입니다.&quot;)
    else:
        print(&quot;양수이며 홀술입니다.&quot;)
 else:
     print(&quot;0 또는 음수입니다.&quot;)</code></pre><hr />
<h2 id="72-반복문-for--while--range">7.2 반복문: for / while / range()</h2>
<p> 반복문은 <strong>같은 코드를 여러 번 실행</strong>할 때 사용됩니다.</p>
<h4 id="for문">for문</h4>
<ul>
<li><strong>시퀸스(list, tuple, dict, str 등)</strong>의 각 요소를 순회합니다.<pre><code>python
</code></pre></li>
</ul>
<p>fruits = [&quot;apple&quot;, &quot;banana&quot;, &quot;cherry&quot;]</p>
<p>for fruit in fruits:
    print(fruit)</p>
<pre><code>
 - **문자열 순회**</code></pre><p>python</p>
<p>for ch in &quot;Python&quot;:
    print(ch)</p>
<pre><code>
 - 딕셔너리 순회</code></pre><p>python</p>
<p>person = {&quot;name&quot;: &quot;Alice&quot;, &quot;age&quot;: 30}</p>
<p>for key in person:
    print(key, &quot;:&quot;, person[key])</p>
<pre><code>
#### range() 함수
 - 정수 반복에 주로 사용되며, range(시작, 끝, 간격) 형태입니다.
 - 끝은 포함하지 않음에 주의합니다.</code></pre><p>python</p>
<p>for i in range(5):            # 0부터 4까지
    print(i)</p>
<p>for i in range(1, 6):        # 1부터 5까지
    print(i)</p>
<p>for i in range(10, 0, -2):    # 10부터 2까지 2씩 감소
    print(i)</p>
<pre><code>
#### while 문
 - 조건이 참인 동안 반복합니다.</code></pre><p>python</p>
<p>count = 0</p>
<p>while count &lt; 5:
    print(&quot;count:&quot;, count)
    count += 1</p>
<pre><code> - 조건이 거짓이 되면 반복을 종료합니다.

---

## 7.2 break, continue, pass
#### break
 - 반복문을 즉시 종료 합니다.</code></pre><p>python</p>
<p>for i in range(10):
    if i == 5:
        break
    print(i)    # 0 ~ 4까지 출력</p>
<pre><code>
#### continue
 - 현재 반복을 건너뛰고, 다음 반복으로 넘어갑니다.</code></pre><p>python</p>
<p>for i in range(5):
    if i == 2:
        continue
    print(i)    # 0, 1, 3, 4 출력 (2는 제외)</p>
<pre><code>
#### pass
 - 아무 작업도 하지 않음(문법적 placeholder)</code></pre><p>python</p>
<p>for i in range(5):
    if i == 2:
        pass    # 이후 구현 예정
    print(i)</p>
<pre><code> - 함수나 클래스의 빈 블록을 정의할 때도 사용됩니다.</code></pre><p>python</p>
<p>def feature_coming_soon():
    pass</p>
<p>```</p>
<hr />
<h4 id="마무리">마무리</h4>
<p>이번 편에서는 Python의 코드 흐름을 제어하는 조건문과 반복문, 그리고 흐름 제어 키워드 들을 알아봤습니다.</p>
<p>다음 편에서는 <strong>함수와 매개변수, 반환값</strong>에 대해 학습해보겠습니다.</p>
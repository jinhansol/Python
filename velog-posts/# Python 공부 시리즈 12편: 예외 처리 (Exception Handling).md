<p>Python은 <strong>예외 처리(try-except)</strong> 구문을 통해 프로그램의 <strong>비정상 종료를 방지</strong>하고, 예외 상황을 <strong>우아하게 처리</strong>할 수 있도록 도와줍니다.</p>
<hr />
<h2 id="1-예외란">1. 예외란?</h2>
<blockquote>
<p>예외(Exception)는 프로그램 실행 중 발생하는 오류입니다.</p>
</blockquote>
<h3 id="예시-zerodivisionerror">예시: ZeroDivisionError</h3>
<pre><code>python

print(10 / 0)

ZeroDivisionError: division by zero</code></pre><p>위처럼 예외가 발생하면 프로그램이 중단됩니다. 이 문제를 해결하려면 예외 처리 구문을 사용해야 합니다.</p>
<hr />
<h2 id="2-try---except-기본-구조">2. try - except 기본 구조</h2>
<pre><code>python

try:
    실행할 코드
except 예외타입:
    예외 발생 시 실행할 코드</code></pre><h3 id="예제">예제</h3>
<pre><code>python

try:
    num = int(input(&quot;숫자를 입력하세요: &quot;))
    print(10/num)
except ZeroDivisionError:
    print(&quot;0으로 나눌 수 없습니다.&quot;)
except ValueError:
    print(&quot;정수를 입력해주세요.&quot;)</code></pre><hr />
<h2 id="3-여러-예외-처리하기">3. 여러 예외 처리하기</h2>
<p>except 블록을 여러 개 사용할 수 있으며, 예외 메시지도 출력할 수 있습니다.</p>
<pre><code>python

try:
    num = int(input(&quot;숫자 입력: &quot;))
    print(10 / num)
except ZeroDivisionError as e:
    print(&quot;오류:&quot;, e)
except ValueError:
    print(&quot;숫자가 아닙니다.&quot;)</code></pre><hr />
<h2 id="4-모든-예외-처리비추천">4. 모든 예외 처리(비추천)</h2>
<pre><code>python

try:
    # 코드
except Exception as e:
    print(&quot;알 수 없는 오류 발생:&quot;, e)</code></pre><ul>
<li>Exception은 모든 예외의 최상위 클래스</li>
<li>디버깅이 어려워질 수 있으므로, 가능한 구체적인 예외만 처리하는 것이 좋습니다.</li>
</ul>
<h2 id="5-else와-finally">5. else와 finally</h2>
<p>🔸 else</p>
<ul>
<li>예외가 발생하지 않는 경우에만 실행됩니다.<pre><code>python
</code></pre></li>
</ul>
<p>try:
    num = int(input(&quot;숫자 입력: &quot;))
except ValueError:
    print(&quot;정수가 아닙니다.&quot;)
else:
    print(&quot;입력 성공:&quot;, num)</p>
<pre><code>
🔸 finally
 - 예외 발생 여부와 관계없이 항상 실행되는 블록
 - 자원 해제, 파일 닫기 등에 사용</code></pre><p>python</p>
<p>try:
    f = open(&quot;file.txt&quot;, &quot;r&quot;)
    print(f.read())
except FileNotFoundError:
    print(&quot;파일이 존재하지 않습니다.&quot;)
finally:
    f.close()
    print(&quot;파일 닫기 완료&quot;)</p>
<pre><code>
---

## 6. raise 키워드 (예외 직접 발생)
개발자가 의도적으로 예외를 발생시킬 수 있습니다.</code></pre><p>python</p>
<p>def divide(x):
    if x == 0:
        raise ValueError(&quot;0으로 나눌 수 없습니다.&quot;)
    return 10 / x</p>
<p>try:
    print(divide(0))
except ValueError as e:
    print(&quot;오류 발생:&quot;, e)</p>
<pre><code>
---

## 7. 사용자 정의 예외 클래스
기존 예외로 처리하기 애매한 상황에 대해 직접 예외 클래스를 정의할 수 있습니다.</code></pre><p>python</p>
<p>class NegativeNumberError(Exception):
    def <strong>init</strong>(self, value):
        self.value = value</p>
<p>def check_number(n):
    if n &lt; 0:
        raise NegativeNumberError(n)</p>
<p>try:
    check_number(-10)
except NegativeNumberError as e:
    print(f&quot;음수는 허용되지 않습니다: {e.value}&quot;)</p>
<p>```</p>
<ul>
<li>Exception을 상속하여 새로운 예외 타입을 정의합니다.</li>
</ul>
<hr />
<p><strong>실전 팁</strong></p>
<ul>
<li>예외 처리는 예상 가능한 오류를 미리 방지하고, 사용자 경험을 향상시킵니다.</li>
<li>너무 많은 예외를 포괄적으로 처리하기보다는, 구체적인 예외를 명시적으로 잡는 것이 중요합니다.</li>
<li>fianlly는 꼭 필요한 경우에만 사용하고, 파일/자원 해제와 같이 반드시 처리해야하는 작업에 활용하세요.</li>
</ul>
<hr />
<p><strong>마무리</strong>
이번 편에서는 Python의 예외 처리 흐름을 기초부터 심화까지 다뤘습니다.
| 키워드       | 역할                 |
| --------- | ------------------ |
| <code>try</code>     | 예외가 발생할 수 있는 코드 블록 |
| <code>except</code>  | 예외 발생 시 실행할 코드     |
| <code>else</code>    | 예외가 발생하지 않았을 때 실행  |
| <code>finally</code> | 무조건 실행되는 코드 블록     |
| <code>raise</code>   | 직접 예외를 발생시킴        |
| 사용자 정의 예외 | 예외 상황을 커스터마이징      |</p>
<p>다음 편에서는 Python의 핵심 개념 중 하나인 객체지향 프로그래밍을 학습해보겠습니다.</p>
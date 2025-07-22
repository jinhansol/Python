<h2 id="61-연산자란">6.1 연산자란?</h2>
<p><strong>연산자(opator)</strong>는 값을 계산하거나 비교하기 위해 사용하는 기호 또는 키워드입니다.
Python은 다양한 연산자를 제공하며, 연산자에 따라 수행하는 동작이 달라집니다.</p>
<hr />
<h2 id="62-산술-연산자arithmetic-operators">6.2 산술 연산자(Arithmetic Operators)</h2>
<table>
<thead>
<tr>
<th>연산자</th>
<th>설명</th>
<th>예시</th>
<th>결과</th>
</tr>
</thead>
<tbody><tr>
<td><code>+</code></td>
<td>덧셈</td>
<td><code>3 + 2</code></td>
<td><code>5</code></td>
</tr>
<tr>
<td><code>-</code></td>
<td>뺄셈</td>
<td><code>5 - 2</code></td>
<td><code>3</code></td>
</tr>
<tr>
<td><code>*</code></td>
<td>곱셈</td>
<td><code>4 * 2</code></td>
<td><code>8</code></td>
</tr>
<tr>
<td><code>/</code></td>
<td>나눗셈 (실수)</td>
<td><code>5 / 2</code></td>
<td><code>2.5</code></td>
</tr>
<tr>
<td><code>//</code></td>
<td>정수 나눗셈</td>
<td><code>5 // 2</code></td>
<td><code>2</code></td>
</tr>
<tr>
<td><code>%</code></td>
<td>나머지</td>
<td><code>5 % 2</code></td>
<td><code>1</code></td>
</tr>
<tr>
<td><code>**</code></td>
<td>거듭제곱</td>
<td><code>2 ** 3</code></td>
<td><code>8</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="63-비교-연산자comparison-operators">6.3 비교 연산자(Comparison Operators)</h2>
<table>
<thead>
<tr>
<th>연산자</th>
<th>설명</th>
<th>예시</th>
<th>결과</th>
</tr>
</thead>
<tbody><tr>
<td><code>==</code></td>
<td>같음</td>
<td><code>3 == 3</code></td>
<td>True</td>
</tr>
<tr>
<td><code>!=</code></td>
<td>다름</td>
<td><code>3 != 2</code></td>
<td>True</td>
</tr>
<tr>
<td><code>&lt;</code></td>
<td>작다</td>
<td><code>2 &lt; 3</code></td>
<td>True</td>
</tr>
<tr>
<td><code>&lt;=</code></td>
<td>작거나 같다</td>
<td><code>3 &lt;= 3</code></td>
<td>True</td>
</tr>
<tr>
<td><code>&gt;</code></td>
<td>크다</td>
<td><code>5 &gt; 3</code></td>
<td>True</td>
</tr>
<tr>
<td><code>&gt;=</code></td>
<td>크거나 같다</td>
<td><code>5 &gt;= 7</code></td>
<td>False</td>
</tr>
</tbody></table>
<hr />
<h2 id="64-논리-연산자logical-operators">6.4 논리 연산자(Logical Operators)</h2>
<table>
<thead>
<tr>
<th>연산자</th>
<th>설명</th>
<th>예시</th>
<th>결과</th>
</tr>
</thead>
<tbody><tr>
<td><code>and</code></td>
<td>모두 참일 때</td>
<td><code>True and True</code></td>
<td>True</td>
</tr>
<tr>
<td><code>or</code></td>
<td>둘 중 하나 참</td>
<td><code>False or True</code></td>
<td>True</td>
</tr>
<tr>
<td><code>not</code></td>
<td>부정</td>
<td><code>not True</code></td>
<td>False</td>
</tr>
</tbody></table>
<hr />
<h2 id="65-비트-연산자bitwise-operators">6.5 비트 연산자(Bitwise Operators)</h2>
<table>
<thead>
<tr>
<th>연산자</th>
<th>설명</th>
<th>예시</th>
<th>결과</th>
<th></th>
<th></th>
</tr>
</thead>
<tbody><tr>
<td><code>&amp;</code></td>
<td>비트 AND</td>
<td><code>5 &amp; 3</code> → <code>101 &amp; 011</code> → <code>001</code> → <code>1</code></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td>`</td>
<td>`</td>
<td>비트 OR</td>
<td>`5</td>
<td>3<code>→</code>101</td>
<td>011<code>→</code>111<code>→</code>7`</td>
</tr>
<tr>
<td><code>^</code></td>
<td>비트 XOR</td>
<td><code>5 ^ 3</code> → <code>101 ^ 011</code> → <code>110</code> → <code>6</code></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>~</code></td>
<td>비트 NOT</td>
<td><code>~5</code> → <code>-6</code> (보수 연산)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>&lt;&lt;</code></td>
<td>왼쪽 시프트</td>
<td><code>5 &lt;&lt; 1</code> → <code>10</code></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td><code>&gt;&gt;</code></td>
<td>오른쪽 시프트</td>
<td><code>5 &gt;&gt; 1</code> → <code>2</code></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody></table>
<hr />
<h2 id="66-할당-연산자assignment-operators">6.6 할당 연산자(Assignment Operators)</h2>
<table>
<thead>
<tr>
<th>연산자</th>
<th>예시</th>
<th>동작</th>
</tr>
</thead>
<tbody><tr>
<td><code>=</code></td>
<td><code>x = 5</code></td>
<td>오른쪽 값을 왼쪽에 대입</td>
</tr>
<tr>
<td><code>+=</code></td>
<td><code>x += 1</code></td>
<td><code>x = x + 1</code>과 같음</td>
</tr>
<tr>
<td><code>-=</code></td>
<td><code>x -= 1</code></td>
<td><code>x = x - 1</code></td>
</tr>
<tr>
<td><code>*=</code></td>
<td><code>x *= 2</code></td>
<td><code>x = x * 2</code></td>
</tr>
<tr>
<td><code>/=</code></td>
<td><code>x /= 3</code></td>
<td><code>x = x / 3</code></td>
</tr>
<tr>
<td><code>//=</code></td>
<td><code>x //= 2</code></td>
<td><code>x = x // 2</code></td>
</tr>
<tr>
<td><code>%=</code></td>
<td><code>x %= 4</code></td>
<td><code>x = x % 4</code></td>
</tr>
<tr>
<td><code>**=</code></td>
<td><code>x **= 2</code></td>
<td><code>x = x ** 2</code></td>
</tr>
</tbody></table>
<hr />
<h2 id="67-항등-연산자identiry-operators">6.7 항등 연산자(Identiry Operators)</h2>
<table>
<thead>
<tr>
<th>연산자</th>
<th>설명</th>
<th>예시</th>
<th>결과</th>
</tr>
</thead>
<tbody><tr>
<td><code>is</code></td>
<td>객체 주소(참조)가 같으면 True</td>
<td><code>a is b</code></td>
<td>True / False</td>
</tr>
<tr>
<td><code>is not</code></td>
<td>객체 주소가 다르면 True</td>
<td><code>a is not b</code></td>
<td>True / False</td>
</tr>
</tbody></table>
<hr />
<h2 id="68-연산자-우선순위operator-precedence">6.8 연산자 우선순위(Operator Precedence)</h2>
<p>Python에서는 여러 연산자가 한 줄에 있을 경우 우선순위(priority)에 따라 계산됩니다.
| 우선순위 | 연산자                                                |    |
| ---- | -------------------------------------------------- | -- |
| 1    | <code>()</code> 괄호                                            |    |
| 2    | <code>**</code> (거듭제곱)                                        |    |
| 3    | <code>+x</code>, <code>-x</code>, <code>~x</code> (단항 연산)                           |    |
| 4    | <code>*</code>, <code>/</code>, <code>//</code>, <code>%</code>                                |    |
| 5    | <code>+</code>, <code>-</code>                                           |    |
| 6    | <code>&lt;&lt;</code>, <code>&gt;&gt;</code>                                         |    |
| 7    | <code>&amp;</code>                                                |    |
| 8    | <code>^</code>                                                |    |
| 9    | `                                                 | ` |
| 10   | 비교: <code>==</code>, <code>!=</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&lt;=</code>, <code>&gt;=</code>, <code>is</code>, <code>in</code> 등 |    |
| 11   | <code>not</code>                                              |    |
| 12   | <code>and</code>                                              |    |
| 13   | <code>or</code>                                               |    |
| 14   | <code>=</code>, <code>+=</code>, <code>-=</code> 등 (할당)                             |    |</p>
<hr />
<h2 id="69-단축-평가short-circuit-evaluation">6.9 단축 평가(Short-circuit Evaluation)</h2>
<p>Python의 논리 연산자 and,or는 왼쪽 피연산자에 따라 오른쪽을 평가하지 않을 수 있습니다.</p>
<ul>
<li>and: 왼쪽이 False면, 전체 결과는 무조건 False -&gt; 오른쪽 평가 생략</li>
<li>or: 왼쪽이 True면, 전체 결과는 무조건 True -&gt; 오른쪽 평가 생략</li>
</ul>
<pre><code>Python

def check():
    print(&quot;check() 호출됨&quot;)
    return True

print(False and check())    #check() 호출되지 않음
print(True or check())        #check() 호출되지 않음</code></pre><hr />
<h4 id="마무리">마무리</h4>
<p>이번 7편에서는 Python의 다양한 연산자와 그 우선순위, 평가 방식까지 상세히 다뤄보았습니다.
다음 편에서는 <strong>조건문과 반복문 제어 흐름</strong>에 대해서 학습해 보겠습니다.</p>
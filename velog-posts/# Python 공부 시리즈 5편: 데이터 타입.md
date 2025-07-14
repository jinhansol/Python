<h2 id="51-숫자형-int-float-complex--decimal-fractions-모듈">5.1 숫자형 (int, float, complex) &amp; 'decimal', 'fractions' 모듈</h2>
<h3 id="정수형-int">정수형 (int)</h3>
<ul>
<li><p><strong>설명</strong> : 소수점 없는 정수, 메모리 한도 내에서 무제한 정밀도 지원.</p>
</li>
<li><p><strong>리터럴</strong></p>
<pre><code>Python

a = 123        # 10진수
b = 0b1010        # 이진(2진수) -&gt; 10
c = 0o17        # 8진수 -&gt; 15
d = 0xFF        # 16진수 -&gt; 255</code></pre><ul>
<li>특징<ul>
<li>type(a) -&gt; &lt;class 'int'&gt;</li>
<li>사칙연산, 비교 연산, 비트 연산 지원</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3 id="부동소수점형float">부동소수점형(float)</h3>
<ul>
<li><p>설명 : 소수점을 포함한 실수. IEEE-754 표준의 배정밀도(double) 사용.</p>
</li>
<li><p>리터럴 &amp; 지수 표기법</p>
<pre><code>Python

x = 3.14
y = 1.5e2
z = -0.005</code></pre></li>
<li><p>특징</p>
<ul>
<li>type(x) -&gt; &lt;class 'float'&gt;</li>
<li>정밀도 한계(0.1+0.2 != 0.3)</li>
<li>round(), math.isclose()로 오차 처리</li>
</ul>
</li>
</ul>
<h3 id="복소수형complex">복소수형(complex)</h3>
<ul>
<li><p>설명 : 실수부와 허수부로 구성된 수.</p>
</li>
<li><p>리터럴</p>
<pre><code>Python

c1 = 2 + 3j
c2 = complex(1,-1)</code></pre></li>
<li><p>속성</p>
<ul>
<li>c1.real -&gt; 실수부 (2.0)</li>
<li>c1.imag -&gt; 허수부 (3.0)</li>
</ul>
</li>
</ul>
<h3 id="decimal-모듈">decimal 모듈</h3>
<ul>
<li><p>목적 : 금융 계산 등 정밀한 소수 연산이 필요할 때 사용</p>
</li>
<li><p>사용법</p>
<pre><code>Python

from decimal import Decimal, getcontext
getcontext().prex = 28
d1 = Decimal('0.1')
d2 = Decimal('0,2')
print(d1 + d2)</code></pre></li>
</ul>
<h3 id="fractions-모듈">fractions 모듈</h3>
<ul>
<li><p>목적: 정수 분수 형태로 수를 표현, 정확한 유리수 연산 지원</p>
</li>
<li><p>사용법</p>
<pre><code>Python

from fractions import Fraction
f1 = Fraction(1, 3)
f2 = Fraction(2, 5)
print(f1 + f2)            # Fraction(11, 15)
print(float(f1 + f2)    # 0.7333333333</code></pre></li>
</ul>
<hr />
<h2 id="52-시퀸스-타입-list-tuple-string">5.2 시퀸스 타입: list, tuple, string</h2>
<h3 id="리스트list">리스트(list)</h3>
<ul>
<li><p>설명 : 순서가 있고, <strong>가변(mutable)</strong>한 컬렉션</p>
</li>
<li><p>생성</p>
<pre><code>Python

fruits = ['apple', 'banana', 'cherry']
nums = [1, 2, 3, 4, 5]</code></pre></li>
<li><p>인덱싱 &amp; 슬라이싱</p>
<pre><code>Python

fruits[0]        #'apple'
nums[1:4]        #[2,3,4]</code></pre></li>
<li><p>주요 메서드</p>
<ul>
<li>append(), extend(), insert(), remove(), pop(), sort(), reverse(), clear()</li>
</ul>
</li>
</ul>
<h3 id="튜플tuple">튜플(tuple)</h3>
<ul>
<li><p>설명 : 순서가 있고, <strong>불변(immutable)</strong>한 컬렉션</p>
</li>
<li><p>생성</p>
<pre><code>Python

coords = (10, 20)
single = (5,)        #한 요소일 때도 쉼표 필요</code></pre></li>
<li><p>특징</p>
<ul>
<li>요소 변경 불가 -&gt; 안전한 참조</li>
<li>리스트보다 메모리 효율이 좋음</li>
</ul>
</li>
<li><p>언패킹</p>
<pre><code>Python

x, y = coords</code></pre></li>
</ul>
<h3 id="문자열-str">문자열 (str)</h3>
<ul>
<li>설명 : 문자들의 순서 있는 불변 시퀸스</li>
<li>생성<pre><code>Python
</code></pre></li>
</ul>
<p>s1 = &quot;Hello, Python!&quot;
s2 = 'kopo'</p>
<pre><code>- 인덱싱 &amp; 슬라이싱</code></pre><p>Python</p>
<p>s1[0]        #'H'
s1[7:13]    #'Python'</p>
<pre><code>- 주요 메서드
  - upper(), lower(), split(), join(), replace(),
startswith(), find(), format(), f-string

---

## 5.3 집합(set) &amp; 사전(dict)

### 집합(set)
 - 설명 : 순서 없고, 중복 제거 되는 가변 컬렉션
 - 생성</code></pre><p> Python</p>
<p>primes = {2, 3, 5, 7}
s = set([1, 2, 2, 3])  # {1, 2, 3}</p>
<pre><code> - 주요 연산
   - 합집합: | 또는 union()
   - 교집합: &amp; 또는 intersection()
   - 차집합: - 또는 difference()
   - 대칭차집합: ^ 또는 symmetric_difference()
 - 메서드
   - add(), remove(), discard(), pop(), clear()

### 사전(dict)
 - 설명 : 키(key)와 값(value)의 쌍을 저장하는 **매핑(mapping)**
 - 생성</code></pre><p> Python</p>
<p> person = {'name': 'Alice', 'age': 30}
 d = dict(x=1, y=2)</p>
<pre><code> - 접근 &amp; 변경</code></pre><p> Python</p>
<p> person['name'] = 'Bob'      # 값 변경
 email = person.get('email', 'N/A')  # 키 없으면 기본값</p>
<pre><code> - 반복</code></pre><p> Python</p>
<p> for key in person:         # key 반복
    print(key, person[key])
for k, v in person.items():# 키, 값 동시에
    print(k, v)</p>
<pre><code> - 컴프리헨션</code></pre><p> Python</p>
<p> squares = {i: i*i for i in range(1, 6)}</p>
<p> ```</p>
<hr />
<p>6편에서는 내장 숫자형, 정밀 연산 모듈, 시퀀스 타입과 컬렉션 타입을 폭넓게 다뤘습니다.
다음 7편에서는 연산자 &amp; 표현식, 흐름 제어를 학습합니다!</p>
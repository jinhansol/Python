<h3 id="41-변수와-상수-선언">4.1 변수와 상수 선언</h3>
<p>Python은 <strong>동적 타이핑</strong> 언어이기 때문에, 변수 선언 시 타입을 명시할 필요가 없으며 <code>=</code> 연산자로 언제든지 값을 재할당할 수 있습니다.
변수는 메모리에 저장된 객체를 가리키는 이름(name)이며, 모든 값은 객체(object)입니다.</p>
<pre><code>python

#기본 할당
a = 10        #int 객체 생성 후 a가 참조
b = 5.2        #float 객체 생성 후 b가 참조
c = &quot;kopo&quot;  #str 객체 생성 후 c가 참조

#다중 할당
x, y, z = 1, 2, 3

#체인 할당(모두 같은 객체를 참조)
m = n = o = 100</code></pre><ul>
<li>상수(Constant) : Python에 언어 차원의 상수 문법은 없지만, 변경하지 않을 값은 모두 대문자 + 밑줄 표기 관례를 따릅니다.<pre><code>python
</code></pre></li>
</ul>
<p>PI = 3.14159
MAX_RETRY = 5</p>
<pre><code>실제로 재할당은 가능하므로, &quot;변경 금지&quot;는 개발자 간 약속입니다.

---

## 4.2 리터럴 : 숫자, 문자열, 불리언, None
리터럴(Literal)은 소스 코드에 직접 쓰인 &quot;원시 데이터&quot;를 가리킵니다.

#### 숫자형 리터럴</code></pre><p>Python</p>
<p>a = 0b1010       # 이진 리터럴 → 10
b = 100          # 십진 리터럴
c = 0o310        # 8진 리터럴 → 200
d = 0x12c        # 16진 리터럴 → 300
f1 = 10.5        # 부동소수점 리터럴
f2 = 1.5e2       # 지수 표기법 → 150.0
z = 3.14j        # 복소수 리터럴</p>
<pre><code>
#### 문자열 리터럴</code></pre><p>Python</p>
<p>s1 = &quot;Hello, Python&quot;               # 작은/큰따옴표
s2 = 'kopo'                        # 한 글자도 str
s3 = &quot;&quot;&quot;여러 줄
문자열 예제&quot;&quot;&quot;                      # 멀티라인 문자열
s4 = r&quot;raw \n string&quot;              # 원시 문자열 (이스케이프 무시)
s5 = u&quot;\u00dcnic\u00f6de&quot;          # 유니코드 리터럴</p>
<pre><code>
#### 불리언 &amp; None</code></pre><p>Python</p>
<p>flag = True                        # True, False
nothing = None                     # 값 없음 표시</p>
<pre><code>
- True는 내부적으로 1, False는 0으로 취급되기도 합니다.

---
## 4.3 컬렉션 리터럴(list, tuple, dict, set)
Python의 주요 컬렉션 타입들은 모두 리터럴 문법을 제공합니다.

#### 리스트(List)
 - 선언 : 대괄호 [ ] 내부에 쉼표로 구분하여 요소 나열
 - 특징 : 순서 유지, 변경 가능(mutable), 다양한 메서드 지원</code></pre><p>Python</p>
<p>fruits = [&quot;apple&quot;, &quot;mango&quot;, &quot;orange&quot;]
print(fruits[0])         # apple
fruits.append(&quot;banana&quot;)  # [&quot;apple&quot;,&quot;mango&quot;,&quot;orange&quot;,&quot;banana&quot;]
fruits[1:3] = [&quot;kiwi&quot;]   # 슬라이싱으로 치환</p>
<pre><code>- 주요 메서드 : append(), extend(), insert(), remove(), pop(), sort(), reverse()

#### 튜플(Tuple)
- 선언 : 소괄호( ) 또는 쉼표만으로도 가능
- 특징 : 키-값 쌍 저장, 순서 유지, 검색 최적화</code></pre><p>Python</p>
<p>coords = (10, 20)</p>
<h1 id="coords0--5-----typeerror-튜플은-재할당-불가">coords[0] = 5    # TypeError: 튜플은 재할당 불가</h1>
<p>nested = (1, 2, [3, 4])
nested[2].append(5)      # 내부 리스트는 변경 가능</p>
<pre><code>- 재할당 : 전체 객체를 새 튜플로 교체 가능

#### 사전(Dictionary)
- 선언 : 중괄호 { key: value, ... }
- 특징 : 키-값 쌍 저장, 순서 유지, 검색 최적화</code></pre><p>Python</p>
<p>person = {&quot;name&quot;: &quot;Jack&quot;, &quot;age&quot;: 26}
print(person[&quot;name&quot;])          # Jack
print(person.get(&quot;email&quot;))     # None (KeyError 방지)
person[&quot;age&quot;] = 27             # 값 변경
person[&quot;city&quot;] = &quot;Seoul&quot;       # 새 키 추가</p>
<pre><code>-생성 방법: dict(), 리스트 튜플 페어, 딕셔너리 컴프리헨션</code></pre><p>python</p>
<p>squares = {i: i*i for i in range(1, 6)}</p>
<pre><code>
#### 집합(Set)
- 선언 : 중괄호 {1, 2, 3} 또는 set( )
- 특징 : 중복 제거, 순서 없음, 변경 가능</code></pre><p>Python</p>
<p>vowels = {&quot;a&quot;, &quot;e&quot;, &quot;i&quot;, &quot;o&quot;, &quot;u&quot;}
vowels.add(&quot;y&quot;)               # 요소 추가
vowels.update([&quot;a&quot;, &quot;i&quot;])     # 중복은 자동 제거
vowels.remove(&quot;e&quot;)            # 요소 삭제</p>
<p>```</p>
<ul>
<li>연산 : 합칩합( | ), 교집합(&amp;), 차집합(-), 대칭차집합(^)</li>
<li>주요 함수: len(), any(), all(), sorted(), sum()</li>
</ul>
<hr />
<p>다음은 5편 데이터 타입에 대해서 알아보도록 하겟습니다.</p>
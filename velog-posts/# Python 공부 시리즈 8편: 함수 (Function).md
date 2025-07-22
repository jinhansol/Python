<h2 id="81-함수-정의--호출-return">8.1 함수 정의 &amp; 호출, return</h2>
<h3 id="함수-정의-def">함수 정의 (def)</h3>
<pre><code>python

def greet():
    print(&quot;Hello, Python!&quot;)</code></pre><ul>
<li>def 키워드로 함수를 정의합니다.</li>
<li>greet는 함수 이름이며, 괄호 안은 매개변수(parameter) 자리입니다.</li>
</ul>
<hr />
<h3 id="함수-호출">함수 호출</h3>
<pre><code>python

greet()</code></pre><hr />
<h3 id="return-문">return 문</h3>
<pre><code>python

def add(a, b):
    return a + b

result = add(3, 5)
print(result)</code></pre><ul>
<li>return을 사용해 값을 반환할 수 있으며, 반환값은 변수에 저장하거나 다른 함수에서 활용됩니다.</li>
</ul>
<hr />
<h2 id="82-매개변수--반환값-종류">8.2 매개변수 &amp; 반환값 종류</h2>
<p>Python 함수는 다양한 방식으로 <strong>인자(argument)</strong>를 받을 수 있습니다.</p>
<hr />
<h3 id="위치인자positional-argument">위치인자(Positional Argument)</h3>
<ul>
<li>인자의 순서가 중요합니다.<pre><code>python
</code></pre></li>
</ul>
<p>def info(name, age):
    print(f&quot;{name}은 {age}살입니다.&quot;)</p>
<p>info(&quot;Alice&quot;, 30)</p>
<pre><code>
### 기본값 인자(Default Argument)
 - 인자에 기본값을 미리 지정할 수 있습니다.</code></pre><p>python</p>
<p>def greet(name=&quot;python&quot;):
    print(f&quot;Hello, {name}!&quot;)</p>
<p>greet()            #Hello, Python!
greet(&quot;Alice&quot;)    #Hello, Alice!</p>
<pre><code>
### 키워드 인자(Keyword Argument)
 - 인자 이름을 명시하여 순서를 무시하고 값을 전달할 수 있습니다.</code></pre><p>python</p>
<p>def student(name, grade):
    print(f&quot;{name}의 성적은 {grade}입니다.&quot;)</p>
<p>student(grade=&quot;A+&quot;, name=&quot;Bob&quot;)</p>
<pre><code>
### 가변 인자(*args, **kwargs)
#### *args(튜플 형태로 여러 인자 받기)</code></pre><p>python</p>
<p>def total(*numbers):
    print(numbers)
    print(sum(numbers))</p>
<p>total(1,2,3,4)</p>
<pre><code> - 인자의 개수가 가변적일 때 사용(튜플로 전달됨)

#### **kwargs(딕셔너리 형태로 키워드 인자 받기)</code></pre><p>python</p>
<p>def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f&quot;{key} : {value}&quot;)</p>
<p>print_info(name=&quot;Alice&quot;, age=25)</p>
<pre><code> - 키워드 인자를 딕셔너리로 전달받을 수 있습니다.

---

## 8.3 익명 함수(lambda), 재귀(Recursion)

### lambda함수 (익명 함수)
 - 이름 없이 사용하는 간단한 함수
 - lambda 인자: 표현식 형태
</code></pre><p>python</p>
<p>square = lambda X: X ** 2
print(square(4))    # 16</p>
<pre><code>
 - 보통 한 줄짜리 계산 함수에 사용됩니다.
 - map(), filter(), sorted()와 자주 함께 사용됩니다.</code></pre><p>python</p>
<p>nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print(squares)    #[1, 3, 9, 16]</p>
<pre><code>
### 재귀 함수(Recursion)
 - 함수 내에서 자기 자신을 호출하는 함수</code></pre><p>python</p>
<p>def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)</p>
<p>print(factorial(5))</p>
<pre><code> - 종료 조건을 명확히 지정하지 않으면 무한 루프 발생에 주의해야 합니다.

---

#### 9.4 스코프(Scope): Global, Local, Nonlocal

### 지역변수(Local Variable)
 - 함수 내부에서 정의된 변수는 그 함수 안에서만 유효</code></pre><p>python</p>
<p>def example():
    x = 10
    print(x)</p>
<p>example()</p>
<pre><code>
### 전역변수(Global Variable)
 - 함수 밖에서 정의된 변수는 전체 코드에서 사용 가능</code></pre><p>python</p>
<p>x = 100</p>
<p>def show():
    print(x)</p>
<p>show()</p>
<pre><code>
### nonlocal 키워드(중첩 함수에서 바깥 함수의 지역 변수 수정)</code></pre><p>python</p>
<p>def outer():
    x = &quot;outer&quot;</p>
<pre><code>def inner():
    nonlocal x
    x = &quot;inner&quot;</code></pre><pre><code> - nonlocal은 바깥쪽 지역 스코프의 변수에 접근할 때 사용됩니다.

---

**요약정리**
| 구분          | 설명                   |
| ----------- | -------------------- |
| `def`       | 함수 정의 키워드            |
| `return`    | 함수의 결과값 반환           |
| `*args`     | 가변 위치 인자 (튜플로 전달)    |
| `**kwargs`  | 가변 키워드 인자 (딕셔너리로 전달) |
| `lambda`    | 익명 함수                |
| `global`    | 전역 변수 수정             |
| `nonlocal`  | 바깥 함수의 지역 변수 수정      |
| `recursion` | 함수가 자기 자신을 호출        |


---

#### 마무리

이번 편에서는 Python의 함수 정의 및 호출, 인자 처리 방식, 익명 함수와 재귀, 그리고 스코프의 개념까지 함수에 대한 핵심적인 내용을 정리했습니다.

다음 편에서는 Python의 예외처리에 대해 공부해보겠습니다.</code></pre>
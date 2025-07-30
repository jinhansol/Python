<p>Python은 <strong>객체 지향 프로그래밍(Object-Oriented Programming)</strong> 을 완전하게 지원합니다.<br />OOP는 <strong>코드를 재사용하고, 확장하며, 유지보수를 쉽게</strong> 만들기 위한 핵심 프로그래밍 패러다임입니다.</p>
<hr />
<ul>
<li>클래스 &amp; 인스턴스</li>
<li>속성(attribute) &amp; 메서드(method)</li>
<li>상속, 다향성, 캡슐화</li>
<li>매직 메서드 (<code>__init__</code>, <code>__str__</code> 등)</li>
</ul>
<hr />
<h2 id="1-클래스class와-인스턴스instance">1. 클래스(Class)와 인스턴스(Instance)</h2>
<h3 id="클래스란">클래스란?</h3>
<ul>
<li><p>객체를 생성하기 위한 <strong>설계도</strong></p>
</li>
<li><p>속성(데이터)과 메서드(기능)를 정의함</p>
<pre><code>python

class Dog:
  def bark(self):
     print(&quot;멍멍!&quot;)</code></pre></li>
<li><p>인스턴스란?</p>
<ul>
<li>클래스를 실제로 사용하기 위해 만든 객체<pre><code>python
</code></pre></li>
</ul>
</li>
</ul>
<p>dog1 = Dog()
dog1.bark()</p>
<pre><code>
---

## 2. 속성(Attribute)과 메서드(Method)

### 인스턴스 속성</code></pre><p>python</p>
<p>class Dog:
    def <strong>init</strong>(self, name):
        self.name = name</p>
<pre><code>def bark(self):
    print(f&quot;{self.name}이(가) 멍멍 짖습니다.&quot;)</code></pre><p>dog = Dog(&quot;초코&quot;)
dog.bark()</p>
<pre><code>
 - __init__은 객체 초기화 시 호출되는 생성자(Constructor)
 - self.name은 해당 객체 고유의 속성

### 클래스 속성(공통 속성)</code></pre><p>python</p>
<p>class Dog:
    species = &quot;Canine&quot;</p>
<pre><code>def __init__(self, name):
    self.name = name</code></pre><p>dog = Dog(&quot;바둑이&quot;)
print(dog.species)</p>
<pre><code>
---

## 3. 상속(Inheritance)
 - 기존 클래스의 속성과 메서드를 물려받는 방식</code></pre><p>python</p>
<p>class Animal:
    def sound(self):
        print(&quot;소리를 냅니다.&quot;)</p>
<p>class Dog(Animal):
    def sound(self):
        print(&quot;멍멍!&quot;)</p>
<p>dog = Dog()
dog.sound()  # 멍멍!</p>
<pre><code> - Dog 클래스는 Animal을 상속
 - 오버라이딩(Overriding)으로 메서드 재정의 가능

---

## 4. 다형성(Polumorphism)
 - 같은 메서드명이 서로 다른 동작을 수행하도록 하는 능력</code></pre><p>python</p>
<p>animals = [Dog(), Animal()]</p>
<p>for animal in animals:
    animal.sound()</p>
<pre><code> - 각 클래스의 sound() 메서드는 동일한 이름이지만 다르게 동작

---

## 5. 캡슐화(Encapsulation)
 - 외부에서 직접 접근하지 못하도록 보호
 - 보통 변수 앞에 _ 또는 __를 붙여 사용
</code></pre><p>python</p>
<p>class Account:
    def <strong>init</strong>(self, balance):
        self.__balance = balance  # 비공개 변수</p>
<pre><code>def deposit(self, amount):
    self.__balance += amount

def get_balance(self):
    return self.__balance</code></pre><p>acc = Account(1000)
acc.deposit(500)
print(acc.get_balance())  # 1500</p>
<h1 id="printacc__balance---attributeerror-발생">print(acc.__balance)  # AttributeError 발생</h1>
<pre><code>
---

## 6. 매직 메서드(Magic Methods, dunder methods)
 - Python 클래스는 특별한 역할을 하는 매직 메서드를 지원합니다.

 | 메서드명                   | 역할              |
| ---------------------- | --------------- |
| `__init__(self, ...)`  | 생성자             |
| `__str__(self)`        | 문자열 표현 반환       |
| `__len__(self)`        | `len()` 사용 시 호출 |
| `__eq__(self, other)`  | 비교 연산자 `==` 정의  |
| `__add__(self, other)` | `+` 연산자 동작 정의   |

</code></pre><p>python</p>
<p>class Person:
    def <strong>init</strong>(self, name):
        self.name = name</p>
<pre><code>def __str__(self):
    return f&quot;이름: {self.name}&quot;</code></pre><p>p = Person(&quot;한솔&quot;)
print(p)  # 이름: 한솔</p>
<p>```</p>
<hr />
<h4 id="정리-클래스-설계-요령">정리: 클래스 설계 요령</h4>
<ul>
<li>상태(state) : 인스턴스 속성으로 표현(self.name, self.age 등)</li>
<li>행동(behavior) : 메서드로 구현 (bark(), run() 등)</li>
<li>접근 제한 : _비공개, __엄격히 비공개</li>
<li>확장성 : 상속으로 기능 확장</li>
<li>재사용성 : 공통 기능은 상위 클래스에 구현</li>
</ul>
<hr />
<p><strong>마무리</strong>
이번 편에서는 Python의 객체지향 개념을 정리했습니다.
| 핵심 용어  | 설명                                      |
| ------ | --------------------------------------- |
| 클래스    | 객체의 설계도                                 |
| 인스턴스   | 클래스 기반으로 생성된 실제 객체                      |
| 속성     | 객체가 가진 데이터 (변수)                         |
| 메서드    | 객체가 할 수 있는 동작 (함수)                      |
| 상속     | 기존 클래스를 확장                              |
| 다형성    | 동일한 메서드 이름, 다른 동작                       |
| 캡슐화    | 내부 구현 숨기기 (<code>__변수</code>)                      |
| 매직 메서드 | 클래스 동작 커스터마이징 (<code>__init__</code>, <code>__str__</code> 등) |</p>
<p>0편 부터 13편까지의 내용을 정리하면서 파이썬에 대해서 자세히 공부할 수 있는 기회가 되었습니다. 다음에는 또 다른 내용을 가지고 정리하는 시간을 가져보도록 하겠습니다.</p>
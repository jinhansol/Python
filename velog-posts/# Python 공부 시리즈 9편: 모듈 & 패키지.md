<p>Python은 모듈(module)과 패키지(package)를 통해 <strong>코드를 논리적으로 분리하고 재사용</strong>할 수 있게 해줍니다.</p>
<hr />
<h2 id="91-import-fromimportas-키워드">9.1 <code>import</code>, <code>from...import...</code>,<code>as</code> 키워드</h2>
<h3 id="import">import</h3>
<p>다른 파이썬 파일(모듈)의 모든 기능을 가져올 때 사용합니다.</p>
<pre><code>python

import math

print(math.sqrt(16))    #4.0</code></pre><ul>
<li>math 모듈 전체를 가져오며, 사용할 때는 math. 접두어가 필요합니다.</li>
</ul>
<hr />
<h3 id="from--import">from ... import...</h3>
<p>모듈 내 특정 함수나 클래스만 선택적으로 가져올 수 잇습니다.</p>
<pre><code>python

from math import sqrt

print(sqrt(25))    #5.0</code></pre><ul>
<li>sqrt()를 바로 사용할 수 있습니다.</li>
</ul>
<hr />
<h3 id="as별칭">as(별칭)</h3>
<p>모듈이나 함수 이름이 길거나 이름 충돌이 날 때 별칭(alias)을 지정합니다.</p>
<pre><code>python

import numpy as np
form math import factorial as fact

print(np.array([1, 2, 3]))
print(fact(5))    # 120</code></pre><hr />
<h2 id="92-모듈-검색-경로syspath-reload">9.2 모듈 검색 경로(sys.path), reload()</h2>
<h3 id="syspath---모듈을-어디서-찾는가">sys.path - 모듈을 어디서 찾는가?</h3>
<p>Python은 모듈을 로딩할 때 여러 디렉토리를 순차적으로 탐색합니다. 이 경로들을 확인하려면 sys 모듈의 path 속성을 확인합니다.</p>
<pre><code>python

import sys

for p in sys.path:
    print(p)</code></pre><p>출력 결과에는 현재 디렉토리, 표준 라이브러리 경로, site-package 등이 포함됩니다.</p>
<hr />
<h3 id="모듈-수정-후-다시-불러오기---importlibreload">모듈 수정 후 다시 불러오기 - importlib.reload()</h3>
<p>한 번 import된 모듈은 재시작 전까지 다시 로딩되지 않음. 수정한 내용을 반영하려면 importlib.reload()</p>
<pre><code>python

import my_module
import importlib

importlib.reload(my_module)</code></pre><ul>
<li>주로 Jupyter Notebook이나 대화형 환경에서 유용합니다.</li>
</ul>
<hr />
<h2 id="93-dir로-네임스페이스-확인-패키지-구조">9.3 dir()로 네임스페이스 확인, 패키지 구조</h2>
<h3 id="dir-현재-네임스페이스의-변수-및-객체-확인">dir(): 현재 네임스페이스의 변수 및 객체 확인</h3>
<pre><code>python

import math

print(dir(math))</code></pre><ul>
<li>해당 모듈에 어떤 함수/클래스/변수들이 포함되어 있는지 확인할 수 있습니다.</li>
</ul>
<pre><code>python

x = 10
y = [1, 2, 3]

print(dir())</code></pre><hr />
<h3 id="패키지란">패키지란?</h3>
<ul>
<li>여러 모듈을 포함하는 폴더 단위의 구조입니다.</li>
<li>폴더 안에 <strong>init</strong>.py 파일이 있으면 Python은 해당 폴더를 패키지로 인식합니다.</li>
</ul>
<p>예시 구조:
my_package/
│
├── <strong>init</strong>.py
├── module1.py
├── module2.py</p>
<hr />
<h3 id="패키지-사용법">패키지 사용법</h3>
<pre><code>python

# 구조: my_package/module1.py

from my_package import module1

module1.my_function()</code></pre><p>또는 모듈 내 개별 함수만 가져올 수도 있습니다.</p>
<pre><code>python

from my_package.module1 import my_function

my_function()</code></pre><hr />
<h2 id="마무리-요약">마무리 요약</h2>
<table>
<thead>
<tr>
<th>키워드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>import</code></td>
<td>전체 모듈 가져오기</td>
</tr>
<tr>
<td><code>from import</code></td>
<td>모듈 내 일부 요소만 가져오기</td>
</tr>
<tr>
<td><code>as</code></td>
<td>별칭 지정</td>
</tr>
<tr>
<td><code>sys.path</code></td>
<td>모듈 탐색 경로</td>
</tr>
<tr>
<td><code>reload()</code></td>
<td>수정된 모듈 다시 불러오기</td>
</tr>
<tr>
<td><code>dir()</code></td>
<td>객체/모듈에 포함된 이름 리스트 확인</td>
</tr>
<tr>
<td><code>패키지</code></td>
<td>모듈들을 디렉토리로 구조화한 형태</td>
</tr>
</tbody></table>
<hr />
<p><strong>마무리</strong>
이번에는 모듈&amp;시리즈에 대해서 학습하였습니다. 다음 시리즈에서는 예외처리를 중심으로 학습해보겠습니다.</p>
<p>Python은 별도의 설치 없이 사용할 수 있는 <strong>강력한 표준 라이브러리</strong>를 제공합니다.</p>
<ul>
<li>수학 계산: <code>math</code></li>
<li>난수 생성: <code>random</code></li>
<li>날짜와 시간 처리: <code>datetime</code></li>
<li>운영체제와 상호작용: <code>os</code>, <code>sys</code></li>
</ul>
<hr />
<h2 id="1-수학-모듈-math">1. 수학 모듈 <code>math</code></h2>
<pre><code>python

import math</code></pre><h3 id="주요함수">주요함수</h3>
<table>
<thead>
<tr>
<th>함수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>math.pi</code></td>
<td>원주율 (3.1415...)</td>
</tr>
<tr>
<td><code>math.e</code></td>
<td>자연로그 밑 e (2.718...)</td>
</tr>
<tr>
<td><code>math.sqrt(x)</code></td>
<td>제곱근</td>
</tr>
<tr>
<td><code>math.pow(x, y)</code></td>
<td>x^y</td>
</tr>
<tr>
<td><code>math.ceil(x)</code></td>
<td>올림</td>
</tr>
<tr>
<td><code>math.floor(x)</code></td>
<td>내림</td>
</tr>
<tr>
<td><code>math.factorial(x)</code></td>
<td>팩토리얼</td>
</tr>
<tr>
<td><code>math.log(x, base)</code></td>
<td>로그 계산</td>
</tr>
</tbody></table>
<h4 id="예제">예제</h4>
<pre><code>python

print(math.sqrt(16))        # 4.0
print(math.ceil(3.14))        # 4
print(maht.log(100, 10))    # 2.0</code></pre><hr />
<h2 id="2-난수-모듈-random">2. 난수 모듈 <code>random</code></h2>
<pre><code>python

import random</code></pre><h3 id="주요함수-1">주요함수</h3>
<table>
<thead>
<tr>
<th>함수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>random.random()</code></td>
<td>0.0 ~ 1.0 사이 float</td>
</tr>
<tr>
<td><code>random.randint(a, b)</code></td>
<td>정수 [a, b] 중 무작위</td>
</tr>
<tr>
<td><code>random.uniform(a, b)</code></td>
<td>실수 [a, b] 중 무작위</td>
</tr>
<tr>
<td><code>random.choice(seq)</code></td>
<td>시퀀스에서 무작위 선택</td>
</tr>
<tr>
<td><code>random.shuffle(list)</code></td>
<td>리스트 섞기</td>
</tr>
<tr>
<td><code>random.sample(population, k)</code></td>
<td>k개의 샘플 추출</td>
</tr>
</tbody></table>
<h4 id="예제-1">예제</h4>
<pre><code>python

print(random.randint(1, 100))
print(random.choice(['apple', 'banana', 'cherry']))</code></pre><hr />
<h2 id="3-날짜와-시간-모듈-datetime">3. 날짜와 시간 모듈 <code>datetime</code></h2>
<pre><code>python

import datetime</code></pre><h3 id="주요-클래스">주요 클래스</h3>
<ul>
<li>datetime.date = 날짜 (년, 월, 일)</li>
<li>datetime.time = 시간 (시, 분, 초)</li>
<li>datetime.datetime = 날짜 + 시간</li>
<li>datetime.timedelta = 시간 간격</li>
</ul>
<h4 id="예제-2">예제</h4>
<pre><code>python

from datetime import datetime, timedelta

now = datetime.now()
print(&quot;현재:&quot;, now)

yesterdat = now - timedelta(days=1)
print(&quot;어제:&quot;, yesterday)

formatted = now.strftime(&quot;%Y-%m-%d %H:%M:%S&quot;)
print(&quot;포맷:&quot;, formatted)</code></pre><h4 id="날짜-문자열-파싱">날짜 문자열 파싱</h4>
<pre><code>python

dt = datetime.strptime(&quot;2025-07-24&quot;, &quot;%Y-%m-%d&quot;)
print(dt)</code></pre><hr />
<h2 id="4-운영체제-모듈-os">4. 운영체제 모듈 <code>os</code></h2>
<pre><code>python

import os</code></pre><h3 id="주요-기능">주요 기능</h3>
<table>
<thead>
<tr>
<th>함수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>os.getcwd()</code></td>
<td>현재 작업 디렉토리 반환</td>
</tr>
<tr>
<td><code>os.listdir()</code></td>
<td>디렉토리 내 파일 리스트</td>
</tr>
<tr>
<td><code>os.mkdir(&quot;폴더명&quot;)</code></td>
<td>새 폴더 생성</td>
</tr>
<tr>
<td><code>os.remove(&quot;파일명&quot;)</code></td>
<td>파일 삭제</td>
</tr>
<tr>
<td><code>os.rename(old, new)</code></td>
<td>파일명 변경</td>
</tr>
<tr>
<td><code>os.path.exists(path)</code></td>
<td>경로 존재 여부 확인</td>
</tr>
</tbody></table>
<h4 id="예제-3">예제</h4>
<pre><code>python

print(&quot;현재 경로:&quot;, os.getcwd())
os.mkdir(&quot;new_folder&quot;)
print(os.listdir())</code></pre><hr />
<h2 id="5-시스템-관련-모듈-sys">5. 시스템 관련 모듈 <code>sys</code></h2>
<pre><code>python

import sys</code></pre><h3 id="주요-기능-1">주요 기능</h3>
<table>
<thead>
<tr>
<th>속성/함수</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>sys.argv</code></td>
<td>명령줄 인자 리스트</td>
</tr>
<tr>
<td><code>sys.exit()</code></td>
<td>프로그램 강제 종료</td>
</tr>
<tr>
<td><code>sys.path</code></td>
<td>모듈 검색 경로 리스트</td>
</tr>
<tr>
<td><code>sys.version</code></td>
<td>Python 버전 확인</td>
</tr>
</tbody></table>
<h4 id="예제-4">예제</h4>
<pre><code>python

print(sys.version)
print(sys.path)
</code></pre><p>sys.argv는 CLI 환경에서 파라미터를 받을 때 유용합니다.</p>
<hr />
<p><strong>실전팁</strong></p>
<ul>
<li>math, random, datetime은 알고리즘 문제 풀이에 필수입니다.</li>
<li>os, sys는 스크립트 자동화, 시스템 점검, 파일 처리 등에서 자주 사용됩니다.</li>
<li>외부 패키지를 사용하기 전, 먼저 표준 라이브러리로 해결할 수 있는지 확인하세요.</li>
</ul>
<hr />
<p><strong>마무리</strong>
이번 편에서는 <strong>핵심적으로 자주 사용하느 모듈</strong>들을 정리하였습니다.
다음 편에서는 예외처리(try / except / finally / raise)를 정리해보겠습니다.</p>
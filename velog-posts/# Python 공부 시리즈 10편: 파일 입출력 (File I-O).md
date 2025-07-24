<p>Python에서는 <code>open()</code> 함수를 사용하여 텍스트 또는 바이너리 파일을 읽고 쓰는 작업을 수행할 수 있습니다.</p>
<hr />
<h2 id="101-open-파일-모드r-w-a-b--close">10.1 <code>open()</code>, 파일 모드(<code>r</code>, <code>w</code>, <code>a</code>, <code>b</code>, <code>+</code>), <code>close()</code></h2>
<h3 id="open-함수">open 함수</h3>
<pre><code>python

f = open(&quot;example.txt&quot;, &quot;r&quot;)</code></pre><ul>
<li>example.txt 파일을 읽기 모드(r)로 열고 파일 객체 f에 할당합니다.</li>
</ul>
<hr />
<h3 id="주요-파일-모드-요약">주요 파일 모드 요약</h3>
<table>
<thead>
<tr>
<th>모드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>'r'</code></td>
<td>읽기 전용 (파일이 없으면 오류 발생)</td>
</tr>
<tr>
<td><code>'w'</code></td>
<td>쓰기 전용 (기존 파일 삭제 후 새로 생성)</td>
</tr>
<tr>
<td><code>'a'</code></td>
<td>쓰기 전용 (파일 끝에 내용 추가)</td>
</tr>
<tr>
<td><code>'b'</code></td>
<td>바이너리 모드 (예: 이미지, 영상)</td>
</tr>
<tr>
<td><code>'+'</code></td>
<td>읽기/쓰기 겸용 (<code>r+</code>, <code>w+</code>, <code>a+</code>)</td>
</tr>
</tbody></table>
<hr />
<h3 id="파일-닫기close">파일 닫기(close())</h3>
<p>파일을 사용한 후에는 반드시 닫아줘야 합니다.</p>
<pre><code>python

f = open(&quot;example.txt&quot;, &quot;r&quot;)
f.close()</code></pre><hr />
<h2 id="102-읽기read-readline-readlines-tell-seek">10.2 읽기:read(), readline(), readlines(), tell(), seek()</h2>
<h3 id="read">read()</h3>
<p>전체 내용을 문자열로 읽습니다.</p>
<pre><code>python

f = open(&quot;example.txt&quot;, &quot;r&quot;)
content = f.read()
print(content)
f.close()</code></pre><hr />
<h3 id="readline">readline()</h3>
<p>한 줄씩 읽습니다.</p>
<pre><code>python

f = open(&quot;example.txt&quot;, &quot;r&quot;)
line1 = f.readline()
line2 = f.readline()
print(line1, line2)
f.close()</code></pre><hr />
<h3 id="readlines">readlines()</h3>
<p>모든 줄을 리스트 형태로 읽습니다.</p>
<pre><code>python

f = open(&quot;example.txt&quot;, &quot;r&quot;)
lines = f.readlines()
print(lines)
f.close()</code></pre><hr />
<h3 id="tell">tell()</h3>
<p>파일 내 현재 위치(바이트)를 반환합니다.</p>
<pre><code>python

f = open(&quot;example.txt&quot;, &quot;r&quot;)
f.read(5)
print(f.tell())  # 5
f.close()</code></pre><hr />
<h3 id="seek">seek()</h3>
<p>파일 내 원하는 위치로 커서를 이동합니다.</p>
<pre><code>python

f = open(&quot;example.txt&quot;, &quot;r&quot;)
f.seek(0)  # 맨 앞으로 이동
print(f.read())
f.close()</code></pre><hr />
<h2 id="103-쓰기-write-writelines">10.3 쓰기: write(), writelines()</h2>
<h3 id="write">write()</h3>
<p>문자열을 파일에 씁니다.</p>
<pre><code>python

f = open(&quot;example.txt&quot;, &quot;w&quot;)
f.write(&quot;Hello, Python!\n&quot;)
f.write(&quot;File I/O is important.&quot;)
f.close()</code></pre><hr />
<h3 id="writelines">writelines()</h3>
<p>리스트로 전달된 여러 줄을 한 번에 씁니다. 줄바꿈 문자(\n)는 직접 포함해야 합니다.</p>
<pre><code>python

lines = [&quot;First line.\n&quot;, &quot;Second line.\n&quot;, &quot;Third line.\n&quot;]

f = open(&quot;example.txt&quot;, &quot;w&quot;)
f.writelines(lines)
f.close()</code></pre><hr />
<h2 id="104-with-문-활용context-manager">10.4 with 문 활용(Context Manager)</h2>
<p>파일 작업 시 가장 추천되는 방식입니다. 자동으로 close()가 호출되어 리소스를 안전하게 반환합니다.</p>
<pre><code>python

with open(&quot;example.txt&quot;, &quot;r&quot;) as f:
    data = f.read()
    print(data)
# f는 자동으로 닫힘</code></pre><hr />
<h2 id="마무리-요약">마무리 요약</h2>
<table>
<thead>
<tr>
<th>함수/키워드</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>open()</code></td>
<td>파일 열기</td>
</tr>
<tr>
<td><code>read()</code>, <code>readline()</code>, <code>readlines()</code></td>
<td>파일 읽기</td>
</tr>
<tr>
<td><code>write()</code>, <code>writelines()</code></td>
<td>파일 쓰기</td>
</tr>
<tr>
<td><code>tell()</code> / <code>seek()</code></td>
<td>위치 정보 확인 및 이동</td>
</tr>
<tr>
<td><code>with open(...) as ...</code></td>
<td>자동으로 close() 처리되는 안전한 방법</td>
</tr>
</tbody></table>
<hr />
<p><strong>마무리</strong></p>
<p>이번 시리즈에서는 파일 입출력에 대해서 공부를 해보았습니다.
다음에는 예외처리 구조에 대해서 학습해보겠습니다.</p>
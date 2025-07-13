<h2 id="1-colab-시작하기">1. Colab 시작하기</h2>
<p>google Colab은 웹 상에서 무료로 GPU/TPU를 활용할 수 있는 Jupyter Notebook 환경입니다.코랩 노트를 생성하는 방법에는 3가지가 있습니다.</p>
<ol>
<li><p><strong>Colab 홈페이지에서 직접 생성</strong></p>
<ul>
<li>브라우저에서 <a href="https://colab.google/">https://colab.google/</a> 으로 접속</li>
<li>상단 중앙 &quot;New notebook&quot; 클릭</li>
</ul>
</li>
<li><p><strong>Google Drive 연동 메뉴 사용</strong></p>
<ul>
<li>내 Google Drive 폴더로 이동</li>
<li>우측 상단 &quot;+ 새로 만들기(new)&quot; -&gt; &quot;더보기(More)&quot; -&gt; <strong>Google Colaboratory</strong> 선택</li>
</ul>
</li>
<li><p><strong>파일 메뉴 이용</strong></p>
<ul>
<li>이미 열려 있는 Colab 탭에서 상단 메뉴 &quot;파일(File)&quot; -&gt; &quot;새 노트(New notebook)&quot; 클릭</li>
</ul>
</li>
</ol>
<hr />
<h2 id="2-런타임-유형-변경-none--gpu--tpu">2. 런타임 유형 변경 (None / GPU / TPU)</h2>
<p>기본적으로 Colab은 CPU 런타임으로 동작합니다. 대규모 연산이 필요할 때는 GPU나 TPU로 전환해보세요.</p>
<ol>
<li>화면 상단 메뉴 &quot;런타임&quot; 클릭</li>
<li>&quot;런타임 유형 변경&quot; 선택</li>
<li><strong>하드웨어 가속기</strong> 옵션에서<ul>
<li>'None' - 순수 GPU</li>
<li>'GPU' - NVDIA Tesla GPU</li>
<li>'TPU' - Google Cloud TPU</li>
</ul>
</li>
<li>&quot;저장&quot; 버튼 클릭</li>
</ol>
<blockquote>
<p><strong>주의: 무료 환경은 사용량 제한이 있으니, 장시간 연산 시 런타임이 중단될 수 있습니다.</strong></p>
</blockquote>
<hr />
<h2 id="3-환경-확인-명령어">3. 환경 확인 명령어</h2>
<p>런타임 설정이 잘 되었는지, 시스템 정보를 한눈에 확인해보세요. 노트북 셀에 아래 명령어를 입력하고 실행하면 됩니다.</p>
<pre><code class="language-bash"># OS 및 커널 정보
!cat /etc/issue.net
!uname -a

# CPU  정보
!cat /proc/cpuinfo | head -n 20

#디스크 사용량
!df -h

#활성화된 GPU 확인
!nvidai -smi

#Python 버전
!python --version</code></pre>
<p>실행 결과를 통해 메모리, 디스크, GPU모델, 드라이버 버전 등을 알 수 있습니다.</p>
<h2 id="4-셀-실행추가삭제이동-단축키">4. 셀 실행,추가,삭제,이동 단축키</h2>
<p>Colab을 빠르게 사용하려면 단축키를 숙지하는 것이 중요합니다. 아래 주요 단축키를 익혀두세요.</p>
<table>
<thead>
<tr>
<th align="left">기능</th>
<th>Windows/Linux</th>
<th align="center">maxOS</th>
</tr>
</thead>
<tbody><tr>
<td align="left">셀 실행</td>
<td>ctrl + Enter</td>
<td align="center">⌘ + Enter</td>
</tr>
<tr>
<td align="left">셀 실행 후 다음 이동</td>
<td>Shift + Enter</td>
<td align="center">Shift + Enter</td>
</tr>
<tr>
<td align="left">실행 후 셀 아래 추가</td>
<td>Alt + Enter</td>
<td align="center">⌥ + Enter</td>
</tr>
<tr>
<td align="left">셀 추가 (위)</td>
<td>Ctrl + M → A</td>
<td align="center">⌘ + M → A</td>
</tr>
<tr>
<td align="left">셀 추가 (아래)</td>
<td>Ctrl + M → B</td>
<td align="center">⌘ + M → B</td>
</tr>
<tr>
<td align="left">셀 삭제</td>
<td>Ctrl + M → D twice</td>
<td align="center">⌘ + M → D twice</td>
</tr>
<tr>
<td align="left">셀 이동 (위/아래)</td>
<td>Ctrl + M → K / J</td>
<td align="center">⌘ + M → K / J</td>
</tr>
<tr>
<td align="left">모든 셀 실행</td>
<td>Ctrl + F10</td>
<td align="center">⌘ + F10</td>
</tr>
<tr>
<td align="left">실행 중단</td>
<td>Ctrl + M → I</td>
<td align="center">⌘ + M → I</td>
</tr>
</tbody></table>
<hr />
<p>다음 3편에서는 Python 언어의 주요 특징을 자세히 다룰 예정입니다!</p>
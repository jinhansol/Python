<h3 id="프로그램--프로그램-언어">프로그램 &amp; 프로그램 언어</h3>
<h4 id="프로그램이란">프로그램이란?</h4>
<ul>
<li>컴퓨터를 실행하기 위해 작성한 순차적인 문령어의 모음</li>
<li>컴퓨터를 이용하여 문제를 해결하기 위하여, 처리하는 방법과 순서를
   기술한 명령문의 집합체</li>
<li>사람의 수작업이 비효율적인/어려운/힘든 작업의 자동화 수행</li>
</ul>
<h4 id="프로그래밍-언어란">프로그래밍 언어란?</h4>
<ul>
<li>컴퓨터가 작업 지시를 이해할 수 있도록 지시하는 언어</li>
<li>프로그램의 용도 및 운영 환경을 고려하여 언어 선택</li>
</ul>
<h4 id="파이썬-소개">파이썬 소개</h4>
<ul>
<li>인터프리터 언어(스크립트 언어)
  -원시코드를 기계어로 변환하는 과정 없이 줄(라인) 단위로 바로 명령어 실행
 -컴파일 언어 : 원시코드 -&gt; 기계어 변환 -&gt; 실행파일 생성</li>
<li>동적 타입 언어
  -변수의 자료 유형(data type)을 실행 중 정하거나, 정해진 자료 유형 변경 가능
 -프로그래밍 유연성 제공<ul>
<li>플랫폼 독립적 언어
-대부분의 운영체계에서 모두 동작
-원도우, 리눅스, 맥 등</li>
</ul>
</li>
</ul>
<h3 id="구글-코랩실습환경">구글 코랩(실습환경)</h3>
<ul>
<li>구글에서 무료로 제공하는 파이썬을 작성하고 실행할 수 있는 환경</li>
<li>GPU기반 딥러닝 환경 무료 제공<ul>
<li>주피터 노트북(Python, R)<ul>
<li>Tesla k80</li>
<li>환경 설정 최소화</li>
<li>관련 라이브러리가 자동으로 설치되어 제공</li>
<li>클라우드 기반</li>
<li>코드 공유 및 수정 수월</li>
<li>인터넷 브라우저만으로도 동작</li>
<li>사용 제약</li>
<li>최대 세션 유지시간 12시간</li>
<li>상업적 용도 불가</li>
</ul>
</li>
</ul>
</li>
</ul>
<h4 id="구글-코랩-링크">구글 코랩 링크</h4>
<ul>
<li>'<a href="https://colab.research.google.com/'">https://colab.research.google.com/'</a></li>
</ul>
<h4 id="구글-코랩-환경-설정">구글 코랩 환경 설정</h4>
<ul>
<li><p>런타임 유형 변경
  -None, GPU, TPU
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/66899546-80b8-4a3d-9d48-e2f0127dd7dd/image.png" />
<img alt="" src="https://velog.velcdn.com/images/hanyeon/post/ac89cb63-dc82-43bc-97e0-7ffaacf65564/image.png" /></p>
</li>
<li><p>환경 확인 명령어
| 용도 | 설명 |
| :- | - | :-: | -: |
| OS 확인 | !cat /etc/issue.net |
| CPU 확인 | !cat /proc/cpuinfo |
| 메모리 확인 | !cat /proc/meminfo |
| 하드디스크 확인 | !df -h |
| GPU 확인 | !nvidia -smi |
| 파이썬버전 확인 | !python --version |</p>
</li>
</ul>
<ul>
<li><p>명령어
-기본 수행 단위 : 셀
-코딩 방법</p>
<ul>
<li>셀에 커서를 위치시키고 명령어 작성</li>
<li>키보드 'Enter' 입력하면 줄 바꿈</li>
</ul>
<p>-셀 수행 방법</p>
<ul>
<li>셀 좌측 버튼 클릭(ctrl + enter) -&gt; 해당 셀만 수행</li>
<li>alt + enter -&gt; 해당 셀 수행 및 다음 셀 생성(커서 이동 포함)</li>
<li>shift + enter<ul>
<li>해당 셀 수행 및 커서를 다음 셀로 이동<ul>
<li>다음 셀이 없다면 셀 생성함</li>
</ul>
</li>
</ul>
</li>
<li>ctrl + F10 : 노트의 모든 셀 실행</li>
<li>ctrl + M + I : 실행 중단</li>
<li>셀 추가
  -셀 추가하고자 하는 곳에 마우스 위치 -&gt; 코드 선택
-ctrl + M + A(위쪽에 셀 추가), ctrl + M + B(아래쪽에 셀 추가)</li>
<li>셀 삭제
  -삭제하고자 하는 셀 클릭 -&gt; 휴지통 선택
-ctrl + M + D</li>
<li>셀 이동
  -이동하고자 하는 셀 클릭 -&gt; 화살표 선택
-ctrl + M + J(아래로 이동,) ctrl + M + K(위로 이동)</li>
</ul>
</li>
</ul>
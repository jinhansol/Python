<h1 id="2-개발-환경-준비">2. 개발 환경 준비</h1>
<p>개발 시작을 위한 환경 구축 방법을 단계별로 안내합니다.<br />API 키 보안 관리와 Git 버전 관리 연동 방법을 포함해, 현업에서 반드시 신경 써야 할 부분들을 꼼꼼히 다룹니다.</p>
<hr />
<h2 id="21-python-310-설치하기">2.1 Python 3.10 설치하기</h2>
<ul>
<li><a href="https://www.python.org/downloads/release/python-3100/">Python 공식 홈페이지</a>에서 운영체제에 맞는 버전 다운로드  </li>
<li>설치 시 <strong>&quot;Add Python 3.10 to PATH&quot;</strong> 옵션을 반드시 선택하세요.  </li>
<li>설치 완료 후, 터미널(명령 프롬프트)에서 아래 명령어로 설치 여부를 확인합니다.</li>
</ul>
<pre><code>python --version</code></pre><ul>
<li><code>Python 3.10.x</code>가 명확히 출력되면 정상 설치된 것입니다.</li>
</ul>
<hr />
<h2 id="22-pycharm-설치-및-새-프로젝트-생성">2.2 PyCharm 설치 및 새 프로젝트 생성</h2>
<ul>
<li><a href="https://www.jetbrains.com/pycharm/download/">PyCharm Community Edition</a>을 다운로드하여 설치합니다.  </li>
<li>PyCharm을 실행 후 <strong>New Project</strong>를 생성합니다.  </li>
<li>인터프리터(Interpreter)로 설치한 <strong>Python 3.10</strong>을 반드시 지정하세요.  </li>
<li>프로젝트 이름과 저장 위치를 선택한 후 생성합니다.</li>
</ul>
<hr />
<h2 id="23-git과-pycharm-연동하기-버전-관리-설정">2.3 Git과 PyCharm 연동하기 (버전 관리 설정)</h2>
<h3 id="git-설치-및-확인">Git 설치 및 확인</h3>
<ul>
<li><a href="https://git-scm.com/">Git 공식 홈페이지</a>에서 최신 버전 설치  </li>
<li>설치 후 터미널에서 버전 확인:</li>
</ul>
<pre><code>git --version</code></pre><ul>
<li>정상 버전 출력 시 설치 완료</li>
</ul>
<h3 id="pycharm에서-git-환경-설정">PyCharm에서 Git 환경 설정</h3>
<ol>
<li>PyCharm에서 <code>File → Settings (Preferences) → Version Control → Git</code> 진입  </li>
<li><code>Path to Git executable</code>에 Git 실행 파일 경로가 자동으로 잡혔는지 확인합니다. (예: Windows는 <code>C:\Program Files\Git\bin\git.exe</code>)  </li>
<li><strong>Test</strong> 버튼 클릭 → &quot;Git executed successfully&quot; 메시지가 나와야 정상입니다.  </li>
<li><code>File → Settings → Version Control → GitHub</code>에서 계정 추가 후 로그인 또는 토큰 인증을 통해 GitHub와 연동하세요.</li>
</ol>
<h3 id="버전-관리-활성화">버전 관리 활성화</h3>
<ul>
<li>상단 메뉴에서 <code>VCS → Enable Version Control Integration</code> 선택 후 <strong>Git</strong>을 활성화  </li>
<li>코드 변경 후 <strong>Commit</strong> 및 <strong>Push</strong>를 통해 버전 관리 및 원격 저장소 동기화가 가능합니다.</li>
</ul>
<hr />
<h2 id="24-필수-라이브러리-설치-및-api-키-관리">2.4 필수 라이브러리 설치 및 API 키 관리</h2>
<h3 id="주요-패키지-설치">주요 패키지 설치</h3>
<pre><code>pip install fastapi langchain openai requests beautifulsoup4 uvicorn python-dotenv</code></pre><ul>
<li>주요 사용 패키지 설명:  <ul>
<li><strong>FastAPI</strong>: 백엔드 API 서버 구현  </li>
<li><strong>LangChain</strong>: LLM 파이프라인 및 뉴스 요약 처리  </li>
<li><strong>OpenAI</strong>: GPT, Whisper, TTS API 호출  </li>
<li><strong>Requests</strong>: 네이버 API 호출  </li>
<li><strong>BeautifulSoup4</strong>: 웹 크롤링 및 HTML 파싱  </li>
<li><strong>Uvicorn</strong>: FastAPI 실행용 ASGI 서버  </li>
<li><strong>python-dotenv</strong>: 환경변수 관리용  </li>
</ul>
</li>
</ul>
<h3 id="안전한-api-키-관리">안전한 API 키 관리</h3>
<ul>
<li>프로젝트 루트에 <code>.env</code> 파일을 만들어 API 키를 다음과 같이 저장합니다.</li>
</ul>
<pre><code>NAVER_CLIENT_ID=your_client_id
NAVER_CLIENT_SECRET=your_client_secret
OPENAI_API_KEY=your_openai_api_key</code></pre><ul>
<li><p><code>.env</code> 파일은 절대 깃허브 등 원격 저장소에 커밋하지 않도록 <code>.gitignore</code>에 반드시 추가합니다.</p>
</li>
<li><p>Python 코드에서 <code>python-dotenv</code>를 사용하여 환경변수를 불러오는 방법:</p>
</li>
</ul>
<pre><code>import os
from dotenv import load_dotenv

load_dotenv()
naver_id = os.getenv(&quot;NAVER_CLIENT_ID&quot;)
openai_key = os.getenv(&quot;OPENAI_API_KEY&quot;)</code></pre><hr />
<h2 id="25-자주-발생하는-문제-및-해결-팁">2.5 자주 발생하는 문제 및 해결 팁</h2>
<ul>
<li><p><strong>Python 설치 문제</strong>  </p>
<ul>
<li>PATH 설정 누락 여부 확인  </li>
<li>최신 버전이 아닌 경우 호환성 문제 발생 가능, 권장 버전 확인  </li>
</ul>
</li>
<li><p><strong>패키지 설치 오류</strong>  </p>
<ul>
<li><p>가상환경(venv) 사용 권장:  </p>
<pre><code>python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate</code></pre></li>
<li><p>관리자 권한 문제 시, 권한 있는 터미널(또는 명령 프롬프트) 실행  </p>
</li>
</ul>
</li>
<li><p><strong>API 키 오류</strong>  </p>
<ul>
<li>키 값 오타 또는 권한 부족 문제  </li>
<li><code>python-dotenv</code>로 환경변수 정상 적용 여부 확인  </li>
</ul>
</li>
<li><p><strong>PyCharm 인터프리터 문제</strong>  </p>
<ul>
<li>프로젝트 설정 내 인터프리터 경로가 정확한지 확인  </li>
<li>패키지 설치 위치와 인터프리터 경로 일치 여부 체크  </li>
</ul>
</li>
</ul>
<hr />
<p>💡 <strong>Tip</strong>  </p>
<ul>
<li>가상환경 활용으로 패키지 충돌 방지 및 환경 분리  </li>
<li><code>.env</code> 파일 관리는 보안상 중요, 절대 공개 저장소에 올리지 않기  </li>
<li>Git 연동으로 팀 협업 및 코드 추적력 강화  </li>
<li>PyCharm 내장 터미널에서 각종 명령어 수행 가능해 편리함</li>
</ul>
<hr />
<p>이제 개발 환경 세팅이 완료되어 프로젝트 코드를 실행하고 개발할 준비가 되었습니다.<br />다음 장에서는 <strong>프로젝트 구조 이해</strong>를 통해 프로젝트의 전체 흐름과 각 구성요소의 역할을 살펴봅니다.</p>
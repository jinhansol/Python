import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@hanyeon'

# 깃허브 레포지토리 경로
repo_path = '.'

# 레포지토리 로드
repo = git.Repo(repo_path)

# ✅ Git 사용자 정보 설정 (이 부분을 repo 정의 이후에!)
repo.git.config('--global', 'user.email', 'jinhan9657@naver.com')
repo.git.config('--global', 'user.name', 'hansoljin')

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'
    file_path = os.path.join(posts_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)

        # Git add & commit
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# Git push
repo.git.push()

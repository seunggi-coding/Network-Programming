가상환경 설정
- 아나콘다 설치 위치의 envs 폴더 안에 가상환경이 존재

- 가상환경 생성
conda create --name 본인학번 python=3.11

- 가상환경 활성화
conda activate 본인학번

- 현재 활성화된 가상환경 비활성화
conda deactivate

- 가상환경 리스트 확인
conda env list

- conda 업데이트
conda update -n base -c defaults conda

- conda로 파이썬 패키지 설치
conda update --all

- conda로 설치한 파이썬 패키지 삭제
conda uninstall 패키지이름

=========================================================

깃

- 깃 상태 확인
git status

- 수정 또는 생성한 파일 스테이징 하기
git add
ex) git add hello.txt or git add .

- 스테이지에 올라온 파일 커밋하기
git commit -m "message"

- 저장소에 저장된 버전 확인
git log

- 스테이징 & 커밋 한번에 처리
git commit -am "message"

- 수정한 부분을 스테이징 하기 전에 하는 과정
git diff

- 작업 트리에서 수정한 파일 되돌리기
git checkout -- 파일이름
ex) git checkout -- hello.txt

- 스테이징 되돌리기
git restore --staged 파일이름

- 최신 커밋 취소하기 
git reset HEAD^

- 특정 커밋으로 되돌리기 (git log로 커밋을 확인하여 최신 커밋의 해시를 확인 후 진행)
git reset 커밋해시

- 원격 저장소 저장하기
git push

- 원격 저장소에서 파일 내려받기
git pull origin main

- 파일 삭제하기 (삭제 후 반드시 커밋을 수행해야 함)
git rm [삭제할 파일 이름]

- 모든 파일 삭제
git rm *

# GIT

## 최초설정
커밋에 기록되는 사용자 정보
```bash
$ git config --global user.name <name>
$ git config --global user.email <email> 
```
## 명령어

working directory는 코딩을 짜는 곳이다. staging area는 무대다 git init은 git directory와 같다.

- `git init`
    - `.git` repository를 생성하는 명령어

초기화를 위해 사용하는 명령어이다. 깃 파일은 현재 숨김파일이다. 생성은 되었지만 파일트리에 보여지지 않는다.
또한 옆에 마스터라는 글자가 나타나는데 '현재 폴더는 깃으로 관리되고 있다'는 뜻이다. 

- `git add <file name>`
    - 작업 파일을 working directory에서 staging area로 추가하는 과정이다.
    - 일반적으로 모든 파일, 폴더를 한번에 추가하기 위해 아래의 명령어로 작성한다.
    - `git add .`

- `git commit -m "first commit"`
    - `staging area`에 올라간 파일들의 스냅샷을 찍어서 ` .git directory`에 저장한다.
    - 일반적으로 -m 옵션을 넣어서 커밋메세지를 추가한다.
    - `git commit -m "message"`


# GIT

## 최초설정
커밋에 기록되는 사용자 정보
```bash
$ git config --global user.name <name>
$ git config --global user.email <email> 
```
## 명령어

working directory는 코딩을 짜는 곳이다. staging area는 무대다 git init은 git directory와 같다.
저장을 한 다음 작업을 하는 것을 추천한다. 

## 로컬명령어
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

이런 식으로 계속해서 쌓아서 업데이트를 하게 된다. 깃허브를 사용하는 이유는 이러한 업데이트들을 저장하는 용도로 사용하는 것이다. 

깃은 브렌치 시스템을 따른다. 브렌치는 나뭇가지라는 뜻이다. 커밋은 점이다. 나무의 중심기둥은 마스터이다. 
> 기존에 마스터로 쓰였지만 인종차별 문제로 인해 main으로 쓰기도 한다.

`git remote add origin https://github.com/micenicen/TIL.git`에 대해 설명해본다면 다음과 같다.
1. 깃을 사용하여 추가한다.
2. 오리진이라는 이름으로 해당 도메인을 업로드할 것이다.
 
## 원격저장소
- `git remote`
    - 원격저장소 주소를 관리하기 위한 명렁어
    - `git remote add origin <url>`

- `git push`
    - 원격 저장소에 로컬 코드를 업로드 하기 위한 명령어
    - `git push <remote> <branch>`


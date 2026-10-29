# AI티타임 · ChatGPT 예약 강의자료

서대문구 AI티타임 동아리를 위한 **ChatGPT 예약(Schedule) 기능 강의 웹페이지**입니다. 슬로건의 색상을 활용한 입체 시계와 실제 화면 캡처로 기능 이해부터 예약 요청문 작성까지 안내합니다.

React + Vite 기반 정적 웹사이트이며, **별도 서버·데이터베이스·API 키가 필요하지 않습니다.**

## 빠르게 실행하기

### 1. 준비

- **Node.js 22 이상**과 함께 설치되는 npm
- 저장소를 복제할 경우 Git 또는 GitHub Desktop

설치 확인:

```sh
node --version
npm --version
```

### 2. 프로젝트 폴더 열기

저장소를 복제하거나 ZIP을 내려받아 압축을 푼 뒤, **package.json이 있는 폴더**에서 터미널을 엽니다.

Windows에서 제공받은 폴더를 바로 사용하는 예시:

```powershell
cd "C:\Users\user\Desktop\이용경 업무\생성형 AI 주간 강의자료 만들기\ai-teatime-schedule-github"
```

### 3. 설치 및 실행

```sh
npm ci
npm run dev
```

터미널에 표시되는 주소를 브라우저에서 엽니다. 기본 주소는 **http://127.0.0.1:5173**이며, 포트가 이미 사용 중이면 다른 번호가 표시됩니다.

실행을 종료하려면 터미널에서 **Ctrl+C**를 누릅니다. 코드를 수정하고 저장하면 개발 화면에 반영됩니다.

> Windows PowerShell에서 npm 실행 정책 오류가 발생하면 `npm` 대신 `npm.cmd`를 사용하세요. 예: `npm.cmd ci`, `npm.cmd run dev`. 실행 정책을 바꿀 필요는 없습니다.

## 배포용 파일 만들기

```sh
npm run build
```

완성된 웹사이트가 **dist/** 폴더에 생성됩니다. 정적 웹사이트 호스팅 서비스에서는 다음 설정을 사용합니다.

| 항목 | 값 |
| --- | --- |
| 설치 명령 | `npm ci` |
| 빌드 명령 | `npm run build` |
| 게시 폴더 | `dist` |
| 환경 변수 | 필요 없음 |

빌드 결과를 로컬에서 확인하려면:

```sh
npm run preview
```

기본 주소는 **http://127.0.0.1:4173**입니다. 이 명령은 빌드 결과 확인용입니다.

일반 실행 시 `index.html`이나 `dist/index.html`을 파일로 직접 열지 말고 개발 서버 또는 미리보기 명령을 사용하세요. 서버 없이 사용할 별도 버전은 아래에서 만들 수 있습니다.

### GitHub 저장과 웹사이트 배포의 차이

이 프로젝트를 GitHub 저장소에 업로드하면 **코드가 보관**됩니다. 웹사이트가 자동으로 공개되는 것은 아닙니다. 호스팅은 별도로 설정해야 합니다.

GitHub Pages 배포 설정을 포함합니다. `vite.config.js`의 상대 경로 설정과 `src/assets.js`의 이미지 경로 처리를 통해 `/chatgpt-schedule-sdm/` 하위에서도 실행됩니다.

### 이 저장소의 GitHub Pages 설정

1. 저장소 Settings → Pages → Build and deployment → Source에서 **GitHub Actions**를 선택합니다.
2. `.github/workflows/deploy.yml`을 포함한 소스를 main 브랜치에 업로드합니다.
3. 저장소의 Actions 탭에서 **Deploy lecture to GitHub Pages** 실행 결과를 확인합니다.
4. 성공하면 https://leeyongkyung.github.io/chatgpt-schedule-sdm/ 에서 열 수 있습니다.

main에 변경사항을 올릴 때마다 자동으로 빌드·배포합니다. Actions → 해당 작업 → Run workflow로 수동 실행할 수도 있습니다. 저장소 루트에 package.json이 있어야 합니다.

## 서버 없이 여는 버전 만들기 — 선택 사항

이 작업에만 Python 3이 추가로 필요합니다. 웹페이지 실행·빌드에는 Python이 필요하지 않습니다.

```sh
npm run build
python make-offline.py
```

- `offline/강의자료.html`: 직접 열어 사용할 파일
- `offline/assets/`: 캡처·이미지 자료
- 프로젝트 폴더의 **상위 폴더**에 `AI티타임_ChatGPT예약_강의웹페이지.zip` 생성

생성한 ZIP은 모두 압축을 푼 뒤 `강의자료.html`을 엽니다. assets 폴더를 같은 위치에 보관하세요. 외부 사이트 링크와 웹 글꼴을 불러올 때는 인터넷 연결이 필요합니다. 인터넷이 없으면 시스템 글꼴을 사용합니다.

## 사용 방법

- **한 장씩 보기**: 한 장면씩 표시합니다. 하단 챕터 목차, 이전·다음 버튼, 좌우 방향키로 이동합니다.
- **전체 펼쳐 보기**: 모든 내용을 세로로 이어서 표시합니다. 스크롤하거나 하단 목차로 이동합니다.
- **보기 방식 버튼**: 상단에 현재 방식을 표시하며 누르면 다른 방식으로 전환합니다.
- **가+**: 글자를 확대합니다. 좁은 모바일 화면에서는 이 버튼이 숨겨집니다.
- **재생·일시정지 아이콘**: 모션을 켜거나 줄입니다.
- **전체화면 아이콘**: 전체화면을 전환합니다. 브라우저에 따라 허용 여부가 다를 수 있습니다.
- **캡처 확대**: 이미지를 누르면 확대 창이 열립니다. +/−로 배율을 바꾸고 Esc로 닫습니다.
- **직접 설계**: 업무·주기·시간·출처를 입력해 요청문을 만들고 복사합니다.

이 페이지는 실제 ChatGPT 예약을 생성하지 않습니다. 작성한 요청문을 ChatGPT에 붙여넣고 생성된 예약 카드와 일정을 확인하세요. 입력한 설계 내용은 서버로 전송하거나 저장하지 않으며, 페이지를 새로 열면 초기화됩니다.

## 강의 구성

| 번호 | 내용 |
| --- | --- |
| 00 | 시작 |
| 01 | 예약의 이해 |
| 02 | 행정 활용 |
| 03 | 설정 시연 — 실제 캡처 기반 6단계 |
| 04 | 결과 확인 |
| 05 | 직접 설계 |
| 06 | 마무리 |

예약 생성 후 확인할 활성 상태·일정·알림과 수정·일시중지·삭제 방법은 **설정 시연 → 저장된 설정 확인**에 통합되어 있습니다.

## 폴더 구조와 수정 위치

```text
ai-teatime-schedule-github/
├── public/
│   ├── assets/                 # 실제 캡처 10장, 슬로건 이미지
│   └── favicon.svg
├── src/
│   ├── components/
│   │   ├── Lesson.jsx          # 강의 내용·시연·요청문 작성 화면
│   │   ├── TiltedCard.jsx      # React Bits 입체 카드
│   │   ├── TiltedCard.css
│   │   └── AnimatedContent.jsx # React Bits 장면 등장 효과
│   ├── App.jsx                 # 화면 구성·보기 전환·챕터 이동
│   ├── content.js              # 목차·시연 단계·사례·출처·요청문
│   ├── main.jsx                # React 시작점
│   └── styles.css              # 색상·배치·입체 시계·모바일 대응
├── index.html                  # 제목·설명·시작 HTML
├── package.json                # 실행 명령·의존성
├── package-lock.json           # 설치 버전 고정
├── make-offline.py             # 서버 없이 여는 버전 생성
├── REACT-BITS-LICENSE.md
└── README.md
```

### 자주 수정하는 항목

| 바꾸려는 것 | 수정 파일 |
| --- | --- |
| 업무 사례·프롬프트·출처·시연 설명 | `src/content.js` |
| 각 장면의 문구·요청문 작성 항목 | `src/components/Lesson.jsx` |
| 챕터 구성·보기 방식·확대 창 | `src/App.jsx` |
| 색상·글자 크기·간격·모바일 배치 | `src/styles.css` |
| 실제 캡처·슬로건 | `public/assets/` |
| 브라우저 탭 제목·설명 | `index.html` |

수정 후 `npm run build`가 성공하는지 확인하고, PC와 모바일에서 해당 화면·버튼을 확인하세요.

## GitHub에 업로드하기

**이 폴더 안의 내용 전체**를 저장소 루트에 넣습니다. package.json과 README.md가 저장소 첫 화면에서 보이도록 배치하세요.

GitHub Desktop을 사용하는 경우 이 폴더로 새 저장소를 만들고 변경사항을 커밋한 다음 Publish repository를 실행할 수 있습니다. GitHub 웹사이트의 Upload files로 올릴 수도 있습니다.

터미널을 사용하는 경우 이 폴더에서 다음 순서로 시작합니다.

```sh
git init
git add .
git commit -m "Add AI teatime scheduled tasks lecture website"
git branch -M main
```

이후 GitHub에서 만든 빈 저장소의 안내에 따라 원격 저장소를 연결하고 push합니다. **node_modules, dist, offline 및 환경 설정 파일은 .gitignore에 의해 제외**됩니다. package-lock.json과 src, public은 함께 올립니다.

이 배포용 소스 폴더에는 기존 Sites 저장소의 .git 이력·비공개 배포 연결 정보·인증 토큰·작성자 PC 전용 검사 경로를 포함하지 않습니다.

## 자료와 라이선스

- React Bits의 **Tilted Card / Animated Content**를 사용했습니다. 원본: https://github.com/DavidHDev/react-bits
- Vite 환경에 맞춰 React 가져오기와 클라이언트 지시문을 조정했습니다. 제공된 `REACT-BITS-LICENSE.md`의 고지와 조건을 함께 유지하세요. 이 파일은 React Bits 구성요소에 대한 라이선스이며 사이트 전체를 동일 라이선스로 선언하는 것은 아닙니다.
- 슬로건과 캡처는 사용자 제공 자료입니다. 첨부 이미지의 권리·개인 대화 표현을 고려하여 저장소 공개 범위를 정하세요.
- ChatGPT 캡처는 2026-10-28 사례입니다. 계정·앱·버전에 따라 화면과 지원 기능이 달라질 수 있습니다.
- 기능 안내: https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
- 웹 글꼴은 Google Fonts에서 불러오며, 불러올 수 없으면 시스템 글꼴로 표시합니다.

## 문제 해결

| 증상 | 확인할 내용 |
| --- | --- |
| npm을 찾을 수 없음 | Node.js 설치 후 터미널을 새로 여세요. |
| PowerShell 실행 정책 오류 | `npm.cmd`로 실행하세요. |
| 설치 오류 | Node.js 버전과 인터넷 연결을 확인하고 `npm ci`를 다시 실행하세요. |
| 기본 포트 접속 안 됨 | 터미널에 실제 표시된 Local 주소를 여세요. |
| 이미지나 화면이 안 나옴 | 파일 직접 열기 대신 `npm run dev` 또는 `npm run preview`를 사용하고 public/assets가 포함되어 있는지 확인하세요. |
| 요청문 복사가 제한됨 | 표시된 요청문을 직접 선택해 복사하세요. |
| GitHub Pages에서 이미지가 안 나옴 | 최신 vite.config.js와 src/assets.js, 수정된 이미지 참조가 함께 업로드되었는지 확인하세요. |

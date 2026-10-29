from pathlib import Path
import re
import zipfile
import shutil

project = Path(__file__).parent
dist = project / 'dist'
html = (dist / 'index.html').read_text(encoding='utf-8')
js = next((dist / 'assets').glob('index-*.js')).read_text(encoding='utf-8')
js = js.replace('</script>', '<\\/script>')
css = next((dist / 'assets').glob('index-*.css')).read_text(encoding='utf-8')
html = re.sub(r'<script[^>]*src=[^>]*></script>', lambda m: '<script type="module">' + js + '</script>', html)
html = re.sub(r'<link[^>]*rel="stylesheet"[^>]*>', lambda m: '<style>' + css + '</style>', html)
html = html.replace('/favicon.svg', './favicon.svg')
out = project / 'offline'
out.mkdir(exist_ok=True)
(out / '강의자료.html').write_text(html, encoding='utf-8')
shutil.copytree(dist / 'assets', out / 'assets', dirs_exist_ok=True)
shutil.copy2(dist / 'favicon.svg', out / 'favicon.svg')
(out / '사용방법.txt').write_text('압축을 모두 푼 뒤 강의자료.html 파일을 여세요. 같은 폴더의 assets 폴더를 함께 보관하세요. 인터넷이 없어도 강의 본문·캡처·요청문 작성이 동작합니다. 외부 사이트 링크와 웹 글꼴은 인터넷이 필요합니다.', encoding='utf-8')
archive = project.parent / 'AI티타임_ChatGPT예약_강의웹페이지.zip'
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as bundle:
    for file in out.rglob('*'):
        if file.is_file():
            bundle.write(file, file.relative_to(out))
print(archive)

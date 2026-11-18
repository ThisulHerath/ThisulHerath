"""Render a local README preview with manual day/night appearance controls."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
body = (root / 'README.md').read_text(encoding='utf-8-sig').replace('./assets/', '../assets/')
body = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', body)
page = '''<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Thisul · Christmas by Day & Night</title>
<style>
:root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;padding:24px;background:#0d1117;color:#e6edf3;font:16px/1.6 Arial;transition:background .3s,color .3s}
body.day{background:#f0f7fc;color:#173649;color-scheme:light}main{max-width:1050px;margin:auto;padding:24px;border:1px solid #456273;border-radius:12px}
nav{max-width:1050px;margin:0 auto 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}button{padding:10px 18px;border:1px solid #7399ad;border-radius:24px;background:transparent;color:inherit;cursor:pointer}button[aria-pressed=true]{background:#275e62;color:white}nav span{margin-right:auto}img{max-width:100%;vertical-align:middle}p[align=center]{display:flex;justify-content:center;gap:7px;flex-wrap:wrap}main>img,main>picture,main>a{display:block;margin-bottom:14px}a{color:#5eaa9c}body.day a{color:#176d62}strong{color:inherit}details{padding:12px;border:1px solid #7399ad;border-radius:10px}@media(max-width:600px){body{padding:8px}main{padding:8px}}
</style><nav><span>Christmas in Orbit · Appearance preview</span><button id="day" onclick="theme('day')">☀ Daytime</button><button id="night" onclick="theme('night')">☾ Nighttime</button></nav><main>'''+body+'''</main><script>
function theme(mode){document.body.classList.toggle('day',mode==='day');document.querySelectorAll('main picture source').forEach(s=>s.media='not all');document.querySelectorAll('main img').forEach(img=>{if(!img.dataset.base)img.dataset.base=img.getAttribute('src').replace('-day.svg','.svg');if(img.dataset.base.startsWith('../assets/orbital/'))img.src=mode==='day'?img.dataset.base.replace('.svg','-day.svg'):img.dataset.base});for(const m of ['day','night'])document.getElementById(m).setAttribute('aria-pressed',String(m===mode));}
theme(new URLSearchParams(location.search).get('theme')||(matchMedia('(prefers-color-scheme: light)').matches?'day':'night'));
</script></html>'''
out = root / '.preview' / 'christmas.html'
out.parent.mkdir(exist_ok=True)
out.write_text(page, encoding='utf-8')
print(out)

import os, re, urllib.parse

# ─── 可根据需要自行修改 ────────────────────────────────
html_folder        = '2-PROJECTS (Code Notes)/scripts'   # 扫描目录
excluded_files     = {'header.html'}                    # 排除文件
background_image   = 'assets/background.jpg'            # 背景图
output_file        = 'index.html'
# ────────────────────────────────────────────────────

def natural_key(name):
    return [int(t) if t.isdigit() else t.lower()
            for t in re.split(r'([0-9]+)', name)]

files = sorted(
    [f for f in os.listdir(html_folder)
     if f.endswith('.html') and f not in excluded_files],
    key=natural_key
)

# ---------- HTML ---------- #
html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>我的Rmarkdown笔记导航</title>
<style>
/* ===== 全局 ===== */
html,body{{margin:0;height:100%;font-family:-apple-system,Segoe UI,Tahoma,Verdana,sans-serif}}
.background{{
  position:fixed;inset:0;
  background:url('{background_image}') center/cover fixed;
  filter:blur(1px);          /* 背景轻模糊 */
  z-index:-1;
}}
.container{{
  display:flex;min-height:100vh;
  background:rgba(255,255,255,.55);
  backdrop-filter:blur(.5px);
}}

/* ===== 侧栏玻璃卡片 ===== */
.sidebar{{
  width:250px;               /* 固定宽度 */
  padding:30px 20px;
  background:rgba(126,200,227,.25);  /* 天青色 + 半透明 */
  backdrop-filter:blur(8px);
  border-right:1px solid rgba(255,255,255,.3);
  color:#fff;
  box-shadow:0 0 6px rgba(0,0,0,.12);
  box-sizing:border-box;
}}
.sidebar h2{{margin:0 0 1rem}}
.sidebar p{{margin:.6rem 0;line-height:1.5;text-shadow:0 0 3px rgba(0,0,0,.45)}}

/* ===== 内容区 ===== */
.content{{flex:1;padding:40px;display:flex;flex-direction:column;align-items:center}}
h1{{margin:0 0 30px;text-align:center}}

/* 通用玻璃卡片（搜索框 & li） */
.card{{
  width:100%;max-width:700px;
  margin:10px 0;
  padding:15px 20px;
  border-radius:12px;
  background:rgba(255,255,255,.25);
  backdrop-filter:blur(8px);
  box-shadow:0 2px 6px rgba(0,0,0,.12);
  box-sizing:border-box;
}}
/* 搜索框 */
.search-box input{{
  all:unset;
  width:100%;
  font-size:18px;line-height:1.4;
  color:#fff;text-shadow:0 0 3px rgba(0,0,0,.6);
}}
.search-box{{margin-bottom:20px}}
/* 列表 */
ul{{list-style:none;padding:0;margin:0;width:100%;max-width:700px}}
li.card{{transition:.25s}}
li.card:hover{{background:rgba(255,255,255,.35);transform:translateX(5px)}}
a{{text-decoration:none;color:#fff;font-size:18px;display:block;text-shadow:0 0 3px rgba(0,0,0,.6)}}
</style>
</head>
<body>
<div class="background"></div>

<div class="container">
  <div class="sidebar">
    <h2>关于笔记</h2>
    <p>这是一个数据科学学习笔记。</p>
    <p>先学着，以后的事以后再说。</p>
    <p>欢迎交流，互相学习！</p>
  </div>

  <div class="content">
    <h1>笔记导航</h1>

    <!-- 搜索框 -->
    <div class="search-box card">
      <input type="text" id="searchInput" placeholder="输入关键词搜索笔记…" onkeyup="filterNotes()">
    </div>

    <!-- 列表 -->
    <ul id="noteList">
'''

for f in files:
    url   = f"{html_folder.replace(' ','%20')}/{urllib.parse.quote(f)}"
    title = re.sub(r'^\d+[-_、\s]*', '', f[:-5])      # 去掉序号与 .html
    html += f'      <li class="card"><a href="{url}" target="_blank">{title}</a></li>\n'

html += '''    </ul>
  </div>
</div>

<script>
function filterNotes(){
  const kw = document.getElementById('searchInput').value.toUpperCase();
  document.querySelectorAll('#noteList li').forEach(li=>{
      li.style.display = li.innerText.toUpperCase().includes(kw)?'':'none';
  });
}
</script>
</body></html>'''

with open(output_file,'w',encoding='utf-8') as f:
    f.write(html)

print('✅ 已生成侧栏+主卡片均为玻璃效果的 index.html')

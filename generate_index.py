import os
import urllib.parse
import re

# 指定HTML文件所在的文件夹（相对于仓库根目录）
html_folder = '2-PROJECTS (Code Notes)/scripts'

# 要排除在目录之外的文件
excluded_files = ['header.html']

# 输出index.html文件
output_file = 'index.html'

# 背景图片相对路径（放仓库内部的 assets/ 目录）
background_image_url = 'assets/background.jpg'

# 自然排序方法
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

# 遍历HTML文件，排除不需要的
html_files = [
    f for f in os.listdir(html_folder) 
    if f.endswith('.html') and f not in excluded_files
]

# 开始生成HTML内容
html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>我的Rmarkdown笔记导航</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            height: 100%;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        .background {{
            background: url('{background_image_url}') no-repeat center center fixed;
            background-size: cover;
            filter: blur(8px);
            height: 100%;
            width: 100%;
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1;
        }}
        .container {{
            display: flex;
            min-height: 100vh;
            background-color: rgba(255,255,255,0.75);
            backdrop-filter: blur(3px);
        }}
        .sidebar {{
            width: 250px;
            background: #2196F3;
            color: white;
            padding: 30px 20px;
        }}
        .sidebar h2 {{
            margin-top: 0;
        }}
        .content {{
            flex-grow: 1;
            padding: 40px;
        }}
        .search-box {{
            margin-bottom: 20px;
        }}
        input[type="text"] {{
            width: 100%;
            padding: 10px;
            border-radius: 6px;
            border: 1px solid #ccc;
            font-size: 16px;
        }}
        ul {{
            list-style-type: none;
            padding: 0;
        }}
        li {{
            background: white;
            margin: 10px 0;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: background 0.3s, transform 0.2s;
        }}
        li:hover {{
            background: #e3f2fd;
            transform: translateX(5px);
        }}
        a {{
            text-decoration: none;
            color: #333;
            font-size: 18px;
            display: block;
        }}
    </style>
</head>
<body>
    <div class="background"></div>
    <div class="container">
        <div class="sidebar">
            <h2>关于我</h2>
            <p>你好，我是 WangYe123123。</p>
            <p>这里是我的 Rmarkdown 学习笔记，记录成长之路。</p>
            <p>未来持续更新，欢迎交流！</p>
        </div>
        <div class="content">
            <h1>笔记导航</h1>
            <div class="search-box">
                <input type="text" id="searchInput" onkeyup="filterNotes()" placeholder="输入关键词搜索笔记...">
            </div>
            <ul id="noteList">
"""

# 排序并生成列表
for file_name in sorted(html_files, key=natural_sort_key):
    file_url = urllib.parse.quote(file_name)
    link = f"{html_folder.replace(' ', '%20')}/{file_url}"
    display_name = re.sub(r'^\d+[-_、\s]*', '', file_name.replace('.html', ''))
    html_content += f'                <li><a href="{link}" target="_blank">{display_name}</a></li>\n'

html_content += """            </ul>
        </div>
    </div>

    <script>
    function filterNotes() {
        var input, filter, ul, li, a, i, txtValue;
        input = document.getElementById('searchInput');
        filter = input.value.toUpperCase();
        ul = document.getElementById('noteList');
        li = ul.getElementsByTagName('li');
        for (i = 0; i < li.length; i++) {
            a = li[i].getElementsByTagName('a')[0];
            txtValue = a.textContent || a.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                li[i].style.display = '';
            } else {
                li[i].style.display = 'none';
            }
        }
    }
    </script>
</body>
</html>
"""

# 写入文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ 成功生成主目录 {output_file}！")
import os
import urllib.parse

# 指定HTML文件所在的文件夹（相对于仓库根目录）
html_folder = '2-PROJECTS (Code Notes)/scripts'

# 要排除在目录之外的文件（可以继续加更多）
excluded_files = ['header.html']

# 输出index.html文件
output_file = 'index.html'

# 遍历HTML文件
html_files = [
    f for f in os.listdir(html_folder) 
    if f.endswith('.html') and f not in excluded_files
]

# 开始生成HTML内容
html_content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>我的Rmarkdown笔记导航</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f9f9f9;
            margin: 40px;
            color: #333;
        }
        h1 {
            text-align: center;
            color: #4CAF50;
        }
        ul {
            list-style-type: none;
            padding: 0;
            max-width: 600px;
            margin: 40px auto;
        }
        li {
            background: white;
            margin: 10px 0;
            padding: 15px 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: background 0.3s, transform 0.2s;
        }
        li:hover {
            background: #e8f5e9;
            transform: translateX(5px);
        }
        a {
            text-decoration: none;
            color: #333;
            font-size: 18px;
            display: block;
        }
    </style>
</head>
<body>
    <h1>我的Rmarkdown笔记导航</h1>
    <ul>
"""

for file_name in sorted(html_files):
    # 因为路径有空格，需要url编码
    file_url = urllib.parse.quote(file_name)
    link = f"{html_folder.replace(' ', '%20')}/{file_url}"
    display_name = file_name.replace('.html', '')
    html_content += f'        <li><a href="{link}" target="_blank">{display_name}</a></li>\n'

html_content += """    </ul>
</body>
</html>
"""

# 写入文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ 成功生成美化版 {output_file}！（已排除非笔记文件）")
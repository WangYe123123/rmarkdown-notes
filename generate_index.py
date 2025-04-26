import os
import urllib.parse
import re

# 指定HTML文件所在的文件夹（相对于仓库根目录）
html_folder = '2-PROJECTS (Code Notes)/scripts'

# 要排除在目录之外的文件
excluded_files = ['header.html']

# 输出index.html文件
output_file = 'index.html'

# 自然排序方法（按数字顺序排序，而不是字符串顺序）
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

# 遍历HTML文件，排除不需要的
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
            background-color: #f0f8ff;
            margin: 40px;
            color: #333;
        }
        h1 {
            text-align: center;
            color: #2196F3; /* 蓝色主题 */
        }
        ul {
            list-style-type: none;
            padding: 0;
            max-width: 700px;
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
            background: #e3f2fd;
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

# 排序html文件
for file_name in sorted(html_files, key=natural_sort_key):
    # url编码处理路径
    file_url = urllib.parse.quote(file_name)
    link = f"{html_folder.replace(' ', '%20')}/{file_url}"

    # 美化显示标题：去掉开头的数字和符号，只留中文标题
    display_name = re.sub(r'^\d+[-_、\s]*', '', file_name.replace('.html', ''))

    html_content += f'        <li><a href="{link}" target="_blank">{display_name}</a></li>\n'

html_content += """    </ul>
</body>
</html>
"""

# 写入index.html
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✅ 成功生成美化版 {output_file}！")
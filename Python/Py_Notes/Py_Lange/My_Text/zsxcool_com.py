# Author : .CseiseiG.
# -*- codeing = utf-8 -*-
# @Time : 2022/10/14 22:25
# @Author : 12542
# @File : zsxcool_com.py
# @Software : PyCharm


import requests
import re


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                  'x64) AppleWebKit/537.36 (KHTML, like Ge'
                  'cko) \Chrome/106.0.0.0 Safari/537.36'
}

for page in range(0, 200, 25):
    url = f"https://movie.douban.com/top250?start={page}&filter="

    respons = requests.get(url=url, headers=headers).text

    titles = re.findall(r'<span class="title">(.*?)</span>', respons, re.S)

    f = open(f"top_250_{page}.txt", "w", encoding="utf-8")
    # f.writelines(titles)
    f.write("\n".join(titles))
    f.close()

print("写入成功！")

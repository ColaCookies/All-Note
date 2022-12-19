# Author : .CseiseiG.
# -*- codeing = utf-8 -*-
# @Time : 2022/10/24 15:10
# @Author : 12542
# @File : top_hot_UK.py
# @Software : PyCharm

import requests

m_url = "https://webfs.ali.kugou.com/202210241511/aa9821ac37366bd58117d01f27c7994f/KGTX/CLTX001/a2b996fc632a8f47a133ab6dc170c3d2.mp3"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}

m_resp = requests.get(url=m_url, headers=headers)


with open('Wake.mp3', 'wb') as f:
    f.write(m_resp.content)
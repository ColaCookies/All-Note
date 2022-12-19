- ## 解析图片链接获取图片二进制数据

```py
img_data = requests.get(url=img_url, headers=headers).content
```
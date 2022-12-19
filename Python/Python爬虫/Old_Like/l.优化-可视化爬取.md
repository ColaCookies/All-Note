- ## 通过 for 循环爬取指定页面

```py
for page in range(9, 11):
```
- ## 添加爬取页数使爬取可视

```py
print(f"===正在爬取第{page}页===")
```
- ## 添加页数
```py
url = {f"https://www.hexuexiao.cn/meinv/guzhuang/list-{page}.html"}
```
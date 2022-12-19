- ## 使用 for 循环逐个解析相册

```py
for href in href_list:
```
- ## 获取相册网页源码

```py
href_data = requests.get(url=href, headers=headers).text
```
- ## 再次转换数据类型,使用 Xpath 解析数据

```py
selector_2 = parsel.Selector(href_data)
```
- ## 解析相册源码获取图片链接

```py
img_url = selector_2.xpath("//div[@class='col-xs-4 text-left']/a/@href").get()
```
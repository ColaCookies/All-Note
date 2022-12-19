- ## 列出网页下所有相册链接

```py
href_list = selector.xpath("//div[@class='waterfall_1box']/dl/dd/a/@href").getall()
```
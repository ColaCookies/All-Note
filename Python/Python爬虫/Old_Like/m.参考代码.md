```py

import requests
import parsel

for page in range(7, 21):
    print("="*10,f'第{page}页ing', "="*10)
    url = f'https://wallhaven.cc/hot?page={page}'
    headers = {
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
	    (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
    }
    respons = requests.get(url=url, headers=headers).text

    if len(respons) >= 200:
        print("#"*10, "解析成功!", "#"*10)

    selects = parsel.Selector(respons)
    img_list_url = selects.xpath('//li/figure/a/@href').getall()

    for img_list in img_list_url:
        respon = requests.get(url=img_list, headers=headers).text
        select = parsel.Selector(respon)
        img_url = select.xpath('//div[@class="scrollbox"]/img/@src').get()

        img_data = requests.get(url=img_url, headers=headers).content

        img_name = img_url.split('-')[-1]

        with open('image\\' + img_name, mode='wb') as f:
            f.write(img_data)
            print("保存完成!", img_name)
    print("^"*10, f"第{page}页爬取结束!", "^"*10)
    print('\n')

```

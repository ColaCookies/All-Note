- ## 打开文件夹并写入

```py
with open('image\\' + file_name, mode='wb') as f :

	f.write(img_data)
	
	print("保存完成！", file_name)
```
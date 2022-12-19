### 4.3 创建数值列表

- 使用 `range()` 函数

|    range(6)    | range(1, 6)  | range(1, 6, 2) |
| :------------: | :----------: | :------------: |
| >>>0 1 2 3 4 5 | >>>1 2 3 4 5 |    >>>1 3 5    |

- 使用 ` range()` 创建数字列表 (两个星号 `**` 表示乘方运算)

    ```python
    #输出一个数字列表
    number = list(range(1 ,6 ,2))
    print(number)
    >>>[1, 3, 5]
    
    # (1-10)的乘方运算
    squares = []
    for figure in range(1, 11):
        square = figure ** 2
        squares.append(square)
    print(squares)
    ```

- 对数字列表进行简单的统计计算

| min()  | max()  | sum() |
| :----: | :----: | :---: |
| 最小值 | 最大值 | 求和  |

- 列表解析将 ```for``` 循环和创建新元素的代码合并成一行， 并自动附加新元素

```python
#l
squares = [value ** 2 for value in range(1, 11)]
```

### 4.4 使用列表的一部分

- 切片 ( [ 起始索引 : 终止索引 ] 例：`numbers = [1, 2, 3, 4, 5]` )

|   [1 : 5]    |     [ : 5]      |    [1 : ]    |  [-3 : ]  | [ : -3] |      [ : ]      |
| :----------: | :-------------: | :----------: | :-------: | :-----: | :-------------: |
| [2, 3, 4, 5] | [1, 2, 3, 4, 5] | [2, 3, 4, 5] | [3, 4, 5] | [1, 2]  | [1, 2, 3, 4, 5] |

- 遍历切片

```python
# 只遍历前三个数字
numbers = [1, 2, 3, 4, 5]
for number in numbers[ : 3]:
    print(number)
>>>1 2 3
```

- 复制列表方法是同时省略起始索引和终止索引（ [ : ] ）

```python
#复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
cbll_foods = my_foods[:]
>>>['pizza', 'falafel', 'carrot cake']
```

### 4.5  元组

- Python将不能修改的值称为==不可变的==，而不可变的列表被称为==元组==
- 定义元组 使用（圆括号）而非【中括号】 
- 修改元组既重新定义整个元组

```Python
#元组重新定义
numbers = (1, 2, 3, 4, 5)
for number in numbers：
	print(number)
>>>1 2 3 4 5
numbers = (2, 3, 4)
for number in numbers:
    print(number)
>>>2 3 4
```




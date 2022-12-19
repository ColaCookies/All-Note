### 5.1 一个简单的示例



###  5.2 条件测试

- 检查是否相等 " == "

```python
#判断car的值是否是bmw
>>> car = 'bwm'
>>> car == 'bmw'
True
```

- 检查是否相等是忽略大小

```python
>>> car = 'Bmw'
>>> car.lower() = 'bmw'
True
```

- 数值比较

- 检查多个条件

  - 使用 ` and` 检查多个条件

  ```python
  #一个条件未达到所以为False
  >>> age_0 = 22
  >>> age_1 = 28
  >>> age_0 >= 21 and age_1 = 21
  False
  #两个条件都达到所以为Ture
  >>> age_1 = 22
  >>> age_0 >= 21 and age_1 >= 21
  True
  ```

  - 改善可读性，可将每个测试分别放在一对圆括号内

  ```python
  (age_0 >= 21) and (age_1 >= 21)
  ```

  - 使用 ` or` 检查多个条件

  ```python
  #一个条件满足所以为True
  >>> age_0 = 22
  >>> age_1 = 18
  >>> age_0 >= 21 or age_1 >= 21
  True
  #两个条件都为达到所以为Flase
  >>> age_0 = 18
  >>> age_0 >= 21 or age_1 >= 21 
  False
  ```

- 检查特定值是否包含在列表中使用 `in` 

```python
>>> numbers = ['1', '2', '3']
>>> '1' in numbers
True
>>> '4' in numbers
False
```

- 检查特定值是否不包含在列表中

```Python
numbers = ['1', '2', '3']
number = '4'
if number not in numbers:
    print(f"{number.title()}, you can not in numbers.")
```

- 布尔表达式(布尔值通常记录条件，如游戏是否正常运行，或者用户是否可以编辑网站的特定内容)

```python
cbl_959 =  True
zl_225 = True
cbl_other = False
```

###  5.3 `if` 语句

- 简单的 `if` 语句
- `if - else` 语句
- `if - else - else` 语句
- 使用多个 `else` 代码块
- 省略 `else` 代码块
- 测试多个条件

```python
#多个if语句可判断多次
numbers = ['1', '2']
if '1' in numbers:
    print('1 of the number')
if '3' in numbers:
    print('3 of the number')
if '2' in numbers:
    print('2 of the number')
print('\nOK')
```

- 如果想执行一个代码块，就使用 `if-else-else` 结构；如果要执行多个代码块，就使用一系列独立的 `if` 语句

# 									End




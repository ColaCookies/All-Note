### 3.1 列表

- 列表由一系列按特定顺序排列的元素组成。
- Python 中，用 [ ] 表示列表，并用逗号分隔其中元素。

```python
#创建列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
```

- 访问列表元素 `print(bicyles[0].title)`
- 索引是从 0 开始而不是从 1 开始，索引为 -1 访问列表最后一个元素、-2 倒数第二个···。
- 使用列表中的各个值

```python
#fz
message = f"My first bicycle was a {bicycles[0].title}."
```

### 3.2 修改、添加和删除元素

- 修改列表元素 `bicycles[0] = 'yamaha' `
- 添加列表元素
  - ` bicycles.append('ducati')` 末尾
  - `bicycles.insert(0, ducati)` 在列表任何位置添加
- 删除列表元素
  - 使用 `del` 语句删除 `del bicycles[0]` 得知道删除元素索引
  - 使用 `pop()` 删除 `popped_bicycles = bicycles.pop() ` 删除列表末尾元素，删除后还可继续使用 `print(popped_bicycles)`
  - 弹出列表中任何位置处的元素 `first_owend = bicycles.pop(0)` 在括号中添加索引.
  - 删除的元素不使用用 `del` 删除的元素还要使用用 `pop()`
  - 根据值删除元素` remove()` ` bicycles.remove('redline')`
    - 若后续还要使用删除元素，可将删除元素赋值给变量在删除 `too_expensive = 'redline'`
    - `remove()` 只删除第一个指定值。如果删除值在列表中出现多次须使用 for 循环删除

### 3.3 组织列表

- 使用 `sort()` 对列表永久排序 `bicycles.sort()` 按字母顺序，向 sort()传递参数`reverse = True` 按与字母相反顺序排序。
- 使用函数 ` sorted()` 对列表临时排序 ` print(sorted(bicycles))`

- 倒着打印列表 ` reverse()` `bicycles.reverse()` 不是按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序。
- 确定列表长度 ` len()` ` len(bicycles)`

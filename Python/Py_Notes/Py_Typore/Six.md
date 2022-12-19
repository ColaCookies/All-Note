### 6.1 一个简单的字典

- 字典用 `{}` 表示

```Python
#简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
>>> green 5
```

### 6.2 使用字典

- 字典是一系列键值对，每个键都与一个值相关联。键值对是两个相关联的值。
- 字典是一种动态结构，可随时在其中添加键值对。

```Python
#添加键值对
alien_0['x_position'] = 2
alien_0['y_position'] = 25
```

- 修改字典中的值，可依次指定字典名、用方括号括起键，以及与该键相关联的新值。
- 可使用 `del` 语句将相应的删除键值对彻底删除。

```python
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
```

- 由类对象组成字典

```python
favorite_languages = {
    'jen': 'Python'
    'sarah': 'C'
    'edward': 'ruby'
}
```

- 使用 `get()` 来访问值
  - 

### 6.3 遍历字典

- 遍历所有键值对

# 初识Vim

## vim的多种模式

### 插入的模式

- `a / A` 单词后 / 行后插入 ( append )
- `i / I` 单词前 / 行前插入 ( insert )
- `o / O` 在下 / 上面打开一行 ( open a line below )
- `:vs` 分屏 (竖分)
- `:sp` 分屏(横分)
- `:set nu` 

## 快速移动大法

### 快速纠错

- `ctrl + h` 删除上一个字符
- `ctrl + w` 删除上一个单词
- `ctrl + u` 删除当前行

### 快速移动

- `gi` 回到最后一次编辑位置
- `w / W` 移动到下一个 word / WORD 开头
- `e / E` 移动到下一个word / WORD 结尾
- `b / B` 移动到上一个word / WORD 开头   *可以理解为 background*
- word 指的是以非空白符分割的单词, WORD 以非空白符分割的单词

### 行间搜索

- 使用 `f{char}` 可以移动到 char 字符上, `t` 移动到 char 的前一个字符
- 用 分号 ( `;` ) / 逗号 ( `,`) 继续搜索下一个 / 上一个
- `F` 搜前面的字符

### 水平移动

- **`0` 移动到行首第一个字符**, `^` 移动到第一个非空白字符
- **`$` 移动到行尾**, `g_` 移动到行尾非空白字符

### 垂直移动

- `( )` 在句子间移动
- `{ }` 在段落之间移动

### 页面移

- `gg / G` 移动到文件开头 / 结尾
- `ctrl + o` 快速返回
- `H / M / L` 跳转到屏幕的开头 ( Head ) , 中间 ( Middle ) 和结尾 ( Lower )
- `ctrl + u / ctrl + f` 上下翻页 ( upword / forword )
- `zz` 把屏幕置为中间

## 快速增删改查

### 增加字符

- [插入](#插入的模式)

### 快速删除

- `x` 快速删除一个字符
- `d` 配合文本对象快速删除一个单词 daw / diw ( delete around word )
- `d` 和 `x` 可以搭配数字来执行多次
- `dd` 删除当前行
- `dt)` 删除到右括号
- `d$` 从当前位置删除到行尾
- `d0` 从当前位置删除到行首
- `2dd` 删除两行
- `4x` 删除四个字符

### 快速修改

- `r` 替换一个字符 ( replace )
- `c` 配合文本对象进行修改，相当于替换并插入 ( change )
- `s` 替换并进入插入模式 ( substitute )
- `% s/foo/bar/g` 全局替换



### 我的Vim笔记
1. 常用命令
	- R 光标功能从插入变为替换
	- r 光标所在位置替换单个字符
	- Y 拷贝一行
	- U
	- u 撤销
	- I 行首插入
	- i 当前位置插入
	- O 向上插入一行
	- o 向下插入一行
	- P 粘贴在光标**前面**
	- p 粘贴在光标**后面**
	- A 光标移动到行尾并插入
	- a 光标后插入
	- S 删除光标所在行并插入

 	- s 删除光标所在处的字符并插入
 	- D
 	- J 合并光标所在的下一行
 	- X
 	- x
 	- C 从光标位置删除至行尾并插入
 	- k 上
 	- j 下
 	- h 左
 	- l 右

2. 常用操作
	- y 拷贝
	- d
	- c 修改
	- `<` 反缩进
	- `>` 缩进

3. 常用动作
	- W/w 下一个单词
	- E/e 词尾
	- { 段首
	- } 段尾

Markdown中输入三个 ` 然后输入编程语言可以快捷创建代码框

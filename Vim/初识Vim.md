# 初识 Vim

## vim 的多种模式

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
- `e / E` 移动到下一个 word / WORD 结尾
- `b / B` 移动到上一个 word / WORD 开头 _可以理解为 background_
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

- `gg / G` 移动到文件开头和结尾
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

### Vim 查询

- 是使用 `/ 或 ?` 进行向前向后搜索
- 使用 `n 或 N` 跳转到上一个或者下一个匹配
- 使用 `* 或 #` 进行当前单词的前向和后向匹配

## Vim 替换命令

- `substitute` 命令允许我们查找并且替换掉文本, 并且支持正则表达式
- `:[ range ] s [ ubstitute ] / { pattern } / {string} /  [ flags ]`
- range 表示范围 比如: 10,20 表示 10 - 20 行, % 表示全部
- pattern 是要替换的模式
- string 是替换后的文本
- flags 替换标志位
  - g ( global ) 表示全局范围内执行
  - c ( confirm ) 表示确认, 可以确认或拒绝修改
  - n ( number ) 报告匹配到的次数而不替换, 可以用来查询匹配次数

## Vim 多文件操作

### 多文件操作相关概念

- Buffer 是指打开的一个文件的内存缓冲区
- 窗口时 Buffer 可视化的分割区域
- Tab 可以组织窗口为一个工作区

1. Buffer
   - Vim 打开一个文件后会加载文件内容到缓冲区
   - 之后的修改都是针对内存中的缓冲区，并不会直接保存到文件
   - 直到我们执行：`w(write)` 的时候才会把修改的内容写到文件里

2. Buffer 切换
   - 使用 `:ls` 会当前缓冲区，然后使用 `:b n` 跳转到第n个缓冲区域
   - `:bpre :bnext :bfirst :blast`
   - 或者用 `:b buffer_name` 加上 tab 补全来跳转

3. Window 窗口
   - 一个缓冲区可以分割成多个窗口，每个窗口也可以打开不同缓冲区
   - `<Ctrl+w> s 水平分割`，`<Ctrl+w> v 垂直分割` 或者 `:sp` 和 `:vs`
   - 每个窗口可以继续被无线分割

4. Tab(标签页) 将窗口分组
   - 用的不多

## Vim 的 tect object

### 文本对象操作方式

- [number] <command> [text_object]
- number:次数，command:命令，d( delete)，c(change)，y(yank)
- text_object 是要操作的文本对象，比如单词 w(word)，句子 s(sentence)，段落 p(paragraph)

### 示例

- `iw` 表示 inner_word。如果键入vim命令，那么首先v将进去选择模式，然后 iw 将选中当前单词
- `aw` 表示 around_word，它不但会选中当前单词，还会包含当前单词之后的空格
- `iW/aw`
- `is/as`
- `ip/ap`
- `3daw` 删除三个单词
- `3cw` 删除三个单词并进入插入模式
- `vi + 符号` 选中符号中的字符
- `ci + 符号` 删除符号中的字符，并进入插入模式

## Vim 复制粘贴与寄存器的使用

### Vim Normal模式复制粘贴

- normal 模式下
  - 复制 y ( yank )
  - 粘贴 p ( Put )
  - 剪贴 d 和 p
- 使用 v(visual) 命令选中所要复制的地方，然后使用 p 粘贴
- 配合文本对象使用
  - 使用 `yiw` 复制一个单词
  - `yy` 复制一行
- Vim 中的 剪切( cut ) 复制( copy ) 粘贴( paste ) 分别是 delete / yank / put

### Insert 模式下的复制粘贴

- 在 vimrc 中设置了 `autoindent` ，粘贴 Python 代码缩进错乱
- 需要使用 `:set paste` 和 `:set nopaste`

### Vim 的寄存器

- Vim 里操作的是寄存器而不是系统剪切板
- 用 `d` 删除或者 `y` 复制的内容都放到了 "无名寄存器"
- 用 `X` 删除一个字符放到无名寄存器，然后 `P` 粘贴，可以调换两字符
- Vim 不使用单一剪切板进行剪贴、复制与粘贴，而是多组寄存器
- 通过 `"{register}` 前缀可以指定寄存器，不指定默认用无名寄存器
- 使用 `"ayim` 复制一个单词到寄存器a中，`"bdd` 删除当前行到寄存器b中

## Vim 宏

- Vim 使用 `q` 来录制，同时也是 `q` 结束
- 使用 `q{register}` 选择要保存的寄存器，把录制的命令保存在其中
- 使用 `@{register}` 回放寄存器中保存的命令
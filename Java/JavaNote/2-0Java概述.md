# Java 概述

## Java 转义字符

### 常用

1. `\t`: 一个制表位，实现对齐的功能
2. `\n`: 换行符
3. `\\`: 一个 \
4. `\"`: 一个 "
5. `\'`: 一个 '
6. `\r`: 一个回车
*注意：**回车**与**换行**是两个概念*

## 注释 （comment）

1. 单行注释 `//注释`
2. 多行注释 `/*注释*/`
3. 文档注释 `javadoc -d f:\\temp -author -version .\_0024.java`
*注意:多行注释里面不允许又多行注释嵌套*

```java
/**
 * @author 大头
 * @version 2.25
 */
```

## 代码规范

1. 类、方法的注释，要以 javadoc 的方式来写
2. 非 Java Doc 的注释，往往是给代码的维护者看的，着重告述读者为什么这样写， 如何修改，注意什么问题等
3. 使用 tab 操作，实现缩进，默认整体向右边移动，时候用 shift+tab 整体向左移
4. 运算符和 = 两边习惯性各加一个空格。*比如 2 + 4* 5 + 345 = 89*
5. 行宽度不要超过 **80** 字符
6. 代码编写 **行尾风格** 和 **次行风格**

```java
//行尾风格
public class _0024 {
    public static void main(String[] args) {
        System.out.println("hello225,CseiseiG!");
    }
}
```

```java
//次行风格
public class _0024
{
    public static void main(String[] args)
    {
        System.out.println("hello225,CseiseiG!");
    }
}
```

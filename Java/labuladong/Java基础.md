# labuladong 的 Java 基础

## 数组

```java
int m = 5, n = 10;

// 初始化一个大小为10的 int 数组
// 其中的值默认初始化 为 0
int[] nums = new int[n];

// 初始化一个 m * n 的二维布尔数组
// 其中的元素默认初始化为 false
boolean[][] visited = new boolean[][];
```

作为原始类型，这就类似 C 语言的 int 数组，操作起来比较麻烦，所以我们更多地使用 ArrayList 动态数组

## 字符串 String

```java
String s1 = "hello world";

// 获取 s1[2] 那个字符
char c = s1.charAt(2);

char[] chars = s1.toCharArray();
chars[1] = 'a';
String s2 = new String(chars);

// 输出：hallo world
System.out.println(s2);

// 注意，一定要用 equals 方法判断字符串是否相同
if (s1.equals(s2)) {
    // s1 和 s2 相同
}
else {
    // s1 和 s2 不相同
}

// 字符串可以用加号进行拼接
String s3 = s1 + "!";

// 输出：hello world!
System.out.println(s3);
```

## 动态数组 ArrayList

ArrayList 相当于把 Java 内置的数组类型做了包装，初始化方法：

```java
// 初始化一个存储 String 类型的动态数组
ArrayList<String> nums = new ArrayList<>();

// 初始化一个存储 int 类型的动态数组
ArrayList<Integer> strings = new ArrayList<>();

// 常用的方法如下（E 代表元素类型）：

// 判断数组是否为空
boolean isEmpty()

// 返回数组的元素个数
int    size()

// 返回索引 index 的元素
E get(int index)

// 在数组尾部添加元素 e
boolean    add(E e)
```

## 双链表 LinkedList

ArrayList 列表底层是数组实现的，而 LinkedList 底层是双链表实现的，初始化方法也是类似：

```java
// 初始化一个存储 int 类型的双链表
LinkedList<Integer> nums = new LinkedList<>();

// 初始化一个存储 String 类型的双链表
LinkedList<String> strings = new LinkedList<>();
本课程中会用到的方法如下（E 代表元素类型）：

// 判断链表是否为空
boolean    isEmpty()

// 返回链表的元素个数
int    size()

// 判断链表中是否存在元素 o
boolean    contains(Object o)

// 在链表尾部添加元素 e
boolean    add(E e)

// 在链表尾部添加元素 e
void addLast(E e)

// 在链表头部添加元素 e
void addFirst(E e)

// 删除链表头部第一个元素
E removeFirst()

// 删除链表尾部最后一个元素
E removeLast()
```

## 哈希表 HashMap

哈希表是非常常用的数据结构，用来存储键值对映射，初始化方法：

```java
// 整数映射到字符串的哈希表
HashMap<Integer, String> map = new HashMap<>();

// 字符串映射到数组的哈希表
HashMap<String, int[]> map = new HashMap<>();
本课程中会用到的方法如下（K 代表键的类型，V 代表值的类型）：

// 判断哈希表中是否存在键 key
boolean    containsKey(Object key)

// 获得键 key 对应的值，若 key 不存在，则返回 null
V get(Object key)

// 将 key, value 键值对存入哈希表
V put(K key, V value)

// 如果 key 存在，删除 key 并返回对应的值
V remove(Object key)
```

## 哈希集合 HashSet

初始化方法：

```java
// 新建一个存储 String 的哈希集合
Set<String> set = new HashSet<>();
本课程中用到的方法（E 表示元素类型）：

// 如果 e 不存在，则添加 e 到哈希集合
boolean    add(E e)

// 判断元素 o 是否存在于哈希集合中
boolean    contains(Object o)

// 如果元素 o 存在，在删除元素 o
boolean    remove(Object o)
```

## Java 类的一些基本用法

# 操作符

> [syntax_and_semantics/operators.md][operators]
>
> [commit 45485f2aa890b84587571fd343d1c4f5b87e9361][commit]

[operators]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/operators.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/45485f2aa890b84587571fd343d1c4f5b87e9361

像 `+` 和 `-` 这样的操作符都是正常的方法调用。例如：

```crystal
a + b
```

is the same as:

```crystal
a.+(b)
```

可以像下面这样为一个类型定义一个操作符：

```crystal
struct Vector2
  getter x, y

  def initialize(@x : Int32, @y : Int32)
  end

  def +(other)
    Vector2.new(x + other.x, y + other.y)
  end
end

v1 = Vector2.new(1, 2)
v2 = Vector2.new(3, 4)
v1 + v2               #=> Vector2(@x=4, @y=6)
```

下面是所有操作符的列表以及其通用含义。

## 一元操作符

```crystal
+   # 正号
-   # 负号
!   # 非
~   # 按位求补
```

其都是无参定义。例如

```crystal
struct Vector2
  def -
    Vector2.new(-x, -y)
  end
end

v1 = Vector2.new(1, 2)
-v1                    #=> Vector2(@x=-1, @y=-2)
```

**注意:** `!` （非）无法定义为一个方法（其意义不可更改）。

## 二元操作符

* `+` – 加法
* `-` – 减法
* `*` – 乘法
* `/` – 除法
* `%` – 取模
* `&` – 按位与
* `|` – 按位或
* `^` – 按位异或
* `**` – 指数运算
* `<<` – 左移，追加
* `>>` – 右移
* `==` – 等于
* `!=` – 不等于
* `<` – 小于
* `<=` – 小于等于
* `>` – 大于
* `>=` – 大于等于
* `<=>` – 比较
* `===` – [真实等于](case.html)

## 索引

```crystal
[]  # 数组索引（越界抛异常）
[]? # 数组索引（越界返回 nil）
[]= # 数组索引赋值
```

例如：

```crystal
class MyArray
  def [](index)
    # ...
  end

  def [](index1, index2, index3)
    # ...
  end

  def []=(index, value)
    # ...
  end
end

array = MyArray.new

array[1]       # invokes the first method
array[1, 2, 3] # invokes the second method
array[1] = 2   # invokes the third method

array.[](1)       # invokes the first method
array.[](1, 2, 3) # invokes the second method
array.[]=(1, 2)   # invokes the third method
```

## 意义

可以为操作符赋予任何意义，但遵从上面所列方便于避免隐晦的或异常行为的代码。

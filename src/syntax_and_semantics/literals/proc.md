# 过程(Proc)

[过程(Proc)](http://crystal-lang.org/api/Proc.html) 表示一个可携带内容（闭包数据）函数指针。其通常用一个过程常量来创建：

```crystal
# A proc without arguments
->{ 1 } # Proc(Int32)

# A proc with one argument
->(x : Int32) { x.to_s } # Proc(Int32, String)

# A proc with two arguments:
->(x : Int32, y : Int32) { x + y } # Proc(Int32, Int32, Int32)
```
参数类型是必不可少的，除非将一个过程常量发送给 C 绑定中一个库 `fun` 。


返回值类型可以从过程体中推断。

同时也提供特定的 `new` 方法：

```crystal
Proc(Int32, String).new { |x| x.to_s } # Proc(Int32, String)
```

这种格式可以让你指定返回值类型以反过来检测过程体。

## 过程类型

可以和这样表示一个过程类型：

```crystal
# A Proc accepting a single Int32 argument and returning a String
Proc(Int32, String)

# A proc accepting no arguments and returning Void
Proc(Void)

# A proc accepting two arguments (one Int32 and one String) and returning a Char
Proc(Int32, String, Char)
```

在类型限制中，泛型类型参数以及其他需要参数的地方，可以像在[类型(type)](../type_grammar.html)中解释的那样使用简化语法：

```crystal
# An array of Proc(Int32, String, Char)
Array(Int32, String -> Char)
```

## 调用

为调用过程，可以在过程之上调用 `call` 方法。参数个数与类型必须和过程的参数个数和类型相匹配：

```crystal
proc = ->(x : Int32, y : Int32) { x + y }
proc.call(1, 2) #=> 3
```

## 从方法中创建过程

可以从一个已存在的方法中创建过程：

```crystal
def one
  1
end

proc = ->one
proc.call #=> 1
```

如果该方法有参数，则需要指定其类型：

```crystal
def plus_one(x)
  x + 1
end

proc = ->plus_one(Int32)
proc.call(41) #=> 42
```

过程也可以指定一个接收者：

```crystal
str = "hello"
proc = ->str.count(Char)
proc.call('e') #=> 1
proc.call('l') #=> 2
```

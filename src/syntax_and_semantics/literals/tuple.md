# 元组(Tuple)

[元组(Tuple)](http://crystal-lang.org/api/Tuple.html) 通常以元组常量来创建：

```crystal
tuple = {1, "hello", 'x'} # Tuple(Int32, String, Char)
tuple[0]                  #=> 1       (Int32)
tuple[1]                  #=> "hello" (String)
tuple[2]                  #=> 'x'     (Char)
```

可以使用 [Tuple.new](http://crystal-lang.org/api/Tuple.html#new%28%2Aargs%29-class-method) 来创建一个空元组。

可以这样描述一个元组

```crystal
# The type denoting a tuple of Int32, String and Char
Tuple(Int32, String, Char)
```

在类型约束中，泛型参数以及其他需要一个参数的地方，可以像[类型语法](../type_grammar.html)中描述的那样使用简化语法：

```crystal
# An array of tuples of Int32, String and Char
Array({Int32, String, Char})
```

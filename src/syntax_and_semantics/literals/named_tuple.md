# 具名元组(NamedTuple)

[具名元组(NamedTuple)](http://crystal-lang.org/api/NamedTuple.html) 通常用一个具有名字的元组字面量来创建：:

```crystal
tuple = {name: "Crystal", year: 2011} # NamedTuple(name: String, year: Int32)
tuple[:name] # => "Crystal" (String)
tuple[:year] # => 2011      (Int32)
```

可以这样来表示一个具名元组的类型：

```crystal
# The type denoting a named tuple of x: Int32, y: String
NamedTuple(x: Int32, y: String)
```

类型约束中，在泛型类型参数以及其他需要类型的地方，可以像在[类型语法](../type_grammar.html)中解释的那样使用简化语法：

```crystal
# An array of named tuples of x: Int32, y: String
Array({x: Int32, y: String})
```

具名元组的 key 也可以是一个字符串：

```crystal
{"this is a key": 1}
```

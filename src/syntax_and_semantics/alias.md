# 别名

可以用 `alias` 来给类型起一个不同的名字：

```crystal
alias PInt32 = Pointer(Int32)

ptr = PInt32.malloc(1) # : Pointer(Int32)
```

每次使用别名时，编译器会用其所引用的类型替换它。

在避免写长类型名时，别名是非常有用的，但也要考虑递归类型。

```crystal
alias RecArray = Array(Int32) | Array(RecArray)

ary = [] of RecArray
ary.push [1, 2, 3]
ary.push ary
ary #=> [[1, 2, 3], [...]]
```

递归类型的一个真实例子是 json ：

```crystal
module Json
  alias Type = Nil |
               Bool |
               Int64 |
               Float64 |
               String |
               Array(Type) |
               Hash(String, Type)
end
```

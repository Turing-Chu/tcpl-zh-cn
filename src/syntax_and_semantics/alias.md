# 别名

> [syntax_and_semantics/alias.md][alias]
>
> [commit c55247a364ee0c01fd8b1e3d78f2e1352faaa1ea][commit]

[alias]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/alias.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/c55247a364ee0c01fd8b1e3d78f2e1352faaa1ea

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

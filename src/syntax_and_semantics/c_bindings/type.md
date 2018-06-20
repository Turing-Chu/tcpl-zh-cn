# 类型

> [syntax_and_semantics/c_bindings/type.md][type]
>
> [commit <hash>][commit]

[type]: xx
[commit]: comit

`lib` 中的 `type` 声明了一种 C 语言的 `typedef`，但比 C 语言的 `typedef` 更强大：

```crystal
lib X
  type MyInt = Int32
end
```

和 C 语言不同，`Int32` 和 `MyInt` 是无法互换的：

```crystal
lib X
  type MyInt = Int32

  fun some_fun(value : MyInt)
end

X.some_fun 1 # Error: argument 'value' of 'X#some_fun'
             # must be X::MyInt, not Int32
```

因此， `type` 声明对于那些由封装的 C 库所创建的难懂的类型是非常有用的。例如，从 `fopen` 函数返回的 `FILE` 类型。

Refer to the [type grammar](../type_grammar.html) for the notation used in typedef types.


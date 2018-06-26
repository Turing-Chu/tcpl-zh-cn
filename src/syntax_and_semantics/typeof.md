# typeof

> [syntax_and_semantics/typeof.md][typeof]
>
> [commit ab174eb5c083fdad72b78c59414a73e9631653c6][commit]

[commit]: https://github.com/crystal-lang/crystal-book/commit/ab174eb5c083fdad72b78c59414a73e9631653c6
[typeof]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/typeof.md

`typeof` 表达式返回一个表达式的类型：

```crystal
a = 1
b = typeof(a) #=> Int32
```

其接收多个参数，结果是表达式类型的联合体：

```crystal
typeof(1, "a", 'a') #=> (Int32 | String | Char)
```

其在一般代码中经常用到，用于编译器的类型推断容量：

```crystal
hash = {} of Int32 => String
another_hash = typeof(hash).new #:: Hash(Int32, String)
```
因为 `typeof` 实际上并不计算表达式，它只能用于编译时的方法中，例如，递归的构成一个内嵌类型参数的联合类型：

```crystal
class Array
  def self.elem_type(typ)
    if typ.is_a?(Array)
      elem_type(typ.first)
    else
      typ
    end
  end
end

nest = [1, ["b", [:c, ['d']]]]
flat = Array(typeof(Array.elem_type(nest))).new
typeof(nest) #=> Array(Int32 | Array(String | Array(Symbol | Array(Char))))
typeof(flat) #=> Array(String | Int32 | Symbol | Char)
```

该表达式也可以在[类型语法](type_grammar.html)中使用。

# sizeof

> [syntax_and_semantics/sizeof.md][sizeof]
>
> [commit 0c157b7eaad13f191ddb73f148171f3579287279][commit]

[sizeof]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/sizeof.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/0c157b7eaad13f191ddb73f148171f3579287279

`sizeof` 表达式返回所给定类型字节大小的 `Int32` 类型值。例如：

```crystal
sizeof(Int32)  #=> 4
sizeof(Int64)  #=> 8
```

对于[引用](http://crystal-lang.org/api/Reference.html)类型来说，其大小等同于指针的大小：

```crystal
# On a 64 bits machine
sizeof(Pointer(Int32)) #=> 8
sizeof(String)         #=> 8
```

这是因为引用的内存是在堆上分配然后一个指针指向它。可以使用 [instance_sizeof](instance_sizeof.html) 来获取一个类的有效大小。

sizeof 的参数是一个[类型](type_grammar.html)，且常和 [typeof](typeof.html) 结合使用。

```crystal
a = 1
sizeof(typeof(a)) #=> 4
```

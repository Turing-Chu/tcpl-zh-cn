# 局部变量

> [syntax_and_semantics/local_variables.md][local_variables]
>
> [commit 1142db80f9452eacce300afd64a846c91ca5cd2f][commit]

[local_variables]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/local_variables.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/1142db80f9452eacce300afd64a846c91ca5cd2f

局部变量以小写字符开始。其以初次赋值变量来声明。

```crystal
name = "Crystal"
age = 1
```

其类型从他们的用法中推断，而不是其初始化变量。通常，局部变量只保留程序员所期望根据其在程序中的位置和用法的类型有关的值。

例如，以一个不同的表达式重新赋值让其变成表达式的类型：

```crystal
flower = "Tulip"
# At this point 'flower' is a String

flower = 1
# At this point 'flower' is an Int32
```

可在变量名前面使用下划线，但这些名字是编译器所保留的，因此，并不建议这样使用（而且这样做让程序更加难读）。

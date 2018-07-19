# if

> [syntax_and_semantics/if.md][if]
>
> [commit d9e62d44ba404aa389ffc81b32a547207a0ab68e][commit]

[if]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/if.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/d9e62d44ba404aa389ffc81b32a547207a0ab68e

`if` 计算给定 if 分支如果其条件为`真`。否则，计算 `else` 分支。

```crystal
a = 1
if a > 0
  a = 10
end
a #=> 10

b = 1
if b > 2
  b = 10
else
  b = 20
end
b #=> 20
```

可以用 `elsif` 来写一个 if-else-if 链：

```crystal
if some_condition
  do_something
elsif some_other_condition
  do_something_else
else
  do_that
end
```

在 `if` 之后，变量的类型依赖于在两个分支中使用的表达式的类型。

```crystal
a = 1
if some_condition
  a = "hello"
else
  a = true
end
# a : String | Bool

b = 1
if some_condition
  b = "hello"
end
# b : Int32 | String

if some_condition
  c = 1
else
  c = "hello"
end
# c : Int32 | String

if some_condition
  d = 1
end
# d : Int32 | Nil
```

注意如果在其中一个分支内声明变量而没有在另一个分支内声明，那么在 `if` 结尾该变量也会包含 `Nil` 类型。

在一个 `if` 分支的内部，变量的类型从在该分支之内的赋值之中获取，如果没有重新赋值的话，则是在该分支之前的赋值之中获取。

```crystal
a = 1
if some_condition
  a = "hello"
  # a : String
  a.size
end
# a : String | Int32
```

也就是说，变量的类型是最后一个赋值给变量的表达式的类型。

如果直到 `if` 的结尾其中一个分支从不会到达，像在一个 `return` 、`next` 、`break` 或 `raise` 的例子中，则在 `if` 结尾并不再考虑该变量类型：

```crystal
if some_condition
  e = 1
else
  e = "hello"
  # e : String
  return
end
# e : Int32
```

# 逻辑与操作符 &&

> [syntax_and_semantics/and.md][and]
>
> [commit 0bb5ad4d2622a98ee4fd93cc2216edf0d6a1485b][commit]

[and]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/and.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/0bb5ad4d2622a98ee4fd93cc2216edf0d6a1485b

`&&` 计算其左边的值。如果为*真*，则计算右边的值并持有改值。否则便持有左边的值。其类型为两边类型的并集。

可以认为 `&&` 是  `if` 的语法糖：

```crystal
some_exp1 && some_exp2

# The above is the same as:
tmp = some_exp1
if tmp
  some_exp2
else
  tmp
end
```

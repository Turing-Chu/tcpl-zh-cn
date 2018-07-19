# 用作后缀

> [syntax_and_semantics/as_a_suffix.md][as_a_suffix]
>
> [commit 0c157b7eaad13f191ddb73f148171f3579287279][commit]

[as_a_suffix]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/as_a_suffix.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/0c157b7eaad13f191ddb73f148171f3579287279

`if` 可以写在一个表达式的后缀之上：

```crystal
a = 2 if some_condition

# The above is the same as:
if some_condition
  a = 2
end
```

这有时候让代码读起来更自然。

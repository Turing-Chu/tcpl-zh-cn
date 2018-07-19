# 三元 if

> [syntax_and_semantics/ternary_if.md][ternary_if]
>
> [commit 0c157b7eaad13f191ddb73f148171f3579287279][commit]

[ternary_if]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/ternary_if.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/0c157b7eaad13f191ddb73f148171f3579287279

三元 `if` 可以以更简短的方式写 `if` 语句：

```crystal
a = 1 > 2 ? 3 : 4

# The above is the same as:
a = if 1 > 2
      3
    else
      4
    end
```

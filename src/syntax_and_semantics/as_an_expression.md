# 用作表达式

> [syntax_and_semantics/as_an_expression.md][as_an_expression]
> 
> [commit 0c157b7eaad13f191ddb73f148171f3579287279][commit]

[as_an_expression]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/as_an_expression.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/0c157b7eaad13f191ddb73f148171f3579287279

一个 `if` 的值是其每个分支最后一个表达式的值。

```crystal
a = if 2 > 1
      3
    else
      4
    end
a #=> 3
```

如果一个 `if` 分支是空的，或者缺失，则认为其有一个 `nil` 值。

```crystal
if 1 > 2
  3
end

# The above is the same as:
if 1 > 2
  3
else
  nil
end

# Another example:
if 1 > 2
else
  3
end

# The above is the same as:
if 1 > 2
  nil
else
  3
end
```

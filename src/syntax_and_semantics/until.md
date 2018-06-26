# until

> [syntax_and_semantics/until.md][until]
>
> [commit 0c157b7eaad13f191ddb73f148171f3579287279][commit]

[until]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/until.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/0c157b7eaad13f191ddb73f148171f3579287279
 
`until` 执行代码块直到其条件为*真*。`until` 只是一个 `while` 循环条件否定的语法糖：

```crystal
until some_condition
  do_this
end

# The above is the same as:
while !some_condition
  do_this
end
```

`break` 和 `next` 在 `until` 里面也可以使用。 

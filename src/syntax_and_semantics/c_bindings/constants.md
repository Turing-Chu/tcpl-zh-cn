# 常量

> [syntax_and_semantics/c_bindings/constants.md][constants]
>
> [commit 0c157b7eaad13f191ddb73f148171f3579287279][commit]

[constants]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/c_bindings/constants.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/0c157b7eaad13f191ddb73f148171f3579287279

也可以在一个 `lib` 声明中声明常量：

```crystal
@[Link("pcre")]
lib PCRE
  INFO_CAPTURECOUNT = 2
end

PCRE::INFO_CAPTURECOUNT #=> 2
```

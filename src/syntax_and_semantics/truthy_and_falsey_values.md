# 真值和假值

> [syntax_and_semantics/truthy_and_falsey_values.md][truthy_and_falsey_values]
> [commit eaf677bbbfb97952961d0b77d48c69f0ef741e7c][commit]

[truthy_and_falsey_values]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/truthy_and_falsey_values.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/eaf677bbbfb97952961d0b77d48c69f0ef741e7c

对于一个 `if` 、`unless` 、 `while` 或 `until` 的标记符号来说，*真*值被认为是一个真的值。*假*值在这些地方被认为是假的值。

唯一的假值是 `nil` ，`false` 和空指针（指针的内存地址为0）。其他的值都是真值。

# 字符(Char)

> [syntax_and_semantics/literals/char.md][char]
>
> [commit 33885563f889c30d6dc8f6ed37af937ee48ef6de][commit]
[char]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/literals/char.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/33885563f889c30d6dc8f6ed37af937ee48ef6de

一个[字符(Char)](http://crystal-lang.org/api/Char.html) 表示一个 32 位的 [Unicode](http://en.wikipedia.org/wiki/Unicode) [码点(code point)](http://en.wikipedia.org/wiki/Code_point) 。

通常用单引号括起来的 UTF-8 字符常量来创建字符。 

```crystal
'a'
'z'
'0'
'_'
'あ'
```

反斜杠(`\`) 表示一个特殊字符，它既可以表示转义序列，又可以表示一个 unicode 码点的数值。

可用的转义序列：

```crystal
'\'' # single quote
'\\' # backslash
'\b' # backspace
'\e' # escape
'\f' # form feed
'\n' # newline
'\r' # carriage return
'\t' # tab
'\v' # vertical tab
'\uNNNN' # hexadecimal unicode character
'\u{NNNN...}' # hexadecimal unicode character
```

反斜杠后跟一个 `u` 表示一个 unicode 码点。其既可以后跟四位精确的十六进制字符以表示 unicode 字节（ `\u0000` 到 `\uFFFF` ）或跟由大括号包围一到六位十六进制字符来表示一个数。

```crystal
'\u0041' # => 'A'
'\u{41}' # => 'A'
'\u{1F52E}' # => '&#x1F52E;'
```

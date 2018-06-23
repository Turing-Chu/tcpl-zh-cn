# 正则(Regex)

正则(Regular) 表达式由 [Regex](http://crystal-lang.org/api/Regex.html) 类来表示，其通常用一个字面量来创建：

```crystal
foo_or_bar = /foo|bar/
heeello    = /h(e+)llo/
integer    = /\d+/
```

正则表达式字面量由 `/` 来限定，且使用 [PCRE](http://pcre.org/pcre.txt) 语法。

正则之后可跟这些修饰词：

* i: ignore case (PCRE_CASELESS)
* m: multiline (PCRE_MULTILINE)
* x: extended (PCRE_EXTENDED)

例如

```crystal
r = /foo/imx
```
斜杠必须转义：

```crystal
slash = /\//
```

也有另一种语法：

```crystal
r = %r(regex with slash: /)
```

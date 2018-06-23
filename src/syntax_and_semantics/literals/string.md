# 字符串(String)

[字符串](http://crystal-lang.org/api/String.html) 表示一个 UTF-8 字符的不可变序列。

字符串通常以双引号（ `"` ）括起来的 UTF-8 字符串常量来创建。

```crystal
"hello world"
```

## 转义

字符串中的反斜杠代表特殊字符，或是一个转义字符，或是一个 unicode 码点的数值表示。

可用的转义序列

```crystal
"\"" # double quote
"\\" # backslash
"\b" # backspace
"\e" # escape
"\f" # form feed
"\n" # newline
"\r" # carriage return
"\t" # tab
"\v" # vertical tab
"\NNN" # octal ASCII character
"\xNN" # hexadecimal ASCII character
"\uNNNN" # hexadecimal unicode character
"\u{NNNN...}" # hexadecimal unicode character
```

反斜杠后的任何其他字符都被解释为该字符自身。

反斜杠后跟至多三个数字表示八进制数的一个码点。

```crystal
"\101" # => "A"
"\123" # => "S"
"\12"  # => "\n"
"\1"   # string with one character with code point 1
```

反斜杠后跟一个 `u` 表示一个 unicode 码点。其既可以明确地跟4位十六进制字符来表示 unicode 字节（ `\u0000` 到 `\uFFFF`）或由大括号包括的一到六位十六进制数的字符（ `\u{0} 到 `\u{10FFF}`）表示的数。

```crystal
"\u0041"    # => "A"
"\u{41}"    # => "A"
"\u{1F52E}" # => "&#x1F52E;"
```

一个大括号可以包括多个由空格分开的多个 unicode 字符。

```crystal
"\u{48 45 4C 4C 4F}" # => "HELLO"
```

## 插值


一个带有插值的字符串常量允许嵌入表达式到字符串中，其在运行时展开。

```crystal
a = 1
b = 2
"sum: #{a} + #{b} = #{a + b}" # => "sum: 1 + 2 = 3"
```

String interpolation is also possible with [String#%](https://crystal-lang.org/api/master/String.html#%25(other)-instance-method).

Any expression may be placed inside the interpolated section, but it’s best to keep the expression small for readability.

Interpolation can be disabled by escaping the `#` character with a backslash or by using a non-interpolating string literal like `%q()`.

```crystal
"\#{a + b}"  # => "#{a + b}"
%q(#{a + b}) # => "#{a + b}"
```

Interpolation is implemented using a [String::Builder](http://crystal-lang.org/api/String/Builder.html) and invoking `Object#to_s(IO)` on each expression enclosed by `#{...}`. The expression `"sum: #{a} + #{b} = #{a + b}"` is equivalent to:

```crystal
String.build do |io|
  io << "sum: "
  io << a
  io << " + "
  io << b
  io << " = "
  io << a + b
end
```

# Percent string literals

Besides double-quotes strings, Crystal also supports string literals indicated by a percent sign (`%`) and a pair of delimiters. Valid delimiters are parenthesis `()`, square brackets `[]`, curly braces `{}`, angles `<>` and pipes `||`. Except for the pipes, all delimiters can be nested meaning a start delimiter inside the string escapes the next end delimiter.

These are handy to write strings that include double quotes which would have to be escaped in double-quoted strings.

```crystal
%(hello ("world")) # => "hello (\"world\")"
%[hello ["world"]] # => "hello [\"world\"]"
%{hello {"world"}} # => "hello {\"world\"}"
%<hello <"world">> # => "hello <\"world\">"
%|hello "world"|   # => "hello \"world\""
```

A literal denoted by `%q` does not apply interpolation nor escapes while `%Q` has the same meaning as `%`.

```crystal
name = "world"
%q(hello \n #{name}) # => "hello \\n \#{name}"
%Q(hello \n #{name}) # => "hello \n world"
```

## Multiline strings

Any string literal can span multiple lines:

```crystal
"hello
      world" # => "hello\n      world"
```

Note that in the above example trailing and leading spaces, as well as newlines,
end up in the resulting string. To avoid this a string can be split into multiple lines
by joining multiple literals with a backslash:

```crystal
"hello " \
"world, " \
"no newlines" # same as "hello world, no newlines"
```

Alternatively, a backslash followed by a newline can be inserted inside the string literal:

```crystal
"hello \
     world, \
     no newlines" # same as "hello world, no newlines"
```

In this case, leading whitespace is not included in the resulting string.

## Heredoc

A *here document* or *heredoc* can be useful for writing strings spanning over multiple lines.
A heredoc is denoted by `<<-` followed by an heredoc identifier which is an alphanumeric sequence starting with a letter (and may include underscores). The heredoc starts in the following line and ends with the next line that starts with the heredoc identifier (ignoring leading whitespace) and is either followed by a newline or a non-alphanumeric character.

```crystal
<<-XML
<parent>
  <child />
</parent>
XML
```

Leading whitespace is removed from the heredoc contents according to the number of whitespace in the last line before the heredoc identifier.

```crystal
<<-STRING
  Hello
    world
  STRING # => "Hello\n  world"

<<-STRING
    Hello
      world
  STRING # => "  Hello\n    world"
```

It is possible to directly call methods on heredoc string literals, or use them inside parentheses:

```crystal
<<-SOME
hello
SOME.upcase # => "HELLO"

def upcase(string)
  string.upcase
end

upcase(<<-SOME
  hello
  SOME) # => "HELLO"
```

A heredoc generally allows interpolation and escapes.

To denote a heredoc without interpolation or escapes, the opening heredoc identifier is enclosed in single quotes:

```crystal
<<-'HERE'
  hello \n #{world}
  HERE # => "hello \n #{world}"
```

# 常量

> [syntax_and_semantics/literals.md][literals]
> 
> [commit 979398f1828ee2dfb9023cbc3f860ac3569e2239][commit]

[literals]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/literals.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/979398f1828ee2dfb9023cbc3f860ac3569e2239

Crystal 提供一些常量以创建部分基本类型的值。
 

| 常量										| 示例									|
| ----------------------------------------- | ------------------------------------- |
| [Nil](./literals/nil.html)				| `nil`									|
| [Bool](./literals/bool.html)              | `true`, `false`                       |
| [Integers](./literals/integers.html)      | `18`, `-12`, `19_i64`, `14_u32`,`64_u8` |
| [Floats](./literals/floats.html)          | `1.0`, `1.0_f32`, `1e10`, `-0.5`      |
| [Char](./literals/char.html)              | `'a'`, `'\n'`, `'あ'`					|
| [String](./literals/string.html)          | `"foo\tbar"`, `%("あ")`, `%q(foo #{foo})` |
| [Symbol](./literals/symbol.html)          | `:symbol`, `:"foo bar"`               |
| [Array](./literals/array.html)            | `[1, 2, 3]`, `[1, 2, 3] of Int32`, `%w(one two three)` |
| [Array-like][Array-like]					| `Set{1, 2, 3}`						|
| [Hash](./literals/hash.html)              | `{"foo" => 2}`, `{} of String => Int32` |
| [Hash-like][Hash-like]					| `MyType{"foo" => "bar"}`				|
| [Range](./literals/range.html)            | `1..9`, `1...10`, `0..var`			|
| [Regex](./literals/regex.html)            | `/(foo)?bar/`, `/foo #{foo}/imx`, `%r(foo/)` |
| [Tuple](./literals/tuple.html)            | `{1, "hello", 'x'}`                   |
| [NamedTuple](./literals/named_tuple.html) | `{name: "Crystal", year: 2011}`, `{"this is a key": 1}` |
| [Proc](./literals/proc.html)              | `->(x : Int32, y : Int32) { x + y }`  |

[Array-like]: ./literals/array.html#array-like-type-literal
[Hash-like]: ./literals/hash.html#hash-like-type-literal

# while 循环

> [syntax_and_semantics/while.md][while]
> 
> [commit 08bd7620ca36c5fcf8b1f1aa14ba9c8bdb8e57b5][commit] 

[while]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/while.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/08bd7620ca36c5fcf8b1f1aa14ba9c8bdb8e57b5

`while` 循环只要判断条件为*真(truth)*，它便一直执行。

```crystal
while some_condition
  do_this
end
```
首先测试判断条件，如果为*真*，那么就执行循环体。既是，循环体有可能一直未被执行。


`while` 循环的类型都是 `Nil` 。

与 `if` 类似，如果 `while` 循环的条件是个变量，要保证该变量在循环体中是非`空`值。如果条件是一个 `var.is_a?(Type)` 测试， 要保证在循环体中 `var` 类型为 Type 。如果判断条件 是一个 `var.responds_to?(:method)` ，要保证 `var` 是该函数的返回类型。

`while` 之后的变量类型依赖于 `while` 之前的类型，并且该类型只在离开 `while` 循环体之前存在。

```crystal
a = 1
while some_condition
  # a : Int32 | String
  a = "hello"
  # a : String
  a.size
end
# a : Int32 | String
```

## 在循环的最后判断条件

如果需要先执行循环体然后再判断退出条件，则可以这样：

```crystal
while true
  do_something
  break if some_condition
end
```

或者使用 `loop`，其可以在标准库中找到。

```crystal
loop do
  do_something
  break if some_condition
end
```

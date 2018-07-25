# 类变量

> [syntax_and_semantics/class_variables.md][class_variables]
>
> [commit f3435e1d16811195be4b05c478e8a542f5de5365][commit]

[class_variables]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/class_variables.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/f3435e1d16811195be4b05c478e8a542f5de5365

类变量是和类而不是实例有关的变量。其以两个 “at”（ `@@` ）符号作为前缀。例如：

```crystal
class Counter
  @@instances = 0

  def initialize
    @@instances += 1
  end

  def self.instances
    @@instances
  end
end

Counter.instances #=> 0
Counter.new
Counter.new
Counter.new
Counter.instances #=> 3
```

可以在类方法或实例方法中读写类变量。

类变量的类型使用[全局类型推断算法](type_inference.html)来猜测。

类变量从父类中继承，这意味着：其类型相同，但每个类都有不同的运行时值。例如：

```crystal
class Parent
  @@numbers = [] of Int32

  def self.numbers
    @@numbers
  end
end

class Child < Parent
end

Parent.numbers # => []
Child.numbers # => []

Parent.numbers << 1
Parent.numbers # => [1]
Child.numbers # => []
```

类变量也可以关联模块或结构体。和上面一样，他们继承自导入类型或父类类型。

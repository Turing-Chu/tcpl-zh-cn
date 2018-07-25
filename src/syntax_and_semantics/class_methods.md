# 类方法

> [syntax_and_semantics/class_methods.md][class_methods]
> 
> [commit 25b85d805ea5650c761308e282e8606cc3635560][commit]

[class_methods]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/class_methods.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/25b85d805ea5650c761308e282e8606cc3635560

类方法是与类或模块而非特定实例相关联的方法。

```crystal
module CaesarCipher
  def self.encrypt(string : String)
    string.chars.map{ |char| ((char.upcase.ord - 52) % 26 + 65).chr }.join
  end
end

CaesarCipher.encrypt("HELLO") # => "URYYB"
```

类方法由方法名和一个带逗点的类型名定义。

```crystal
def CaesarCipher.decrypt(string : String)
  encrypt(string)
end
```

当类方法定义在类或模块内部时，使用 `self` 要比类名更方便。

类方法也可以由[`模块`扩展](modules.md#extend-self)来定义。

类方法可以在其定义的同名之下调用(`CaesarCipher.decrypt("HELLO")`)。

当在相同类或模块范围内调用类方法时，接收者可以是 `self` 或隐式调用 （如`encrypt(string)`）。

# 构造器

构造器是常规类方法，其可以[创建类的新实例](new,_initialize_and_allocate.md)。
Crystal 中所有的类默认至少有一个名为 `new` 的构造器，但也可以以不同的名字定义其他的构造器。

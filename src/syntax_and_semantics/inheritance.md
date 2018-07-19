# 继承

> [syntax_and_semantics/inheritance.md][inheritance]
>
> [commit a32014850bb26937bcee0e2f969e66cb81616cb1][commit]

[inheritance]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/inheritance.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/a32014850bb26937bcee0e2f969e66cb81616cb1

除了层次的根 `Object` 类，每一个类都是从另一个类（该类的父类）继承而来。如果不特别指明，其默认是类的 `Reference` 和结构体的 `Struct` 。

类继承其父类的所有实例变量以及所有实例方法和类方法，包括其构造器（ `new` 和 `initialize` ）。

```crystal
class Person
  def initialize(@name : String)
  end

  def greet
    puts "Hi, I'm #{@name}"
  end
end

class Employee < Person
end

employee = Employee.new "John"
employee.greet # "Hi, I'm John"
```

如果类定义了 `new` 或  `initialize` 方法，则其父类的构造器不会被继承：

```crystal
class Person
  def initialize(@name : String)
  end
end

class Employee < Person
  def initialize(@name : String, @company_name : String)
  end
end

Employee.new "John", "Acme" # OK
Employee.new "Peter" # Error: wrong number of arguments
                     # for 'Employee:Class#new' (1 for 2)
```

可以在派生类中覆盖方法：

```crystal
class Person
  def greet(msg)
    puts "Hi, #{msg}"
  end
end

class Employee < Person
  def greet(msg)
    puts "Hello, #{msg}"
  end
end

p = Person.new
p.greet "everyone" # "Hi, everyone"

e = Employee.new
e.greet "everyone" # "Hello, everyone"
```

除了覆盖，也可以用保留类型来定义特定的方法：

```crystal
class Person
  def greet(msg)
    puts "Hi, #{msg}"
  end
end

class Employee < Person
  def greet(msg : Int32)
    puts "Hi, this is a number: #{msg}"
  end
end

e = Employee.new
e.greet "everyone" # "Hi, everyone"

e.greet 1 # "Hi, this is a number: 1"
```

## super

可以用  `super` 来调用父类的方法：

```crystal
class Person
  def greet(msg)
    puts "Hello, #{msg}"
  end
end

class Employee < Person
  def greet(msg)
    super # Same as: super(msg)
    super("another message")
  end
end
```

不待参数和括号的 `super` 接收和方法相同的参数。否则，接收所传递给它的参数。

# 可见性

> [syntax_and_semantics/visibility.md][visibility]
>
> [commit f510983efc4bd9579c56ecbce5df5b96d54b11b6][commit]

[commit]: https://github.com/crystal-lang/crystal-book/commit/f510983efc4bd9579c56ecbce5df5b96d54b11b6
[visibility]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/visibility.md

方法默认是共有的：编译器总允许调用方法，即使没有 `public` 关键字。

可以将方法标记为 `private` 或 `protected` 。

## 私有方法

私有方法只可以被一个非接收者调用，也就是说，在点号之前无任何东西：

```crystal
class Person
  private def say(message)
    puts message
  end

  def say_hello
    say "hello" # OK, no receiver
    self.say "hello" # Error, self is a receiver

    other = Person.new "Other"
    other.say "hello" # Error, other is a receiver
  end
end
```

注意 `private` 方法是可以被子类访问的：

```crystal
class Employee < Person
  def say_bye
    say "bye" # OK
  end
end
```

## 私有类型

私有类型只可以在其定义的命名空间内部引用。

```crystal
class Foo
  private class Bar
  end

  Bar      # OK
  Foo::Bar # Error
end

Foo::Bar # Error
```

`private` 可以用于 `class` 、 `module` 、 `lib` 、 `enum` 、 `alias` 以及常量： 


```crystal
class Foo
  private ONE = 1

  ONE # => 1
end

Foo::ONE # Error
```

## protected 方法

一个`protected` 方法只可以被下面两种请况下调用：

1. 与当前类型相同类型的实例
2. 与当前类型在同一命名空间内的实例 （ class 、 struct 、 module 等）


```crystal
### Example of 1

class Person
  protected def say(message)
    puts message
  end

  def say_hello
    say "hello" # OK, implicit self is a Person
    self.say "hello" # OK, self is a Person

    other = Person.new "Other"
    other.say "hello" # OK, other is a Person
  end
end

class Animal
  def make_a_person_talk
    person = Person.new
    person.say "hello" # Error, person is a Person
                       # but current type is an Animal
  end
end

one_more = Person.new "One more"
one_more.say "hello" # Error, one_more is a Person
                     # but current type is the Program

### Example of 2

module Namespace
  class Foo
    protected def foo
      puts "Hello"
    end
  end

  class Bar
    def bar
      # Works, because Foo and Bar are under Namespace
      Foo.new.foo
    end
  end
end

Namespace::Bar.new.bar
```

`protected` 类方法可以在一个实例方法中调用：

```crystal
class Person
  protected def self.say(message)
    puts message
  end

  def say_hello
    Person.say "hello" # OK
  end
end
```

## 私有顶级方法

一个 `private` 的顶级方法只可以在当前文件中被访问。

```crystal
# In file one.cr
private def greet
  puts "Hello"
end

greet #=> "Hello"

# In file two.cr
require "./one"

greet # undefined local variable or method 'greet'
```

这可以在一个文件中定义只为该文件所知的辅助方法。

## 私有顶级类型

一个 `private` 的顶级类型只能在当前文件中被访问。


```crystal
# In file one.cr
private class Greeter
  def self.greet
    "Hello"
  end
end

Greeter.greet #=> "Hello"

# In file two.cr
require "./one"

Greeter.greet # undefined constant 'Greeter'
```

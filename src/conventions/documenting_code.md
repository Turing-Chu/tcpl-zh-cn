# 文档化代码

Crystal 文档注释使用 [Markdown](https://daringfireball.net/projects/markdown/) 的子集。

* 文档应该放在类、模块以及方法的正上面。二者之间无空格。

```crystal
# A unicorn is a **legendary animal** (see the `Legendary` module) that has been
# described since antiquity as a beast with a large, spiraling horn projecting
# from its forehead.
class Unicorn
end

# Bad: This is not attached to any class.

class Legendary
end
```

* 方法文档放在方法摘要和方法实现的内部。前者只有第一行，后者包括整个文档。简言之，是指：

  1. 在第一行说明方法的目的或功能。
  2. 随后补充使用细节。

例如：

```crystal
# Returns the number of horns this unicorn has.
#
# ```
# Unicorn.new.horns # => 1
# ```
def horns
  @horns
end
```

* 使用第三人称：`Returns the number of horns this unicorn has` 而不是 `Return the number of horns this unicorn has` 。

* 参数名应该 *italicized* （以单个`星号`或`下划线`包围）：

```crystal
# Creates a unicorn with the specified number of *horns*.
def initialize(@horns = 1)
  raise "Not a unicorn" if @horns != 1
end
```

* 有 Crystal 代码的代码块应该使用三个反引号(```) 或四个空格缩进。

```crystal
# ```
# unicorn = Unicorn.new
# unicorn.speak
# ```
```

或者

```crystal
#     unicorn = Unicorn.new
#     unicorn.speak
```

* 文本块必须以三个反引号(```) 并随后跟 "text" 来包围，例如，显示程序输出。

```crystal
# ```text
# "I'm a unicorn"
# ```
```

* 使用一个反引号来自动连接到其他的类型。

```crystal
# the `Legendary` module
```

* 使用 `#horns` 或 `#index(char)`并用单个反引号包围这样的 hash 来把当前文档化的类型自动连接到方法上。

* 使用 `OtherType#method(arg1, arg2)` 或只用 `OtherType#method` 并用单个反引号包围来将其他类型自动链接到方法上。

例如：

```crystal
# Check the number of horns with `#horns`.
# See what a unicorn would say with `Unicorn#speak`.
```

* 使用 `# =>` 来显示代码块中表达式的值。

```crystal
1 + 2             # => 3
Unicorn.new.speak # => "I'm a unicorn"
```

* 像之前的声明那样把 `ditto` 应用于同样的注释中。 

```crystal
# ditto
def number_of_horns
  horns
end
```

* 在生成的文档中，使用 `:nodoc:` 来隐藏共有的声明。私有的和受保护的方法总是被隐藏的。

```crystal
class Unicorn
  # :nodoc:
  class Helper
  end
end
```

### 标记类、模块和方法

考虑到关键字，Crystal 会自动生成可视化标记以帮助高亮问题、注意点或（和）可能的问题。

支持的标记：

- BUG
- DEPRECATED
- FIXME
- NOTE
- OPTIMIZE
- TODO

关键字标记必须放在各自行的行首，并且都必须大写。为了可读性，可选择结尾冒号。

```crystal
# Makes the unicorn speak to STDOUT
#
# NOTE: Although unicorns don't normally talk, this one is special
# TODO: Check if unicorn is asleep and raise exception if not able to speak
# TODO: Create another `speak` method that takes and prints a string
def speak
  puts "I'm a unicorn"
end

# Makes the unicorn talk to STDOUT
#
# DEPRECATED: Use `speak`
def talk
  puts "I'm a unicorn"
end
```

### 使用 Crystal 的代码格式器

Crystal 内置的代码格式器不仅可以用于格式化代码，而且也可以格式化文档块中的代码示例。

当调用 `crystal tool format` 时，这会自动完成，其会自动格式化当前目录下的所有 `.cr` 文件。

格式化单个文件：

```
$ crystal tool format file.cr
```

格式化目录下所有 `.cr` 文件：

```
$ crystal tool format src/
```

用这个工具来统一代码风格并为 Crystal 自身提升文档化。

格式化也非常快，所以相比于单个文件，格式化整个项目只使用一点点时间。

### 一个完整的例子

``````crystal
# A unicorn is a **legendary animal** (see the `Legendary` module) that has been
# described since antiquity as a beast with a large, spiraling horn projecting
# from its forehead.
#
# To create a unicorn:
#
# ```
# unicorn = Unicorn.new
# unicorn.speak
# ```
#
# The above produces:
#
# ```text
# "I'm a unicorn"
# ```
#
# Check the number of horns with `#horns`.
class Unicorn
  include Legendary

  # Creates a unicorn with the specified number of *horns*.
  def initialize(@horns = 1)
    raise "Not a unicorn" if @horns != 1
  end

  # Returns the number of horns this unicorn has
  #
  # ```
  # Unicorn.new.horns # => 1
  # ```
  def horns
    @horns
  end

  # ditto
  def number_of_horns
    horns
  end

  # Makes the unicorn speak to STDOUT
  def speak
    puts "I'm a unicorn"
  end

  # :nodoc:
  class Helper
  end
end
``````

### 生成文档

调用 `crystal docs` 来生成项目文档。这会创建一个以 `docs/index.html` 为入口的 `docs` 目录。要考虑在 `src` 根目录下的所有文件。

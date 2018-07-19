# 赋值

> [syntax_and_semantics/assignment.md][assignment]
> 
> [commit bc665fe1a4c144c464fdd5002ce3848e882ffdee][commit]

[assignment]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/assignment.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/bc665fe1a4c144c464fdd5002ce3848e882ffdee

赋值以等号字符（ `=` ）来执行。

```crystal
# Assigns to a local variable
local = 1

# Assigns to an instance variable
@instance = 2

# Assigns to a class variable
@@class = 3
```

随后会解释上面每一种变量类型。

一些包含 `=` 符号的可用语法糖：

```crystal
local += 1  # same as: local = local + 1

# The above is valid with these operators:
# +, -, *, /, %, |, &, ^, **, <<, >>

local ||= 1 # same as: local || (local = 1)
local &&= 1 # same as: local && (local = 1)
```

以 `=` 结尾的函数调用语法糖：

```crystal
# A setter
person.name=("John")

# The above can be written as:
person.name = "John"

# An indexed assignment
objects.[]=(2, 3)

# The above can be written as:
objects[2] = 3

# Not assignment-related, but also syntax sugar:
objects.[](2, 3)

# The above can be written as:
objects[2, 3]
```

`=` 操作符也可用于 setter 和 indexer 之上。注意 `||` 和 `&&` 使用 `[]?` 方法来检测键的存在性。

```crystal
person.age += 1        # same as: person.age = person.age + 1

person.name ||= "John" # same as: person.name || (person.name = "John")
person.name &&= "John" # same as: person.name && (person.name = "John")

objects[1] += 2        # same as: objects[1] = objects[1] + 2

objects[1] ||= 2       # same as: objects[1]? || (objects[1] = 2)
objects[1] &&= 2       # same as: objects[1]? && (objects[1] = 2)
```

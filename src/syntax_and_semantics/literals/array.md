# 数组(Array)

[数组(Array)](http://crystal-lang.org/api/Array.html) 是一个以整数为索引的泛型有序集合，其元素为一个指定类型 `T` 。

数组通常用一个以方括号（ `[]` ）表示的数组常量创建，其不同元素以逗号（ `,` ）分开。

```crystal
[1, 2, 3]
```

## 泛型类型参数

数组的泛型类型参数 `T` 是指内部常量元素的类型。当数组的所有元素类型都相同时，`T` 为该类型。否则 `T` 则是所有元素类型的并集。

```crystal
[1, 2, 3]          # => Array(Int32)
[1, "hello", 'x']  # => Array(Int32 | String | Char)
```

可以直接使用闭括号后跟 `of` 和类型来指定一个明确的类型，每一部分都用空格隔开。这样便覆盖了类型推断，例如，可以创建一个拥有一些初始类型的数组，但之后能够接收其他的类型。

```crystal
array_of_numbers = [1, 2, 3] of Number  # => Array(Number)
array_of_numbers + [0.5]                # => [1, 2, 3, 0.5]

array_of_int_or_string = [1, 3, 4] of Int32 | String  # => Array(Int32 | String)
array_of_int_or_string + ["foo"]                      # => [1, 2, 3, "foo"]
```


空数组常量需要一个指定的类型：

```crystal
[] of Int32  # => Array(Int32).new
```

## 部分数组常量(percent array literals)

[字符串数组](./string.html#Percent String Array Literal) 以及[符号数组](./symbol.html#Percent Symbol Array Literal) 可以使用部分数组常量来创建

```crystal
%w(one two three)  # => ["one", "two", "three"]
%i(one two three)  # => [:one, :two, :three]
```

## 类数组类型常量

Crystal 支持 另一中数组和类数组类型的常量。其包含类型名，后跟由大括号 `{}` 包括的元素列表，同时各个元素以 (`,`) 分开。

```crystal
Array{1, 2, 3}
```

该常量可以用于任何类型，只要其有一个空参构造函数以及对 `<<` 的反应。

```crystal
IO::Memory{1, 2, 3}
Set{1, 2, 3}
```

对于一个像 `IO::Memory` 这样的非泛型类型来说，这等于：

```crystal
array_like = IO::Memory.new
array_like << 1
array_like << 2
array_like << 3
```

对于一个像 `Set` 这样的泛型来说，泛型 `T` 的类型可以像数组一样从元素的类型上推断出来。上面的代码等价于：

```crystal
array_like = Set(typeof(1, 2, 3)).new
array_like << 1
array_like << 2
array_like << 3
```

可以用部分类型名来明确地指定类型参数。

```crystal
Set(Number) {1, 2, 3}
```

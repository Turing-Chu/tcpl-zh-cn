# 性能

> [guides/performance.md][performance]
>
> [commit 1513574a9de427281f7d9a9d44af499796f721b1][commit]

[performance]: https://github.com/crystal-lang/crystal-book/blob/master/guides/performance.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/1513574a9de427281f7d9a9d44af499796f721b1

遵从这些提示来让程序在运行速度和内存上获得更好的输出。

## 过早的优化

Donald Knuth 曾经说过：

> 我们应该忘记小的效率，既是 97% 的时间：过早优化是万恶之源。然而我们不应该放弃那至关重要的 3% 的机会。

但是，如果你正在编写程序，并且意识到编写相等的语义，更快的版本只涉及很小的更改，则不应该错过这个机会。

并始终确保分析程序以了解其瓶颈是什么。对于分析来说，在 Mac OSX 上可以使用 XCode 的 [Instruments Time Profiler][ITP] 。在 Linux 上，任何可以分析 C/C++ 程序的程序，像 [perf][perf] 或 [Callgrind][Callgrind] ，应该有用。

[ITP]: https://developer.apple.com/library/prerelease/content/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Instrument-TimeProfiler.html
[perf]: https://perf.wiki.kernel.org/index.php/Main_Page
[Callgrind]: http://valgrind.org/docs/manual/cl-manual.htm

确保始终通过使用 `--release` 标志编译并运行程序来对程序进行分析，这开启优化。


## 避免内存分配 

可以在程序中进行的最好优化之一是避免额外的或无用的内存分配。在创建一个**类**的实例时会发生内存分配，这最终会分配堆内存。创建**结构体**的实例会使用栈内存，且不会招致性能惩罚。如果你不清楚栈内存和堆内存的区别，请务必[阅读这个][read_this]。

[read_this]: https://stackoverflow.com/questions/79923/what-and-where-are-the-stack-and-heap

分配堆内存很慢，并且它会给垃圾收集器（GC）带来更大的压力，因为它以后必须释放该内存。

这里有几种可以避免堆内存分配的方法。设计的标准库可以帮助你实现它。

### 在写 IO 时不要创建中间字符串

要将数字打印到标准输出，可以编写：

```
puts 123
```

在很多编程语言中，会发生 `to_s` 调用，或相似的方法来将这个对象转换成其字符串表示，随后该字符串将会被写到标准输出。这是可以的，但有个缺陷：其在堆内存上创建一个中间字符串，只写这个字符串然后丢弃。这样做，调用了堆内存分配然后为 GC 增加了些工作。

在 Crystal 中 `puts` 会在对象上调用 `to_s(io)` ，将其传递给应该写入字符串表示的 IO。

所以，你永远不要这样做：

```
puts 123.to_s
```

因为它创建一个中间字符串。总是将对象直接追加到 IO 上。

在编写自定义类型时，请务必确保重载 `to_s(io)`，而不是  `to_s` ，并避免在该方法中创建中间字符串。例如：

```crystal
class MyClass
  # Good
  def to_s(io)
    # appends "1, 2" to IO without creating intermediate strings
    x = 1
    y = 2
    io << x << ", " << y
  end

  # Bad
  def to_s(io)
    x = 1
    y = 2
    # using a string interpolation creates an intermediate string.
    # this should be avoided
    io << "#{x}, #{y}"
  end
end
```

这种追加到 IO 而不是返回中间字符串的原则导致在性能上比处理中间字符串更好。你也应该在 API 定义中使用此策略。


比较下时间：

```crystal
# io_benchmark.cr
require "benchmark"

io = IO::Memory.new

Benchmark.ips do |x|
  x.report("without to_s") do
    io << 123
    io.clear
  end

  x.report("with to_s") do
    io << 123.to_s
    io.clear
  end
end
```

输出：

```
$ crystal run --release io_benchmark.cr
without to_s  77.11M ( 12.97ns) (± 1.05%)       fastest
   with to_s  18.15M ( 55.09ns) (± 7.99%)  4.25× slower
```

要记住，这不只是时间上的提升：内存用量也有所减少。

### 使用字符串插值而非串联

有时需要将字符串和其他值直接构建字符串组合。不应该只使用 `String#+(String)` 来连接这些字符串，而应该使用[字符串插值](syntax_and_semantics/literals/string.html#interpolation)，它可以将表达式嵌入到字符串字面量中：`"Hello, #{name}"` 要比 `"Hello, " +  name.to_s` 更好。

编译器转换插值字符串并将其追加到一个字符串 IO 上，以便其自动避免中间字符串。上面的例子可以转换为：`(StringBuilder.new << "Hello, " << name).to_s` 。

### 避免为字符串构建分配 IO

宁愿为构建字符串使用优化的专用 `String.build` ，而不要创建中间内存分配 `IO::Memory`。

```crystal
require "benchmark"

Benchmark.ips do |bm|
  bm.report("String.build") do
    String.build do |io|
      99.times do
        io << "hello world"
      end
    end
  end
  bm.report("IO::Memory") do
    io = IO::Memory.new
    99.times do
      io << "hello world"
    end
    io.to_s
  end
end
```

输出：

```
$ crystal run --release str_benchmark.cr
String.build 597.57k (  1.67µs) (± 5.52%)       fastest
  IO::Memory 423.82k (  2.36µs) (± 3.76%)  1.41× slower
```


### 避免反复创建临时对象

看下这个程序：

```crystal
lines_with_language_reference = 0
while line = gets
  if ["crystal", "ruby", "java"].any? { |string| line.includes?(string) }
    lines_with_language_reference += 1
  end
end
puts "Lines that mention crystal, ruby or java: #{lines_with_language_reference}"
```

上面的程序可以运行但有很大的性能问题：每次迭代都会为 `["crystal", "ruby", "java"]` 创建一个新的数组。记住：数组常量只是创建一个数组实例并向其添加一些值的语法糖，并且这在每次迭代时反复发生。

There are two ways to solve this:
有两种解决办法：

1. 使用元组。如果在上面的程序中使用 `{"crystal", "ruby", "java"}` ，其会以相同的方式运行，但因为元组不涉及堆内存，其会更快且消耗更少的内存，并给予编译器更多优化该程序的机会。

  ```crystal
  lines_with_language_reference = 0
  while line = gets
    if {"crystal", "ruby", "java"}.any? { |string| line.includes?(string) }
      lines_with_language_reference += 1
    end
  end
  puts "Lines that mention crystal, ruby or java: #{lines_with_language_reference}"
  ```

2. 将数组定义为常量。

  ```crystal
  LANGS = ["crystal", "ruby", "java"]

  lines_with_language_reference = 0
  while line = gets
    if LANGS.any? { |string| line.includes?(string) }
      lines_with_language_reference += 1
    end
  end
  puts "Lines that mention crystal, ruby or java: #{lines_with_language_reference}"
  ```

使用元组是首选的方式。

在循环中明确的数组常量是创建临时对象的方式之一，但这也可以通过方法调用来创建。例如 每次 `Hash#keys` 调用时将会返回一个新数组。除了这样做，可以使用 `Hash#each_key` 、 Hash#has_key?` 以及其他方法。

### 如果可能请使用结构体

如果为类型声明为一个**结构体**而不是**类**，那么创建该类型的实例将会使用堆内存，这要比堆内存更廉价，并且不会为 GC 增加压力。

也不要一直使用结构体。结构体是值传递的，所以将其传递给方法而方法修改了它，那么调用者将不会看到这些变化，所以这可能出错。最好的做法是只在可变对象上使用结构体，尤其它们都比较小时。

例如：

```crystal
# class_vs_struct.cr
require "benchmark"

class PointClass
  getter x
  getter y

  def initialize(@x : Int32, @y : Int32)
  end
end

struct PointStruct
  getter x
  getter y

  def initialize(@x : Int32, @y : Int32)
  end
end

Benchmark.ips do |x|
  x.report("class") { PointClass.new(1, 2) }
  x.report("struct") { PointStruct.new(1, 2) }
end
```

输出：

```
$ crystal run --release class_vs_struct.cr
 class  28.17M (± 2.86%) 15.29× slower
struct 430.82M (± 6.58%)       fastest
```

## 字符串迭代

Crystal 中的字符串一直以 UTF-8 编码。UTF-8 是一个变长编码：一个字符可能由几个字节表示，尽管字符在 ASCII 范围中总是由单个字节表示。因为这，用 `String#[]` 索引字符串并非 `O(1)` 操作，因为字节每次需要解码来找到给定位置的字符。Crystal 的 `String` 在这里有一种优化：如果知道字符串中所有的字符都是 ASCII，那么 `String#[]` 可以在 `O(1)` 内实现。然而通常这并不对。

由于这个原因，以这样的方法迭代字符串并不是最佳的，实际上是 `O(n^2)` 的复杂度：

```crystal
string = ...
while i < string.size
  char = string[i]
  # ...
end
```

上面的程序有第二个问题：计算字符串的 `大小` 也很慢，因为其并不是简单的字符串中的字节数（`bytesize`）。然而，一旦字符串的大小被计算出，它便被缓存了。

在这个案例中提升性能的方式是或使用迭代方法 (`each_char`，`each_byte`，`each_codepoint`) 之一，或使用更低级的 `Char::Reader` 结构体。例如，使用 `each_char` ：

```crystal
string = ...
string.each_char do |char|
  # ...
end
```

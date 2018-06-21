# 浮点数(Floats)

> [syntax_and_semantics/literals/floats.md][float]
>
> [commit 78d18cf29258956326c0989ff395b888b3a09d81][commit]

[float]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/literals/floats.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/78d18cf29258956326c0989ff395b888b3a09d81

浮点数有两种类型，[32位浮点数(Float32)][float32] 和 [64位浮点数(Float64)][float64]，但都相当于由IEEE定义的 [binary32][binary32] 和 [binary64][binary64] 。

[float32]: http://crystal-lang.org/api/Float32.html
[float64]: http://crystal-lang.org/api/Float64.html
[binary32]: http://en.wikipedia.org/wiki/Single_precision_floating-point_format
[binary64]: http://en.wikipedia.org/wiki/Double_precision_floating-point_format

一个浮点数常量由一个可选的 `+` 号或 `-` 号，一个数字序列或下划线，一个点号，数字或下划线，一个可选的指数后缀，一个可选的类型后缀组成。如果无后缀可以显示，该常量类型为 `Float64` 。

```crystal
1.0      # Float64
1.0_f32  # Float32
1_f32    # Float32

1e10     # Float64
1.5e10   # Float64
1.5e-7   # Float64

+1.3     # Float64
-0.5     # Float64
```

后缀之前的下划线 `_` 是可选的。

下划线使一些数字更可读：

```crystal
1_000_000.111_111 # a lot more readable than 1000000.111111, yet functionally the same
```

# 范围(Range)

[范围(Range)](http://crystal-lang.org/api/Range.html)通常由范围字面量构成：

```crystal
x..y  # an inclusive range, in mathematics: [x, y]
x...y # an exclusive range, in mathematics: [x, y)
```

方便记住一边包含而另一边不包含的方法是：想下这个额外的点，貌似它把 *y* 放的更远，因而出了范围的边界。

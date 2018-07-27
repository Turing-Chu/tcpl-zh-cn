# 不安全代码

> [syntax_and_semantics/unsafe.md][unsafe]
>
> [commit 0c157b7eaad13f191ddb73f148171f3579287279][commit]

[unsafe]: https://github.com/crystal-lang/crystal-book/blob/master/syntax_and_semantics/unsafe.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/0c157b7eaad13f191ddb73f148171f3579287279

Crystal 语言的这部分被认为是不安全的：

* 代码调用原生指针：[Pointer](http://crystal-lang.org/api/Pointer.html) 类型与 [pointerof](pointerof.html)
* [allocate](new,_initialize_and_allocate.html) 类方法
* 代码调用 C 语言绑定
* [未初始化变量声明](declare_var.html)

“不安全”意味着可能发生内存泄漏、段错误和程序崩溃。例如：

```crystal
a = 1
ptr = pointerof(a)
ptr[100_000] = 2   # undefined behaviour, probably a segmentation fault
```

然而，正常的代码通常不会调用指针操作或未初始化变量，以及 C 语言绑定通常被封装在安全的封装器之中，其包括空指针和范围检查。

没有语言是 100% 安全的：一些部分必将处于低级别，操作系统相关的接口和涉及指针操作。但是一旦将其抽象然后在更高级别上操作，并假设（经过数学证明或彻底测试之后）低级部分是安全的，则可以确信整个代码是安全的。

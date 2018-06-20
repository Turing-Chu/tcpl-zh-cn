# 从源码编译

如果你希望贡献，那么你可以源码编译 Crystal。

1. [安装最新发布版 Crystal ](https://crystal-lang.org/docs/installation)。需要 Crystal 来编译 Crystal :) 。
2. 确保当前路径下 LLVM 版本是可用的。目前，Crystal 支持 LLVM 3.8、3.9、4.0 和 5.0 。如果可能，请使用最新版。如果使用 Mac 以及 Homebrew 方式，当加上 `--with-llvm` 参数时会自动为你配置。
3. 确保已经安装了[所有依赖库](https://github.com/crystal-lang/crystal/wiki/All-required-libraries)。可以看下 [贡献指引](https://github.com/crystal-lang/crystal/blob/master/CONTRIBUTING.md) 。
4. 克隆仓库：
```
git clone https://github.com/crystal-lang/crystal
```
5. 运行 `make` 来构建你自己版本的编译器。
6. 运行 `make spec` 以确保所有的 specs(specifications) 都通过，之后一切便都正确安装了。
7. 使用 `bin/crystal` 来运行 crystal 文件。

如果想获取更多关于 `bin/crystal` 的信息，请查阅[编译器使用](https://crystal-lang.org/docs/using_the_compiler)文档。 

注意：实际的二进制文件会被构建到 `.build/crystal` ，但是 `bin/crystal` 则是应该用以执行 crysta 的封装脚本。

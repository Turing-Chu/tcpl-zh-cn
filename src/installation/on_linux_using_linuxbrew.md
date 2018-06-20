# 在 Linux 上使用 Linuxbrew

在 Linux 的分支系统上，可以很容易地使用 [Linuxbrew](http://linuxbrew.sh/) 来安装 Crystal 。

```
brew update
brew install crystal-lang
```

如果打算为 Crystal 语言做贡献，也可以安装 LLVM。因此使用下面这行命令代替最后一行：

```
brew install crystal-lang --with-llvm
```

# 在 Mac OSX 上使用 Homebrew

在 Mac 上可以很容易地使用 [Homebrew](http://brew.sh/) 来安装 Crystal 。

```
brew update
brew install crystal-lang
```
如果打算为 Crystal 语言做贡献，也可以安装 LLVM 。因此，以下面代码代替最后一行：

```
brew install crystal-lang --with-llvm
```

## 在 OSX 10.11 (El Capitan) 上的异常处理

如果得到一个类似这样的错误:

```
ld: library not found for -levent
```

则需要重新安装命令行工具并选择默认的有效工具链：


```
$ xcode-select --install
$ xcode-select --switch /Library/Developer/CommandLineTools
```

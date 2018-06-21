# 在 Windows 子系统 Ubuntu 的 Bash 上

> [installation/on_bash_on_ubuntu_on_windows.md][on_bash_on_ubuntu_on_windows]
> 
> [commit 9015d4fde569f9ab80de819cd79a1d6f19594649][commit]

[on_bash_on_ubuntu_on_windows]: https://github.com/crystal-lang/crystal-book/blob/master/installation/on_bash_on_ubuntu_on_windows.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/9015d4fde569f9ab80de819cd79a1d6f19594649

Crystal _尚未_支持 Windows，如果正在使用 Windows 10 则可以（尝试）通过 [Bash on Ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/about) -- 运行在 Windows 上的 Bash 测试环境来使用Crystal。本部分的安装说明与 [Debian/Ubuntu](on_debian_and_ubuntu.md) 的类似，但并没那么多毛边需要注意。

记住：**这只是一个测试环境**。

## 设置仓库

首先必须把仓库加到 APT 配置里面去。这很容易设置，只需在命令行中执行：

```
curl -sSL https://dist.crystal-lang.org/apt/setup.sh | sudo bash
```

这行脚本会加上签名密钥和仓库配置。如果希望手动配置，则可以执行下面的命令：

```
sudo apt-key adv --keyserver keys.gnupg.net --recv-keys 09617FD37CC06B54
echo "deb https://dist.crystal-lang.org/apt crystal main" | sudo tee /etc/apt/sources.list.d/crystal.list
sudo apt-get update
```

## 依赖

Crystal 需要 C 编译器 （ `cc` ）和连接器 （ `ld` ）来编译 Crystal程序，所以也需要安装 `cc` 和 `ld` ：

```
sudo apt-get install clang binutils
```

## 安装

一旦配置好仓库，就可以准备安装 Crystal 了：

```
sudo apt-get install crystal
```

## 升级

当 Crystal 新版本发布时，可以使用下面命令升级系统：

```
sudo apt-get update
sudo apt-get install crystal
```

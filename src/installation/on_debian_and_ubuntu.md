# Debian 和 Ubuntu

在 Debian 衍生的分支系统上，可以使用官方 Crystal 仓库来安装。

## 设置仓库

首先必须把仓库加到 APT 配置里面去。这很容易设置，只需在命令行中执行：

```
curl https://dist.crystal-lang.org/apt/setup.sh | sudo bash
```

这行脚本会加上签名密钥和仓库配置。如果希望手动配置，则需要以 *root* 执行下面的命令：

```
apt-key adv --keyserver keys.gnupg.net --recv-keys 09617FD37CC06B54
echo "deb https://dist.crystal-lang.org/apt crystal main" > /etc/apt/sources.list.d/crystal.list
apt-get update
```

## 安装

一旦配置好仓库，就可以准备安装 Crystal 了：

```
sudo apt-get install crystal
```

当运行或构建 Crystal 程序时，你[可能需要][need]安装 `build-essential` 包。可以使用下面命令来安装： 

[need]: https://github.com/crystal-lang/crystal/issues/4342

```
sudo apt-get install build-essential
```

## 升级

当 Crystal 新版本发布时，可以使用下面命令升级系统：

```
sudo apt-get update
sudo apt-get install crystal
```

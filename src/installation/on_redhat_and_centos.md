# RedHat 和 CentOS

在 RedHat 衍生的分支系统上，可以使用官方 Crystal 仓库。

## 设置仓库

首先必须把仓库加到 YUM 配置里面去。这很容易设置，只需在命令行中执行：

```
curl https://dist.crystal-lang.org/rpm/setup.sh | sudo bash
```

这行脚本会加上签名密钥和仓库配置。如果希望手动配置：

```
rpm --import https://dist.crystal-lang.org/rpm/RPM-GPG-KEY

cat > /etc/yum.repos.d/crystal.repo <<END
[crystal]
name = Crystal
baseurl = https://dist.crystal-lang.org/rpm/
END
```

## 安装

一旦配置好仓库，就可以准备安装 Crystal 了：

```
sudo yum install crystal
```

## 升级

当 Crystal 新版本发布时，可以使用下面命令升级系统：

```
sudo yum update crystal
```

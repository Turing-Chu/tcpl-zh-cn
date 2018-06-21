#  Gentoo Linux

> [installation/on_gentoo_linux.md][on_gentoo_linux]
>
> [commit dd80919fe40cc3cab8597155fadb002593fdf329][commit]

[on_gentoo_linux]: https://github.com/crystal-lang/crystal-book/blob/master/installation/on_gentoo_linux.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/dd80919fe40cc3cab8597155fadb002593fdf329

Gentoo Linux 的主干分支上覆盖了 Crystal 编译器。

## 配置

或许需要先看下可用的配置：

```
# equery u dev-lang/crystal
[ Legend : U - final flag setting for installation]
[        : I - package is installed with flag     ]
[ Colors : set, unset                             ]
 * Found these USE flags for dev-lang/crystal-0.18.7:
 U I
 - - doc      : Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
 - - examples : Install examples, usually source code
 + + xml      : Use the dev-libs/libxml2 library to enable Crystal xml module
 + - yaml     : Use the dev-libs/libyaml library to enable Crystal yaml module
```

## 安装

```
su -
emerge -a dev-lang/crystal
```

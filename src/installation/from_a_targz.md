# 从 tar.gz 中安装

> [installation/from_a_targz.md][from_a_targz]
>
> [commit d14f351a8c523e9d9d11efd29ed1a0552c04d7db][commit]

[from_a_targz]: https://github.com/crystal-lang/crystal-book/blob/master/installation/from_a_targz.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/d14f351a8c523e9d9d11efd29ed1a0552c04d7db 

如果因为某个原因或不愿意使用上面的安装方式，也可以下载 Crystal 的单独的 .tar.gz 文件。

最新文件可以在 GitHub 上的发布页面找到：[https://github.com/crystal-lang/crystal/releases](https://github.com/crystal-lang/crystal/releases)

下载对应平台的文件并解压。在压缩包里会有一个可执行文件 `bin/crystal`。

为了便于使用，也可以创建一个符号链接：

`ln -s [full path to bin/crystal] /usr/local/bin/crystal`

然后就可以键入 `crystal` 来使用编译器了。

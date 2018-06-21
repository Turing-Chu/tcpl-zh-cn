# 编译器的使用 

> [using_the_compiler/README.md][readme]
>
> [commit 02f9bfe04acd4495e4bd72f480941224b5ec231e][commit]

[readme]: https://github.com/crystal-lang/crystal-book/blob/master/using_the_compiler/README.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/02f9bfe04acd4495e4bd72f480941224b5ec231e

当[安装](../installation/README.md)好编译器之后，在你的环境<!-- 原文单词 disposal-->中便生成了一个二进制文件 `crystal` 。

在接下来的部分中， `$` 符号表示命令行。

## 单次编译和运行

可以调用 带有单个文件名的 `crystal` 来一次性编译和运行一个程序：

```
$ crystal some_program.cr
```

crystal 文件皆以 `.cr` 扩展名结尾。

或者也可以使用 `run` 命令：

```
$ crystal run some_program.cr
```

## 创建可执行的动态链接

可以使用 `build` 命令创建一个可执行文件。

```
$ crystal build some_program.cr
```

这会生成一个 `some_program` 文件然后你可以执行：

```
$ ./some_program
```

**注意：** 默认生成的可执行文件**并没有全部优化**。可以使用 `--release` 参数来优化：

```
$ crystal build some_program.cr --release
```

当可执行文件准备用于生产或基于性能考虑时，确保总是使用 `--release`。

这是因为没有全部优化的性能仍然相当好，并且编译时间也很快，因此 `crystal` 命令几乎相当于一个解释程序。

为了降低二进制文件的大小，可以加上 `--no-debug` 参数并使用 `strip` 命令。如果文件大小是个问题或者无需调试程序的话，使用这个选项会删除掉 Debug 符号。

## 创建一个可执行的独立文件

把你的程序构建成一个独立的可执行文件：

```
$ crystal build some_program.cr --release --static
```

关于静态链接的更多信息可以在[wiki](https://github.com/crystal-lang/crystal/wiki/Static-Linking) 找到。

## 生成一个项目或库

使用 `init` 命令来创建一个 标准目录结构的 Crystal 项目：

```
$ crystal init lib my_cool_lib
      create  my_cool_lib/.gitignore
      create  my_cool_lib/.editorconfig
      create  my_cool_lib/LICENSE
      create  my_cool_lib/README.md
      create  my_cool_lib/.travis.yml
      create  my_cool_lib/shard.yml
      create  my_cool_lib/src/my_cool_lib.cr
      create  my_cool_lib/src/my_cool_lib/version.cr
      create  my_cool_lib/spec/spec_helper.cr
      create  my_cool_lib/spec/my_cool_lib_spec.cr
Initialized empty Git repository in ~/my_cool_lib/.git/
```

## 其他命令和选项

调用不带参数的 `crystal` 命令来查看所有的命令集。

```
$ crystal
Usage: crystal [command] [switches] [program file] [--] [arguments]

Command:
    init                     generate a new project
    build                    build an executable
    deps                     install project dependencies
    docs                     generate documentation
    env                      print Crystal environment information
    eval                     eval code from args or standard input
    play                     starts crystal playground server
    run (default)            build and run program
    spec                     build and run specs (in spec directory)
    tool                     run a tool
    help, --help, -h         show this help
    version, --version, -v   show version
```

通过命令后跟 `--help` 选项来查看一个命令可用的选项：

```
$ crystal build --help
Usage: crystal build [options] [programfile] [--] [arguments]

Options:
    --cross-compile                  cross-compile
    -d, --debug                      Add full symbolic debug info
    --no-debug                       Skip any symbolic debug info
    -D FLAG, --define FLAG           Define a compile-time flag
    --emit [asm|llvm-bc|llvm-ir|obj] Comma separated list of types of output for the compiler to emit
    -f text|json, --format text|json Output format text (default) or json
    --error-trace                    Show full error trace
    -h, --help                       Show this message
    --ll                             Dump ll to Crystal's cache directory
    --link-flags FLAGS               Additional flags to pass to the linker
    --mcpu CPU                       Target specific cpu type
    --mattr CPU                      Target specific features
    --no-color                       Disable colored output
    --no-codegen                     Don't do code generation
    -o                               Output filename
    --prelude                        Use given file as prelude
    --release                        Compile in release mode
    -s, --stats                      Enable statistics output
    -p, --progress                   Enable progress output
    -t, --time                       Enable execution time output
    --single-module                  Generate a single LLVM module
    --threads                        Maximum number of threads to use
    --target TRIPLE                  Target triple
    --verbose                        Display executed commands
    --static                         Link statically
    --stdin-filename                 Source file name to be read from STDIN
```

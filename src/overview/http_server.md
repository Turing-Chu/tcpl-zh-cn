# HTTP Server

一个更有意思的例子是 HTTP 服务器：

```crystal
require "http/server"

server = HTTP::Server.new(8080) do |context|
  context.response.content_type = "text/plain"
  context.response.print "Hello world! The time is #{Time.now}"
end

puts "Listening on http://127.0.0.1:8080"
server.listen
```

当你阅读正个语言参考书的时候，上面的代码便可以理解了，但我们已经学习了一些东西。

* 可以[导入](../syntax_and_semantics/requiring_files.html)定义在其他文件中的代码：


    ```crystal
    require "http/server"
    ```
* 可以定义[局部变量](../syntax_and_semantics/local_variables.html)而无需指定其类型：

    ```crystal
    server = HTTP::Server.new ...
    ```

* 通过在对象上调用[方法](../syntax_and_semantics/classes_and_methods.html)或发送消息来编写代码。

    ```crystal
    HTTP::Server.new(8080) ...
    ...
    Time.now
    ...
    puts "Listening on http://127.0.0.1:8080"
    ...
    server.listen
    ```

* 可以使用代码块或简化[代码块](../syntax_and_semantics/blocks_and_procs.html)，其在重用代码或在实用的世界中得到一些特性时非常方便：

    ```crystal
    HTTP::Server.new(8080) do |context|
      ...
    end
    ```
* 可以使用嵌入式内容比较容易地创建字符串，即所谓字符串插值。语言本身也自带了其他的语法以创建数组、哈希、范围、元组等等：

    ```crystal
    "Hello world! The time is #{Time.now}"
    ```

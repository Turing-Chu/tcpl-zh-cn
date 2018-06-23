# 连接池

当创建连接时，通常意味着打开了一个 TCP 连接或 Socket 。该 socket 一次处理一条语句。如果程序需要同时执行多条查询，或者处理旨在使用数据库的同时发生的请求，则需要多个有效连接。

鉴于应用在使用数据库时，数据库是独立的服务，连接可能丢失，服务可能重启，以及其他各种程序无需关心的情况。

在处理这样的问题上，一般连接池（ connection pool ）是一个利索的解决方法。


当使用 `crystal-db` 打开一个数据库时，已经有一个连接池在运行了。`DB.open` 返回一个 `DB::Database` 对象，其管理整个连接池而不仅仅是单个连接。

```crystal
DB.open("mysql://root@localhost/test") do |db|
  # db is a DB::Database
end
```

当使用 `db.query` 、 `db.exec` 、 `db.scalar` 等执行语句时，该算法：

1. 在连接池中找到一个可用连接。
	1. 如果需要或可能的话，则创建一个连接。
	2. 如果连接池不再允许创建新的连接，则等待连接可用。
		1. 如果等待太久，则会被中断。
2. 从连接池中检出该连接。
3. 执行 SQL 命令。
4. 如果无 `DB::ResultSet 产生，则将该连接返回给连接池。否则，则在 结果集关闭时返回给连接池。
5. 返回语句结果。

如果无法创建连接，或者在赤星语句时发生连接丢失，则重复上面的过程。

> 重试逻辑只在通过 `DB::Database` 发送语句时发生。但如果用 `DB::Connection` 或 `DB::Transaction` 发送语句，是不执行重复逻辑的，因为代码规定了使用确定的连接对象。

## 配置

可以用一个参数集来配置连接池的行为，该参数集出现在 URI 连接的查询语句中。

| Name | Default value |
| :--- | :--- |
| initial\_pool\_size | 1 |
| max\_pool\_size | 0 \(unlimited\) |
| max\_idle\_pool\_size | 1 |
| checkout\_timeout | 5.0 \(seconds\) |
| retry\_attempts | 1 |
| retry\_delay | 1.0 \(seconds\) |

当 `DB::Database` 打开时，则初始创建了 `initial_pool_size` 个连接。该连接池不会持有超过 `max_pool_size` 个连接。当把一个连接返回或释放给连接池时，如果有 `max_idle_pool_size` 个空闲连接，则该连接会被关闭。

如果达到 `max_pool_size` 而又需要一个连接时，则会等待一个已有连接可用直到 `checkout_timeout` 秒超时。

如果连接丢失或无法创建，重试至多 `retry_attempts` 次，每次间隔 `retry_delay` 秒。

## 示例

下面的程序会打印从 MySQL 中读取的当前时间，但如果丢失连接或整个服务宕机几秒，该程序仍然运行而没有抛异常。

```crystal
# file: sample.cr
require "mysql"

DB.open "mysql://root@localhost?retry_attempts=8&retry_delay=3" do |db|
  loop do
    pp db.scalar("SELECT NOW()")
    sleep 0.5
  end
end
```

```
$ crystal sample.cr
db.scalar("SELECT NOW()") # => 2016-12-16 16:36:57
db.scalar("SELECT NOW()") # => 2016-12-16 16:36:57
db.scalar("SELECT NOW()") # => 2016-12-16 16:36:58
db.scalar("SELECT NOW()") # => 2016-12-16 16:36:58
db.scalar("SELECT NOW()") # => 2016-12-16 16:36:59
db.scalar("SELECT NOW()") # => 2016-12-16 16:36:59
# stop mysql server for some seconds
db.scalar("SELECT NOW()") # => 2016-12-16 16:37:06
db.scalar("SELECT NOW()") # => 2016-12-16 16:37:06
db.scalar("SELECT NOW()") # => 2016-12-16 16:37:07
```

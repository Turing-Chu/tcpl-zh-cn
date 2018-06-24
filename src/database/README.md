# 数据库

> [database/README.md][readme]
>
> [commit 266dc253028ecdf07a0e8cb14fb783e747c7104c][commit]

[readme]: https://github.com/crystal-lang/crystal-book/blob/master/database/README.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/266dc253028ecdf07a0e8cb14fb783e747c7104c

可以使用一个为数据库服务器设计的 shard 来访问关系型数据库。在不同的驱动上，[crystal-lang/crystal-db](https://github.com/crystal-lang/crystal-db) 提供了统一的 api 接口。

下面的包适用于 crystal-db：


* sqlite 的 [crystal-lang/crystal-sqlite3](https://github.com/crystal-lang/crystal-sqlite3)
* mysql 和 mariadb 的 [crystal-lang/crystal-mysql](https://github.com/crystal-lang/crystal-mysql)
* postgres 的 [will/crystal-pg](https://github.com/will/crystal-pg)

该指引提供 crystal-db 的 api ，鉴于 postgres 、mysql 和 sqlit 的差异，根据具体的驱动，需要 合适的 sql 命令。

另外，一些驱动可能会提供额外的功能，如 postgres 的 `LISTEN`/`NOTIFY` 。

## 安装 shard

和其他 shard 一样，从上面列表中选择适当的驱动并把它加入到应用的 `shard.yml` 文件中。

不需要再明确地导入 `crystal-lang/crystal-db` 。

在本指引中，使用 `crystal-lang/crystal-mysql` 。

```yaml
dependencies:
  mysql:
    github: crystal-lang/crystal-mysql
```

## 打开数据库连接

通过连接 url ，可以很容易地使用 `DB.open` 来连接数据库。uri 的规则决定了所需要的驱动。下面的例子用 root 用户以及空密码连接到一个本地 mysql 数据库中的 test 库。

```crystal
require "db"
require "mysql"

DB.open "mysql://root@localhost/test" do |db|
  # ... use db to perform queries
end
```

其他的 连接  uri 为：

* `sqlite3:///path/to/data.db`
* `mysql://user:password@server:port/database`
* `postgres://server:port/database`

Alternatively you can use a non yielding `DB.open` method as long as `Database#close` is called at the end.
另外，在 `Database#close` 被调用之前，可以使用一个非生产的 `DB.open` 方法。

```crystal
require "db"
require "mysql"

db = DB.open "mysql://root@localhost/test"
begin
  # ... use db to perform queries
ensure
  db.close
end
```

## 执行

可以用 `Database#exec` 来执行 sql 语句。

```crystal
db.exec "create table contacts (name varchar(30), age int)"
```

用参数来提交数据以防止 sql 注入。

```crystal
db.exec "insert into contacts values (?, ?)", "John", 30
db.exec "insert into contacts values (?, ?)", "Sarah", 33
```

Note: When using the pg driver, use `$1`, `$2`, etc. instead of `?`
注意：当用 pg 驱动时，用 `$` 、 `$2` 等代替 `?` 。

## 查询

使用 `Database#query` 来执行查询并获取结果集，在 `Database#exec` 中可以使用参数。

`Database#query` 需要返回 `ResultSet` 类型来关闭查询。和在 `Database#open` 中一样，如果在代码块中调用，`ResultSet` 会默认关闭。

```crystal
db.query "select name, age from contacts order by age desc" do |rs|
  rs.each do
    # ... perform for each row in the ResultSet
  end
end
```

当从数据库中读取值时，crystal 在编译时并无类型信息可用。你需要在类型 `T` 上调用 `rs.read(T)` 方法来从数据库中获取你想要的。

```crystal
db.query "select name, age from contacts order by age desc" do |rs|
  rs.each do
    name = rs.read(String)
    age = rs.read(Int32)
    puts "#{name} (#{age})"
    # => Sarah (33)
    # => John Doe (30)
  end
end
```

有很多方便的查询方法被编译进 `#query` 里。

可以一次读取多个列：

```crystal
name, age = rs.read(String, Int32)
```

或读取一行：

```crystal
name, age = db.query_one "select name, age from contacts order by age desc limit 1", as: { String, Int32 }
```

也可以读取标量值而无需用 ResultSet  明确的处理：

```crystal
max_age = db.scalar "select max(age) from contacts"
```

所有在数据库中执行语句的可用方法都定义在 `DB::QueryMethods` 中。


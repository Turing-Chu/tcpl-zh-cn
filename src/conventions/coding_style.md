# 代码风格

> [conventions/coding_style.md][coding_style]
> 
> [commit 261694dcfb416870928ca6593f065b39d2d6c283][commit]

[coding_style]: https://github.com/crystal-lang/crystal-book/blob/master/conventions/coding_style.md
[commit]: https://github.com/crystal-lang/crystal-book/commit/261694dcfb416870928ca6593f065b39d2d6c283 

该代码风格在标准库中被使用。可以在你自己的项目中使用该代码风格，以便为其他开发者所熟悉。

## 命名

驼峰式__类型名__。例如：

```crystal
class ParseError < Exception
end

module HTTP
  class RequestHandler
  end
end

alias NumericValue = Float32 | Float64 | Int32 | Int64

lib LibYAML
end

struct TagDirective
end

enum Time::DayOfWeek
end
```

下划线式__方法名__。例如：

```crystal
class Person
  def first_name
  end

  def date_of_birth
  end

  def homepage_url
  end
end
```

下划线式__变量名__。例如：

```crystal
class Greeting
  @@default_greeting = "Hello world"

  def initialize(@custom_greeting = nil)
  end

  def print_greeting
    greeting = @custom_greeting || @@default_greeting
    puts greeting
  end
end
```

尖锐式__常量名__。例如：

```crystal
LUCKY_NUMBERS     = [3, 7, 11]
DOCUMENTATION_URL = "http://crystal-lang.org/docs"
```

### 缩写

类名中，缩写全部_大写_。例如：`HTTP` 和 `LibXML`。

方法名中，缩写全部小写。例如 `#from_json` 和 `#to_io` 。

### 库

`Lib` 名以 `Lib` 为前缀。例如：`LibC` 和 `LibEvent2` 。

### 目录和文件名

在项目中：

- `/` 包含 readme 、任何项目配置（如 CI 或其他配置）、任何其他项目级文档（如 changlog 或贡献指引）。
- `src/` 包含项目源代码。
- `spec/` 包含[项目 specs](../guides/testing.md) ，其可以用 `crystal spec` 来执行。
- `bin/` 包含可执行文件。

文件路径与其内容相匹配。文件以其定义的类名或命名空间名为名，并使用_下划线式_。
例如，`HTTP::WebSocket` 定义在 `src/http/web_socket.cr` 中。

## 空格

在命名空间、代码块或其他内嵌内容中，使用__两个空格__缩进代码。例如：

```crystal
module Scorecard
  class Parser
    def parse(score_text)
      begin
        score_text.scan(SCORE_PATTERN) do |match|
          handle_match(match)
        end
      rescue err : ParseError
        # handle error ...
      end
    end
  end
end
```

在类中，用__换行符__隔开代码定义、常量以及其他类内部的定义。例如：

```crystal
module Money
  CURRENCIES = {
    "EUR" => 1.0,
    "ARS" => 10.55,
    "USD" => 1.12,
    "JPY" => 134.15,
  }

  class Amount
    getter :currency, :value

    def initialize(@currency, @value)
    end
  end

  class CurrencyConversion
    def initialize(@amount, @target_currency)
    end

    def amount
      # implement conversion ...
    end
  end
end
```

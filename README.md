# selenium-pom

selenium 页面模型框架

增加你自己的 pytest.ini 文件 和 variables.json 文件

eg, pytest.ini

```
  [pytest]
  python_paths = .
  addopts = --maxfail=2 -rf
  testpaths = tests
  base_url = http://www.baidu.com
  sensitive_url = example\.cn
```

eg, variables.json

```
{
  "users": {
    "default": {
      "password": "",
      "username": ""

    },
    "cookie": {
      "name":"",
      "value": ""
    }
  },
  "api": {
    "user": "",
    "key": ""
  }
}

```



运行你的 case：
`py.test --driver Chrome --variable path/to/variables.json`

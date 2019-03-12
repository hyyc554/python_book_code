# InfluxDB——python使用手册

![AStdAS.png](https://s2.ax1x.com/2019/03/09/AStdAS.png)

## 准备工作

安装InfluxDB：

请参考笔者相关博文：[Centos7安装InfluxDB1.7](https://www.cnblogs.com/huang-yc/p/10500098.html)

安装pip ：

```bash
yum install python-pip
```

安装influxdb-python ：

```bash
pip install influxdb 
```

实际上py的influx官方包的doc也已经足够详细，值得过一遍：[py-influxdb](https://influxdb-python.readthedocs.io/en/latest/include-readme.html)

## 基本操作

使用InfluxDBClient类操作数据库，示例如下：

```python
# 初始化
client = InfluxDBClient('localhost', 8086, 'your_username', 'yuor_password', 'your_dbname') 
```

- 显示已存在的所有数据库

　　使用get_list_database函数，示例如下：

　　`print client.get_list_database() # 显示所有数据库名称`

- 创建新数据库

　　使用create_database函数，示例如下：

　　`client.create_database('testdb') # 创建数据库`

- 删除数据库

　　使用drop_database函数，示例如下：

　　`client.drop_database('testdb') # 删除数据库`

数据库操作完整示例如下：

```python
from influxdb import InfluxDBClient

# 初始化（指定要操作的数据库）
client = InfluxDBClient('localhost', 8086, 'your_username', 'yuor_password', 'your_dbname') 
print(client.get_list_database()) # 显示所有数据库名称
client.create_database('testdb') # 创建数据库
print(client.get_list_database()) # 显示所有数据库名称
client.drop_database('testdb') # 删除数据库
print(client.get_list_database()) # 显示所有数据库名称
```

### 表操作

InfluxDBClient中要指定连接的数据库，示例如下：

```python
client = InfluxDBClient('localhost', 8086, 'your_username', 'yuor_password', 'your_dbname') 
```

- 显示指定数据库中已存在的表

　　可以通过influxql语句实现，示例如下：

```python
result = client.query('show measurements;') # 显示数据库中的表
print("Result: {0}".format(result))
```

- 创建新表并添加数据

InfluxDB没有提供单独的建表语句，可以通过并添加数据的方式建表，示例如下：

```python
current_time = datetime.datetime.utcnow().isoformat("T")
body = [
    {
        "measurement": "students",
        "time": current_time,
        "tags": {
            "class": 1
        },
        "fields": {
            "name": "Hyc",
            "age": 3
        },
    }
]

res = client.write_points(body)
```

- 删除表

可以通过influxql语句实现，示例如下：

```
client.query("drop measurement students") # 删除表
```

数据表操作完整示例如下：

```python
import datetime
from influxdb import InfluxDBClient


client = InfluxDBClient('localhost', 8086, 'your_username', 'yuor_password', 'your_dbname') 
current_time = datetime.datetime.utcnow().isoformat("T")
body = [
    {
        "measurement": "students",
        "time": current_time,
        "tags": {
            "class": 1
        },
        "fields": {
            "name": "Hyc",
            "age": 3
        },
    }
]
res = client.write_points(body)
client.query("drop measurement students")
```

## 数据操作

InfluxDBClient中要指定连接的数据库，示例如下：

```
# 初始化（指定要操作的数据库）
client = InfluxDBClient('localhost', 8086, 'your_username', 'yuor_password', 'your_dbname')  
```

- 添加

**经过笔者测试write_points相当于其它数据库的批量写入操作，建议处理大量数据是对数据进行缓存后利用write_points一次批量写入。**

可以通过write_points实现，示例如下：

```python
body = [
    {
        "measurement": "students",
        "time": current_time,
        "tags": {
            "class": 1
        },
        "fields": {
            "name": "Hyc",
            "age": 3
        },
    }，
    {
        "measurement": "students",
        "time": current_time,
        "tags": {
            "class": 2
        },
        "fields": {
            "name": "Ncb",
            "age": 21
        },
    }，
]
res = client.write_points(body)
```

- 查询

可以通过influxql语句实现，示例如下：

```python
result = client.query('select * from students;')
print("Result: {0}".format(result))
```

- 更新

tags 和 timestamp相同时数据会执行覆盖操作，相当于InfluxDB的更新操作。

- 删除

使用influxql语句实现，delete语法，示例如下：

```python
client.query('delete from students;') # 删除数据
```



## 参考文章

> InfluDB官方文档：https://docs.influxdata.com/influxdb/v1.7/introduction/installation/
> python-influx doc:https://influxdb-python.readthedocs.io/en/latest/include-readme.html
> [Mike_Zhang](https://home.cnblogs.com/u/MikeZhang/):[使用python操作InfluxDB](https://www.cnblogs.com/MikeZhang/p/InfluxDBPythonOpt20170312.html)
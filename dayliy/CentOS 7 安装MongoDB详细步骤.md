# CentOS 7 安装MongoDB详细步骤

![kHCmeP.png](https://s2.ax1x.com/2019/02/28/kHCmeP.png)

创建`/etc/yum.repos.d/mongodb-org-4.0.repo`文件，编辑内容如下：

```ini
[mongodb-org-4.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc
```

运行以下命令安装最新版的mongodb：

```bash
sudo yum install -y mongodb-org
```

配置`mongod.conf`允许远程连接：

```bash
$ vim /etc/mongod.conf

# Listen to all ip address
bind_ip = 0.0.0.0
```

启动mongodb：

```bash
sudo service mongod start
```

创建管理员用户：

```bash
$ mongo
>use admin
 db.createUser(
  {
    user: "myUserAdmin",
    pwd: "abc123",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
  }
 )
```

启用权限管理：

```bash
$ vim /etc/mongod.conf

#security 
security:
  authorization: enabled
```

重启mongodb：

```bash
sudo service mongod restart
```

大功告成！
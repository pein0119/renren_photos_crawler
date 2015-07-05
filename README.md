renren_photos_crawler
=======

人人相册爬虫，只爬取公开相册(不公开的我也没法儿访问呀)

# 前提

**首先要成功登录你的人人账号，获得cookie！！**
**首先要成功登录你的人人账号，获得cookie！！**

# 测试环境
* OSX Yosemite 10.10.4
* Python 2.7.9

# 依赖库
* lxml
* requests

可以通过一下命令安装
``` shell
$ pip install lxml requests
```
# 配置文件
`config.ini`

* [cookie]  
你的人人网cookie

登录你得人人,在`renren.com`域下打开chrome的console，输入以下命令：

``` javascript
document.cookie
```
按下回车，即可得到你在renren的cookie

范例：
```
cookie = a=1; b=2; c=3
```
`a=1; b=2; c=3`就是你使用`document.cookie`得到的cookie

* [dir]  
你要将你的相册存储在哪里

范例：
```
start_dir = '/home/work/me/'
```
* [person]  
你想下载的相册的人的"人人ID"和"姓名"
在`start_dir`下会建一个以“姓名”命名得文件夹，存储他的所有相册
"人人ID"是该人在人人网得账号，就像你的QQ号一样，比如我得人人网首页是 `http://www.renren.com/353077725/profile`， 我得人人ID就是`353077725`

范例：
```
123456 = 呵呵
```

# 使用方法

* 按以上方法安装Python及依赖得Python库
* 下载该代代码
* 修改`config.ini`
* 使用`python renren_photos_crawler.py`命令运行，即可下载相册

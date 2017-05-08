ddconnector
===========

依赖
-----------

* Python: > 3.6

安装
-----------

安装指令::

    python3.6 -m venv venv
    source venv/bin/active
    python setup.py install

配置
-----------

**config.ini**


操作
------------

打开DEBUG级别日志::

    ddconnector_cli debug 1

关闭DEBUG级别日志::

    ddconnector_cli debug 0
    
查看当前门禁设备连接数

    ddconnector_cli total
    
启动gc回收
    ddconnector_cli gc


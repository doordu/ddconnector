ddconnector
===========

依赖
-----------

* Python: > 3.6

安装
-----------

::
    python3.6 -m venv venv
    source venv/bin/active
    python setup.py install

配置
-----------

**config.ini**


操作
------------

打开DEBUG级别日志::

    telnet localhost 9501
    eyJjbWQiOiAiZGVidWciLCAiZW5hYmxlZCI6IHRydWV9*

关闭DEBUG级别日志::

    telnet localhost 9501
    eyJjbWQiOiAiZGVidWciLCAiZW5hYmxlZCI6IGZhbHNlfQ==*


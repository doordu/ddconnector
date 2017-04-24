## Work in progress!

## 心跳包

门禁机 -> 服务器：

{"guid":"testzz20161020001","cmd":"heart_beat","version":"5.8.001.0"}

服务器 -> 门禁机:

{"request_id":"testzz20161020001","token_id":"","cmd":"heart_beat","response_type":true,"response_params":{"success":true,"message":"","data":[],"totalCount":"0"}}


## 开门

发起开门：

{"fd":679,"cmd":"open_door","from_id":0,"guid":"test20170310-111","isClient":true,"time":"2017-04-19 20:42:31","data":"{\"door_guid\":\"test20170310-111\",\"room_id\":\"424990\",\"floor\":1,\"operate_type\":2,\"device_type\":\"2\",\"content\":\"%7B%22doorGuid%22%3A%22test20170310-111%22%2C%22roomId%22%3A%22424990%22%2C%22userId%22%3A%22280846%22%7D\",\"device_guid\":\"74ad0d4e1570e08f-a47a7898481eabf77a1a5ce061f7908b-280846\"}"}

eyJmZCI6NzY4LCJjbWQiOiJvcGVuX2Rvb3IiLCJmcm9tX2lkIjowLCJndWlkIjoidGVzdDIwMTcwMzEwLTExMSIsImlzQ2xpZW50Ijp0cnVlLCJ0aW1lIjoiMjAxNy0wNC0yMCAxNDoyODoxMiIsImRhdGEiOiJ7XCJkb29yX2d1aWRcIjpcInRlc3QyMDE3MDMxMC0xMTFcIixcInJvb21faWRcIjpcIjQyNDk5MFwiLFwiZmxvb3JcIjoxLFwib3BlcmF0ZV90eXBlXCI6MixcImRldmljZV90eXBlXCI6XCIyXCIsXCJjb250ZW50XCI6XCIlN0IlMjJkb29yR3VpZCUyMiUzQSUyMnRlc3QyMDE3MDMxMC0xMTElMjIlMkMlMjJyb29tSWQlMjIlM0ElMjI0MjQ5OTAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjIyODA4NDYlMjIlN0RcIixcImRldmljZV9ndWlkXCI6XCI3NGFkMGQ0ZTE1NzBlMDhmLWE0N2E3ODk4NDgxZWFiZjc3YTFhNWNlMDYxZjc5MDhiLTI4MDg0NlwifSJ9*


服务器下发：

{"request_id":"testzz20170418001","token_id":"","cmd":"open_door","response_type":false,"response_params":{"success":true,"message":"","data":[{"door_guid":"testzz20170418001","room_id":"424990","floor":1,"operate_type":2,"device_type":"2","content":"%7B%22doorGuid%22%3A%22testzz20170418001%22%2C%22roomId%22%3A%22424990%22%2C%22userId%22%3A%22280846%22%7D","device_guid":"74ad0d4e1570e08f-a47a7898481eabf77a1a5ce061f7908b-280846"}],"totalCount":"0"}}

门禁机返回：

{"guid":"testzz20170418001","success":true,"cmd":"open_door","version":"5.8.000.0"}

## 默认配置

web -> 9501

{"fd":1020,"cmd":"Prompt","from_id":null,"guid":"test20170418001","data":"{\"qrcode\":\"https:\\\/\\\/doordustorage.oss-cn-shenzhen.aliyuncs.com\\\/app\\\/android\\\/c4471287797d9071630126b4f56da1a3.jpg\",\"qrcode_hint\":\"\\u626b\\u63cf\\u4e8c\\u7ef4\\u7801\\uff0c\\u4e0b\\u8f7d\\u5ba2\\u6237\\u7aef\",\"agent_mobile\":\"01010205\",\"door_name\":\"\\u8b66\\u52a1\\u52a9\\u624b\\u81ea\\u52a9\\u6388\\u6743\",\"dial_hint\":\"<b>\\u4f34\\u751f\\u6d3b\\u4f7f\\u7528\\u5e2e\\u52a9<\\\/b>\\n<p><font color=\\\"#FF0000\\\">\\u4e00\\u3001\\u547c\\u53eb\\u5f00\\u95e8\\u5e2e\\u52a9<\\\/font><\\\/a><br \\\/>\\n\\u5927\\u95e8\\u4e3b\\u673a\\u547c\\u53eb\\u62e8\\u53f7\\u89c4\\u5219\\uff1a\\u680b\\u53f7\\uff0b\\u5355\\u5143\\u53f7\\uff0b\\u623f\\u53f7\\uff0c\\u5982\\u62e8\\u62531\\u680b1\\u5355\\u5143201\\u7528\\u6237\\uff0c\\u53ea\\u9700\\u6309\\u952e\\u8f93\\u516501010201\\uff0c\\u6309\\u201cOK\\u201d\\u952e\\uff0c\\u5373\\u53d1\\u51fa\\u547c\\u53eb\\u3002<br \\\/>\\n\\u5355\\u5143\\u95e8\\u4e3b\\u673a\\u547c\\u53eb\\u62e8\\u53f7\\u89c4\\u5219\\uff1a\\u5982\\u62e8\\u6253201\\u7528\\u6237\\uff0c\\u53ea\\u9700\\u6309\\u952e\\u8f93\\u51650201\\uff0c\\u6309\\u201cOK\\u201d\\u952e\\uff0c\\u5373\\u53d1\\u51fa\\u547c\\u53eb\\u3002<br \\\/>\\n\\u547c\\u53eb\\u65e0\\u5e94\\u7b54\\uff1a\\u8be5\\u623f\\u53f7\\u65e0\\u4eba\\u5728\\u5bb6\\u6216\\u5df2\\u5f00\\u542f\\u514d\\u6253\\u6270\\u6a21\\u5f0f\\u3002\\u5982\\u9700\\u5e2e\\u52a9\\u8bf7\\u6309\\u201c\\u7ba1\\u7406\\u5904\\u201d\\u6309\\u952e\\u4e0e\\u7269\\u4e1a\\u7ba1\\u7406\\u5904\\u53d6\\u5f97\\u8054\\u7cfb\\u3002<br \\\/>\\n\\u547c\\u53eb\\u5931\\u8d25\\uff1a\\u7f51\\u7edc\\u7e41\\u5fd9\\uff0c\\u8bf7\\u7a0d\\u5019\\u518d\\u8bd5\\u3002\\u5982\\u9700\\u5e2e\\u52a9\\u8bf7\\u6309\\u201c\\u7ba1\\u7406\\u5904\\u201d\\u6309\\u952e\\u4e0e\\u7269\\u4e1a\\u7ba1\\u7406\\u5904\\u53d6\\u5f97\\u8054\\u7cfb\\u3002<br \\\/><br \\\/>\\n<font color=\\\"#FF0000\\\">\\u4e8c\\u3001APP\\u5f00\\u95e8\\u5e2e\\u52a9<\\\/font><br \\\/>\\nAPP\\u4f7f\\u7528\\uff1a\\u5728\\u624b\\u673a\\u5e94\\u7528\\u5e02\\u573a\\u4e0b\\u8f7d\\u5b89\\u88c5\\u201c\\u4f34\\u751f\\u6d3b\\u201dAPP\\u540e\\uff0c\\u901a\\u8fc7\\u6ce8\\u518c\\u767b\\u5f55\\uff0c\\u5e76\\u5728\\u7ba1\\u7406\\u5904\\u6388\\u6743\\uff0c\\u5373\\u53ef\\u4f7f\\u7528\\u624b\\u673aAPP\\u5f00\\u95e8\\u3002<br \\\/>\\nAPP\\u5f00\\u95e8\\u5931\\u8d25\\uff1a\\u8bf7\\u68c0\\u67e5\\u624b\\u673a\\u7f51\\u7edc\\u662f\\u5426\\u6b63\\u5e38\\uff0c\\u91cd\\u65b0\\u5237\\u65b0\\u5c0f\\u533a\\u5217\\u8868\\u518d\\u8fdb\\u884c\\u5f00\\u95e8\\u64cd\\u4f5c\\u3002\\u5982\\u9700\\u5e2e\\u52a9\\u8bf7\\u6309\\u201c\\u7ba1\\u7406\\u5904\\u201d\\u6309\\u952e\\u4e0e\\u7269\\u4e1a\\u7ba1\\u7406\\u5904\\u53d6\\u5f97\\u8054\\u7cfb\\u3002<br \\\/>\\n<p align=\\\"right\\\"><font color=\\\"#FF0000\\\">\\u66f4\\u591a\\u5e2e\\u52a9\\u6b22\\u8fce\\u81f4\\u7535\\u4f34\\u751f\\u6d3b\\u5168\\u56fd\\u670d\\u52a1\\u70ed\\u7ebf\\uff1a4008-528-400<\\\/font><\\\/p>\",\"background\":\"\",\"hint\":\"\\u63d0\\u793a\\u4fe1\\u606f\\u606f\"}","isClient":true,"time":"2017-04-24 14:20:41"}

9501 -> 门禁机

{"request_id":"test20170418001","token_id":"","cmd":"Prompt","response_type":false,"response_params":{"success":true,"message":"","data":[{"qrcode":"https:\/\/doordustorage.oss-cn-shenzhen.aliyuncs.com\/app\/android\/c4471287797d9071630126b4f56da1a3.jpg","qrcode_hint":"扫描二维码，下载客户端","agent_mobile":"01010205","door_name":"警务助手自助授权","dial_hint":"<b>伴生活使用帮助<\/b>\n<p><font color=\"#FF0000\">一、呼叫开门帮助<\/font><\/a><br \/>\n大门主机呼叫拨号规则：栋号＋单元号＋房号，如拨打1栋1单元201用户，只需按键输入01010201，按“OK”键，即发出呼叫。<br \/>\n单元门主机呼叫拨号规则：如拨打201用户，只需按键输入0201，按“OK”键，即发出呼叫。<br \/>\n呼叫无应答：该房号无人在家或已开启免打扰模式。如需帮助请按“管理处”按键与物业管理处取得联系。<br \/>\n呼叫失败：网络繁忙，请稍候再试。如需帮助请按“管理处”按键与物业管理处取得联系。<br \/><br \/>\n<font color=\"#FF0000\">二、APP开门帮助<\/font><br \/>\nAPP使用：在手机应用市场下载安装“伴生活”APP后，通过注册登录，并在管理处授权，即可使用手机APP开门。<br \/>\nAPP开门失败：请检查手机网络是否正常，重新刷新小区列表再进行开门操作。如需帮助请按“管理处”按键与物业管理处取得联系。<br \/>\n<p align=\"right\"><font color=\"#FF0000\">更多帮助欢迎致电伴生活全国服务热线：4008-528-400<\/font><\/p>","background":"","hint":"提示信息息"}],"totalCount":"0"}}

门禁机 -> 9501

{"guid":"test20170418001","success":false,"cmd":"Prompt","version":"5.8.000.0"}

回包

## 下发SIP信息

web -> 9501
{"fd":1020,"cmd":"get_config","from_id":null,"guid":"test20170418001","data":"{\"sipNumber\":\"13662331\",\"sipPassword\":\"97292971\",\"sipDomain\":\"hj.t3tl.com\"}","isClient":true,"time":"2017-04-24 14:24:00"}

9501 -> 门禁机
{"request_id":"test20170418001","token_id":"","cmd":"get_config","response_type":false,"response_params":{"success":true,"message":"","data":[{"sipNumber":"13662331","sipPassword":"97292971","sipDomain":"hj.t3tl.com"}],"totalCount":"0"}}

门禁机 -> 9501
{"guid":"test20170418001","success":true,"cmd":"get_config","version":"5.8.000.0"}




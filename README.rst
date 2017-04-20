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
# Javlibrary
-----------------------------------
### 口袋48APP 监控(Python3)，该项目实现以下功能:
* 登录并获取token
* 管理token，支持多账号登录
* 计划任务，支持多成员监控
* 获取成员房间roomid
* 获取成员房间消息
* mongodb存放消息
* 通过酷Q向群和私人发送消息

## Update Log
--------------------------
#### 2019.04.22 Ver.1.0

1.增加计划任务支持，支持多偶像监控

2.增加token管理，支持多账号登录

3.改善项目结构

#### 2019.04.19 Ver.0.2 

增加对酷Q机器人的支持

#### 2019.04.18 Ver.0.1
实现基本功能

## 使用方法
--------------------------
1.开启mongodb本地服务器、从botserver.py开启酷Q本地服务器

2.修改pocket48.py中的用户名和偶像名

3.开启pocket48.py

## 方法说明
--------------------------
|方法|功能|参数|
| :----------: | :-----------:|:-----------:|
| login   | 登录  | 手机，密码 |
| searchroom   |  查询指定成员roomId  | 成员全名 |
| chatroom   |  查询成员房间消息  | roomId,ownerId |

## 数据库
-------------------------------------------
### 本项目使用MongoDB作为数据库：
--------------------------
|数据库|表名|参数|
| :----------: | :-----------:| :-----------:|
| Poket48   | dbtoken | 所有登录账号token |
| Poket48   |  { room_id1 }  | 成员1的房间消息 |
| Poket48   |  { room_id2 }  | 成员2的房间消息 |
| Poket48   |  ...  | ... |

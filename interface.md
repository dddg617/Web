# 普通用户


## 普通用户注册

接口 URL：```/api/user/register```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|username|是|string|用户名|
|name|是|string|用户姓名|
|ID-type|是|string|证件类型（中华人民共和国居民身份证，台湾居民往来大陆通行证，港澳居民来往内地通行证，军人证件，护照，香港身份证，澳门身份证）|
|ID|是|string|证件号|
|password|是|string|密码|
|phone|否|string|电话（11位）|
|introduction|否|string|用户简介|
|city|是|string|注册城市（要和证件匹配）|
|community|是|string|注册社区|
|time|是|string("xx-xx-xx")|注册时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|
|user_ID|string|注册用户标识|

## 普通用户查询个人信息

接口 URL：```/api/user/check```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|user_ID|是|string|用户标识|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|username|string|用户名|
|name|string|用户姓名|
|ID|string|证件号|
|phone|string|电话（11位）|
|introduction|string|用户简介|
|city|string|注册城市（要和证件匹配）|
|community|string|注册社区|

## 普通用户修改信息

接口 URL：```/api/user/change```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|user_ID|是|string|用户标识|
|phone|否|string|联系电话（11位）|
|password|否|string|密码|
|introduction|否|string|用户简介|
|time|是|string("xx-xx-xx")|修改时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|

## 用户登录

接口 URL：```/api/user/login```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|username|是|string|用户名|
|password|是|string|密码|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|isAdmin|Boolean|普通用户为``False``，管理员为``True``|
|user_ID|string|用户标识|

## 普通用户发布请求信息

接口 URL：```/api/user/require```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|user_ID|是|string|用户标识|
|type|是|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|
|topic|是|string|请求主题|
|description|是|string|请求描述|
|number|是|int|请求人数|
|end_time|是|string("xx-xx-xx")|请求结束时间|
|time|是|string("xx-xx-xx")|发起请求时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|
|require_ID|string|请求标识|

## 普通用户查询自己发布的请求

接口 URL：```/api/user/require_check```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数


|参数名称|必选|类型|说明|
|----|----|----|----|
|user_ID|是|string|用户标识|

### 返回JSON

> list类型，包含以下内容

|属性|类型|说明|
|---|---|---|
|require_ID|string|请求标识|

## 普通用户查询自己发布的请求的详细信息

接口 URL：```/api/user/require_check/details```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|require_ID|是|string|请求标识|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|type|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|
|topic|string|请求主题|
|description|string|请求描述|
|number|int|请求人数|
|time|string("xx-xx-xx")|发起请求时间|
|state|int|状态（0代表已完成，1代表待响应，2代表已取消，3代表到期未完成）|

## 普通用户查询自己发布的请求，别人的响应信息：

接口 URL：```/api/user/require_check/response_check```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|require_ID|是|string|请求标识|

### 返回JSON
> list类型，包含以下内容

|属性|类型|说明|
|---|---|---|
|response_ID|string|响应标识|
|name|string|响应用户名|
|user_ID|string|响应用户标识|
|response|string|响应描述|
|time|string("xx-xx-xx")|响应时间|

## 普通用户处理响应信息

接口 URL：```/api/user/require_check/response_confirm```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|response_ID|是|string|响应标识|
|accept|是|Boolean|是否接受响应，接受为``True``，拒绝为``False``|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|

## 普通用户修改请求信息

接口 URL：```/api/user/require_check/require_change```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|require_ID|是|string|请求标识|
|type|否|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|
|topic|否|string|请求主题|
|description|否|string|请求描述|
|number|否|int|请求人数|
|time|是|string("xx-xx-xx")|请求修改时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|

## 普通用户删除请求信息

接口 URL：```/api/user/require_check/require_delete```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|require_ID|是|string|请求标识|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|

## 普通用户查看所有帮忙请求信息

接口 URL：```/api/user/response```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|community|是|string|用户所属社区|

### 返回JSON

> list类型，包含以下内容

|属性|类型|说明|
|---|---|---|
|require_ID|string|请求标识|


## 普通用户查看所有帮忙请求信息的详细信息

接口 URL：```/api/user/response/details```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|require_ID|是|string|请求标识|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|type|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|
|topic|string|请求主题|
|description|string|请求描述|
|number|int|请求人数|
|time|string("xx-xx-xx")|发起请求时间|

## 普通用户查看自己发布的响应信息

接口 URL：```/api/user/response_check```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|user_ID|是|string|用户标识|

### 返回JSON

> list类型，包含以下内容


|属性|类型|说明|
|---|---|---|
|response_ID|string|响应标识|

## 普通用户查看自己发布的响应信息的详细内容

接口 URL：```/api/user/response_check/details```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|response_ID|是|string|用户标识|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|require_ID|string|请求标识|
|description|string|响应描述|
|time|string("xx-xx-xx")|响应创建时间|
|state|int|状态（0代表待接收，1代表同意，2代表拒绝，3代表取消）|


## 普通用户修改还未被接受的响应信息

接口 URL：```/api/user/response_check```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|response_ID|是|string|响应标识|
|description|否|string|响应描述|
|time|是|string("xx-xx-xx")|修改时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|

## 普通用户删除还未被接受的响应信息

接口 URL：```/api/user/response_check```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|response_ID|是|string|响应标识|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|

## 普通用户响应请求信息

接口 URL：```/api/user/response_check```

请求方法：```POST```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|user_ID|是|string|用户标识|
|require_ID|是|string|请求标识|
|description|是|string|响应描述|
|time|是|string("xx-xx-xx")|响应创建时间|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|success|Boolean|成功为``True``，失败为``False``|
|response_ID|string|响应标识|

# 管理员

## 管理员查询所有请求帮忙信息的状态

接口 URL：```/api/admin/check```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|admin_ID|是|string|管理员标识|

### 返回JSON

> list类型，包含以下内容

|属性|类型|说明|
|---|---|---|
|require_ID|string|请求ID|
|state|int|状态（0代表已完成，1代表待响应，2代表已取消，3代表到期未完成）|

## 管理员查询所有请求帮忙信息的用户信息

接口 URL：```/api/admin/check/user```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|admin_ID|是|string|管理员标识|

### 返回JSON

> list类型，包含以下内容

|属性|类型|说明|
|---|---|---|
|username|string|用户名|
|name|string|用户姓名|
|ID-type|string|证件类型（中华人民共和国居民身份证，台湾居民往来大陆通行证，港澳居民来往内地通行证，军人证件，护照，香港身份证，澳门身份证）|
|ID|string|证件号|
|phone|string|电话（11位）|
|introduction|string|用户简介|
|city|string|注册城市（要和证件匹配）|
|community|string|注册社区|
|time|string("xx-xx-xx")|注册时间|

## 管理员查询所有接受请求信息

接口 URL：```/api/admin/accept_check```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|admin_ID|是|string|管理员标识|

### 返回JSON

> list类型，包含以下内容

|属性|类型|说明|
|---|---|---|
|require_ID|string|接受请求的请求标识|
|type|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|
|topic|string|请求主题|
|description|string|请求描述|
|number|int|请求人数|
|time|string("xx-xx-xx")|发起请求时间|

## 管理员查询接受请求对应的响应用户

接口 URL：```/api/admin/accept_check/user```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|required_ID|是|string|请求ID|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|username|string|用户名|
|name|string|用户姓名|
|ID-type|string|证件类型（中华人民共和国居民身份证，台湾居民往来大陆通行证，港澳居民来往内地通行证，军人证件，护照，香港身份证，澳门身份证）|
|ID|string|证件号|
|phone|string|电话（11位）|
|introduction|string|用户简介|
|city|string|注册城市（要和证件匹配）|
|community|string|注册社区|
|time|string("xx-xx-xx")|注册时间|

## 管理员查询所有已完成请求的中介费

接口 URL：```/api/admin/cost```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|admin_ID|是|string|管理员标识|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|money|int|总中介费用|

# 统计模块

接口 URL：```/api/statistics```

请求方法：```GET```

编码方式：```application/x-www-form-urlencoded```

### 请求参数

|参数名称|必选|类型|说明|
|----|----|----|----|
|start|是|date|起始时间|
|end|是|date|终止时间|
|city|是|string|地区|
|community|是|string|社区|
|type|是|string|请求类型（小时工 、 搬重物 、 上下班搭车 、 社区服务自愿者）|

### 返回JSON

|属性|类型|说明|
|---|---|---|
|time|string("xx-xx-xx")|时间（按月）|
|money|int|每月中介费|
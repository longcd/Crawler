# 爬取租房信息

### 1. 进入[小猪短租](http://www.xiaozhu.com/)。在详情页中爬取以下信息：

- 标题
- 地址
- 日租金
- 第一张房源链接
- 房东图片链接
- 房东性别
- 房东名字

### 2. 爬取300个房源

还是刚刚那些信息。需要先从列表页获取每个详情页的链接。

### 3. 注：

`房东性别`，这不是一个可以直接爬取的信息，只要运用`if-else`这个条件判断就能解决。

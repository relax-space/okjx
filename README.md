# okjx

总共5条线路, 目前只支持默认线路: 即1号线路

## 如何开始
### 配置
```
    # 设置好下面参数即可, 第一个参数是电影名,第二个是电影地址, 可以一次下载多部
    video_list = [
        ('test2', 'https://v.qq.com/x/cover/mzc00200tgro986.html'),
    ]

```
### 安装包
1. 安装python  `pip install -r requirements.txt`

### 运行
```
python main.py
```


## 整体思路
1. 得到域名:https://api.okjx.cc:3389, 通过请求: https://okjx.cc/?url=
2. 得到路由: /m3.php, 通过请求:https://api.okjx.cc:3389/3jx.php
3. 得到m3u8地址和参数t: 此时地址是加密的, 通过请求: https://m3u8.okjx.cc:3389/m3.php
4. 得到授权: 通过请求 https://shouquan.laohutao.com/shouquan.php?t=7c402f51c83dd00a,另外一个d参数是通过m3u8.okjx.cc|7c402f51c83dd00a加密获得
5. 得到解密key: 固定值: 36606EE9A59DDCE2 ,全局搜索:getVideoInfo即可在附近找到
6. 解密m3u8地址: 有以下三种形式
``` 
https://api.nxflv.com/Cache/YouKu/678e9917dc3e5bac5b727ad185876703.m3u8

https://json.nbjx.vip:4399/hls/1649044731.m3u8?vkey=1754ZnVT61_FwZoYBdv3CCdu6oEF8fXnOBQA1n_utOaAZ46_cnAc1ko26Hk_Z7sgaZWeDPQvAj17-KFmNyQmYOrUoq3eQ0DaVajHL4lPug

https://subtitle.apdcdn.tc.qq.com/vipzj.video.tc.qq.com/o0035orc73u.mp4?vkey=3720E30A4B7300CFA1E660BB57EEEBD44C66DAEA268EA1C44A8C8894BC67AEF02D28D77222D25DCDFA58D68FF1C8E1977CEFA82106EFECB096FF60AA60AF80E14E3D620368463E8B76C7E09FC818143FADA0AD1E2A083FCB623191077C1B9A0D14B0D87BAF1DBEA2E55F149DFFADFDC4F4E2CF44B5B4944C&QQ=335583&From=www.nxflv.com
```
7. 获取ts地址: 通过请求m3u8文件,记得header中要加上origin:https://api.okjx.cc:3389
8. 下载ts: 通过请求ts地址,记得带上origin


## 注意点

1. 合并视频: 中文乱码

```
# 意思是 把cmd命令行的字符集改成utf8
out = subprocess.call(['chcp', '65001'], shell=True,
                          stdout=subprocess.DEVNULL)
```

2. 通过u3m8下载的是图片,需要去掉前面212个字节,才能变成ts文件


## 引用

https://blog.csdn.net/feiyu361/article/details/121196667

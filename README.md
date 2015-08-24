# LookupOwner
####A python script that can automatically find out the location of each IP address saved in Nginx log file
####It can automatically filter the same IP address

####pyhon getIP.py [filename]
---

##Example

####Run
	python getIP.py nginx_error.log
---
####Result
	1: 117.121.26.197 ==>> 1970870981 ==>> 北京互联通网络科技有限公司
	49: 121.42.0.17 ==>> 2032795665 ==>> 浙江省杭州市 阿里云BGP数据中心
	67: 125.71.229.5 ==>> 2101863685 ==>> 四川省成都市 电子科技大学清水河校区
	102: 182.138.127.100 ==>> 3062529892 ==>> 四川省成都市 电信
	103: 125.71.229.4 ==>> 2101863684 ==>> 四川省成都市 电子科技大学清水河校区
	124: 222.212.2.168 ==>> 3738436264 ==>> 四川省成都市 电信
	158: 182.138.127.99 ==>> 3062529891 ==>> 四川省成都市 电信

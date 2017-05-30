# NSE-Search
NSE 脚本快速搜索

Author: v1ll4n

## 使用方法
```
usage: nse_searcher.py [-h] [-k KEYWORD] [--update] [--detail]

optional arguments:
  -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
  --update
  --detail
```

* -k（--keyword） 搜索关键字
* --update 从官网（nmap.org）更新数据库
* --detail 展示 NSE 脚本概要信息（简要描述）

### 使用范例

搜索心脏出血漏洞（关键字为 heart）

```
#python nse_searcher.py -k heart

 _   _ ____  _____     ____                      _
| \ | / ___|| ____|   / ___|  ___  __ _ _ __ ___| |__   ___ _ __
|  \| \___ \|  _| ____\___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|
| |\  |___) | |__|_____|__) |  __/ (_| | | | (__| | | |  __/ |
|_| \_|____/|_____|   |____/ \___|\__,_|_|  \___|_| |_|\___|_|     -by v1ll4n


[*] Search Keyword: heart
[*] Details about the result? False



----------------------------------------------------------------
Script Name: ssl-heartbleed
Script Usage URL: https://nmap.org/nsedoc/scripts/ssl-heartbleed.html
```

关于该脚本的简要描述信息：

```
python nse_searcher.py -k heart --detail

 _   _ ____  _____     ____                      _
| \ | / ___|| ____|   / ___|  ___  __ _ _ __ ___| |__   ___ _ __
|  \| \___ \|  _| ____\___ \ / _ \/ _` | '__/ __| '_ \ / _ \ '__|
| |\  |___) | |__|_____|__) |  __/ (_| | | | (__| | | |  __/ |
|_| \_|____/|_____|   |____/ \___|\__,_|_|  \___|_| |_|\___|_|     -by v1ll4n


[*] Search Keyword: heart
[*] Details about the result? True



----------------------------------------------------------------
Script Name: ssl-heartbleed
Script Usage URL: https://nmap.org/nsedoc/scripts/ssl-heartbleed.html
Script Summary(Description):

Detects whether a server is vulnerable to the OpenSSL Heartbleed bug (CVE-2014-0160).
The code is based on the Python script ssltest.py authored by Jared Stafford (jspenguin@jspenguin.org)
```

### 其他注意事项：
* 搜索的时候务必使用英文关键字
* 关于脚本的用法，在给出的 “Script Usage URL” 中
* 搜索依据：脚本名称／脚本 Summry 中的英文关键字

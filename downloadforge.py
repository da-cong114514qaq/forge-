# 调用库
import requests
import sys
import os

# 提示
print('爬虫：下载类型要小写呦。')

# 赋值
version = input('爬虫：请输入您的mc版本：')
version2 = input('爬虫：请输入您的forge版本：')
type = input('爬虫：请输入您的下载类型：')

# name2（后缀名）赋值
if type == 'changelog':
    name2 = 'txt'

if type == 'server':
    name2 = 'zip'

if type == 'client':
    name2 = 'zip'

if type == 'src':
    name2 = 'zip'

if type == 'installer':
    name2 = 'jar'

if type == 'mdk':
    name2 = 'zip'

name = 'forge-' + version + '-' + version2 + '-' + type + '.' + name2
url = 'https://maven.minecraftforge.net/net/minecraftforge/forge/' + version + '-' + version2 + '/forge-' + version + '-' + version2 + '-' + type + '.' + name2
download = requests.get(url)

# 检查是否可以访问
if download.status_code == 200:
    with open(name,"wb") as code:
        code.write(download.content)
        input('已执行成功！按回车关掉此页！')
        sys.exit()

if download.status_code > 200:
    input('您输入的不正确，请按回车结束并重试。')
    sys.exit()

if download.status_code < 200:
    input('您输入的不正确，请按回车结束并重试。')
    sys.exit()

# 检查是不是数字
if version.isdecimal():
    with open(name,"wb") as code:
        code.write(download.content)
        input('执行成功！按回车关掉此页！')
        sys.exit()
else:
    input('您输入的不正确，请按回车结束并重试。')
    sys.exit()

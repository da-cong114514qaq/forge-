# 调用库
import requests
import sys

# 提示
print('下载类型要小写呦。')

# 赋值
forge = print('推荐使用：\n14.23.5.2847')
version = input('请输入您的forge版本：')
type = input('请输入您的下载类型：')

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

name = 'forge-' + '1.12.2' + '-' + '1.12.2' + '-' + type + '.' + name2
url = 'https://maven.minecraftforge.net/net/minecraftforge/forge/' + '1.12.2' + '-' + version + '/forge-' + '1.12.2' + '-' + version + '-' + type + '.' + name2
download = requests.get(url)

old = '14.23.5.2847'
new = '14.23.5.2851'

if  version > new:
    print('您使用的是新版本。')

if  version == new:
    print('您使用的是新版本。')

if  version < old:
    print('您使用的是旧版本。')

if version == old:
    print('您使用的是旧版本。')

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

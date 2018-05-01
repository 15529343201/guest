# chapter1 Python 学习必知
## 1.1 Python2.x 与 Python3.x 选择
&emsp;&emsp;对于想要学习 Python 的同学来说首先要面对的就是版本选择的问题， 到底是学习 Python2.x 还是学习
Python3.x？ 之所以会有这样的疑问主要归结于 Python 语言发展的历史遗留问题导致。<br>
&emsp;&emsp;Python 语言早在 1989 由 Guido van Rossum 开发， 第一个公开发行版发行于 1991 年。 因为早期的 Python
版本在基础方面设计存在着一些不足之处。在 2008 年的时候 Guido van Rossum 又重新开发 Python 3.0，Python3
在设计的时候很好地解决了这些遗留问题， 并且在性能上也有了一定的提升， 然而 Python3 带来的最大的问题
就是不完全向后兼容， 当时向后兼容的版本是 Python2.6。 因为经过多年的发展， Python 已经是一门非常成熟
的语言了， 大量的项目在使用 Python 语言运行， 围绕着 Python 语言有着极其丰富的类库。 无法一下子就让所
有项目和类库都转到 Python3.0 上面。 所以， 两个版本就进入了长期并行开发和维护的状态。<br>
&emsp;&emsp;正是由于官方对 Python2.x 纵容的态度， 致使到目前为止， Python2 的使用者依然过半。 从近两年来看，
官方的态度有所改变， Python2.x 的开发进入消极状态， 版本更新速度明显要比 Python3.x 慢得多， 而且不再加
入新的特性， 以维护为主。 所以， 这将非常有利于 Python3 的发展， 那么对于新手来说， 我建议读者直接学习
Python3.x， 因为 Python3.x 代表了 Python 发展的未来； 而且目前主流的库基本都已经支持了 Python3.x， 不支
持的库也在积极的向 Python3.x 迁移。 那么， 在本书中除非特别声明， 否则默认情况所有代码将在 Python3.x
下运行。<br>
## 1.2 Python 的安装
### 1.2.1 Window 下安装 Python
&emsp;&emsp;Python 下载地址： https://www.python.org/downloads/<br>
&emsp;&emsp;目前最新版本为 Python3.5。 读者可根据自己的平台选择相应的版本进行下载。 对于 Windows 用户来说，
如果 32 位系统是则选择 x86 版本； 如果是 64 位系统， 则选择 x86-64 版本。 选择“executable installer” 的连
接进行下载， 下载完成后会得到一个以.msi 为后缀名的文件， 双击进行安装， 如图 1.1 所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.1.PNG)<br>
&emsp;&emsp;安装过程与一般的 Windows 程序类似。 安装完成， 将在开始菜单中将看到安装好的 Python 目录， 如图 1.2
所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.2.PNG)<br>
在 Windows 系统中， 安装好的 Python 提供了四个选项。<br>
&emsp;&emsp;IDLE(Python 3.5 64-bit) ： 该选项为 Python 自带的 IDE， 推荐新手使用。<br>
&emsp;&emsp;Python 3.5 (64-bit)： 该选项会直接在 window 名称提示符下进入 Python Shell 模式。<br>
&emsp;&emsp;Python 3.5 Manuals(64-bit) ： 该选项为 Python 自带的官方文档。<br>
&emsp;&emsp;Python 3.5 Module Docs(64-bit)： 该选项为 Python 的模块文档。 它自动启动一个服务， 并打 Web 形式的文档。<br>
### 1.2.2 安装 Python2.x 和 Python3.x 两个版本
&emsp;&emsp;虽然 Python3.x 正在努力的想取代 Python2.x， 但是当前来看 Python2.x 的使用者仍然超过半数， 抛开一部
分用户仍然是 Python2.x 的坚定拥护者外， 最主要的原因仍然是因为有少部分的类库仍然不支持 Python3.x， 虽
然这种情况在不断改善中。 所以， 有时为了使用某个库而不得不在两个版本之间切换使用。 这个时就需要系
统同时安装两个版本。<br>
&emsp;&emsp;当然， Python 早就考虑到了你可能会有这样的需求， 所以， 它允许你在一个操作系统中同时安装两个版
本。 并且， 主流 Linux（例如， Ubuntu） 系统已经默认为你安装了两个版本的 Python。 对于 Windows 系统来
说你需要手动的来安装两个版本的 Python， 不过， 在使用两个版本的时候， 需要做好区分。<br>
&emsp;&emsp;例如， 我本机安装的 Python2.7.x 版本， 如图 1.3。 在 Python27 的根目录下， Python 的可执行文件的命名
为“python.exe” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.3.PNG)<br>
&emsp;&emsp;当我们想运行 Python2.7.x 版本时， 只需要在 Windows 命令提示符下输入“python” 命令即可。 如图 1.4。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.4.PNG)<br>
&emsp;&emsp;然后， 我又安装了 Python3.5， 再来看看 Python3.5 的目录。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.5.PNG)<br>
&emsp;&emsp;图示 1.5 所示， 除了有一个默认的“python.exe” 文件外， 还有一个“python3.exe” ， 此时， 如果想
运行 Python3.5 时就可以使用“python3” 命令。 如图 1.6。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.6.PNG)<br>
&emsp;&emsp;需要说明的是， Python 可执行文件的名称是可以随意修改的。 如果你愿意可以将其改成任意名称。<br>
### 1.2.3 ‘python’ 不是内部或外部命令
&emsp;&emsp;这个问题也是新手可能会碰到的， 虽然在安装 Python 的时候， 它默认会将 Python 的安装路径添加到环
境变量 Path 下面， 但是保不准你在安装时忘记了勾选“Add Python 3.5 to PATH” 的选项。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.7.PNG)<br>
&emsp;&emsp;这个时候你就要找一找你的 Python 到底安装到哪个目录下了， 并且把这个目录添加到系统环境变量 Path
下面。 如图 1.3 和 1.5 分别为我的 Python2.7.10 和 Python3.5 的安装目录， 并且将它分别添加到系统环境变量下
面。 如图 1.8。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.8.PNG)<br>
## 1.3 安装 Python 扩展库
&emsp;&emsp;如果你只学习 Python 的基本语法的话， 那么安装好 Python 就可以开始找一本 Python 基础教程， 照着书
中的例子一个一个地进行练习。 当然， 对于我们大多数人来说， 一开始学习 Python 可能就是为了使用它完成
某项任务，这种情况下，就需要去安装第三方扩展库。比如，我在一开始学习 Python 的目的是为了使用 Selenium
编写 UI 自动化测试脚本。 所以， 对我来说只安装好 Python 是不够的， 必须还要安装扩展库 Selenium。<br>
&emsp;&emsp;所以， 接下来可以 Python 的第三方仓库 PyPI 中查找想要的库。<br>
&emsp;&emsp;PyPI 地址： https://pypi.python.org/pypi<br>
&emsp;&emsp;如果你知道你要找的库的名字， 那么只需要在右上角搜索栏查找即可。<br>
### 1.3.1 pip 安装扩展库
&emsp;&emsp;pip 是一个安装和管理 Python 包的工具， 通过 pip 来管理 Python 包非常简单， 我们将省去搜索→查找版
本→下载→安装等烦琐的步骤。<br>
&emsp;&emsp;当安装 Python 完成， 在 Windows 命令提示符下输入 pip 命令：<br>
```
>pip
Usage:
pip <command> [options]
Commands:
install Install packages.
uninstall Uninstall packages.
freeze Output installed packages in requirements format.
list List installed packages.
show Show information about installed packages.
search Search PyPI for packages.
wheel Build wheels from your requirements.
zip DEPRECATED. Zip individual packages.
unzip DEPRECATED. Unzip individual packages.
bundle DEPRECATED. Create pybundles.
help Show help for commands.
General Options:
-h, --help Show help.
-v, --verbose Give more output. Option is additive, and can be
used up to 3 times.
-V, --version Show version and exit.
-q, --quiet Give less output.
--log-file <path> Path to a verbose non-appending log, that only
……
```
&emsp;&emsp;如果出现 pip 命令的说明信息， 则说明 pip 可以正常使用。 如果提示“pip 不是内部或外部命令” ， 则表
示 pip 的可执行文件所在的目录（例如， ...\Python35\Scripts\） 不在系统环境变量 Path 下面， 参考 1.2.3 小节，
将目录添加到系统环境变量下的 Path 下面。<br>
#### 1） 使用 pip 安装扩展库。
`>pip install django`<br>
&emsp;&emsp;Django 为 Python 下面开发 Web 项目非常强大的一个库， 也是本书学习的一个重点。<br>
#### 2） 使用 pip 安装指定版本的扩展库。
`>pip install django==1.9.7`<br>
&emsp;&emsp;pip 默认会安装该库的最新版本， 如果我们知道该库的版本号， 也可以指定某个版本号安装。<br>
#### 3） 使用 pip 查看当前安装的库。
```
>pip show django
Requires:
Classifiers:
Development Status :: 5 - Production/Stable
Environment :: Web Environment
Framework :: Django
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Internet :: WWW/HTTP
Topic :: Internet :: WWW/HTTP :: Dynamic Content
Topic :: Internet :: WWW/HTTP :: WSGI
Topic :: Software Development :: Libraries :: Application Frameworks
Topic :: Software Development :: Libraries :: Python Modules
Entry-points:
[console_scripts]
django-admin = django.core.management:execute_from_command_line
```
&emsp;&emsp;不同的库显示的信息会有所不同， 比如有些库用 show 命令查看， 会显示当前的版本号， 以及它的安装
路径等。<br>
#### 4） 使用 pip 卸载库。
`>pip uninstall django`<br>
&emsp;&emsp;使用 uninstall 命令就可以将安装的库轻松卸载了。<br>
#### 5） 如何区别 Python2 与 Python3 的 pip。
&emsp;&emsp;这个问题也很简单， 首先“pip” 命令与前面提到的“python” 命令一样。 同样是一个可执行文件， 其文
件名称也可以随意修改， 我们可以将她们分别修改为“pip2.exe” 和“pip3.exe” 分别表示两个版本的 Python
下的“pip” 命令。 读者可找到 Python 的安装目录下查看 pip 的可执行文件叫具体什么。 查看目录， 例如：<br>
`C:\Python27\Scripts\`<br>
`C:\Python35\Scripts\`<br>
### 1.3.2 tar.gz 文件安装
&emsp;&emsp;并不是所有的扩展库都支持 pip 命令安装。 对于个别库来可能只提供了压缩包文件， 或者我们安装的环
境并不能上网。 这个时候就不能 pip 命令安装了。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.10.PNG)<br>
&emsp;&emsp;如图 1.10 所示， 点击 Django-1.10.2.tar.gz 文件进行下载， 然后进行解压， 进入解压目录， 通过“python”
命令安装。<br>
`...\Django-1.10.2>python setup.py install`<br>
### 1.3.3 whl 文件安装
&emsp;&emsp;wheel 本质上是一个 zip 包格式， 它使用 .whl 扩展名， 用于 Python 模块的安装。<br>
&emsp;&emsp;如图 1.10， Django 提供了.whl 文件的安装包。 同样先下载 Django-1.10.2-py2.py3-none-any.whl 文件。 .whl
文件的安装， 同样需要使用 pip 命令。<br>
`...\pypackage>pip install Django-1.9.7-py2.py3-none-any.whl`<br>
## 1.4 Python 开发工具选择
&emsp;&emsp;开发工具的选择也是新手所面临的问题之一。 当然， 选择使用开发工具充满了个人偏好。 如果你已经自
己熟悉的开发工具， 那么可以直接跳过这一小节， 如果还在为使用什么开发工具而纠结。 不如， 听一听我的
建议。<br>
### 1.4.1 Python IDLE
&emsp;&emsp;如果读者初学 Python， 并且不精通其他编程语言及 IDE（Integrated Development Environment ） ， 则建议
从这个款 IDE 入手， 它自带的 Shell 模式可以帮助我们快速练习 Python 语法， 笔者初学 Python 时用了半年左右。<br>
&emsp;&emsp;打开 Python 自带的 IDLE， 就可以编写 Python 程序了， Python Shell 界面。 如图 1.11 所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.11.PNG)<br>
&emsp;&emsp;启动 IDLE 时， 会显示“三个尖括号” 提示符（>>>） ， 可以在这里输入代码。 在 Python Shell 输入代码
回车后会立即执行， 并直接在下面显示执行的结果。<br>
&emsp;&emsp;在 Python Shell 模式下编写的代码只停留于内存当中， 当关闭 Python Shell 窗口后会自动消失， 那么如果，
想把代码写到文件里保存起来， 则可以单击菜单栏 File→New File ， 或通过组合键 Ctrl+N 打开新的窗口， 在
此文件中编写代码， 完成后单击菜单栏 File→Save 或通过组合键 Ctrl+S 保存， 如图 1.12 所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.12.PNG)<br>
### 1.4.2 Sublime Text3
&emsp;&emsp;Sublime Text 是一款通用型轻量级编辑器， 支持多种编程语言。 有许多功能强大的快捷键（如 Ctrl+d） ，
支持丰富的插件扩展。 如果平时需要在不同编程语言间切换， 那么它将会是一个， 不错的选择。 这也是笔者
最喜欢的编辑器之一。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.13.PNG)<br>
&emsp;&emsp;如果读者安装了两个版本的 Python， 并且想用该编辑器分别运行两个版本的 Python， 那么需要添加配置
文件来进行配置。 首先启动 Sublime Text3 工具。 菜单栏“Tool” -->“Build System” -->“New Build System...”。
在打开的 untitled.sublime-build 文件中输入以下配置信息。<br>
```
{
"cmd": ["python3", "-u", "$file"],
"encoding": "cp936",
"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
"selector": "source.python",
}
```
&emsp;&emsp;其中“python3” 为执行 Python 的命令， 根据 1.2.2 小节的设置来修改这里的设置， 从而来实现的两个版
本的 Python 之间的切换。<br>
&emsp;&emsp;将 untitled.sublime-build 文件保存为： python3.sublime-build。<br>
&emsp;&emsp;保存路径为...\Sublime Text 3\Packages\User\； 读者可以通过菜单栏“Preferences” -->“Browser Packages...”查看该目录。<br>
&emsp;&emsp;切换到配置的 python3 版本， 通过菜单栏“Tool” -->“Build System” -->“python3” 。 （小提示： 这里的
“python3” 与配置文件保存时的命名有关“python3.sublime-build” ）<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.14.PNG)<br>
&emsp;&emsp;最后， Python 程序的执行通过快捷键“Ctrl+B” 进行。<br>
### 1.4.3 PyCharm
&emsp;&emsp;PyCharm 是 Python 重量级 IDE， 功能强大， 自动检测语法， 可以帮助我们写出更规范的代码。 对于处女
座的开发者来说是个不错的选择。 笔者使用半天过后果断拥抱之。<br>
&emsp;&emsp;前面介绍的两款 IDE 适合编写一些简单的 Python 程序， 而如果想开发 Python 项目， 那么 PyCharm 会是
很好的选择。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.15.PNG)<br>
### 1.4.4 Atom
&emsp;&emsp;Atom 由目前全球范围内影响力最大的代码仓库/开源社区 GitHub 开发。 它开源免费跨平台， 并且整合
GIT 并提供类似 SublimeText 的包管理功能， 支持插件扩展， 可配置性非常高。<br>
&emsp;&emsp;Atom 官方地址： https://atom.io/<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.16.PNG)<br>
&emsp;&emsp;Atom 与 Sublime Text 有很多相似之后， Atom 体积相对比较大， 启动速度略慢， 但它有两点是我非常喜
欢的， 一是代码着色看上去很舒服， 二是插件的安装极其方便， 只需要在“Settings” 中搜索安装即可。<br>
&emsp;&emsp;好吧！ 我已经介绍了四款自己比较熟悉的编辑器， 你可以根据自己的选择使用它们吧！ 但我这里的介绍
过于简单， 你在使用过程中还要做一些额外的功课才能把它们用好。<br>
## 1.5 Python 程序报错不要慌
&emsp;&emsp;我是按照书上的例子一行一行敲出来的， 结果一运行出错了， 报错对于初学编程的同学都是恐惧的。 笔
者就根据自己的经验谈谈如何应对程序的报错。<br>
### 1.5.1 缩进错误
&emsp;&emsp;Python 对程序中， 我们不需要“｛｝ ” 来表示一个语句体， 也不需要“;” 表示一个语句的结束。 这就要
求我们对程序的缩进有着严格的要求。 但有时候， 看上去我们的程序格式没有问题， 但程序依旧报错。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.17.PNG)<br>
&emsp;&emsp;如图 1.17 的程序， 看上去没有问题， 但运行的时候却提示： “IndentationError: unindent does not match any
outer indentation level” 。 其实错误信息描述已经很清楚了， 但新手往往恐惧这样的错误。<br>
![image](https://github.com/15529343201/guest/blob/chapter1/image/1.18.PNG)<br>
&emsp;&emsp;如果将程序全选（Ctrl+a） ， 就会发现错误， 如图 1.18 所示。 在 add()函数的语句体中， “c = a + b” 前
面是一个 Tab 的间距， 而“return c” 前面是四个空格的间距。 所以， 看上去他们的位置是对齐了， 但它们使
用了不同的缩进方法， 从而会导致 Python 执行报错。<br>
### 1.5.2 引包错误
&emsp;&emsp;引包错误也是新手常常遇到的一类问题， 但这其中有一个大坑。<br>
```
import unittest
class test(unittest.TestCase):
    pass
```
&emsp;&emsp;运行程序：<br>
```
Traceback (most recent call last):
File "D:\pydemo\unittest.py", line 1, in <module>
import unittest
File "C:\pydemo\unittest.py", line 3, in <module>
class test(unittest.TestCase):
AttributeError: module 'unittest' has no attribute 'TestCase'
```
&emsp;&emsp;我们明明要引用的是 Python 自带的 unittest 模块， 完全没有错误， 然而程序却提示“module 'unittest' has no
attribute 'TestCase” 。 这个错误跟 Python 的引包机制有关， 当我们在“import” 一个模块或库时， Python 首先会查找当前目录下有没有这样名字的模块或库。<br>
&emsp;&emsp;显然， 我把自己写的程序文件名也命名为了“unittest.py” ， 但我在程序中又引用“unittest” ， 那么这就
相当于自引用了。 而我的真实意图是要引用 Python 的 unittest 模块。 当然， 有时也并不一定是自身被引用了，
也可能是程序的当前目录下出现的重名文件或目录。 所以， 自己编写的程序文件命名一定要注意， 千万要避
免与引用的模块或库重名。<br>
### 1.5.3 编码错误
在开发 Python 程序的过程中， 会涉及到三个方面的编码：
- Python 程序文件的编码。

&emsp;&emsp;我们在编写的程序本身也存在编码问题， 一般的解决方式是在程序的开头加上“#coding=utf-8” 或
“#coding=gbk” 来使程序统一为 UTF-8 或 GBK 编码。<br>
- Python 程序运行时环境（IDE） 的编码。

&emsp;&emsp;不是管是 Sublime Text 或是 PyCharm 也它， 使用的 IDE 工具也存在编码问题。 如果你不确定是否是 IDE
的编码引起程序出错的， 根据我的经验， 建议你切换回 Python IDLE 去执行程序。<br>
- Python程序读取外部文件、 网页的编码。

&emsp;&emsp;当然， 最容易出现编码问题应该是在读取外部数据或文件的时候。 首先要确定读取的数据或文件的编码，
然后通过 decode()和 encode()方法来进行编码转换。<br>
&emsp;&emsp;decode 的作用是将其他编码的字符串转换成 Unicode 编码。<br>
&emsp;&emsp;encode 的作用是将 Unicode 编码转换成其他编码的字符串。<br>
&emsp;&emsp;当我们在遇到 Python 的编码问题时， 从以上三个方法分析就会很容易找到解决编码问题的办法。<br>
### 1.5.4 学会分析错误
&emsp;&emsp;新手往往在面对程序抛出的一大堆报错时不知如何分析， 如果认真阅读报错信息， 你将很容易找到错误原
因。 其实， 比起一大堆的报错， 最难解决的问题是没有任何报错信息， 而程序却无法正确的执行。<br>
```
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")虫师原创----http://fnng.cnblogs.com
24
driver.find_element_by_id("kwsss").send_keys("Selenium2")
driver.find_element_by_id("su").click()
driver.quit()
```
```
Traceback (most recent call last):
File "D:\pydemo\pyse.py", line 8, in <module>
driver.find_element_by_id("kwsss").send_keys("Selenium2")
File "C:\Python35\lib\site-packages\selenium\webdriver\remote\webdriver.py",
line 266, in find_element_by_id
return self.find_element(by=By.ID, value=id_)
File "C:\Python35\lib\site-packages\selenium\webdriver\remote\webdriver.py",
line 744, in find_element
{'using': by, 'value': value})['value']
File "C:\Python35\lib\site-packages\selenium\webdriver\remote\webdriver.py",
line 233, in execute
self.error_handler.check_response(response)
File "C:\Python35\lib\site-packages\selenium\webdriver\remote\errorhandler.py",
line 194, in check_response
raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.NoSuchElementException: Message: no such element
(Session info: chrome=43.0.2357.134)
(Driver info: chromedriver=2.10.267521,platform=Windows NT 6.3 x86_64)
Traceback (most recent call last):
```
&emsp;&emsp;对上面这段报错， 我们要学会查看错误信息， 一般看错误信息开始和结束。<br>
```
Traceback (most recent call last):
File "D:\pydemo\se_test.py", line 8, in <module>
driver.find_element_by_id("kwsss").send_keys("Selenium2")
……
```
&emsp;&emsp;一般在错误信息的开始位置会显示你的程序是从哪一行开始出错的。 比如， 这里就很清楚的告诉在我在
se_test.py 文件的第 8 行。 这一行是用来定位百度首页上的输入框。<br>
```
……
selenium.common.exceptions.NoSuchElementException: Message: no such element
(Session info: chrome=43.0.2357.134)
(Driver info: chromedriver=2.10.267521,platform=Windows NT 6.3 x86_64)
Traceback (most recent call last):
```
&emsp;&emsp;错误信息的结尾部分会告诉你是错误的类型“NoSuchElementException” 以及错误信息“Message: no such
element” 。 很显然， 这是由于元素的定位方式错误导致程序执行时“no such element” 。 这个时候只要修改我
的定位方式即可。<br>
&emsp;&emsp;如果你依然没明白“Message: no such element” 是什么意思， 那么接下来就通过搜索引擎来查找这段报错
的提示吧！ 当你解决了一个类型的报错， 再遇到这样的问题就会很容易解决了， 学习的积累就是在解决一个
又一个错误的过程中不断进步的。<br>
# chapter2 Django 入门
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.0.PNG)<br>
## 2.1 Django 开发环境
&emsp;&emsp;Django 的版本大体分为三种： 一种是长时期支持版本（Long Term Support， 简称 LTS） ， 第二种是最新
版本， 正式发布的稳定版本； 第三种是预览版（一般版本号中带 a1、 a2， b1， b2 的标识） ， 主要为愿意尝试
新功能的用户使用。<br>
### 2.1.1 Windows 安装 Django
&emsp;&emsp;Django 官方网站： https://www.djangoproject.com/<br>
&emsp;&emsp;Python 官方仓库下载地址： https://pypi.python.org/pypi/Django<br>
`> pip install django==1.10.3`<br>
或者：<br>
`> pip3 install django==1.10.3`<br>
或者：<br>
`>python3 -m pip install django==1.10.3`<br>
或者：<br>
`pip install -i https://pypi.douban.com/simple/ django=1.10.3`<br>
&emsp;&emsp;如果你只安装一个版本的 Python， 那么第一个命令即可成功安装 Django， 后两个命令是在你同时安装了
Python2.x 和 Python3.x 两版本的情况下， 用于区别 Python2.x 时使用。 当然， 对于访问国外网站比较慢的读者
也可以选择豆瓣源， 如第四行命令。<br>
### 2.1.2 Ubuntu 下安装 Django
&emsp;&emsp;Linux 操作系统的版本很多， 这里以流行的 Ubuntu 系统为例。<br>
&emsp;&emsp;因为 Ubuntu 系统本身对 Python 有很强的依赖， 所以 Ubuntu 自带的就有 Python。<br>
&emsp;&emsp;当前在 Ubuntu 系统中已经同时集成了 Python2 与 Python3， 打开终端， 输入“python” 或“Python3” 命
令回车， 即可进入相应版本的 Shell 模式。<br>
```
fnngj@fnngj-PC:~$ python
28
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
fnngj@fnngj-PC:~$ python3
Python 3.4.3 (default, Jul 28 2015, 18:20:59)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```
## 2.2 开始第一个 demo
### 2.2.1、 创建项目与应用
&emsp;&emsp;如果你已经成功的安装 Django， 在.../python35/Scripts/目录中将会多出一个 django-admin.exe 文件。 在
Windows 命令提示符下输入“django-admin” 命令回车。<br>
```
D:\pydj>django-admin
Type 'django-admin help <subcommand>' for help on a specific subcommand.
Available subcommands:
[django]
check
compilemessages
createcachetable
dbshell
diffsettings
dumpdata
flush
inspectdb
loaddata
makemessages
makemigrations
migrate
runserver
sendtestemail
shell
showmigrations
sqlflush
sqlmigrate
sqlsequencereset
squashmigrations
startapp
startproject
test
testserver
```
`D:\pydj>django-admin startproject guest #创建 guest 项目`<br>
为该项目命名为“guest” 。 项目结构如下：<br>
```
guest/
├── guest/
│ ├── __init__.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└──manage.py
```
&emsp;&emsp;`guest/__init__.py`： 一个空的文件， 用它标识一个目录为 Python 的标准包。<br>
&emsp;&emsp;`guest/settings.py`： Django 项目的配置文件， 包括 Django 模块应用配置， 数据库配置， 模板配置等。<br>
&emsp;&emsp;`guest/urls.py`： Django 项目的 URL 声明。<br>
&emsp;&emsp;`guest/wsgi.py`： 为 WSGI 兼容的 Web 服务器服务项目的切入点。<br>
&emsp;&emsp;`manage.py`： 一个命令行工具， 可以让你在使用 Django 项目时以不同的方式进行交互。<br>
```
D:\pydj>cd guest # 进入 guest 项目目录
D:\pydj\guest>python3 manage.py # 查看 manage 所提供的命令
Type 'manage.py help <subcommand>' for help on a specific subcommand.
Available subcommands:
[auth]
changepassword
createsuperuser
[django]
check
compilemessages
createcachetable
dbshell
diffsettings
flush
inspectdb
loaddata
makemessages
makemigrations
migrate
sendtestemail
shell
showmigrations
sqlflush
sqlmigrate
sqlsequencereset
squashmigrations
startapp
startproject
test
testserver
[sessions]
clearsessions
[staticfiles]
collectstatic
findstatic
runserver
```
&emsp;&emsp;你会发现 manage.py 所提供的许多命令与 django-admin 相同。如果想进一步了解它们的作用与区别
可以查看 Django 的官方文档。<br>
&emsp;&emsp;https://docs.djangoproject.com/en/1.10/ref/django-admin/<br>
&emsp;&emsp;对于新手来说， 我们不需要弄清楚每一个细节， 你只需要跟着我一步一步操作即可。 接下来， 使用
“startapp” 命令创建应用。 一个项目可以包含多个应用， 而我们要开发的签到系统应该在具体应用下面完
成。<br>
`D:\pydj\guest>python3 manage.py startapp sign #创建 sign 项目`<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.1.PNG)<br>
&emsp;&emsp;如图 2.1， Django 应用的目录（截图是通过 PyCharm 开发工具） 。<br>
&emsp;&emsp;`migrations/`： 用于记录 models 中数据的变更。<br>
&emsp;&emsp;`admin.py`： 映射 models 中的数据到 Django 自带的 admin 后台。<br>
&emsp;&emsp;`apps.py`： 在新的 Django 版本中新增， 用于应用程序的配置。<br>
&emsp;&emsp;`models.py`： 创建应用程序数据表模型（对应数据库的相关操作） 。<br>
&emsp;&emsp;`tests.py`： 创建 Django 测试。<br>
&emsp;&emsp;`views.py`： 控制向前端显示哪些数据。<br>
### 2.2.2、 运行项目
&emsp;&emsp;现在我们要把项目运行起来， Django 提供了 Web 容器， 只需要通过“runserver” 命令就可以把项目运行
起来。<br>
```
D:\pydj\guest>python3 manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).
You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.
July 30, 2016 - 22:37:53
Django version 1.10.3, using settings 'guest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
&emsp;&emsp;Django 默认会通过本机的 8000 端口来启动项目， 如果你的当前环境该端口号被占用了， 也可以在启动
时指定 IP 地址和端口号。<br>
```
D:\pydj\guest>python3 manage.py runserver 127.0.0.1:8001
Performing system checks...
System check identified no issues (0 silenced).
You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.
July 30, 2016 - 22:42:44
Django version 1.10.3, using settings 'guest.settings'
Starting development server at http://127.0.0.1:8001/
Quit the server with CTRL-BREAK.
```
&emsp;&emsp;其中“127.0.0.1” 为指向本机的 IP 地址， “8001” 为设置的端口号。<br>
&emsp;&emsp;打开浏览器， 访问： http://127.0.0.1:8001/<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.2.PNG)<br>
### 2.2.3、 Hello Django！
&emsp;&esmp;大多编程语言的教程， 第一个例子总是会教你如何打印“Hello xxx！ ” ， 我们也不免俗套， 接下来和我
一起开发一个“Hello Django!” 的页面。<br>
&emsp;&emsp;在此之前， 我们首先需要配置一下 guest/settings.py 文件， 将 sign 应用添加到项目中。<br>
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sign',
]
```
&emsp;&emsp;接下来想一想， 我们应该用哪个路径来显示“Hello Django!” 。 命名一个/index/路径。 在浏览器地址栏输
入： http://127.0.0.1:8001/index/<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.3.PNG)<br>
&emsp;&emsp;显然， 我们访问的路径并不存在， 如图 2.3， Django 提示“Page not found(404)” ， 不要害怕， 这并不是
一个严重的错误， 只是因为我们访问了一个不存在的路径而已， 认真读一下页面上的提示， 将会得到不少有
用信息：<br>
&emsp;&emsp;Django 在项目中的 guest 子目录下通过 urls.py 文件来定义 URLconf。<br>
&emsp;&emsp;但是， 在 urls.py 文件中只找到了一个 admin/的路由配置。<br>
&emsp;&emsp;当前网址 index/， 并没有匹配到。<br>
&emsp;&emsp;根据本 Django 的提示， 再接下来打开 guest/urls.py 文件添加该目录。<br>
```
from django.conf.urls import url
from django.contrib import admin
from sign import views  # 导入 sign 应用 views 文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index),  # 添加 index/路径配置
]
```
views.py:<br>
```
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello Django!")
```
&emsp;&emsp;定义 index 函数， 并通过 HttpResponse 类向页面返回字符串“Hello Django!” 。<br>
&emsp;&emsp;HttpResponse 类存在 django.http.HttpResponse 中， 以字符串的形式传递给前端页面数据。<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.4.PNG)<br>
### 2.2.4、 使用模板
&emsp;&emsp;现在要用 HTML 页面来替代“Hello Django！ ” 字符串， 那么处理方式也会有所不同， 你可以认为这是
一次重构。<br>
&emsp;&emsp;在应用 sign/目录下创建 templates/index.html 文件。 （读者需要注意该 HTML 文件的所在路径， 不要弄错
噢！ ）<br>
index.html:<br>
```
<html>
    <head>
        <title>Django Page</title>
    </head>
    <body>
        <h1>Hello Django!</h1>
    </body>
</html>
```
views.py:<br>
```
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")
```
&emsp;&emsp;这里抛弃 HttpResponse 类， 转而使用 Django 的 render 函数。 该函数的第一个参数是请求对象的， 第二个参
数返回一个 index.html 页面。<br>
&emsp;&emsp;再次刷新页面， 查看 index.html 中所展示的内容。<br>
## 2.3 Django 工作流
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.5.PNG)<br>
&emsp;&emsp;需要说明的是， 这个处理流程并非 Django 的完整处理过程， 其中最主要的就是缺失了数据层（model）
的操作， 但目前我们并没有涉及这数据层的操作， 所以先暂时忽略。<br>
&emsp;&emsp;在学习更多 Django 开发知识之前， 希望你能把这个处理流程能记下来。 因为后续的 Django 开发都会是
在此基础上对每一步骤的延伸笔扩展。 所以， 接下来进一步对每个步骤进行解释。<br>
### 2.3.1、 URL 组成
&emsp;&emsp;作为一个网站的用户， 我们首先会在浏览器的 URL 地栏输入： http://127.0.0.1:8000/index/<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.6.PNG)<br>
&emsp;&emsp;URL 地址由以下几部分组成：<br>
&emsp;&emsp;协议类型： HTTP/HTTPS<br>
&emsp;&emsp;HTTP 协议（HyperText Transfer Protocol， 超文本传输协议） 是用于从 WWW 服务器传输超文本到
本地浏览器的传送协议。 它可以使浏览器更加高效， 使网络传输减少。 它不仅保证计算机正确快速地传输超
文本文档， 还确定传输文档中的哪一部分， 以及哪部分内容首先显示等 。<br>
&emsp;&emsp;HTTPS（全称： Hyper Text Transfer Protocol over Secure Socket Layer） ， 是以安全为目标的
HTTP 通道， 简单讲是 HTTP 的安全版。<br>
&emsp;&emsp;主机地址： itest.info ， 127.0.0.1<br>
&emsp;&emsp;itest.info 为一个网址， 网址通过域名解析服务器会找到对应的 IP 主机。<br>
&emsp;&emsp;127.0.0.1 为一个 IP 地址， 不过， 该 IP 地址比较特殊， 用来指向的本机。<br>
&emsp;&emsp;端口号： 8000<br>
&emsp;&emsp;一台主机上有很多应用， 不同的应用占用不同的端口号， 除了要指定主机（网址或 IP 地址） 之外， 还要
进一步指定相应的端口号才能访问到具体的应用。<br>
&emsp;&emsp;前面在运行 Django 服务器， 默认使用 8000 的端口号， 所以， 在浏览器除了输入 IP 地址之后， 还要指向
端口号， 才能访问到 Django 应用。<br>
&emsp;&emsp;路径 ： /index/ 、 /admin<br>
&emsp;&emsp;一般用来表示主机上的一个目录或文件地址。<br>
### 2.3.2、 urls 的配置
&emsp;&emsp;当 Django 拿到浏览器 URL 的地址之后， 取端口号后面的路径 “/index” 、 “/admin” 。 然后在 urls.py
文件中匹配。<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.7.PNG)<br>
&emsp;&emsp;这里使用了 Python 的正则表达式。<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.8.PNG)<br>
&emsp;&emsp;通过^index/$ 匹配到/index/目录。 并且将处理指向 sign 应用的视图文件 views.py 的 index 函数。<br>
### 2.3.3、 views 视图
&emsp;&emsp;接下来请求的处理就到了.../sign/views.py 中的 index 视图函数。 如图 2.7<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.9.PNG)<br>
&emsp;&emsp;视图在我看来， 它在 Django 中非常重要， 是连接页面与数据的中间纽带。 拿登录的例子来讲， 用户在页
面上输入了用户名和密码点击登录。 那么 request 请求会由视图来接收， 如何提取出用户名和密码的数据， 如何用这些数据去查询数据库， 再如何将登录成功的页面返回给用户， 这些全部由视图层来完成。<br>
### 2.3.4、 templates 模板
&emsp;&emsp;打开.../sign/templates/index.html 文件。 如图 3.8。<br>
![image](https://github.com/15529343201/guest/blob/chapter2/image/2.10.PNG)<br>
&emsp;&emsp;模板的载体就是我们所熟悉的 Web 页面了， Django 自带的有模板语言。 它的主要作用是如何展示数据，
比如视图层返回的是一个字符串， 要如何显示在页面上； 返回的对象数组要如何显示等。 当然， 为了使页面
更漂亮需要借助前端技术， 比如 CSS、 JavaScript 等。<br>
## 2.4 MTV 开发模式
&emsp;&emsp;进一步探讨一下 Django 的开发模式。<br>
&emsp;&emsp;MTV 开发模式<br>
&emsp;&emsp;在钻研更多代码之前， 让我们先花点时间考虑下 Django 数据驱动 Web 应用的总体设计。 Django 的设计
鼓励松耦合及对应用程序中不同部分的严格分割。 遵循这个理念的话， 要想修改应用的某部分而不影响其它
部分就比较容易了。 在视图函数中， 我们已经讨论了通过模板系统把业务逻辑和表现逻辑分隔开的重要性。 在
数据库层中， 我们对数据访问逻辑也应用了同样的理念。 把数据存取逻辑、 业务逻辑和表现逻辑组合在一起
的概念有时被称为软件架构的 Model-View-Controller（MVC） 模式。 在这个模式中， Model 代表数据存取层，
View 代表的是系统中选择显示什么和怎么显示的部分， Controller 指的是系统中根据用户输入并视需要访问模
型， 以决定使用哪个视图的那部分。<br>
&emsp;&emsp;为什么用缩写？<br>
&emsp;&emsp;像 MVC 这样的明确定义模式的主要用于改善开发人员之间的沟通。 比起告诉同事， “让我们采用抽象
的数据存取方式， 然后单独划分一层来显示数据， 并且在中间加上一个控制它的层” ， 一个通用的说法会让
你收益， 你只需要说： “我们在这里使用 MVC 模式吧。 ” 。 Django 紧紧地遵循这种 MVC 模式， 可以称得上
是一种 MVC 框架。 以下是 Django 中 M、 V 和 C 各自的含义：<br>
&emsp;&emsp;M ， 数据存取部分， 由 Django 数据库层处理， 本章要讲述的内容。<br>
&emsp;&emsp;V ， 选择显示哪些数据要显示以及怎样显示的部分， 由视图和模板处理。<br>
&emsp;&emsp;C ， 根据用户输入委派视图的部分， 由 Django 框架根据 URLconf 设置， 对给定 URL 调用适当的
Python 函数。<br>
&emsp;&emsp;由于 C 由框架自行处理， 而 Django 里更关注的是模型（Model） 、 模板(Template)和视图（Views） ，
Django 也被称为 MTV 框架 。 在 MTV 开发模式中：<br>
&emsp;&emsp;M 代表模型（Model） ， 即数据存取层。 该层处理与数据相关的所有事务： 如何存取、 如何验证有效<br>
&emsp;&emsp;T 代表模板(Template)， 即表现层。 该层处理与表现相关的决定： 如何在页面或其他类型文档中进行显
示。<br>
&emsp;&emsp;V 代表视图（View） ， 即业务逻辑层。 该层包含存取模型及调取恰当模板的相关逻辑。 你可以把它看
作模型与模板之间的桥梁。<br>
&emsp;&emsp;如果你熟悉其它的 MVC Web 开发框架， 比方说 Ruby on Rails， 你可能会认为 Django 视图是控制器， 而
Django 模板是视图。 很不幸， 这是对 MVC 不同诠释所引起的错误认识。 在 Django 对 MVC 的诠释中， 视图
用来描述要展现给用户的数据； 不是数据 如何展现 ,而且展现 哪些 数据。 相比之下， Ruby on Rails 及一些同
类框架提倡控制器负责决定向用户展现哪些数据， 而视图则仅决定 如何展现数据， 而不是展现 哪些 数据。<br>
&emsp;&emsp;两种诠释中没有哪个更加正确一些。 重要的是要理解底层概念。<br>
# chapter3 Django 视图
## 3.1 来写个登录
&emsp;&emsp;继续在上一章的基础上开发， 不过这一次， 我们先从前端页面写起。 打开.../sign/templates/index.html 文
件， 修改代码如下。<br>
```
<html>
    <head>
        <title>Django Page</title>
    </head>
    <body>
        <h1>发布会管理</h1>
        <from>
            <input name="username" type="text" placeholder="username"><br>
            <input name="password" type="password" placeholder="password"><br>
            <button id="btn" type="submit">登录</button>
        </from>
    </body>
</html>
```
&emsp;&emsp;启动 Django 服务， 访问： http://127.0.0.1:8000/index/<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.1.PNG)<br>
&emsp;&emsp;虽然在页面上已经看到了一个登录功能， 但它目前还并不可用。 要想真正实现登录还需要思考以一些问
题。 当点输入用户名密码并点击“登录” 按钮之后， 表单（form） 中的数据要以什么方式（GET/POST） 提交
系统？ 系统如何验证得到的用户名密码？ 如果验证成功应该跳转到什么页面？ 如果验证失败如何将错误提示
返加给用户？<br>
### 3.1.1、 GET 与 POST 请求
&emsp;&emsp;当客户机通过 HTTP 协议向服务器提交请求时， 最常用到的方法是 GET 和 POST。<br>
&emsp;&emsp;GET - 从指定的资源请求数据。<br>
&emsp;&emsp;POST - 向指定的资源提交要被处理的数据<br>
- GET 请求

先来看看 GET 方法是如何传参数， 给 form 添加属性 method="get"。<br>
index.html:<br>
```html
<from method="get">
    <input name="username" type="text" placeholder="username"><br>
    <input name="password" type="password" placeholder="password"><br>
    <button id="btn" type="submit">登录</button>
</from>
```
&emsp;&emsp;然后保存在 index.html 文件， 重新刷新页面。 输入用户名、 密码， 点击登录。<br>
&emsp;&emsp;查看浏览器 URL 地址栏：<br>
&emsp;&emsp;http://127.0.0.1:8000/index/?username=admin&password=admin123<br>
&emsp;&emsp;GET 方法会将用户提交的数据添加到 URL 地址中， 路径后面跟问号“？ ” ， username 和 password 为
HTML 代码中<input>标签的 name 属性值， username=admin 表示用户名输入框得到的输入数据为“admin” 。
password=admin123 密码输入框得到的输入数据为“admin123” 。 多个参数之间用“&” 符号隔开。<br>
- POST 请求
&emsp;&emsp;同样是上面的代码， 再将 form 表单的中的属性改为 method="post" 。 重新刷新页面后， 再次输入用户名
密码， 点击“登录” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.2.PNG)<br>
&emsp;&emsp;“CSRF verification failed. Request aborted.”<br>
&emsp;&emsp;这个提示非常有意思， 而且被许多初学 Django 的同学问到。 如果你仔细阅读上面的帮助信息， 那么将会
知道这个错误的原因， 并且找到解决办法。 然而， 新手往往面对错误提示时显得恐慌和手足无措， 从而忽略
掉页面上的提示信息。<br>
&emsp;&emsp;如果你从未听说过“跨站请求伪造” （Cross-Site Request Forgery， CSRF） 漏洞， 现在就去查资料吧。
Django 针对 CSRF 的保护措施是在生成的每个表单中放置一个自动生成的令牌， 通过这个令牌判断 POST
请求是否来自同一个网站。<br>
&emsp;&emsp;之前的模板都是纯粹的 HTML， 在这里要首次使用到 Django 的模板， 使用“模板标签”（template tag）
添加 CSRF 令牌。 在 from 表单中添加{% csrf_token %}。<br>
```html
<form method="post">
     <input name="username" type="text" placeholder="username" ><br>
     <input name="password" type="password" placeholder="password"><br>
     <button id="btn" type="submit">登录</button>
     {% csrf_token %}
</form>
```
&emsp;&emsp;然后， 刷新页面并重新提交登录表单， 错误提示页面消失了。<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.3.PNG)<br>
&emsp;&emsp;如图 3.3， 借助 Firebug 前端调试工具进行查看 POST 请求。 你会看到除了 usrname 和 password 参数外，
还多了一个 csrfmiddlewaretoken 的参数。 当页面向 Django 服务器发送一个 POST 请求时， 服务器端要求客户
端加上 csrfmiddlewaretoken 字段， 该字段的值为当前会话 ID 加上一个密钥的散列值。<br>
&emsp;&emsp;如果想忽略掉该检查， 可以在.../guest/settings.py 文件中注释掉 csrf。<br>
settings.py:<br>
```html
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```
### 3.1.2、 处理登录请求
&emsp;&emsp;现在了解了将表单中的数据提交给服务器的方式（GET/POST） ， 那么将登录数据提交给 Django 服务器
的谁来处理？ 可以通过 form 表单的 action 属性来指定提交的路径。<br>
index.html:<br>
```html
<form method="post" action="/login_action/">
```
&emsp;&emsp;打开../guest/urls.py 文件添加 login_action/的路由。<br>
urls.py:<br>
```Python
......
from sign import views
urlpatterns = [
    ......
    url(r'^login_action/$', views.login_action),
]
```
&emsp;&emsp;打开 sign/views.py 文件， 创建 login_action 视图函数。<br>
```Python
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "index.html")


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            return HttpResponse('login success!')
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
```
&emsp;&emsp;通过 login_aciton 函数来处理登录请求。<br>
&emsp;&emsp;客户端发送的请求信息全部包含在 request 中。 关于如何获取 request 中包含的信息， 参考 Django 文档。<br>
&emsp;&emsp;https://docs.djangoproject.com/en/1.10/ref/request-response/<br>
&emsp;&emsp;首先， 通过 request.method 方法得到客户发送的请求方式， 判断其是否为 POST 请求类型。<br>
&emsp;&emsp;接着， 通过 request.POST 来获取 POST 请求。 通过.get()方法来寻找 name 为“username” 和“password”<br>
的 POST 参数， 如果参数没有提交， 返回一个空的字符串。 此处的“username” 和“password” 对应 form 表
单中<input> 标签的 name 属性， 可见这个属性的重要性。<br>
&emsp;&emsp;再接下来， 判断 POST 请求得到的 username 和 password 是否为“admin/admin123” ， 如果是则通过
HttpResponse 类返回“login success!” 字符串。 否则， 将通过 render 返回 index.html 登录页面， 并且顺带返回
错误提示的字典“{'error': 'username or password error!'}” 。<br>
&emsp;&emsp;但是， 显然 index.html 页面上并没有显示错误提示的地方， 所以， 需要在 index.html 页面中添加 Django
模板。<br>
index.html:<br>
```html
<form method="post" action="/login_action/">
     <input name="username" type="text" placeholder="username" ><br>
     <input name="password" type="password" placeholder="password"><br>
     {{ error }}<br>
     <button id="btn" type="submit">登录</button>
     {% csrf_token %}
</form>
```
&emsp;&emsp;此处又使用到了 Django 的模板语言， 添加{{ error }}， 它对应 render 返回字典中的 key， 并且在登录失败
的页面中显示 value， 即“username or password error!” 信息。 好了， 现在来体验一下登录功能， 分别看看登录
失败和成功的效果。 如图 3.4、 3.5。<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.4.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.5.PNG)<br>
### 3.1.3、 登录成功页
&emsp;&emsp;显然， 登录成功返回的“login success!” 字符串只是一种临时方案， 只是为了方便验证登录的处理逻辑，
现在没有问题之后， 需要通过 HTML 页面来替换。<br>
&emsp;&emsp;我们要开发的是发布会签到系统， 那么我希望登录之后默认显示发布会列表。 所以， 首先创
建.../templates/event_manage.html 页面。<br>
```
<html>
    <head>
        <title>Event Manage Page</title>
    </head>
    <body>
        <h1>Login Success!</h1>
    </body>
</html>
```
&emsp;&emsp;修改.../sign/views.py 中的 login_action 函数。<br>
views.py:<br>
```
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
......
# 登录动作
......
if username == 'admin' and password == 'admin123':
    return HttpResponseRedirect('/event_manage/')
......
# 发布会管理
def event_manage(request):
    return render(request,"event_manage.html")
```
&emsp;&emsp;此处又用到的一个新的类 HttpResponseRedirect， 它可以对路径进行重定向， 从而将登录成功之后的请求
指向/event_manage/目录。<br>
&emsp;&emsp;创建 event_manage 函数， 用于返回发布会管理 event_manage.html 面页。<br>
&emsp;&emsp;最后， 不要忘记在../guest/urls.py 文件中添加路径 event_manage/的路由。<br>
urls.py:<br>
```Python
from sign import views
urlpatterns = [
......
    url(r'^event_manage/$', views.event_manage),
]
```
## 3.2 Cookie 和 Session
&emsp;&emsp;接下来继续另外一个有意思的话题， 在不考虑数据库验证的情况下， 假如用户通过“zhangsan” 登录，
然后， 在登录成功页显示“嘿， zhangsan 你好！ ” ， 这是一般系统都会提供的一个小功能， 接下来我们将分别
通过 Cookie 和 Session 来实现它。<br>
&emsp;&emsp;Cookie 与 Session<br>
&emsp;&emsp;Cookie 机制： 正统的 Cookie 分发是通过扩展 HTTP 协议来实现的， 服务器通过在 HTTP 的响应头中加上
一行特殊的指示以提示浏览器按照指示生成相应的 Cookie。然而纯粹的客户端脚本如 JavaScript 或者 VBScript
也可以生成 Cookie。 而 Cookie 的使用是由浏览器按照一定的原则在后台自动发送给服务器的。 浏览器检查所
有存储的 Cookie， 如果某个 Cookie 所声明的作用范围大于等于将要请求的资源所在的位置， 则把该 cookie 附
在请求资源的 HTTP 请求头上发送给服务器。<br>
&emsp;&emsp;Session 机制： Session 机制是一种服务器端的机制， 服务器使用一种类似于散列表的结构（也可能就是
使用散列表） 来保存信息。<br>
### 3.2.1、 Cookie 的使用
&emsp;&emsp;继续修改.../sign/views.py 文件：<br>
views.py:<br>
```Python
# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user',username,3600) # 添加浏览器cookie
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
    else:
        return render(request, 'index.html', {'error': 'username or password error!'})


# 发布会管理
def event_manage(request):
    username = request.COOKIES.get('user','') # 读取浏览器cookie
    return render(request, "event_manage.html",{"user":username})
```
&emsp;&emsp;当用户登录成功后， 在跳转到 event_manage 页面时， 通过 set_cookie()方法来添加浏览器 Cookie。<br>
&emsp;&emsp;这里给 set_cookie()方法传了三个参数， 第一个参数“user” 是用于表示写入浏览器的 Cookie 名， 第二个
参数 username 是由用户在登录页上输入的用户名， 第三个参数 3600 用于表示该 cookie 信息在浏览器中的停
留时间， 默认以秒为单位。<br>
&emsp;&emsp;而在 event_manage 视图函数中， 通过 request.COOKIES 来读取 Cookie 名为“user”的值。 并且通过 render
将和 event_manage.html 页面一起返回给客户端浏览器。<br>
&emsp;&emsp;修改.../templates/event_manage.html 页面， 添加<div>标签来显示用户登录的用户名。<br>
event_manage.html:<br>
```html
<div style="float:right;">
    <a>嘿! {{ user }} 欢迎</a><hr />
</div>
```
&emsp;&emsp;重新再来登录一次,将会看到页面如图3.6.<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.6.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.7.PNG)<br>
### 3.2.2、 Session 的使用
&emsp;&emsp;Cookie 固然好， 但存在一定的安全隐患。 Cookie 像我们以前用的存折， 用户的存钱、 取钱都会记录在这
张存折上（即浏览器中会保存所有用户信息） ， 那么对于有非分想法的人可能会去修改存折上的数据（这个
比喻忽略掉银行同样会记录用户存取款的金额） 。<br>
&emsp;&emsp;相对于存折， 银行卡要安全的得多， 客户拿到的只是一个银行卡号（即浏览器只保留一个 Sessionid） ，
那么用户的存钱、 取钱都会记录在银行的系统里（即服务器端） ， 只得到一个 sessionid 是没有任何意义的，
所以相对于 Cookie 来说就会安全很多。<br>
&emsp;&emsp;在 Django 中使用 Session 和 Cookie 类似。 我们只用将 Cookie 的几步操作替换成 session 即可。<br>
&emsp;&emsp;修改.../sign/views.py 文件， 在 login_action 函数中， 将：<br>
&emsp;&emsp;`response.set_cookie('user', username, 3600)`<br>
&emsp;&emsp;替换为：<br>
&emsp;&emsp;`request.session['user'] = username # 将 session 信息记录到浏览器`
&emsp;&emsp;在 event_manage 函数中， 将：<br>
&emsp;&emsp;`username = request.COOKIES.get('user', '')`<br>
&emsp;&emsp;替换为：<br>
&emsp;&emsp;`username = request.session.get('user', '') # 读取浏览器 session`<br>
&emsp;&emsp;再次尝试登录， 不出意外的话将会得到一个错误。<br>
&emsp;&emsp;`“no such table: django_session”`<br>
&emsp;&emsp;这个错误跟 Session 的机制有关， 既然要服务器端记录用户的数据， 那么一定要有地方来存放用户
Sessionid 对应的信息才对。 所以， 我们需要创建 django_session 表。 别着急！ Django 已经帮我们准备好这些常
用的表， 只需要将他们生成即可， 是不是很贴心。<br>
`D:\pydj\guest>python3 manage.py migrate`<br>
&emsp;&emsp;通过“migrate” 命令进行数据迁移。<br>
&emsp;&emsp;等等， 我们好像并没配置数据库啊， 为什么数据库已经生成了表呢？ 这是因为 Django 已经默认帮我设置
sqlite3 数据库。 打开.../settings.py 文件， 查看 sqlite3 数据库的配置。<br>
```Python
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
&emsp;&emsp;另外， 在 guest 项目的根目录下会生成一个 db.sqlite3 文件。 关于数据的操作我们会放在下一章讨论。 此
时， 先来验证 Session 功能是否生效， 重新登录。<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.8.PNG)<br>
## 3.3 Django 认证系统
&emsp;&emsp;到目前为止， 虽然实现了登录， 但显然用户登录信息的验证并未真正实现， 目前的做法只是简单的用 if
语句判断用户名和密码是否为“admin/admin123” ， 所以， 我们并没有完整的用户数据。<br>
### 3.3.1、 登录 Admin 后台
&emsp;&emsp;在上一小节执行 manage.py 的“migrate” 命令时， Django 同时也帮我们生成了 auth_user 表。 同时， 我们
可以通过 URL 地址： http://127.0.0.1:8000/admin/ 来访问 Django 自带的 Admin 管理后台。 在此， 之前先来创
建登录 Admin 后台的管理员账号。<br>
```
D:\pydj\guest>python3 manage.py createsuperuser
Username (leave blank to use 'fnngj'): admin #输入用户名
Email address: admin@mail.com #输入邮箱
Password: #输入密码
Password (again): #重复输入密码
Superuser created successfully.
```
&emsp;&emsp;创建的超级管理员帐号/密码为： admin/admin123456<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.9.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.10.PNG)<br>
&emsp;&emsp;如图 3.9、 3.10， 通过创建的管理员账号登录 Admin 后台， 尝试点击“Add” 链接添加新的用户， 并且用
新创建的用户再次登录后台。 尝试一下吧！ 相信你可以做到。<br>
### 3.3.2、 引用 Django 认证登录
&emsp;&emsp;既然 Django 已经帮我们做好用户体系， 那么就直接拿来使用好了。<br>
&emsp;&emsp;打开.../sign/views.py 文件修改 login_action 函数。<br>
views.py:<br>
```Python
from django.contrib import auth
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user) # 登录
            request.session['user']=username # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
    else:
        return render(request, 'index.html', {'error': 'username or password error!'})
```
&emsp;&emsp;使用 authenticate()函数认证给出的用户名和密码。 它接受两个参数， 用户名 username 和密码 password，
并在用户名密码正确的情况下返回一个 user 对象。 如果用户名密码不正确， 则 authenticate()返回 None。<br>
&emsp;&emsp;通过 if 语句判断 authenticate()返回如果不为 None， 说明用户认证通过。 那么接下来调用 login()函数进行
登录。 login()函数接收 HttpRequest 对象和一个 user 对象。<br>
&emsp;&emsp;重新使用 admin 管理后台创建用户账户来验证登录功能吧！<br>
### 3.3.3、 关上窗户
&emsp;&emsp;“上帝为你关上了一扇门， 也一定会为你打开一扇窗户” ， 我们为系统开发了一个需要用户认证的登录，
然而， 我们不需要通过登录也可以直接访问到登录成功的页面。<br>
&emsp;&emsp;现在， 尝试直接访问： http://127.0.0.1:8000/event_manage/<br>
&emsp;&emsp;看！ 是不是直接打开了登录成功页， 那为什么还需要通过登录来访问这个页面呢？ 所以， 我们要把这些
“窗户” 都关上， 使用户只能通过登录来访问系统。<br>
&emsp;&emsp;再来感受一下 Django 的强大之处吧！ 一秒钟让你关好窗户。<br>
views.py:<br>
```
from django.contrib.auth.decorators import login_required
......
# 发布会管理
@login_required
def event_manage(request):
    username= request.session.get('user','') # 读取浏览器session
    return render(request, "event_manage.html",{"user":username})
```
&emsp;&emsp;是的， 就是这么简单， 如果想限制某个视图函数必须登录才能访问， 只需要在这个函数的前面加上
@login_required 即可。<br>
&emsp;&emsp;你可以再次尝试访问/event_manage/目录（千万不要忘记清理浏览器缓存再试！ ） ， 看看还能否直接访问
到.<br>
![image](https://github.com/15529343201/guest/blob/chapter3/image/3.11.PNG)<br>
&emsp;&emsp;如图 3.11， Django 会告诉访问的路径并不存在（404） 。<br>
&emsp;&emsp;如 果 你 细 心 ， 会 发 布 在 访 问 被 @login_required 装 饰 的 视 图 时 ， 默 认 会 跳 转 的 URL 中 会 包 含
“/accounts/login/” ， 为什么不让它直接跳转到登录页面呢？ 不但要告诉你窗户是关着的， 还要帮你指引到门
的位置。<br>
&emsp;&emsp;接下来修改.../urls.py 文件， 添加以下路径。<br>
urls.py:<br>
```
......
from sign import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^accounts/login/$', views.index),
......
]
```
&emsp;&emsp;当用户访问：<br>
&emsp;&emsp;http://127.0.0.1:8000/<br>
&emsp;&emsp;http://127.0.0.1:8000/index/<br>
&emsp;&emsp;http://127.0.0.1:8000/event_manage/<br>
&emsp;&emsp;默认， 都会跳转到登录页面。 但是， 如果你访问的是其它不存的路径， 比如/abc/， 依然会显示图 3.11 的
页面。 这个时候需要设置默认的 404 页面<br>
# chapter4 Django 模型
## 4.1 设计系统表
&emsp;&emsp;Django 提供完善的模型（model） 层主要用来创建和存取数据， 不需要我们直接对数据库操作。<br>
&emsp;&emsp;Django 模型基础知识：<br>
&emsp;&emsp;每个模型是一个 Python 类， 继承 django.db.models.model 类。<br>
&emsp;&emsp;该模型的每个属性表示一个数据库表字段。<br>
&emsp;&emsp;所有这一切， 已经给你一个自动生成的数据库访问的 API。<br>
&emsp;&emsp;打开.../sign/models.py 文件， 完成表的创建。<br>
models.py:<br>
```Python


from django.db import models


# Create your models here.
# 发布会表
class Event(models.Model):
    name = models.CharField(max_length=100)  # 发布会标题
    limit = models.IntegerField()  # 参加人数
    status = models.BooleanField()  # 状态
    address = models.CharField(max_length=200)  # 地址
    start_time = models.DateTimeField('events time')  # 发布会时间
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    def __str__(self):
        return self.name


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event)  # 关联发布会 id
    realname = models.CharField(max_length=64)  # 姓名
    phone = models.CharField(max_length=16)  # 手机号
    email = models.EmailField()  # 邮箱
    sign = models.BooleanField()  # 签到状态
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname
```
&emsp;&emsp;对于产品发布会来说， 显然它是一个事件。 那么时间、 地点、 人物等要素必不可少。 数据库表的设计需
要围绕着这些要素进行。<br>
&emsp;&emsp;关于发布会表（Event 类） 和嘉宾表（Guest 类） 的每一个字段， 在代码中已经做了注解。 有些字段的设
计需要做一下简单的说明。<br>
&emsp;&emsp;首先， 发布会表和嘉宾表中默认都会生成自增 id， 而我们在创建模型时不需要声明该字段。<br>
&emsp;&emsp;其次， 发布会表中增加了 status 字段用于表示发布会的状态是否开启， 用于控制该发布会是否可用。<br>
&emsp;&emsp;再次， 嘉宾表中通过 event_id 关联发布会表， 一条嘉宾信息一定所属于某一场发布会。<br>
&emsp;&emsp;最后， 对于一场发布会来说， 一般会选择手机号作为一位嘉宾的验证信息， 所以， 对于一场发布会来说，
手机号必须是唯一。 除了嘉宾 id 外， 这里通过发布会 id +手机号来做为联合主键。<br>
&emsp;&emsp;__str__()方法告诉 Python 如何将对象以 str 的方式显示出来。 所以， 为每个模型类添加了__str__()方法。
（如果读者使用的是 Python2.x 的话， 这里需要使用__unicode__()） 。<br>
`D:\pydj\guest>python3 manage.py makemigrations sign`<br>
`D:\pydj\guest>python3 manage.py migrate`<br>
## 4.2 admin 后台管理
&emsp;&emsp;在第三章 3.3.1 小节， 通过 Admin 后台管理用户组/用户表非常方便。 那么， 我们创建的发布会和嘉宾表
同样可以通过 Admin 后台去管理。<br>
&emsp;&emsp;打开.../sign/admin.py 文件。<br>
admin.py:<br>
```Python
from django.contrib import admin
from sign.models import Event, Guest

# Register your models here.
admin.site.register(Event)
admin.site.register(Guest)
```
&emsp;&emsp;这些代码通知 admin 管理工具为这些模块逐一提供界面。<br>
&emsp;&emsp;登录 admin 后台： http://127.0.0.1:8000/admin/ （admin/admin123456）<br>
![image](https://github.com/15529343201/guest/blob/chapter4/image/4.1.PNG)<br>
&emsp;&emsp;现在点击“Add” 添加一条发布会（Event） 数据。<br>
![image](https://github.com/15529343201/guest/blob/chapter4/image/4.2.PNG)<br>
&emsp;&emsp;如图 4.2， 显示的是一条发布会数据， 然而只有发布会名称， 如何才能显示表中的更多字段呢？ 继续修
改.../sign/admin.py 文件。<br>
admin.py:<br>
```Python
from django.contrib import admin
from sign.models import Event, Guest


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time', 'id']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']


admin.site.register(Event)
admin.site.register(Guest)
```
&emsp;&emsp;新建了 EventAdmin 类， 继承 django.contrib.admin.ModelAdmin 类， 保存着一个类的自定义配置， 以供
Admin 管理工具使用。 这里只自定义了一项： list_display， 它是一个字段名称的数组， 用于定义要在列表中显
示哪些字段。 当然， 这些字段名称必须是模型中的 Event()类定义的。<br>
&emsp;&emsp;接下来修改 admin.site.register()调用， 添加了 EventAdmin。 你可以这样理解： 用 EventAdmin 选项注册
Event 模块。<br>
&emsp;&emsp;然后， 对 Guest 模块也做了同样的操作。<br>
&emsp;&emsp;保存代码后， 重新刷新 Event 列表， 如图 4.3。<br>
![image](https://github.com/15529343201/guest/blob/chapter4/image/4.3.PNG)<br>
再接下来， 点击“Add” 添加一条嘉宾（Guest） 数据。 如图 4.4。<br>
![image](https://github.com/15529343201/guest/blob/chapter4/image/4.4.PNG)<br>
&emsp;&emsp;除此之外， Admin 管理后台提供了的很强的定制性， 我们甚至可以非常方便生成搜索栏和过滤器。 重新
打开.../sign/admin.py 文件， 做如下修改。<br>
admin.py:<br>
```Python
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time', 'id']
    search_fields = ['name'] # 搜索栏
    list_filter = ['status'] # 过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone'] # 搜索栏
    list_filter = ['sign'] # 过滤器
```
&emsp;&emsp;search_fields 用于创建表字段的搜索器， 可以设置搜索关键字匹配多个表字段。 list_filter 用于创建字段过
滤器。<br>
&emsp;&emsp;查看 Event 列表与者 Guest 列表， 如图 4.5、 4.6。<br>
![image](https://github.com/15529343201/guest/blob/chapter4/image/4.5.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter4/image/4.6.PNG)<br>




































































































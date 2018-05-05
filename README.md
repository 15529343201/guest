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
## 4.3 基本数据访问
`D:\pydj\guest> python3 manage.py shell`<br>
```
>>> from sign.models import Event, Guest
>>> Event.objects.all()
<QuerySet [<Event: 小米 5 发布会>]>
>>> Guest.objects.all()
<QuerySet [<Guest: jack>]>
```
&emsp;&emsp;`from sign.models import Event, Guest`<br>
&emsp;&emsp;导入 sign 应用下的 models.py 中的 Event 表和 Guest 表。<br>
&emsp;&emsp;`table.objects.all()`<br>
&emsp;&emsp;获得 table（Event、 Gues 表） 中的所有对象。<br>
### 4.3.1、 插入数据
```
>>> from datetime import datetime
>>> e1 = Event(id=2,name='红米 Pro 发布会',limit=2000,status=True,address='北京水立
方',start_time=datetime(2016,8,10,14,0,0))
>>> e1.save()
C:\Python35\lib\site-packages\django\db\models\fields\__init__.py:1453:
RuntimeWarning: DateTimeField Event.start_time received a naive datetime
(2016-08-10 14:00:00) while time zone support is active.
RuntimeWarning)
```
&emsp;&emsp;因为 start_time 字段需要设置日期时间， 所以导入和 datetime.datetime()方法。 但是， 我们收到了一行警告
信息“RuntimeWarning: DateTimeField Event.start_time received a naive datetime (2016-08-10 14:00:00) while time
zone support is active.”<br>
&emsp;&emsp;这跟 UTC 有关， 如果读者感兴趣可以百度 UTC 是什么？ 这里， 我们暂时忽略掉这个问题， 最简单的方
式就是在.../settings.py 文件中设置： USE_TZ = False。<br>
&emsp;&emsp;修改 settings.py 文件保存后， 需要执行“quit()”命令退出 shell 模式， 并重新执行“Python3 manage.py shell”
进入， 刚才的设置才会生效。<br>
&emsp;&emsp;如果你觉得创建和保存分两步完成过于麻烦， 也可以通过 table.objects.create()方法将两步合为一步， 方
法如下<br>
```
>>> Event.objects.create(id=3,name='红米 MAX 发布会',limit=2000,status=True,
address='北京会展中心',start_time=datetime(2016,9,22,14,0,0))
<Event: 红米 MAX 发布会>
>>> Guest.objects.create(realname='andy',phone=13611001101,email=
'andy@mail.com',sign=False,event_id=3)
<Guest: andy>
```
&emsp;&emsp;需要说明的是， 表的 id 字段已经设置了自增， 所以， 该字段为空可以添加数据， 但在创建嘉宾时数据时
需要指定关联的发布会 id。 Event 表指定了 id=3， Guest 表指定 event_id=3， 所以嘉宾 andy 对应的是红米 MAX
发布会。<br>
### 4.3.2、 查询数据
&emsp;&emsp;查询无疑是数据库表中使用频率最高的操作。<br>
&emsp;&emsp;table.objects.get()方法用于从数据库表中取得一条匹配的结果， 返回一个对象， 如果记录不存在的话， 那
么它会报 DoesNotExist 类型错误。<br>
&emsp;&emsp;通过 name='红米 MAX 发布会' 做为查询条件：<br>
```
>>> e1 = Event.objects.get(name='红米 MAX 发布会')
>>> e1
<Event: 红米 MAX 发布会>
>>> e1.address
'北京会展中心'
>>> e1.start_time
datetime.datetime(2016, 9, 22, 14, 0)
>>>
>>> Event.objects.get(name='红米 MAX 发布会').status
True
>>> Event.objects.get(name='红米 MAX 发布会').limit
2000
>>> Event.objects.get(name='发布会').address
Traceback (most recent call last):
File "<console>", line 1, in <module>
File "C:\Python35\lib\site-packages\django\db\models\manager.py", line 85, in
manager_method
return getattr(self.get_queryset(), name)(*args, **kwargs)
File "C:\Python35\lib\site-packages\django\db\models\query.py", line 385, in get
self.model._meta.object_name
sign.models.DoesNotExist: Event matching query does not exist.
```
&emsp;&emsp;因为 name='发布会' 并没有完全匹配到发布会名称， 所以会抛出 DoesNotExist 异常， 但更多的时候希望
使用模糊查询。<br>
&emsp;&emsp;table.objects.filter()方法是从数据库的取得匹配的结果， 返回一个对象列表， 如果记录不存在的话， 它会
返回[]。<br>
```
>>> e2 = Event.objects.filter(name__contains='发布会')
>>> e2
<QuerySet [<Event: 小米 5 发布会>, <Event: 红米 Pro 发布会>, <Event: 红米 MAX 发布会>]>
```
&emsp;&emsp;在 name 和 contains 之间用双下划线。 这里， contains 部分会被 Django 翻译成 LIKE 语句。<br>
&emsp;&emsp;接下来， 通过嘉宾信息查询其关联的发布会信息。 查看 phone='13611001101' 这位嘉宾所参加的发布会信
息：<br>
```
>>> g1 = Guest.objects.get(phone='13611001101')
>>> g1.event
<Event: 红米 MAX 发布会>
>>> g1.event.name
'红米 MAX 发布会'
>>> g1.event.address
'北京会展中心'
```
### 4.3.3、 删除数据
&emsp;&emsp;查询 phone='13611001101' 的嘉宾， 通过 delete()方法删除。<br>
```
>>> g2 = Guest.objects.get(phone='13611001101')
>>> g2.delete()
(1, {'sign.Guest': 1})
>>> Guest.objects.get(phone='13611001101').delete()
(1, {'sign.Guest': 1})
```
### 4.3.4、 更新数据
&emsp;&emsp;查询 phone='13611001101' 的嘉宾， 更新 realname='andy2' 。<br>
```
>>> g3=Guest.objects.get(phone='13611001101')
>>> g3.realname='andy2'
>>> g3.save()
>>> Guest.objects.select_for_update().filter(phone='13611001101').update(
realname='andy')
1
```
## 4.4 SQLite管理工具
### 4.4.1 SQLiteManager
&emsp;&emsp;SQLiteManager 是一个支持多国语言基于 Web 的 SQLite 数据库管理工具， 它的特点包括多数据库管理，
创建和连接； 表格， 数据， 索引操作； 视图， 触发器， 和自定义函数管理， 数据导入/导出， 数据库结构导出
等。<br>
&emsp;&emsp;在 Firefox 浏览器插件库中可以搜索到 SQLiteManager， 所以， 这装起来非常方便。 打开 Firefox 浏览器，
菜单栏“工具” -->“添加组件” ， 搜索“SQLiteManager” 安装， 并重启动 Firefox 浏览。 从菜单栏“工具”
下拉菜单中将会出现“SQLiteManager” 的选项， 打开如图 4.7<br>
![image](https://github.com/15529343201/guest/blob/chapter4/image/4.7.PNG)<br>
### 4.4.2、 SQLiteStudio
&emsp;&emsp;SQLiteStudio 是一款 SQLite 数据库可视化工具， 是使用 SQLite 数据库开发应用的必备软件， 软件无需安
装， 下载后解压即可使用， 很小巧但很好用， 绿色中文版本。 比起其它 SQLite 管理工具， 我喜欢用这个。 很
方便易用， 不用安装的单个可执行文件， 支持中文。<br>
&emsp;&emsp;SQLiteStudio 是一个跨平台的 SQLite 数据库的管理工具， 采用 Tcl 语言开发。<br>
&emsp;&emsp;下载地址： http://sqlitestudio.pl/<br>
![image](https://github.com/15529343201/guest/blob/chapter4/image/4.8.PNG)<br>
## 4.5 配置 MySQL
&emsp;&emsp;前面用的数据库是 Python 自带的 SQLite3， 这种数据库并不适用大型的项目。 除 SQLite3 之外， Django
还支持以下几种数据库：<br>
 PostgreSQL (http://www.postgresql.org/)<br>
 MySQL (http://www.mysql.com/)<br>
 Oracle (http://www.oracle.com/)<br>
&emsp;&emsp;本节以 MySQL 为例， 介绍 MySQL 的安装， 以及在 Django 中的配置。<br>
### 4.5.1、 安装 MySQL
&emsp;&emsp;下载 MySQL： http://dev.mysql.com/downloads/mysql/<br>
### 4.5.2、 安装 PyMySQL
&emsp;&emsp;这里遇到小小的分歧，如果读者使用的 Python2.x 版本，那么连接 MySQL 数据库可以使用 MySQL-python。
但是， MySQL-python 只支持 Python2.x 版本， 并在 2014 年 1 月之后就不再更新了， 但这并不影响对该库的使
用。 目前 Django 默认使用的是该驱动。<br>
&emsp;&emsp;下载地址： https://pypi.python.org/pypi/MySQL-python<br>
&emsp;&emsp;而 且 如 果 读 者 使 用 的 操 作 系 统 是 Win 64 位 ， 还 需 要 单 独 查 找 安 装 64 位 版 本 的 安 装 包 ，
mysql-python-1.2.5.win-amd64-py2.7.exe。<br>
&emsp;&emsp;而当前我们使用的是 Python3.x 版本的 Django， 所以这里推荐使用 PyMySQL 驱动。<br>
&emsp;&emsp;下载地址： https://pypi.python.org/pypi/PyMySQL<br>
&emsp;&emsp;PyMySQL 同样支持 pip 命令安装。<br>
`C:\Users\fnngj>python3 -m pip install PyMySQL`<br>
```
import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
user='root',
password='',
db='test',
charset='utf8mb4',
cursorclass=pymysql.cursors.DictCursor)
try:
with connection.cursor() as cursor:
# Create a new record
sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id,
create_time) VALUES ("alen",18800110001,"alen@mail.com",0,1,NOW());'
cursor.execute(sql)
# connection is not autocommit by default. So you must commit to save
# your changes.
connection.commit()
with connection.cursor() as cursor:
# Read a single record
sql = "SELECT realname,phone,email,sign FROM sign_guest WHERE phone=%s"
cursor.execute(sql, ('18800110001',))
result = cursor.fetchone()
print(result)
finally:
connection.close()
```
&emsp;&emsp;connect() 建立数据库连接。<br>
&emsp;&emsp;execute() 执行 SQL 语句。<br>
&emsp;&emsp;close() 关闭数据连接。<br>
### 4.5.3、 Django 配置 MySQL
```
# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'guest',
        'USER': 'root',
        'PASSWORD': '123456',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```
&emsp;&emsp;配置信息从上到下依次是驱动（ENGINE） ， 主机地址（HOST） ， 端口号（PORT） ， 数据库（NAME），
登录用户名（USER） ， 登录密码（PASSWORD） 。<br>
&emsp;&emsp;关于， sql_mode 的设置， 请参考 Django 文档。<br>
&emsp;&emsp;https://docs.djangoproject.com/en/1.10/ref/databases/#mysql-sql-mode<br>
&emsp;&emsp;注意： 切换了数据库后， 之前 Sqlite3 数据库里的数据并不能复制到 MySQL 中， 所以需要重新进行数据
库同步， 使数据模型重新在 MySQL 数据库中生成表。<br>
```
D:\pydj\guest>python3 manage.py migrate
Traceback (most recent call last):
File "C:\Python35\lib\site-packages\django\db\backends\mysql\base.py", line 25,
in <module>
import MySQLdb as Database
ImportError: No module named 'MySQLdb'
During handling of the above exception, another exception occurred:
……
File "C:\Python35\lib\site-packages\django\db\backends\mysql\base.py", line 28,
in <module>
raise ImproperlyConfigured("Error loading MySQLdb module: %s" % e)
django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No
module named 'MySQLdb'
```
&emsp;&emsp;出错了！ 这是因为 Django 在连接 MySQL 数据库时默认使用的是 MySQLdb 驱动， 然而我们没有安装该
驱动， 因为它并不支持 Python3， 我们现在安装的是 PyMySQL 驱动， 如何让当前的 Django 通过 PyMySQL 来
连接 MySQL 数据库呢？ 方法很简单。<br>
&emsp;&emsp;在.../guest/__init__.py 目录下添加：<br>
```
import pymysql
pymysql.install_as_MySQLdb()
```
```
D:\pydj\guest>python3 manage.py migrate
Operations to perform:
Apply all migrations: admin, auth, contenttypes, sessions, sign
Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying admin.0002_logentry_remove_auto_add... OK
Applying contenttypes.0002_remove_content_type_name... OK
Applying auth.0002_alter_permission_name_max_length... OK
Applying auth.0003_alter_user_email_max_length... OK
Applying auth.0004_alter_user_username_opts... OK
Applying auth.0005_alter_user_last_login_null... OK
Applying auth.0006_require_contenttypes_0002... OK
Applying auth.0007_alter_validators_add_error_messages... OK
Applying auth.0008_alter_user_username_max_length... OK
Applying sessions.0001_initial... OK
Applying sign.0001_initial... OK
```
&emsp;&emsp;另外， 因为更换了数据库， 所以， Admin 后台超级管理员账号（admin/admin123456） 也需要重新创建。<br>
```
D:\pydj\guest>python3 manage.py createsuperuser
Username (leave blank to use 'fnngj'): admin #输入登录用户名
Email address: admin@mail.com #输入用户邮箱
Password: #输入登录密码
Password (again): #再次输入用户密码
Superuser created successfully.
```
### 4.5.4、 MySQL 管理工具
- Navicat
- SQLyog

# chapter5 Django 模板
&emsp;&emsp;https://github.com/defnngj/guest<br>
## 5.1 Django-bootstrap3
&emsp;&emsp;Django-bootstrap3 pypi 仓库地址： https://pypi.python.org/pypi/django-bootstrap3<br>
&emsp;&emsp;1、 通过 Python 的 pip 命令安装：<br>
&emsp;&emsp;`C:\pydj\guest>python3 -m pip install django-bootstrap3`<br>
&emsp;&emsp;2、 在.../guest/settings.py 文件中添加“bootstrap3” 应用。<br>
settings.py:<br>
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
    'bootstrap3',
]
```
## 5.2 发布会管理
### 5.2.1、 发布会列表
&emsp;&emsp;继续回到视图的开发中， 打开.../sign/views.py 文件， 修改 event_manage()视图函数。<br>
views.py:<br>
```Python
# 发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username= request.session.get('user','') # 读取浏览器session
    return render(request, "event_manage.html",{"user":username,"events":event_list})
```
&emsp;&emsp;Event.objects.all() 用于查询所有发布会对象（数据） ， 通过 render()函数附加在 event_manage.html 页面
返回给客户端浏览器。<br>
&emsp;&emsp;打开并编写.../templates/event_manage.html 页面。<br>
event_manage.html:<br>
```html
<html lang="zh-CN">
    <head>
        {% load bootstrap3 %}
        {% bootstrap_css %}
        {% bootstrap_javascript %}
        <title>Event Manage</title>
    </head>
    <body role="document">
        <!--导航栏-->
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="/event_manage/">Guest Manage System</a>
                </div>
                <div id="navbar" class="collapse navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li class="active"><a href="#">发布会</a></li>
                        <li><a href="/guest_manage/">嘉宾</a></li>
                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="#">{{ user }}</a></li>
                        <li><a href="/logout/">退出</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!--发布会列表-->
        <div class="row" style="padding-top: 80px;">
            <div class="col-md-6">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>id</th><th>名称</th><th>状态</th><th>地址</th><th>时间</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for event in events %}
                            <tr>
                                <td>{{ event.id }}</td>
                                <td>{{ event.name }}</td>
                                <td>{{ event.status }}</td>
                                <td>{{ event.address }}</td>
                                <td>{{ event.start_time }}</td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
</html>
```
&emsp;&emsp;对于 BootStrap 框架来说， 它主要通过 class 属性来设置 HTML 标签的样式。<br>
&emsp;&emsp;`{% load bootstrap3 %}`<br>
&emsp;&emsp;`{% bootstrap_css %}`<br>
&emsp;&emsp;`{% bootstrap_javascript %}`<br>
&emsp;&emsp;加载 Bootstrap3 应用， CSS 和 JavaScript 文件。 ｛% %｝ 为 Django 的模板标签， Django 的模板语言将会
在该标签下编写。<br>
&emsp;&emsp;`<title>Guest Manage</title>`<br>
&emsp;&emsp;设置页面标题为 Guest Manage。<br>
&emsp;&emsp;`<li class="active"><a href="#">发布会</a></li>`<br>
&emsp;&emsp;`<li><a href="/guest_manage/">嘉宾</a></li>`<br>
&emsp;&emsp;设置页面导航栏， class="active" 表示， 当前菜单处于选中状态。 href="/guest_manage/" 用于跳转到到嘉
宾管理页， 我们稍后完善该页面。<br>
&emsp;&emsp;`<li><a href="#">{{ user }}</a></li>`<br>
&emsp;&emsp;`<li><a href="/logout/">退出</a></li>`<br>
&emsp;&emsp;{{ }} Django 的模板标签， 用于定义显示变量。 这里将会通过浏览器 sessionid 获取到对应的登录用户名，
并显示。 href="/logout/" 定义退出路径， 稍后完善该功能。<br>
```html
{% for event in events %}
<tr>
<td>{{ event.id }}</td>
<td>{{ event.name }}</td>
<td>{{ event.status }}</td>
<td>{{ event.address }}</td>
<td>{{ event.start_time }}</td>
</tr>
{% endfor %}
```
&emsp;&emsp;Django 模板语言， 用于循环打印发布的 id、 name、 status、 address 和 start_time 等字段。 Django 模板语
言与 Python 有所不同。 for 语句需要有对应 endfor 来表示语句的结束， 同样， if 分支语句也需要 endif 来表示
语句的结束。<br>
![image](https://github.com/15529343201/guest/blob/chapter5/image/5.1.PNG)<br>
&emsp;&emsp;如图 5.1， 发布会管理页面， 通过对 Django-bootstrap3 应用的使用， 可以非常轻松的创建出漂亮的网页。<br>
### 5.2.2、 发布会搜索
&emsp;&emsp;对于列表管理来说， 搜索功能必不可少， 接下来开发针对发布会名称的搜索功能。<br>
&emsp;&emsp;这一次， 先在.../templates/event_manage.html 页面上创建搜索表单。<br>
event_manage.html:<br>
```html
<!--发布会搜索表单-->
<div class="page-header" style="padding-top: 60px;">
    <div id="navbar" class="navbar-collapse collapse">
        <form class="navbar-form" method="get" action="/search_name/">
            <div class="form-group">
                <input name="name" type="text" placeholder="名称" class="form-control">
            </div>
            <button type="submit" class="btn btn-success">搜索</button>
        </form>
    </div>
</div>
```
&emsp;&emsp;查询表单和我们前面开发的登录表单一样。 所以这里不再做过多介绍。 不过需要注意的几个地方，
method="get" HTTP 请求方式； action="/search_name/" 搜索请求路径； name="name" 搜索输入框的 name 属性
值。<br>
&emsp;&emsp;不要忘记在.../guest/urls.py 文件中添加搜索路径的路由。<br>
urls.py:<br>
```Python
from sign import views
urlpatterns = [
......
    url(r'^search_name/$', views.search_name),
]
```
&emsp;&emsp;打开.../sign/views.py 文件， 创建 search_name()视图函数。<br>
views.py:<br>
```Python
# 发布会搜索名称
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username,
"events": event_list})
```
&emsp;&emsp;通过 GET 方法接收搜索关键字， 并通过模糊查询， 匹配发布会 name 字段， 然后把匹配到的发布会列表
返回到页面上。 查询功能如图 5.2。<br>
![image](https://github.com/15529343201/guest/blob/chapter5/image/5.2.PNG)<br>
## 5.3 嘉宾管理
### 5.3.1、 嘉宾列表
&emsp;&emsp;创建.../templates/guest_manage.html 页面。<br>
guest_manage.html:<br>
```html
<html lang="zh-CN">
    <head>
        {% load bootstrap3 %}
        {% bootstrap_css %}
        {% bootstrap_javascript %}
        <title>Event Manage</title>
    </head>
    <body role="document">
        <!--导航栏-->
        <nav class="navbar navbar-inverse navbar-fixed-top">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="/event_manage/">Guest Manage System</a>
                </div>
                <div id="navbar" class="collapse navbar-collapse">
                    <ul class="nav navbar-nav">
                        <li><a href="/event_manage/">发布会</a></li>
                        <li class="active"><a href="#">嘉宾</a></li>
                    </ul>
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="#">{{user}}</a></li>
                        <li><a href="/logout/">退出</a></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!--嘉宾列表-->
        <div class="row" style="padding-top: 80px;">
            <div class="col-md-6">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th>id</th><th>名称</th><th>手机</th><th>Email</th><th>签到</th>
                            <th>发布会</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for guest in guests %}
                        <tr>
                            <td>{{ guest.id }}</td>
                            <td>{{ guest.realname }}</td>
                            <td>{{ guest.phone }}</td>
                            <td>{{ guest.email }}</td>
                            <td>{{ guest.sign }}</td>
                            <td>{{ guest.event }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </body>
</html>
```
&emsp;&emsp;`<li><a href="/event_manage/">发布会</a></li>`<br>
&emsp;&emsp;`<li class="active"><a href="#">嘉宾</a></li>`<br>
&emsp;&emsp;当前处理嘉宾管理页面， 所以， 设置嘉宾按钮的处于选中状态（class="active"） 。 为发布按钮设置跳转
路径（href="/event_manage/"）<br>
```html
{% for guest in guests %}
<tr>
<td>{{ guest.id }}</td>
<td>{{ guest.realname }}</td>
<td>{{ guest.phone }}</td>
<td>{{ guest.email }}</td>
<td>{{ guest.sign }}</td>
<td>{{ guest.event }}</td>
</tr>
{% endfor %}
```
&emsp;&emsp;通过 Django 模板语言的 for 语句循环读取嘉宾列表， 并显示 id、 realname、 phone、 email、 sign、 event
等字段。<br>
&emsp;&emsp;在.../guest/urls.py 文件中添加嘉宾路径的路由。<br>
urls.py:<br>
```Python
from sign import views
urlpatterns = [
......
    url(r'^guest_manage/$', views.guest_manage),
]

```
&emsp;&emsp;打开.../sign/views.py 文件， 创建 guest_manage()视图函数。<br>
views.py:<br>
```Python
# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})
```
&emsp;&emsp;嘉宾管理页面如图5.3<br>
![image](https://github.com/15529343201/guest/blob/chapter5/image/5.3.PNG)<br>
&emsp;&emsp;关于嘉宾管理页面的搜索功能， 这里不再介绍， 来吧！ 参考发布会管理页面上的搜索功能完成， 你可以
的。 接下来， 我们将开发另外一个常见的功能分页器。<br>
### 5.3.2、 分页器
&emsp;&emsp;对于嘉宾管理页面来说， 特别需要一个分页功能， 一场大型的发布会可能需要几千条嘉宾信息， 如果将
所有的嘉宾信息不做分页的显示在页面上， 首先页面的打开速度会受到严重的影响， 其次， 页面一次显示几
千条甚至几万条数据并不方便查看。<br>
&emsp;&emsp;Django 已经为我们准备好了 Paginator 分页类。 所以， 只需要调用它即可完成列表的分页功能。 分页功能
略为复杂， 首先进入 Django 的 shell 模式， 练习 Paginator 类的基本使用。<br>
```
D:\pydj\guest>python3 manage.py shell
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)]
on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.paginator import Paginator # 导入 Paginator 类
>>> from sign.models import Guest # Guest 下的所有表
>>> guest_list = Guest.objects.all() # 查询 uest 表的所有数据
>>> p = Paginator(guest_list,2) # 创建每页 2 条数据的分页器
>>> p.count # 查看共多少条数据
5>
>> p.page_range #查看共分多少页（每页 2 条数据） 循环结果为 1， 2， 3（共 3 页）
range(1, 4)
>>>
##########第一页#############
>>> page1 = p.page(1) # 获取第 1 页的数据
>>> page1 # 当前第几页
<Page 1 of 3>
>>> page1.object_list # 当前页的对象
[<Guest: andy>, <Guest: jack>]
>>> page1 = p.page(1)
>>> for p in page1: # 循环打印第 1 页嘉宾的 realname
... p.realname
...
'andy'
'jack'
##########第二页#############
>>> page2 = p.page(2) # 获取第 2 页的数据
>>> page2.start_index() # 本页的第一条数据
3>
>> page2.end_index() # 本页的最后一条数据
4>
>> page2.has_previous() # 是否有上一页
True
>>> page2.has_next() # 是否有下一页
True
>>> page2.previous_page_number() # 上一页是第几页
1>
>> page2.next_page_number() # 下一页是第几页
3>
>>
##########第三页#############
>>> page3 = p.page(3) # 获取第 3 页的数据
>>> page3.has_next() # 是否有下一页
False
>>> page3.has_previous() # 是否有上一页
True
>>> page3.has_other_pages() # 是否有其它页
True
>>> page3.previous_page_number() # 前一页是第几页
2
```
&emsp;&emsp;通过对 Guest 表的练习， 现在已经学会了 Paginator 类的基本操作， 那么下面就来实现分页面吧！<br>
&emsp;&emsp;打开.../sign/views.py 文件， 修改 guest_manage()视图函数。<br>
views.py:<br>
```Python
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})
```
&emsp;&emsp;`paginator = Paginator(guest_list, 2)`<br>
&emsp;&emsp;把查询出来的所有嘉宾列表 guest_list 放到 Paginator 类中， 划分每页显示 2 条数据。<br>
&emsp;&emsp;`page = request.GET.get('page')`<br>
&emsp;&emsp;通过 GET 请求得到当前要显示第几页的数据。<br>
&emsp;&emsp;`contacts = paginator.page(page)`<br>
&emsp;&emsp;获取第 page 页的数据。 如果当前没有页数， 抛 PageNotAnInteger 异常， 返回第一页的数据。 如果超出最
大页数的范围， 抛 EmptyPage 异常， 返回最后一页面的数据。<br>
&emsp;&emsp;最终， 将得到的某一页数据返回到嘉宾管理页面上。<br>
&emsp;&emsp;在`.../templates/guest_manage.html` 页面也需要添加分页器的代码。<br>
guest_manage.html:<br>
```html
<!--列表分页器-->
        <div class="pagination">
            <span class="step-links">
                {% if guests.has_previous %}
                    <a href="?page={{ guests.previous_page_number }}">previous</a>
                {% endif %}
                <span class="current">
                    Page {{ guests.number }} of {{ guests.paginator.num_pages }}.
                </span>
                {% if guests.has_next %}
                    <a href="?page={{ guests.next_page_number }}">next</a>
                {% endif %}
            </span>
        </div>
```
![image](https://github.com/15529343201/guest/blob/chapter5/image/5.4.PNG)<br>
## 5.4 签到功能
### 5.4.1、 添加签到链接
&emsp;&emsp;对于签到功能页面来说， 它应该所属于某一场发布会， 所以， 在打开签到页面之前， 我们应知道这是针
对哪一场发布会的签到。 所以， 最好的方式是在发布列表中， 每一条发布会都提供一个“签到” 链接用来打
开对应的签到页面。<br>
&emsp;&emsp;在`.../templates/event_manage.html` 页面， 增加签到列链接。<br>
event_manage.html:<br>
```html
<!--发布会列表-->
<div class="row" style="padding-top: 80px;">
    <div class="col-md-6">
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>id</th><th>名称</th><th>状态</th><th>地址</th><th>时间</th><th>签到</th>
                </tr>
            </thead>
            <tbody>
                {% for event in events %}
                    <tr>
                        <td>{{ event.id }}</td>
                        <td>{{ event.name }}</td>
                        <td>{{ event.status }}</td>
                        <td>{{ event.address }}</td>
                        <td>{{ event.start_time }}</td>
                        <td><a href="/sign_index/{{ event.id }}/" target="{{ event.id }}_blank">sign</a> </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
```
&emsp;&emsp;当点击 sign 链接时， 路径会默认跳转到“/sign_index/{{ event.id }}/” 路径。 其中{{ event.id }} 为发布会
的 id。 target="{{ event.id }}_blank" 属性表示链接在新窗口打开。<br>
&emsp;&emsp;在`.../guest/urls.py` 文件中添加路径路由。<br>
urls.py:<br>
```Python
from sign import views
urlpatterns = [
......
    url(r'^sign_index/(?P<event_id>[0-9]+)/$', views.sign_index),
]
```
&emsp;&emsp;此处与我们之前添加的路径在匹配方式上略有不同。<br>
&emsp;&emsp;`(?P<event_id>[0-9]+)` 配置二级目录， 发布会 id， 要求必须为数字。而且匹配的数字， 将会作为 sign_index()
视图函数的参数。<br>
### 5.4.2、 签到页面
&emsp;&emsp;打开.../sign/views.py 文件， 创建 sign_index()视图函数。<br>
views.py:<br>
```Python
from django.shortcuts import render, get_object_or_404
# 签到页面
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request,'sign_index.html',{'event':event})
```
&emsp;&emsp;创建.../templates/sign_index.html 签到页面。<br>
sign_index.html:<br>
```html
<!--导航栏-->
<nav class="navbar navbar-inverse navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">{{ event.name }}</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">发布会</a></li>
                <li><a href="/guest_manage/">嘉宾</a></li>
            </ul>
        </div>
    </div>
</nav>

<!--签到功能-->
<div class="page-header" style="padding-top: 80px;">
    <div id="navbar" class="navbar-collapse collapse">
        <form class="navbar-form" method="post" action="/sign_index_action/{{ event.id }}/">
            <div class="form-group">
                <input name="phone" type="text" placeholder="输入手机号" class="form-control"></div>
                <button type="submit" class="btn btn-success">签到</button>
            </div>
        </form>
    </div>
</div>
```
&emsp;&emsp;`<a class="navbar-brand" href="#">{{ event.name }}</a>`<br>
&emsp;&emsp;将页面标题设置为发布会名称。<br>
&emsp;&emsp;`<li><a href="/event_manage/">发布会</a></li>`<br>
&emsp;&emsp;`<li><a href="/guest_manage/">嘉宾</a></li>`<br>
&emsp;&emsp;设置发布会与嘉宾导航链接。<br>
&emsp;&emsp;`<form class="navbar-form" method="post" action="/sign_index_action/{{ event.id }}/">`<br>
&emsp;&emsp;签到表单会通过 POST 请求提交到/sign_index_action/{{ event.id }}/ ， 二级目录会以发布会 id 替换。<br>
&emsp;&emsp;签到页面， 如图 5.5。<br>
![image](https://github.com/15529343201/guest/blob/chapter5/image/5.5.PNG)<br>
### 5.4.3、 签到动作
&emsp;&emsp;继续开发签到功能， 接下来考虑， 当在签到输入框中输入手机号， 点击“签到” 按钮之后， 改动作要如
何处理？<br>
&emsp;&emsp;首先， 打开.../guest/urls.py 文件， 添加签到路径的路由。<br>
urls.py:<br>
```Python
......
from sign import views
urlpatterns = [
......
    url(r'^sign_index_action/(?P<event_id>[0-9]+)/$', views.sign_index_action),
]
```
&emsp;&emsp;打开.../sign/views.py 文件， 创建 sign_index_action()视图函数。<br>
views.py:<br>
```Python
# 签到动作
@login_required
def sign_index_action(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    phone = request.POST.get('phone', '')
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.'})
    result = Guest.objects.filter(phone=phone, event_id=event_id)
    if not result:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': 'event id or phone error.'})
    result = Guest.objects.get(phone=phone, event_id=event_id)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': "user has sign in."})
    else:
        Guest.objects.filter(phone=phone, event_id=event_id).update(sign='1')
    return render(request, 'sign_index.html', {'event': event,
                                               'hint': 'sign in success!',
                                               'guest': result})
```
&emsp;&emsp;对于发布会的签到动作， 做了以下条件的判断。<br>
&emsp;&emsp;首先， 查询 Guest 表判断用户输入的手机号是否存在， 如果不存在将提示用户“手机号为空或不存在” 。<br>
&emsp;&emsp;然后， 通过手机和发布会 id 两个条件来查询 Guest 表， 如果结果为空将提示用户“该用户未参加此次发
布会” 。<br>
&emsp;&emsp;最后， 再通过手机号查询 Guest 表， 判断该手机号的签到状态是否为 1， 如果为 1， 表示已经签过到了，
返回用户“已签到” ， 否则， 将提示用户“签到成功！ ” ， 并返回签到用户的信息。<br>
&emsp;&emsp;修改.../templates/sign_index.html 页面， 增加 sign_index_action()视图函数返回的提示信息的位置。<br>
```html
<!--签到功能-->
<div class="page-header" style="padding-top: 80px;">
    <div id="navbar" class="navbar-collapse collapse">
        <form class="navbar-form" method="post" action="/sign_index_action/{{ event.id }}/">
            <div class="form-group">
                <input name="phone" type="text" placeholder="输入手机号" class="form-control">
            </div>
            <button type="submit" class="btn btn-success">签到</button>
            <font color="red">
                <br>{{ hint }}
                <br>{{ guest.realname }}
                <br>{{ guest.phone }}
            </font>
        </form>
    </div>
</div>
```
&emsp;&emsp;如果签到失败， 将会显示 {{ hint }}提示信息； 如果签到成功， 将会显示{{ hint }}提示信息和用户名称，
及手机号。 如果 5.16。<br>
![image](https://github.com/15529343201/guest/blob/chapter5/image/5.6.PNG)<br>
## 5.5 退出系统
&emsp;&emsp;之前留了一个坑， 在发布会管理页面和嘉宾管理页面的右上角有“退出” 按钮， 但我们一直没实现登录
的退出。 现在是时候该填补上它了。<br>
&emsp;&emsp;打开.../urls.py 文件， 添加退出目录的路由。<br>
urls.py:<br>
```Python
from sign import views
urlpatterns = [
......
    url(r'^logout/$', views.logout),
]
```
&emsp;&emsp;打开.../sign/views.py 文件， 创建 logout()视图函数。<br>
views.py:<br>
```Python
# 退出登录
@login_required
def logout(request):
    auth.logout(request) # 退出登录
    response=HttpResponseRedirect('/index/')
    return response
```
&emsp;&emsp;Django 不单单为我们提供了方便的 auth.login()函数用于登录，还为我们准备了 auth.logout()函数用于系统
的退出， 它可以帮我们清除掉浏览器保存的用户信息， 所以， 我们不用再考虑如何删除浏览器 cookie 等问题
了<br>
# chapter6 Django 测试
## 6.1 unittest framework
&esmp;&emsp;在学习 Django 单元测试之前， 我们先来学习一下 unittest 单元测试框架。 首先， 更新一个误区， 单元测
试框架不单单只适用于程序单元级别的测试。<br>
&esmp;&emsp;一般单元测试框架主要完成以下几件事儿：<br>
&esmp;&emsp;提供用例组织与执行： 当你的测试用例只有几条时， 可以不必考虑用例的组织， 但是， 当测试用例达到
成百上千条时， 大量的测试用例堆砌在一起， 就产生了扩展性与维护性等问题， 需要考虑用例的规范与组织
问题了。 单元测试框架就是用来解决这个问题的。<br>
&esmp;&emsp;提供丰富的比较方法： 不论是功能测试， 还是单元测试， 在用例执行完成之后都需要将实际结果与进行
预期结果的进行比较（断言） ， 从而断定用例是否执行通过。 所以， 作为单元测试框架一般也会提供丰富的
断言方法。 例如， 判断相等/不等、 包含/不包含、 Trure/False 的断言方法等。<br>
&esmp;&emsp;提供丰富的日志： 当测试用例执行失败时能抛出清晰的失败原因， 当所有用例执行完成后能提供丰富的
执行情况结果信息。 例如， 总执行时间、 失败用例数、 成功用例数等。<br>
&esmp;&emsp;从这几点来看， 单元测试框架可以帮助我们完成任何级别测试的自动化。<br>
&esmp;&emsp;单元测试： unittest<br>
&esmp;&emsp;HTTP 接口自动化测试： unittest + Requests<br>
&esmp;&emsp;Web UI 自动化测试： unittest + Selenium<br>
&esmp;&emsp;移动自动化测试： unittest + Appium<br>
&esmp;&emsp;例如， 开发一了个简单的计算器， 用于两个数的加、 减、 乘、 除， 功能代码如下。<br>
count.py:<br>
```
'''
Author:shiyongchao
Date: 2018/5/2
Describe:实现简单计算器:+,-,*,/
'''


class Calculator():
    '''
    实现两个数的加
    '''

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # 加法
    def add(self):
        return self.a + self.b

    # 减法
    def sub(self):
        return self.a - self.b

    # 乘法
    def mul(self):
        return self.a * self.b

    # 除法
    def div(self):
        return self.a / self.b
```
&emsp;&emsp;首先， 需要说明的是， 不用单元测试框架一样可以做单元测试。 使用单元测试框架来做单元测试的优点
是由测试更加规范和简单。 回顾前面关于单元测试框架所完成的几件事。<br>
&emsp;&emsp;那么， 通过 unittest 单元测试框架如何编写测试用例。<br>
test_count.py:<br>
```import unittest
from count import Calculator


class CountTest(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator(8, 4)

    def tearDown(self):
        pass

    def test_add(self):
        result = self.cal.add()
        self.assertEqual(result, 12)

    def test_sub(self):
        result = self.cal.sub()
        self.assertEqual(result, 4)

    def test_mul(self):
        result = self.cal.mul()
        self.assertEqual(result, 32)

    def test_div(self):
        result = self.cal.div()
        self.assertEqual(result, 2)


if __name__ == "__main__":
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(CountTest("test_add"))
    suite.addTest(CountTest("test_sub"))
    suite.addTest(CountTest("test_mul"))
    suite.addTest(CountTest("test_div"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
```
&emsp;&emsp;首先从感官上来看， 通过 unittest 单元测试框架编写测试用例更加规范和整洁。 接下来， 分析一下 unittest单元测试用例。<br>
&emsp;&emsp;首先， 通过 import 导入 unittest 单元测试框架。<br>
&emsp;&emsp;创建 CountTest 类继承 unittest.TestCase 类。<br>
&emsp;&emsp;setUp()和 tearDown()在单元测试框架中比较特别， 它们分别在每一个测试用例的开始和结束执行。setUp()
方法用于测试用例执行前的初始化工作， 例如初始化变量、 生成数据库测试数据、 打开浏览器等。 tearDown()
方法与 setUp()方法相呼应， 用于测试用例执行之后的善后工作， 例如清除数据库测试数据、 关闭文件、 关闭
浏览器等。<br>
&emsp;&emsp;unittest 要求测试方法必须以“test” 开头。 例如， test_add、 test_sub 等。<br>
&emsp;&emsp;接下来， 调用 unittest.TestSuite()类中的 addTest()方法向测试套件中添加测试用例。 简单的可以将测试套
件理解成运行测试用例的集合。<br>
&emsp;&emsp;通过 unittest.TextTestRunner()类中的 run()方法运行测试套件中的测试用例。<br>
&emsp;&emsp;如果想默认运行当前测试文件下的所有测试用例， 可以直接使用 unittest.main()方法。 那么 main()方法在
查找测试用例时按照两个规则。 首先， 该测试类必须继承 unittest.TestCase 类； 其次， 该测试类下面的方法必
须以“test” 开头。<br>
&emsp;&emsp;最后， 执行结果如下：<br>
```
> python3 test_count.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK
```
&emsp;&emsp;从执行结果可以看到通过一个小点“.” 来表示一条运行通过的用例， 总共运行 4 条测试用例， 用时 0.001
秒。<br>
https://docs.python.org/3/library/unittest.html<br>
## 6.2 Testing in Django
&emsp;&emsp;对于 Web 开发人员来说， 自动化测试是一个非常有用的发现 bug 的手段。 您可以使用一个测试集合或一
个测试套件来解决， 或避免一些问题：<br>
&emsp;&emsp;当你编写新的代码， 你可以使用测试来验证你的代码是否按预期工作。<br>
&emsp;&emsp;当你重构或修改旧代码， 你可以使用测试， 以确保您的更改不会影响您的应用程序的行为意外。<br>
&emsp;&emsp;测试一个 Web 应用是一项复杂的任务， 因为在 Web 应用程序是由逻辑几层 - 从 HTTP 的级请求处理，<br>
以形成验证和处理， 以模板渲染。 随着 Django 的测试执行框架和各种实用工具， 可以模拟请求， 插入测试数
据， 检查您的应用程序的输出， 一般检查你的代码是做什么的， 应该做的事情。<br>
&emsp;&emsp;Django 使用的是内置于 Python 标准库中的 unittest 单元测试框架。 您也可以使用任何其他的 Python 测试
框架； Django 提供了一个 API 和工具， 可以融合其它的单元测试框架。<br>
### 6.2.1、 A simple example
&emsp;&emsp;Django 的单元测试使用 Python 标准库模块： unittest。 该模块定义使用基于类的方法测试。 在我们创建
Django 应用时， 默认已经帮我们生成了 tests.py 文件， 打开.../sign/tests.py 文件， 编写测试如下代码：<br>
```Python
from django.test import TestCase
from sign.models import Event, Guest


# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, name="oneplus 3 event", status=True, limit=2000, address='shenzhen',
                             start_time='2016-08-31 02:18:22')
        Guest.objects.create(id=1, event_id=1, realname='alen', phone='13711001101', email='alen@mail.com', sign=False)

    def test_event_models(self):
        result = Event.objects.get(name="oneplus 3 event")

        self.assertEqual(result.address, "shenzhen")
        self.assertTrue(result.status)

    def test_guest_models(self):
        result = Guest.objects.get(phone='13711001101')

        self.assertEqual(result.realname, "alen")
        self.assertFalse(result.sign)
```
&emsp;&emsp;我们以测试发布会和嘉宾模型为例， 如果不清楚该模型的字段和在 Django 中的操作， 请回到本书的第四
章进行学习。<br>
&emsp;&emsp;分析一下测试用例的实现：<br>
&emsp;&emsp;首先， 创建 ModelTest 类， 继承 django.test 的 TestCase 测试类。<br>
&emsp;&emsp;然后， 在 setUp()初始化方法中， 创建一条发布会和嘉宾数据。<br>
&emsp;&emsp;最后， 通过 test_event_models()和 test_guest_models()测试方法， 分别查询两张表的数据， 断言表中的数
据是否正确。<br>
&emsp;&emsp;执行测试用例， 切换到项目的根目录下， 通过 manage.py 所提供的“test” 命令运行测试。<br>
&emsp;&emsp;`D:\pydj\guest>python3 manage.py test`<br>
```
Creating test database for alias 'default'...
..
----------------------------------------------------------------------
Ran 2 tests in 0.216s
OK
Destroying test database for alias 'default'...
```
&emsp;&emsp;Django 在执行 setUp()方法中的数据库初始化时， 并非真正的向数据库表中插入了数据。 所以， 数据库并
不会因为运行测试而产生测试数据。<br>
&emsp;&emsp;当用例执行失败时又是怎样的呢？ 修改用例中的预期结果， 你可以试着把断言结果由"shenzhen"改为
"beijing"， 再次执行测试。<br>
```
D:\pydj\guest>python3 manage.py test
Creating test database for alias 'default'...
F.
======================================================================
FAIL: test_event_models (sign.tests.ModelTest)
----------------------------------------------------------------------
Traceback (most recent call last):
    File "D:\pydj\guest\sign\tests.py", line 15, in test_event_models
        self.assertEqual(result.address, "beijing")
AssertionError: 'shenzhen' != 'beijing'
- shenzhen
+ beijing
----------------------------------------------------------------------
Ran 2 tests in 0.183s
FAILED (failures=1)
Destroying test database for alias 'default'...
```
&emsp;&emsp;从上面的提示信息中， 将会很容易就可以找到错误的原因。<br>
### 6.2.2、 Run test case
&emsp;&emsp;当编写完测试， 最简单的方式是通过 manage.py 中“test” 命令来直接执行所有测试。 但是编写的测试用
例越来越多的时候， 测试运行的情况就复杂起， 比如要指定特定的测试模块， 或测试类， 又或者想执行测试
文件名包含了“test” 的文件。<br>
&emsp;&emsp;通过参数可以控制 Django 项目不同级别的测试。<br>
&emsp;&emsp;运行 sign 应用下的所有测试用例：<br>
```
D:\pydj\guest>python3 manage.py test sign
Creating test database for alias 'default'...
..
----------------------------------------------------------------------
Ran 2 tests in 0.283s
OK
Destroying test database for alias 'default'...
```
&emsp;&emsp;运行 sign 应用下的 tests.py 测试文件：<br>
```
D:\pydj\guest>python3 manage.py test sign.tests
Creating test database for alias 'default'...
..
----------------------------------------------------------------------
Ran 2 tests in 0.308s
OK
Destroying test database for alias 'default'...
```
&emsp;&emsp;运行 sign 应用 tests.py 测试文件下的 ModelTest 测试类：<br>
```
D:\pydj\guest>python3 manage.py test sign.tests.ModelTest
Creating test database for alias 'default'...
..
----------------------------------------------------------------------
Ran 2 tests in 0.304s
OK
Destroying test database for alias 'default'...
```
&emsp;&emsp;下面执行 ModelTest 测试类下面的 test_event_models 测试方法（用例） ：<br>
```
D:\pydj\guest>python3 manage.py test sign.tests.ModelTest.test_event_models
Creating test database for alias 'default'...
.-
---------------------------------------------------------------------
Ran 1 test in 0.226s
OK
Destroying test database for alias 'default'...
```
&emsp;&emsp;除此之外， 我们还可以使用 -p （或 --pattern） 参数模糊匹配测试文件：<br>
```
D:\pydj\guest>python3 manage.py test -p test*.py
Creating test database for alias 'default'...
..
----------------------------------------------------------------------
Ran 2 tests in 0.185s
OK
Destroying test database for alias 'default'...
```
&emsp;&emsp;指定匹配运行的测试文件--->test*.py， 匹配以“test” 开头， 以“.py” 结尾的测试文件。<br>
## 6.3 The test views
&emsp;&emsp;客户端测试是一个 Python 类， 它充当一个虚拟的网络浏览器， 让您测试您的视图层， 并与你的 Django的应用程序编程方式进行交互。<br>
&emsp;&emsp;客户端测试可以做的事情：<br>
 模拟“GET” 和“POST” 请求， 观察响应结果--从 HTTP(headers， status codes)到页面内容.<br>
 检查重定向链(如果有的话)， 在每一步检查 URL 和 status code。<br>
 用一个包括特定值的模板 context 来测试一个 request 被 Django 模板渲染。<br>
&emsp;&emsp;进入 Django Shell 模式 ， 建立测试环境：<br>
```
D:\pydj\guest>python3 manage.py shell
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)]
on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>>
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
```
&emsp;&emsp;setup_test_environment()用测试前的初始化测试环境。<br>
&emsp;&emsp;导入 Client()测试类， 测试登录视图：<br>
```
>>> from django.test import Client
>>> c = Client()
>>> response = c.get('/index/')
>>> response.status_code
200
```
&emsp;&emsp;Client()类提供的 get()和 post()方法可以模式 GET/POST 请求。 通过 get()请求“/index/” 路径， 即为登录
页面， 得到的返回码为 200， 表示成功。<br>
### 6.3.1、 Test Index
&emsp;&emsp;接下来打开.../sign/tests.py 文件， 编写测试用例。<br>
```Python
class IndexPageTest(TestCase):
    '''测试index登录首页'''

    def test_index_page_renders_index_template(self):
        '''测试index视图'''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
```
&emsp;&emsp;client.get()方法从 TestCase 父类继承而来， 用于请求一个路径， assertEqual()服务器对客户端的应答是否
为 200， assertTemplateUsed()断言是否用给定的是 index.html 模版响应。<br>
### 6.3.2、 Test Login action
&emsp;&emsp;继续在.../sign/tests.py 文件中编写登录测试用例。<br>
```Python
class LoginActionTest(TestCase):
    '''测试登录函数'''

    def setUp(self):
        User.objects.create_user('admin', 'admin@mail.com', 'admin123456')
        self.c = Client()

    def test_login_action_username_password_null(self):
        '''用户名密码为空'''
        test_data = {'username': '', 'password': ''}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_username_password_error(self):
        ''' 用户名密码错误 '''
        test_data = {'username': 'abc', 'password': '123'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"username or password error!", response.content)

    def test_login_action_success(self):
        ''' 登录成功 '''
        test_data = {'username': 'admin', 'password': 'admin123456'}
        response = self.c.post('/login_action/', data=test_data)
        self.assertEqual(response.status_code, 302)
```
&emsp;&emsp;在 setUp()初始化方法中， 调用 User.objects.create_user()创建登录用户数据。Client()类提供的 get()和 post()
方法可以模式 GET/POST 请求。<br>
&emsp;&emsp;`“/login_action/” `为用户登录的路径。<br>
&emsp;&emsp;`{'username':'admin','password':'admin123456'} `字典中的内容为用户登录的用户名密码。<br>
&emsp;&emsp;前两条例分别为用户名/密码为空， 和用户名/密码错误。 assertIn()断言在返回的 HTML 中包含“username
or password error!” 提示。<br>
&emsp;&emsp;当用例中输入了正确的用户名和密码（admin/admin123456）， 为什么 HTTP 返回的结果是 302 而不是 200
呢？ 这是因为在 login_action 视图函数中， 当用户登录验证成功后， 通过 HttpResponseRedirect('/event_manage/')
跳转到了发布会管理视图， 这是一个重定向， 所以 HTTP 返回码是 302。<br>
### 6.3.3、 Test Event Manage
&emsp;&emsp;继续在.../sign/tests.py 文件中编写发布会管理的测试用例。<br>
```Python
class EventManageTest(TestCase):
    ''' 发布会管理 '''

    def setUp(self):
        Event.objects.create(id=2, name='xiaomi5', limit=2000, status=True, address='beijing',
                             start_time=datetime(2016, 8, 10, 14, 0, 0))
        self.c = Client()

    def test_event_manage_success(self):
        ''' 测试发布会:xiaomi5 '''
        response = self.c.post('/event_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)

    def test_event_manage_search_success(self):
        ''' 测试发布会搜索 '''
        response = self.c.post('/search_name/', {"name": "xiaomi5"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"xiaomi5", response.content)
        self.assertIn(b"beijing", response.content)
```
&emsp;&emsp;关于发布会管理的测试代码与登录视图相同， 这里不再解释。<br>
&emsp;&emsp;此 用 例 要 想 运 行 通 过 ， 需 要 在 views.py 视 图 文 件 中 将 event_manage() 和 search_name() 函 数 的
@login_required 装饰器去掉， 因为这两个函数依赖于登录， 然而， Client()所提供的 get()和 post()方法并没有验
证登录的参数。<br>
### 6.3.4、 Test Guest Manage
&emsp;&emsp;继续在.../sign/tests.py 文件中编写嘉宾管理的测试用例。<br>
```Python
class GuestManageTest(TestCase):
    ''' 嘉宾管理 '''

    def setUp(self):
        Event.objects.create(id=1, name="xiaomi5", limit=2000,
                             address='beijing', status=1, start_time=datetime(2016, 8, 10, 14, 0, 0))
        Guest.objects.create(realname="alen", phone=18611001100,
                             email='alen@mail.com', sign=0, event_id=1)
        self.c = Client()

    def test_event_manage_success(self):
        ''' 测试嘉宾信息: alen '''
        response = self.c.post('/guest_manage/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"18611001100", response.content)

    def test_guest_manage_search_success(self):
        ''' 测试嘉宾搜索 '''
        response = self.c.post('/search_phone/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"alen", response.content)
        self.assertIn(b"18611001100", response.content)
```
&emsp;&emsp;关于嘉宾管理的用例要想运行通过， 需要在 views.py 视图文件中将 guest_manage()和 search_phone()函数
的@login_required 装饰器去掉， 原因同上。<br>
### 6.3.5、 Test User Sign
&emsp;&emsp;继续在.../sign/tests.py 文件中编写用户签到的测试用例。<br>
```Python
class SignIndexActionTest(TestCase):
    ''' 发布会签到 '''

    def setUp(self):
        Event.objects.create(id=1, name="xiaomi5", limit=2000, address='beijing', status=1,
                             start_time='2017-8-10 12:30:00')
        Event.objects.create(id=2, name="oneplus4", limit=2000, address='shenzhen', status=1,
                             start_time='2017-6-10 12:30:00')
        Guest.objects.create(realname="alen", phone=18611001100, email='alen@mail.com', sign=0, event_id=1)
        Guest.objects.create(realname="una", phone=18611001101, email='una@mail.com', sign=1, event_id=2)
        self.c = Client()

    def test_sign_index_action_phone_null(self):
        ''' 手机号为空 '''
        response = self.c.post('/sign_index_action/1/', {"phone": ""})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"phone error.", response.content)

    def test_sign_index_action_phone_or_event_id_error(self):
        ''' 手机号或发布会 id 错误 '''
        response = self.c.post('/sign_index_action/2/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"event id or phone error.", response.content)

    def test_sign_index_action_user_sign_has(self):
        ''' 用户已签到 '''
        response = self.c.post('/sign_index_action/2/', {"phone": "18611001101"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"user has sign in.", response.content)

    def test_sign_index_action_sign_success(self):
        ''' 签到成功 '''
        response = self.c.post('/sign_index_action/1/', {"phone": "18611001100"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"sign in success!", response.content)
```
&emsp;&emsp;首先用例要想运行通过， 需要在 views.py 视图文件中将 sign_index_action()函数的@login_required 装饰器
去掉， 原因同上。<br>
&emsp;&emsp;其次， 关于签到功能， 测试的情况比较多， 所以在 setUp()中创建测试数据需要注意。 创建了两条发布会
“xiaomi5” 和“oneplus4” ， 嘉宾“alen” 所属于“xiaomi5” ， 嘉宾“una” 所属于“oneplus4” ， 并且“una”
的签到状态为已签到。<br>
&emsp;&emsp;当通过“alen”的手机号（18611001100）在“oneplus4”发布会页面签到时会， 将会提示：“event id or phone
error.” 发布会 id 与手机号不匹配。<br>
&emsp;&emsp;当通过“una” 手机号签到时， 将会提示： “user has sign in.” 用户已签到。<br>
&emsp;&emsp;另外两条用例相对比较好理解， 这里不再解释。<br>
&emsp;&emsp;关于 Django 测试讨论到此为止， 参考 Django 官方文档。<br>
&emsp;&emsp;https://docs.djangoproject.com/en/1.9/topics/testing/tools/<br>
# chapter7 接口相关概念
## 7.1 分层的自动化测试
&emsp;&emsp;测试金字塔的概念由敏捷大师 Mike Cohn 在他的《Succeeding with Agile》 一书中首次提出， 如图7.1所示。
他的基本观点是： 我们应该有更多的低级别的单元测试， 而不仅仅是通过用户界面运行高层的端到端的测试。<br>
![image](https://github.com/15529343201/guest/blob/chapter7/image/7.1.PNG)<br>
&emsp;&emsp;Martin Fowler 大师在测试金字塔模型的基础上提出分层自动化测试的概念。 在自动化测试之前加了一个
“分层” 的修饰， 用来区别于“传统的” 自动化测试。 那么什么是传统的自动化测试？ 为何要提倡分层自动
化测试的思想呢？<br>
&emsp;&emsp;所谓传统的自动化测试我们可以理解为基于产品 UI 层的自动化测试， 它是将黑盒功能测试转化为由程序
或工具执行的一种自动化测试。<br>
&emsp;&emsp;在目前的大多数研发组织当中， 都存在开发与测试团队割裂（部门墙） 、 质量职责错配（测试主要对质
量负责） 的问题， 在这种状态下， 测试团队的一个“正常” 反应就是试图在测试团队能够掌控的黑盒测试环
节进行尽可能全面的覆盖， 甚至是尽可能全面的 UI 自动化测试。<br>
&emsp;&emsp;这可能会导致两个恶果： 一是测试团队规模的急剧膨胀； 二是所谓的全面 UI 自动化测试运动。 因为 UI
是非常易变的， 所以 UI 自动化测试维护成本相对高昂。<br>
&emsp;&emsp;分层自动化测试倡导的是从黑盒（UI） 单层到黑白盒多层的自动化测试体系， 从全面黑盒自动化测试到
对系统的不同层次进行自动化测试， 如图7.2所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter7/image/7.2.PNG)<br>
&emsp;&emsp;我在《Selenium2自动化测试实战---基本 Python 语言》 一书中第一章也曾对分层自动化测试的概念进行
了介绍， 这本书通过对 Selenium 的讲解全面展示了 Web UI 层自动化测试的应用。 那么本书写作的出发点同样
遵循分层自动化测试的思想， 将自动化测试技术延伸到 Service 层， 关注 Web 接口的开发与自动化测试。<br>
## 7.2 单元测试与模块测试
&emsp;&emsp;不管读者是软件开发人员还是软件测试人员， 相信对这两个概念都不陌生。 但是， 当我试图要描述这两
个概念时， 发现却很难描述清楚， 因为在前面开发的 Web 项目中， 并不能直接找到与之对应的概念。 在开发
的 Web 项目中只有项目目录、 程序文件、 函数、 类和方法。 并没有“单元” ， 也没有“模块” 。<br>
&emsp;&emsp;我试图在网上找到了一些关于这两个概念的大多数人认同的定义， 来看看它们有何区别。<br>
&emsp;&emsp;单元测试（Unit testing）<br>
&emsp;&emsp;In computer programming, unit testing is a software testing method by which individual units
of source code, sets of one or more computer program modules together with associated control data, usage
procedures, and operating procedures, are tested to determine whether they are fit for use.<br>
&emsp;&emsp;Intuitively, one can view a unit as the smallest testable part of an application. In procedural programming,
a unit could be an entire module, but it is more commonly an individual function or procedure.
In object-oriented programming, a unit is often an entire interface, such as a class, but could be an individual
method. Unit tests are short code fragments created by programmers or occasionally by white box
testers during the development process. It forms the basis for component testing。<br>
&emsp;&emsp;---引用《维基百科》<br>
&emsp;&emsp;通过这段定义， 我们读到几个关于单元测试的描述：<br>
&emsp;&emsp;1、 单元测试是应用程序的最小可测试部分。<br>
&emsp;&emsp;2、 在面向过程编程中， 单元也可以是整个模块， 但常见的是单个函数或过程。<br>
&emsp;&emsp;3、 在面向对象编程中， 单元通常是整个接口， 例如类， 但可以是单独的方法。<br>
&emsp;&emsp;4、 单元测试多数情况下是由程序员自己完成的。<br>
&emsp;&emsp;模块测试（Module testing）<br>
&emsp;&emsp;大多时候， 我们认为单元测试与模块测试是一样的。 我在国外某网站找到另段关于模块测试的定义。<br>
&emsp;&emsp;A library may be composed of a single compiled object or several compiled objects. There is only a slight
difference between unit testing and module testing. Modules are fully formed chunks of coherent source code
that can typically be tested by driving a few function signatures with various stimuli. On the other hand, unit
testing (which is considered as part of the implementation phase for this software development process) may
involve testing one small part of a function that will never formally implement any function interface.<br>
&emsp;&emsp;---引用国外某大学网站<br>
&emsp;&emsp;通过这一段定义， 我们读到了几个模块测试的解释：<br>
&emsp;&emsp;1、 首先， 这段定义认为模块测试与单元测试有细微的区别。<br>
&emsp;&emsp;2、 模块测试是针对具有明显的功能特征的代码块进行的测试。<br>
&emsp;&emsp;3、 并且， 它认为单元测试可能只涉及测试一小部分的功能。<br>
&emsp;&emsp;4、 模块测试多数情况下由其它程序员或测试人员进行。 （嗯， 这一条是自己加的。 ）<br>
&emsp;&emsp;通过对单元测试和模块测试的概念的分析， 读者是否对这两个概念有了更清晰的认识。 其实， 我们可以
认为是同一个事物用不同的两个角度去解释。 单元测试更强调的是程序的最小可测试单元； 而且模块测试更
强调所测试程序的功能完整性。<br>
&emsp;&emsp;模块接口测试： 对于这个叫法并没有找到规范的概念， 它更多的只是一个口头概念。 其实它就是模块测
试， 加上“接口” 两个字， 更强调了被测试的模块有规范的输入和输出。 因为这是一个可测试的模块最显著
的特征之一。<br>
## 7.3 接口测试
&emsp;&emsp;关于接口的概念， 这里就不再引用一些资料中的定义了。 我根据自己的理解和认识大致把接口分为两类：
程序接口和协议接口。<br>
&emsp;&emsp;关于程序接口， 也可以看作是程序模块接口， 具体到程序中一般就是提供了输入输出的类、 方法或函数。
对于程序接口的测试， 一般需要使用与开发程序接口相同的编程语言， 通过不同的传入不同的参数， 来验证
程序接口的功能。<br>
&emsp;&emsp;关于协议接口， 一般指系统通过不同的协议来提供的接口， 例如 HTTP/SOAP 协议等。 这种类型接口对
底层代码做了封装， 通过协议的方式对外提供调用。 因为不涉及到程序层面， 所以， 不受编程语言的限制；
我们可以通过其它编程语言或工具对其进行测试。 那么本书的重点也是对这类接口的测试。<br>
### 7.3.1 接口的分类
&emsp;&emsp;接口的大体分为以下三类：<br>
- 系统与系统之间的接口

![image](https://github.com/15529343201/guest/blob/chapter7/image/7.3.PNG)<br>
&emsp;&emsp;系统与系统之间的接口， 这里可以是公司内部不同系统之间的接口调用， 也可以不同公司之间系统接口
的调用。 对于前者来说， 笔者所测试 MAC 平台就是一个对公司内部提供接口的系统。 例如用户接口、 抽奖接
口、 图片相册接口等。 而对于公司的其它系统， 如社区网站和微信活动可以调用这些接口快速的实现相应的
功能。 而对于后者来说， 如微信， 微博所提供的第三方登录接口， 如果你开发的系统不想自建用户体系， 完
全可以调用这些接口来实现用户的登录。<br>
- 下层服务对上层服务的接口

![image](https://github.com/15529343201/guest/blob/chapter7/image/7.4.PNG)<br>
&emsp;&emsp;应用层， 从认知上你可以看成是系统所提供的 UI 层功能。 对于 Web 系统来说， 你可以认为是浏览器页面
上所提供的功能， 登录、 注册、 查询、 删除等。<br>
&emsp;&emsp;Service 层， 可以理解为服务器所提供数据和逻辑的处理。<br>
&emsp;&emsp;DB 层， (Data Base) 数据库主要用来存放数据， 例如用户的个人信息， 商品的信息等。<br>
&emsp;&emsp;访问对象， 它是一个面向对象的数据库访问接口。<br>
&emsp;&emsp;举例来说明各层的工作过程， 首先是 Service 提供了一个查询接口， 这个接口需要一个参数（查询的关键
字） ； 然后应用层提供了一个输入框， 需要用户输入查询关键字， 并且还提供了一个查询按钮用于提交查询
的关键字。 当用户输入查询关键字并点击提交按钮后， 相当于调用的查询接口， 查询接口需要对用户提交的
关键字做出相应的判断， 是否为空？ 然后， 通过 DAO 层调用数据库， 根据关键字查询表中的数据， 最后， 再
将拿到的数据返回给应用层， 应用层负责将数据展示到 Web 页面上。<br>
&emsp;&emsp;在这个过程中， 各层之间的交互就是通过接口， 应用层与 Service 主要通过 HTTP 接口。 Service 层与 DB
层主要通过 DAO（Data Access Object） 数据库访问接口， 对于 Python 与 MySQL 之间的调用， 本书第四章中
PyMySQL 驱动就扮演着这样的角色。<br>
- 系统内， 服务与服务之间的调用

![image](https://github.com/15529343201/guest/blob/chapter7/image/7.5.PNG)<br>
&emsp;&emsp;系统内部， 服务与服务之间的调用， 大多情况下是程序之间的调用。<br>
&emsp;&emsp;继续举例， 假设系统开发一个用户查询接口， 输入用户名， 返回用户信息（性别、 年龄、 手机号、 邮箱
地址等） ， 如果用户不存在则返回 null； 现在需要新开发一个用户抽奖的接口， 该接口需要用户名和抽奖动 id，
抽奖接口得到用户名后可以调用用户查询接口， 如果用户查询接口返回 null， 那么抽奖接口就可以直接返回用
户不存在了。 在这个例子中， 用户抽奖接口就调用的用户查询接口。<br>
&emsp;&emsp;那么这里的用户查询接口和抽奖接口本质上就是程序开发的函数或类方法， 提供入参与返回值。<br>
### 7.3.2 接口测试的意义
&emsp;&emsp;根据分层自动化测试中的定义， 最底层由开发人员编写的单元测试保证代码质量， 最上层由功能测试人
员手工+UI 自动化进行大量的功能测试保证功能的可用。 那么进行接口测试的意义是什么？<br>
&emsp;&emsp;更早的发现问题<br>
&emsp;&emsp;不少的测试资料中强调， 测试应该更早的介入到项目开发中， 因为越早的发现 bug， 修复的成本越低。
然而功能测试必须要等到系统提供可测试的界面才能对系统进行测试。 而接口测试可以功能界面开发出来之
前对系统进行测试。 系统接口是上层功能的基础， 接口测试可以更早更低成本的发现和解决问题。<br>
&emsp;&emsp;然而， 在实际的开发过程中， 开发人员并没有充足的时间去编写单元测试， 并且他们往往对自己编写的
代码有足够的信心， 不愿意将“浪费” 时间在编写单元测试上面。 这个时候接口测试的作用就会变得更加重
要。<br>
&emsp;&emsp;缩短产品研发周期：<br>
&emsp;&emsp;对于产品研发周期来说， 如果将所有测试工作都集中在功能测试阶段。 那么测试的问题和修复周期就会
变长。 因为测试可以更早的介入产品开发中， 所以， 可以有效的控制功能阶段 bug 的数量； 从而有效的缩短
产品开发周期。<br>
&emsp;&emsp;发现更底层的问题：<br>
&emsp;&emsp;系统的有些底层逻辑是在 UI 功能测试中不太容易触发的， 那么这些逻辑可能会存在问题。 接口测试可以
更容易更全面的测试到这些底层的逻辑。<br>
&emsp;&emsp;检查服务器的异常处理能力：<br>
&emsp;&emsp;我们通常把前端的验证称为弱验证， 因为它很容易被绕过， 这个时候如果只站在功能的层面进行测试，
就很难发现一些安全的问题。 不以功能为入口的接口测试就会很容易的验证这些异常情况。<br>
## 7.4 编程语言中的 Interface
&emsp;&emsp;在大多面向对象的编程语言中都提供了 Interface（接口） 的概念。 既然本章要介绍接口的概念， 那么这
里简单介绍一下面向对象编程语言中的 Interface。<br>
### 7.4.1、 Java 中的 Interface
&emsp;&emsp;在 Java 中定义接口使用 interface 关键字来声明， 可以看做是一种特殊的抽象类， 可以指定一个类必须做
什么， 而不是规定它如何去做。<br>
&emsp;&emsp;为什么使用 Interface？<br>
&emsp;&emsp;在大型项目开发中， 可能需要从继承链的中间插入一个类， 让它的子类具备某些功能而不影响它们的父
类。 例如 A -> B -> C -> D -> E（“->” 表示继承关系） ， A 是祖先类， 如果需要为 C、 D、 E 类添加某些通
用的功能， 最简单的方法是让 C 类再继承另外一个类。 但是问题来了， Java 是一种单继承的语言， 不能再让
C 继承另外一个父类了， 只到移动到继承链的最顶端， 让 A 再继承一个父类。 这样一来， 对 C、 D、 E 类的修
改， 影响到了整个继承链， 不具备可插入性的设计。<br>
&emsp;&emsp;接口是可插入性的保证。 在一个继承链中的任何一个类都可以实现一个接口， 这个接口会影响到此类的
所有子类， 但不会影响到此类的任何父类。 此类将不得不实现这个接口所规定的方法， 而子类可以从此类自
动继承这些方法， 这时候， 这些子类具有了可插入性。<br>
&emsp;&emsp;我们关心的不是哪一个具体的类， 而是这个类是否实现了我们需要的接口。<br>
&emsp;&emsp;接口提供了关联以及方法调用上的可插入性， 软件系统的规模越大， 生命周期越长， 接口使得软件系统
的灵活性、 可扩展性和可插入性方面得到保证。<br>
&emsp;&emsp;接口在面向对象的 Java 程序设计中占有举足轻重的地位。 事实上在设计阶段最重要的任务之一就是设
计出各部分的接口， 然后通过接口的组合， 形成程序的基本框架结构。<br>
&emsp;&emsp;所以简单总结其用途为： 实现类的多继承， 以解决 Java 只能单继承， 不支持多继承的问题。<br>
&emsp;&emsp;下面通过例子介绍 Java 中接口的使用。<br>
&emsp;&emsp;定义接口：<br>
IAnimal.java:<br>
```Java
package mypor.interfaces.demo;
public interface IAnimal {
    public String Behavior(); //行为方法， 描述各种动物的特性
}
```
&emsp;&emsp;实现接口（一） ：<br>
Dog.java:<br>
```Java
package mypor.interfaces.demo;
import mypor.interfaces.demo.IAnimal;
//类: 狗
public class Dog implements IAnimal{
    public String Behavior()
    {
        String ActiveTime = "我晚上睡觉,白天活动";
        return ActiveTime;
    }
}
```
&emsp;&emsp;实现接口（二） ：<br>
Cat.java:<br>
```Java
package mypor.interfaces.demo;
import mypor.interfaces.demo.IAnimal;
//类： 猫
public class Cat implements IAnimal{
    public String Behavior()
    {
        String ActiveTime = "我白天睡觉,晚上捉老鼠。 ";
        return ActiveTime;
    }
}
```
&emsp;&emsp;测试接口的实现：<br>
Test.java:<br>
```Java
package mypor.interfaces.demo;
import mypor.interfaces.demo.Dog;
import mypor.interfaces.demo.Cat;
public class Test {
    public static void main(String[] args) {
    //调用 dog 和 cat 的行为
    Dog d = new Dog();
    Cat c = new Cat();
    System.out.println(d.Behavior());
    System.out.println(c.Behavior());
    }
}
```
&emsp;&emsp;注意， 这里的测试， 并不是测试的接口， 因为接口本身只是抽象的定义， 并没有可测试性， 这里真正所
测试的是继承了接口的类， 或者叫已经实例化的对象。<br>
### 7.4.2、 Python 中的 Zope.interface
&emsp;&emsp;那么读者要问了， 在 Python 编程语言中是否有 Interface 的概念， 然而 Python 本身并不提供 Interface
的创建和使用， 但是我们可以通过第三方扩展库来使用类似 Interface 的概念， 这里选用 Zope.interface 库。<br>
&emsp;&emsp;下载地址： https://pypi.python.org/pypi/zope.interface<br>
&emsp;&emsp;先来看个普通的例子。<br>
demo.py:<br>
```Python
class Host(object):
    def goodmorning(self, name):
        """Say good morning to guests"""
        return "Good morning, %s!" % name
if __name__ == '__main__':
    h = Host()
    hi = h.goodmorning('zhangsan')
    print(hi)
```
&emsp;&emsp;下面在这个例子的基础中使用 Interface（Python3） 。<br>
interface_demo.py:<br>
```Python
from zope.interface import Interface
from zope.interface.declarations import implementer
# 定义接口
class IHost(Interface):
    def goodmorning(self,host):
    """Say good morning to host"""

@implementer(IHost) #继承接口
class Host:
    def goodmorning(self, guest):
        """Say good morning to guest"""
        return "Good morning, %s!" % guest
if __name__ == '__main__':
    p = Host()
    hi = p.goodmorning('Tom')
    print(hi)
```
# chapter8 开发 Web 接口
&emsp;&emsp;前端和后端分离是近年来 Web 应用开发的一个发展趋势。 这种模式将带来以下优势：<br>
&emsp;&emsp;1、 后端可以不用必须精通前端技术（HTML/JavaScript/CSS） ， 只专注于数据的处理， 对外提供 API 接口。<br>
&emsp;&emsp;2、 前端的专业性越来越高， 通过 API 接口获取数据， 从而专注于页面的设计。<br>
&emsp;&emsp;3、 前后端分离增加接口的应用范围， 开发的接口可以应用到 Web 页面上， 也可以应用到移动 APP 上。<br>
&emsp;&emsp;简单介绍了前后端分离的好处， 相信读者应该已经明白了为什么开发接口以及开发的接口主要给谁来用。
那么， 在这种开发模式下， 那么接口测试工作就会变得尤为重要。<br>
## 8.1 HTTP 协议与 JSON
&emsp;&emsp;在正确开发 Web 接口之前先来简单介绍一下 HTTP 协议和 Json 数据格式。 在当前 Web 接口开发中应用
最普遍的就是 HTTP 协议， 而 Json 是目前非常流行接口数据传输格式之一。<br>
### 8.1.1、 HTTP 协议
&emsp;&emsp;超文本传输协议（HTTP， HyperText Transfer Protocol)是互联网上应用最为广泛的一种网络协议。<br>
&emsp;&emsp;HTTP 协议的主要特点可概括如下：<br>
&emsp;&emsp;1、 支持客户/服务器模式。<br>
&emsp;&emsp;简单快速： 客户向服务器请求服务时， 只需传送请求方法和路径。 请求方法常用的有 GET、 POST。 每种
方法规定了客户与服务器联系的类型不同。 由于 HTTP 协议简单， 使得 HTTP 服务器的程序规模小， 因而通
信速度很快。<br>
&emsp;&emsp;2.灵活： HTTP 允许传输任意类型的数据对象。 正在传输的类型由 Content-Type 加以标记。<br>
&emsp;&emsp;3.无连接： 无连接的含义是限制每次连接只处理一个请求。 服务器处理完客户的请求， 并收到客户的应
答后， 即断开连接。 采用这种方式可以节省传输时间。<br>
&emsp;&emsp;4.无状态： HTTP 协议是无状态协议。 无状态是指协议对于事务处理没有记忆能力。 缺少状态意味着如果
后续处理需要前面的信息， 则它必须重传， 这样可能导致每次连接传送的数据量增大。 另一方面， 在服务器
不需要先前信息时它的应答就较快。<br>
&emsp;&emsp;HTTP 请求类型：<br>
&emsp;&emsp;请求行以一个方法符号开头， 以空格分开， 后面跟着请求的 URI 和协议的版本， 格式如下： Method
Request-URI HTTP-Version CRLF<br>
&emsp;&emsp;其中 Method 表示请求方法； Request-URI 是一个统一资源标识符； HTTP-Version 表示请求的 HTTP
协议版本； CRLF 表示回车和换行（除了作为结尾的 CRLF 外， 不允许出现单独的 CR 或 LF 字符） 。<br>
&emsp;&emsp;请求方法（所有方法全为大写） 有多种， 各个方法的解释如下：<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.1.PNG)<br>
&emsp;&emsp;响应状态码：<br>
&emsp;&emsp;状态代码有三位数字组成， 第一个数字定义了响应的类别， 且有五种可能取值：<br>
&emsp;&emsp;1xx： 指示信息--表示请求已接收， 继续处理<br>
&emsp;&emsp;2xx： 成功--表示请求已被成功接收、 理解、 接受<br>
&emsp;&emsp;3xx： 重定向--要完成请求必须进行更进一步的操作<br>
&emsp;&emsp;4xx： 客户端错误--请求有语法错误或请求无法实现<br>
&emsp;&emsp;5xx： 服务器端错误--服务器未能实现合法的请求<br>
&emsp;&emsp;常见状态代码、 状态说明：<br>
&emsp;&emsp;200 OK //客户端请求成功<br>
&emsp;&emsp;400 Bad Request //客户端请求有语法错误， 不能被服务器所理解<br>
&emsp;&emsp;401 Unauthorized //请求未经授权， 这个状态代码必须和 WWW-Authenticate 报头域一起使用<br>
&emsp;&emsp;403 Forbidden //服务器收到请求， 但是拒绝提供服务<br>
&emsp;&emsp;404 Not Found //请求资源不存在， eg： 输入了错误的 URL<br>
&emsp;&emsp;500 Internal Server Error //服务器发生不可预期的错误<br>
&emsp;&emsp;503 Server Unavailable //服务器当前不能处理客户端的请求， 一段时间后可能恢复正常<br>
&emsp;&emsp;请求头信息与响应头信息：<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.2.PNG)<br>
&emsp;&emsp;1、 请求头信息<br>
&emsp;&emsp;请求报头允许客户端向服务器端传递请求的附加信息以及客户端自身的信息。<br>
&emsp;&emsp;常用的请求报头：<br>
&emsp;&emsp;Accept： 请求报头域用于指定客户端接受哪些类型的信息。 eg： Accept： image/gif， 表明客户端希望接
受 GIF 图象格式的资源； Accept： text/html， 表明客户端希望接受 html 文本。<br>
&emsp;&emsp;Accept-Encoding： 请求报头域类似于 Accept， 但是它是用于指定可接受的内容编码。<br>
&emsp;&emsp;Accept-Language： 请求报头域类似于 Accept， 但是它是用于指定一种自然语言。<br>
&emsp;&emsp;Connection： 允许发送指定连接的选项。 例如指定连接是连续， 或者指定“close” 选项， 通知服务器，
在响应完成后， 关闭连接。 从 HTTP/1.1 起， 默认都开启了 Keep-Alive， 保持连接特性。<br>
&emsp;&emsp;Host（发送请求时， 该报头域是必需的） ， Host 请求报头域主要用于指定被请求资源的 Internet 主机和
端口号， 它通常从 HTTP URL 中提取出来的。<br>
&emsp;&emsp;User-Agent： 请求报头域允许客户端将它的操作系统、 浏览器和其它属性告诉服务器。 不过， 这个报头
域不是必需的， 如果我们自己编写一个浏览器， 不使用 User-Agent 请求报头域， 那么服务器端就无法得知我
们的信息了。<br>
&emsp;&emsp;2、 响应头信息<br>
&emsp;&emsp;响应报头允许服务器传递不能放在状态行中的附加响应信息， 以及关于服务器的信息和对 Request-URI
所标识的资源进行下一步访问的信息。<br>
&emsp;&emsp;常用的响应报头<br>
&emsp;&emsp;Location： 响应报头域用于重定向接受者到一个新的位置。 Location 响应报头域常用在更换域名的时候。<br>
&emsp;&emsp;Server： 响应报头域包含了服务器用来处理请求的软件信息。 与 User-Agent 请求报头域是相对应的。<br>
&emsp;&emsp;WWW-Authenticate： 响应报头域必须被包含在 401（未授权的） 响应消息中， 客户端收到 401 响应消
息时候， 并发送 Authorization 报头域请求服务器对其进行验证时， 服务端响应报头就包含该报头域。<br>
&emsp;&emsp;X-Frame-Options: 有三个值： DENY 表示该页面不允许在 frame 中展示， 即便是在相同域名的页面
中嵌套也不允许。 SAMEORIGIN 表示该页面可以在相同域名页面的 frame 中展示。 ALLOW-FROM uri 表示
该页面可以在指定来源的 frame 中展示。<br>
### 8.1.2、 JSON
&emsp;&emsp;什么是 JSON？<br>
- JSON 指的是 JavaScript 对象表示法（JavaScript Object Notation）
- JSON 是轻量级的文本数据交换格式
- JSON 独立于语言 *
- JSON 具有自我描述性， 更易理解
- JSON 使用 JavaScript 语法来描述数据对象， 但是 JSON 仍然独立于语言和平台。JSON 解析器和 JSON
库支持不同的编程语言。

&emsp;&emsp;JSON 数据格式<br>
```
{
    "employees": [
        { "firstName":"Bill" , "lastName":"Gates" },
        { "firstName":"George" , "lastName":"Bush" },
        { "firstName":"Thomas" , "lastName":"Carter" }
    ]
}
```
&emsp;&emsp;JSON 语法是 JavaScript 对象表示法语法的子集。<br>
- 数据在名称/值对中。
- 数据由逗号分隔。
- 花括号保存对象。
- 方括号保存数组。

## 8.2 什么是 Web 接口
&emsp;&emsp;什么是 Web 接口？ 在解释这个问题之前， 先来通过浏览器前端工具（Firebug） 捕捉一下发布会管理页
面的请求。<br>
&emsp;&emsp;发布会管理页面： http://127.0.0.1:8000/event_manage/<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.3.PNG)<br>
&emsp;&emsp;当我们通过 F5 刷新页面时， 服务器返回图 8.5 的资源， 其中包含了 HTML、 CSS 和 JavaScript， 除此
之外， 服务器还可以返回图片、 视频、 字体和插件等类型的资源。<br>
&emsp;&emsp;虽然这些资源的传输使用的是 HTTP 协议， 但我们不能将其看作为 Web 接口。 然而接口关心的是只数
据， 它的输入和输出是具有一定格式的数据， 接口并不关心数据展示在哪里， 要以什么样式去展示。 而 HTML、
CSS、 和 JavaScript 等关心的是数据展示在哪里， 如何展示。<br>
&emsp;&emsp;一般 Web 接口返回数据如图 8.6。<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.4.PNG)<br>
&emsp;&emsp;显然， 这样的接口并不是直接给普通用户来使用的， 它一般为其它开者提供调用。 后端与前端开发之间，
不同系统的开发之间， 以及不同公司的开发之间的调用。 至于调用接口数据的开发者如何使用这些数据， 对
于接口开发者来说并不需要关心。<br>
## 8.3 开发系统的 Web 接口
&emsp;&emsp;了解的什么是 Web 接口， 以及它的作用。 那么接下来就针对发布会签到系统来开发 Web 接口。<br>
### 8.3.1、 发布会添加接口
&emsp;&emsp;首先， 单独创建.../sign/views_if.py 文件， 开发添加发布会接口。<br>
views_if.py:<br>
```Python
from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError


# 添加发布会接口
def add_event(request):
    eid = request.POST.get('eid', '')  # 发布会 id
    name = request.POST.get('name', '')  # 发布会标题
    limit = request.POST.get('limit', '')  # 限制人数
    status = request.POST.get('status', '')  # 状态
    address = request.POST.get('address', '')  # 地址
    start_time = request.POST.get('start_time', '')  # 发布会时间
    if eid == '' or name == '' or limit == '' or address == '' or start_time == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status': 10022, 'message': 'event id already exists'})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status': 10023, 'message': 'event name already exists'})
    if status == '':
        status = 1
    try:
        Event.objects.create(id=eid, name=name, limit=limit, address=address, status=int(status), start_time=start_time)
    except ValidationError as e:
        error = 'start_time format error. It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status': 10024, 'message': error})
    return JsonResponse({'status': 200, 'message': 'add event success'})
```
&emsp;&emsp;通过 POST 请求接收发布会参数： 发布会 id、 标题、 人数、 状态、 地址和时间等参数。<br>
&emsp;&emsp;首先， 判断 eid、 name、 limit、 address、 start_time 等字段均不能为空， 否则 JsonResponse()返回相应的
状态码和提示。 JsonResponse()是一个非常有用的方法， 它可以直接将字典转化成 Json 格式返回到客户端。<br>
&emsp;&emsp;接下来， 判断发布会 id 是否存在， 以及发布会名称（name） 是否存在； 如果存在将返回相应的状态码和
提示信息。<br>
&emsp;&emsp;再接下来， 判断发布会状态是否为空， 如果为空， 将状态设置为 1（True） 。<br>
&emsp;&emsp;最后， 将数据插入到 Event 表， 在插入的过程中如果日期格式错误， 将抛出 ValidationError 异常， 接收
该异常并返回相应的状态和提示， 否则， 插入成功， 返回状态码 200 和“add event success” 的提示。<br>
### 8.3.2、 发布会查询接口
&emsp;&emsp;打开.../sign/views_if.py 文件， 添加发布会查询接口。<br>
```Python
from django.core.exceptions import ValidationError, ObjectDoesNotExist
# 发布会查询
def get_event_list(request):
    eid = request.GET.get("eid", "")  # 发布会 id
    name = request.GET.get("name", "")  # 发布会名称
    if eid == '' and name == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    if eid != '':
        event = {}
        try:
            result = Event.objects.get(id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            event['name'] = result.name
            event['limit'] = result.limit
            event['status'] = result.status
            event['address'] = result.address
            event['start_time'] = result.start_time
            return JsonResponse({'status': 200, 'message': 'success', 'data': event})
    if name != '':
        datas = []
        results = Event.objects.filter(name__contains=name)
        if results:
            for r in results:
                event = {}
                event['name'] = r.name
                event['limit'] = r.limit
                event['status'] = r.status
                event['address'] = r.address
                event['start_time'] = r.start_time
                datas.append(event)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
```
&emsp;&emsp;通过 GET 请求接收发布会 id 和 name 参数。 两个参数都是可选的。 首先， 判断当两个参数同时为空， 接
口返回状态码 10021， 参数错误。<br>
&emsp;&emsp;如果发布会 id 不为空， 优先通过 id 查询， 因为 id 的唯一性， 所以， 查询结果只会有一条， 将查询结果
以 key:value 对的方式存放到定义的 event 字典中， 并将数据字典作为整个返回字典中 data 对应的值返回。<br>
&emsp;&emsp;name 查询为模糊查询， 查询数据可能会有多条， 返回的数据稍显复杂； 首先将查询的每一条数据放到一
个字典 event 中， 再把每一个字典再放到数组 datas 中， 最后再将整个数组做为返回字典中 data 对应的值返回。<br>
### 8.3.3、 嘉宾添加接口
&emsp;&emsp;打开.../sign/views_if.py 文件， 添加嘉宾添加接口。<br>
```Python
# 添加嘉宾接口
def add_guest(request):
    eid = request.POST.get('eid', '')  # 关联发布会 id
    realname = request.POST.get('realname', '')  # 姓名
    phone = request.POST.get('phone', '')  # 手机号
    email = request.POST.get('email', '')  # 邮箱
    if eid == '' or realname == '' or phone == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status': 10022, 'message': 'event id null'})
    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status': 10023, 'message': 'event status is not available'})
    event_limit = Event.objects.get(id=eid).limit  # 发布会限制人数
    guest_limit = Guest.objects.filter(event_id=eid)  # 发布会已添加的嘉宾数
    if len(guest_limit) >= event_limit:
        return JsonResponse({'status': 10024, 'message': 'event number is full'})
    event_time = Event.objects.get(id=eid).start_time  # 发布会时间
    etime = str(event_time).split(".")[0]
    timeArray = time.strptime(etime, "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))
    now_time = str(time.time())  # 当前时间
    ntime = now_time.split(".")[0]
    n_time = int(ntime)
    if n_time >= e_time:
        return JsonResponse({'status': 10025, 'message': 'event has started'})
    try:
        Guest.objects.create(realname=realname, phone=int(phone), email=email, sign=0, event_id=int(eid))
    except IntegrityError:
        return JsonResponse({'status': 10026, 'message': 'the event guest phone number repeat'})
    return JsonResponse({'status': 200, 'message': 'add guest success'})
```
&emsp;&emsp;通过 POST 请求接收嘉宾参数： 关联的发布会 id、 姓名、 手机号和邮箱等参数。<br>
&emsp;&emsp;首先， 判断 eid、 realname、 phone 等参数均不能为空。<br>
&emsp;&emsp;接下来， 判断嘉宾关联的发布会 id 是否存在， 以及关联的发布会状态是否为 True（即 1） ， 如果不存在
或不为 True， 将返回相应的状态码和提示信息。<br>
&emsp;&emsp;再接下来的步骤是判断当前时间是否大于发布会时间， 如果大于则说明发布已开始， 或者早已经结束。
那么该发布会就应该不能允许再添加嘉宾。<br>
&emsp;&emsp;最后， 插入嘉宾数据， 如果发布会的手机号重复则抛 IntegrityError 异常， 接收该异常并返回相应的状态
码和提示信息。 如果添加成功， 则返回状态码 200 和“add guest success” 的提示。<br>
### 8.3.4、 嘉宾查询接口
&emsp;&emsp;打开.../sign/views_if.py 文件， 继续添加嘉宾查询接口。<br>
```Python
# 嘉宾查询接口
def get_guest_list(request):
    eid = request.GET.get("eid", "")  # 关联发布会 id
    phone = request.GET.get("phone", "")  # 嘉宾手机号
    if eid == '':
        return JsonResponse({'status': 10021, 'message': 'eid cannot be empty'})
    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status': 200, 'message': 'success', 'data': guest})
```
### 8.3.5、 嘉宾签到接口
&emsp;&emsp;打开.../sign/views_if.py 文件， 添加嘉宾签到接口。<br>
```Python
# 嘉宾签到接口
def user_sign(request):
    eid = request.POST.get('eid', '')  # 发布会 id
    phone = request.POST.get('phone', '')  # 嘉宾手机号
    if eid == '' or phone == '':
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
    result = Event.objects.filter(id=eid)
    if not result:
        return JsonResponse({'status': 10022, 'message': 'event id null'})
    result = Event.objects.get(id=eid).status
    if not result:
        return JsonResponse({'status': 10023, 'message': 'event status is not available'})
    event_time = Event.objects.get(id=eid).start_time  # 发布会时间
    etime = str(event_time).split(".")[0]
    timeArray = time.strptime(etime, "%Y-%m-%d %H:%M:%S")
    e_time = int(time.mktime(timeArray))
    now_time = str(time.time())  # 当前时间
    ntime = now_time.split(".")[0]
    n_time = int(ntime)
    if n_time >= e_time:
        return JsonResponse({'status': 10024, 'message': 'event has started'})
    result = Guest.objects.filter(phone=phone)
    if not result:
        return JsonResponse({'status': 10025, 'message': 'user phone null'})
    result = Guest.objects.filter(event_id=eid, phone=phone)
    if not result:
        return JsonResponse({'status': 10026, 'message': 'user did not participate in the conference'})
    result = Guest.objects.get(event_id=eid, phone=phone).sign
    if result:
        return JsonResponse({'status': 10027, 'message': 'user has sign in'})
    else:
        Guest.objects.filter(event_id=eid, phone=phone).update(sign='1')
        return JsonResponse({'status': 200, 'message': 'sign success'})
```
&emsp;&emsp;签到接口通过 POST 请求接收发布会 id 和嘉宾手机号。 签到接口的判断条件比较多。<br>
&emsp;&emsp;首先， 判断两个参数均不能为空。<br>
&emsp;&emsp;接着， 判断发布会 id 是否存在， 以及发布会状态是否为 True， 如果不存在或不为 True， 将返回相应的状
态码和提示信息。<br>
&emsp;&emsp;再接着， 判断当前时间是否大于发布会时间， 如果大于发布会时间说明发布会已开始， 不允许签到。<br>
&emsp;&emsp;然后， 再判断嘉宾的手机号是否存在， 以及嘉宾的手机号与发布会 id 是否为对应关系。 否则返回相应的
错误码和提示信息。<br>
&emsp;&emsp;最后， 判断该嘉宾的状态是否为已签到， 如果已签到， 返回相应的状态码和提示； 如果未签到修改状态
为已签到， 并返回状态码 200 和“sign success” 的提示。<br>
### 8.3.6、 配置接口路径
&emsp;&emsp;当所有接口都已经开发完成， 需要配置接口的访问路径。<br>
&emsp;&emsp;打开.../guest/urls.py 文件， 添加接口基本路径“/api/” ：<br>
urls.py:<br>
```Python
from django.conf.urls import url, include
urlpatterns = [
......
    url(r'^api/', include('sign.urls', namespace="sign")),
]
```
&emsp;&emsp;创建.../sign/urls.py 文件， 配置具体接口的二级路径。<br>
```Python
from django.conf.urls import url
from sign import views_if

urlpatterns = [
    # guest system interface:
    # ex : /api/add_event/
    url(r'^add_event/', views_if.add_event, name='add_event'),
    # ex : /api/add_guest/
    url(r'^add_guest/', views_if.add_guest, name='add_guest'),
    # ex : /api/get_event_list/
    url(r'^get_event_list/', views_if.get_event_list, name='get_event_list'),
    # ex : /api/get_guest_list/
    url(r'^get_guest_list/', views_if.get_guest_list, name='get_guest_list'),
    # ex : /api/user_sign/
    url(r'^user_sign/', views_if.user_sign, name='user_sign'),
]
```
## 8.4 编写 Web 接口文档
&emsp;&emsp;编写接口文档是接口开发非常重要的一个环节， 因为开发的接口是给其它开发人员调用的， 那么其它开
发如何知道我们的开发的接口怎么调用？ 当然需要通过查看接口文档了。 那么对接口文档就必须要做到内容
准确， 以及当接口变动时要实时更新。<br>
&emsp;&emsp;1、 添加发布会接口<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.5.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.6.PNG)<br>
&emsp;&emsp;2、 添加嘉宾接口<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.7.PNG)<br>
&emsp;&emsp;3、 查询发布会接口<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.8.PNG)<br>
&emsp;&emsp;4、 查询嘉宾接口<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.9.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.10.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.11.PNG)<br>
&emsp;&emsp;5、 嘉宾签到接口<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.12.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter8/image/8.13.PNG)<br>
&emsp;&emsp;接口文档的形式也可以是多样的， 这里做成了 Word 文档的形式， 除此之外， 我们还可以将其做在线 Wike
的形式。<br>
# chapter9 接口测试工具介绍
&emsp;&emsp;用于接口测试的工具非常多， 在开始介绍接口测试工具之前， 我大致把接口工具分为以下几类。<br>
&emsp;&emsp;接口测试工具： 这类工具比较简单， 可以模拟和发送 HTTP 请求， 并显示返回数据。 返回的数据由人工
来检查正确性。 例如 Poster、 Postman 等。<br>
&emsp;&emsp;接口自动化测试工具： 相比接口测试要工具， 功能要更加强大， 一般提供用例的批量执行， 返回结果的
断言以及测试报告的生成等， 如 Jmeter、 Robot Framework、 soapUI 等。<br>
&emsp;&emsp;接口性能测试工具： 主要用于测试接口的性能测试， 验证接口处理并发的能力。 如 Jmeter、 LoadRunner、
soapUI 等工具。<br>
## 9.1 Poster 与 Postman
&emsp;&emsp;之所以会把这两款工具放到一起介绍， 因为它们分别作为 Firefox 和 Chrome 浏览器的插件而存在， 所以，
要想使用它们分别需要安装这两款浏览器。<br>
### 9.1.1、 Poster
&emsp;&emsp;Poster 为 Firefox 浏览器的一个插件， 主要用来模拟发并 HTTP 请求。 随着 Chrome 浏览器的流行， 它也
出了 chrome 版本： Chrome Poster<br>
&emsp;&emsp;在 Fiefox 浏览器中的安装非常简单。 首先， 打开 Fiefox 浏览器， 菜单栏“工具” --> “添加组件” ， 搜
索“poster” ， 在搜索例表中点击“安装” ， 然后重启浏览器即可。<br>
&emsp;&emsp;打开方法： 菜单栏“工具” --> “Poster” 。 如图 9.1。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.1.PNG)<br>
&emsp;&emsp;发送 GET 请求（查询发布会信息） ： http://127.0.0.1:8000/api/get_event_list/?eid=1<br>
&emsp;&emsp;获取发布会 id（eid） 为 1 的发布会信息。 如图 9.2， 左侧为填写的请求地址， 右则为接口返回值。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.2.PNG)<br>
&emsp;&emsp;发送 POST 请求（添加发布会信息） ： http://127.0.0.1:8000/api/add_event/<br>
&emsp;&emsp;POST 请求的参数与 GET 不同； 如图 9.3， 在 Parameters 标签中添加 POST 请求的参数， “Name” 为参
数名， “Value” 为参数值。 然后点击“Add/Change” 按钮添加。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.3.PNG)<br>
&emsp;&emsp;然后， 切换到“Content to Send” 标签页， 点击“Body from Parameters” 按钮， 添加 POST 请求的参数。
然后， 点击“POST” 按钮发送请求， 并得得返回结果， 如图 9.4。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.4.PNG)<br>
### 9.1.2、 Postman
&emsp;&emsp;Postman 是一款功能强大的网页调试与发送网页 HTTP 请求的 Chrome 插件。<br>
&emsp;&emsp;Postman 官方网站： http://www.getpostman.com/<br>
&emsp;&emsp;（备注： 需要科学上网才能安装）<br>
&emsp;&emsp;安装完成， 点击 Chrome 浏览器右上角菜单栏“更多工具” -->“扩展程序” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.5.PNG)<br>
&emsp;&emsp;如图 9.5 所示， 说明 Postman 已经安装完成。 接下来可以在 Windows 系统开始运行中搜索 Postman 应用
打开。 如图 9.6 为 Postman 应用主界面。 Postman 的使用方式与 Poster 相似。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.6.PNG)<br>
&emsp;&emsp;发送 GET 请求（查询嘉宾信息） ： http://127.0.0.1:8000/api/get_guest_list/?eid=1&phone=18600110011<br>
&emsp;&emsp;如图 9.8， 选择“GET” 请求， 查询关联发布会 id 为 1， 手机号为 18600110011 的嘉宾信息。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.7.PNG)<br>
&emsp;&emsp;发送 POST 请求（添加嘉宾信息） ： http://127.0.0.1:8000/api/add_guest/<br>
&emsp;&emsp;需要注意的是， POST 请求参数需要在 Body 标签中添加。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.8.PNG)<br>
&emsp;&emsp;相对于 Poster 来说， Postman 功能更为强大一些， 使用也更加广泛， 网上也很容易找到使用教程。 在开发
Web 接口时， 通过这两款工具来测试接口的实现是个很不错的选择。<br>
### 9.2.1、 安装 Jmeter
&emsp;&emsp;Jmeter 官方网址： http://jmeter.apache.org/<br>
&emsp;&emsp;相信你可以在官网上找到下载地址并把它下载下来。 Jmeter 由 Java 语言开发， 最新的 Jmeter3.0 版本的
运行需要有 Java 7 或之后版本的环境。<br>
&emsp;&emsp;接下来，将下载的 apache-jmeter-3.0.zip 解压，进入解压目录.../apache-jmeter-3.0/bin 。双击 ApacheJMeter.jar
启动， 如图 9.10：<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.9.PNG)<br>
### 9.2.2、 添加 HTTP 接口测试
&emsp;&emsp;打开 Jmeter 工具， 按照下面的步骤来创建一个 HTTP 接口测试。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.10.PNG)<br>
&emsp;&emsp;如图 9.11， 右键点击“测试计划” -->“添加” -->“Threads(Users)” -->“线程组” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.11.PNG)<br>
&emsp;&emsp;如图 9.12 设置线程组， 线程组主要包含三个参数： 线程数、 准备时长（Ramp-Up Period(in seconds)） 、
循环次数。<br>
&emsp;&emsp;线程数： 虚拟用户数。 一个虚拟用户占用一个进程或线程。 设置多少虚拟用户数在这里也就是设置多少
个线程数。<br>
&emsp;&emsp;准备时长： 设置的虚拟用户数全部启动的时长。 如果线程数为 20 ， 准备时长为 10（秒） ， 那么需要 10
秒钟启动 20 个线程。 也就是平均每秒启动 2 个线程。<br>
&emsp;&emsp;循环次数： 每个线程发送请求的个数。 如果线程数为 20 ， 循环次数为 100 ， 那么每个线程发送 100 次请
求。 总请求数为 20*100=2000 。 如果勾选了“永远” ， 那么所有线程会一直发送请求， 直到手动点击工具栏
上的停止按钮， 或者设置的线程时间结束。<br>
&emsp;&emsp;因为这里要做接口功能测试， 所以各个参数均为 1。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.12.PNG)<br>
&emsp;&emsp;如图 9.13， 右键点击“线程组” -->“添加” -->“Sampler” -->“HTTP 请求” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.13.PNG)<br>
&emsp;&emsp;名称： 本属性用于标识一个取样器， 建议使用一个有意义的名称。<br>
&emsp;&emsp;注释： 对于测试没有任何作用， 仅用于记录用户可读的注释信息。<br>
&emsp;&emsp;服务器名称或 IP ： HTTP 请求发送的目标服务器名称或 IP 地址。<br>
&emsp;&emsp;端口号： 目标服务器的端口号， 默认值为 80 。<br>
&emsp;&emsp;协议： 向目标服务器发送 HTTP 请求时的协议， 可以是 HTTP 或者是 HTTPS ， 默认值为 http 。<br>
&emsp;&emsp;方法： 发送 HTTP 请求的方法， 可用方法包括 GET、 POST、 HEAD、 PUT、 OPTIONS、 TRACE、 DELETE
等。<br>
&emsp;&emsp;Content encoding ： 内容的编码方式， 默认值为 iso8859<br>
&emsp;&emsp;路径： 目标 URL 路径（不包括服务器地址和端口）<br>
&emsp;&emsp;自动重定向： 如果选中该选项， 当发送 HTTP 请求后得到的响应是 302/301 时， JMeter 自动重定向到新
的页面。<br>
&emsp;&emsp;Use keep Alive ： 当该选项被选中时， jmeter 和目标服务器之间使用 Keep-Alive 方式进行 HTTP 通信，
默认选中。<br>
&emsp;&emsp;Use multipart/from-data for HTTP POST ： 当发送 HTTP POST 请求时， 使用 Use multipart/from-data 方
法发送， 默认不选中。<br>
&emsp;&emsp;同请求一起发送参数 ： 在请求中发送 URL 参数， 对于带参数的 URL ， Jmeter 提供了一个简单的参数化
的方法。 用户可以将 URL 中所有参数设置在本表中， 表中的每一行是一个参数值对（对应 RUL 中的 名称 1=
值 1） 。<br>
&emsp;&emsp;接下来， 添加“察看结果树” 。 如图 9.15， 右键点击“线程组” -->“添加” -->“监听器” -->“察看结
果树” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.14.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.15.PNG)<br>
### 9.2.3、 添加 GET/POST 请求
&emsp;&emsp;在 HTTP 请求元件中添加 GET/POST 请求。<br>
&emsp;&emsp;首先， 添加一个 GET 请求类型的 HTTP 协议接口。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.16.PNG)<br>
&emsp;&emsp;图 9.17， 填写选项如下表（获取嘉宾信息） ：<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.17.PNG)<br>
&emsp;&emsp;再次添加一下“HTTP 请求” ， 填写内容如下表（添加嘉宾信息） ：<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.18.PNG)<br>
&emsp;&emsp;执行测试， 点击工具栏“启动” 按钮运行测试， 并查看结果树。 如图 9.18。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.19.PNG)<br>
### 9.2.4、 添加断言
&emsp;&emsp;对于自动化测试来说， 断言必须必不可少， 如果没有断言只能人工比对接口返回的数据， 如果接口很多，
这种过程就会非常耗时， 而且也容易出错。 Jmeter 提供了丰富的断言策略来帮助我们完成这项工作。<br>
&emsp;&emsp;如图 9.19， 右键点击 HTTP 请求“添加” -->“断言” -->“响应断言” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.20.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.21.PNG)<br>
&emsp;&emsp;要测试的响应字段： 响应文本、 Document(text)、 URL 样本、 响应信息、 Response Headers、 Lgnore Staus
等选项。 虽然接口返回的是 Json 格式的数据， 但对于 Jmeter 来说返回数据为文本， 所以， 这里可以勾选“响
应文本”<br>
&emsp;&emsp;模式匹配规则： 包括、 匹配、 Equals、 Substring。 这里只需要验证返回数据中是否包含主要的关键字， 所
以， 这里勾选“包括” 。<br>
&emsp;&emsp;要测试的模式： 其实就是断言的数据。 点击“添加” 按钮， 输入要断言的数据。<br>
&emsp;&emsp;对于获取嘉宾信息的断言，可以添加模糊匹配，“200”、“success”以及查询到的嘉宾手机号“13511001100”。<br>
&emsp;&emsp;对于添加嘉宾信息的断言， 可以模糊匹配， “200” 、 “add guest success” 等信息。<br>
&emsp;&emsp;添加断言过后， 再次点击工具栏的“启动” 按钮， 运行测试。 通过“全部清除” 按钮可以清除掉上一次
运行的结果。<br>
## 9.3 Robot Framework 测试框架
&emsp;&emsp;Robot Framework 的架构是一个通用型的验收测试和验收测试驱动开发的自动化测试框架（ATDD） 。 它
具有易于使用的表格来组织测试过程和测试数据。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.22.PNG)<br>
&emsp;&emsp;Robot Framework 特点：<br>
- 使用简单
- 非常丰富的库
- 可以像编程一样写测试用例
- 支持开发系统关键字

### 9.3.1、 环境搭建
&emsp;&emsp;目前 Robot Framework3.0 已经支持 Python3.x，但是基于该框架的大多 Library 还并未完全支持 Python3.x，
好在用来做接口测试的 RequestsLibrary 已经支持了 Python3.x， 所以， 我们可以在 Python3.x 进行环境的搭建
和接口自动化测试。<br>
&emsp;&emsp;Python3.x：<br>
&emsp;&emsp;在本书的第一章已经详细的介绍了两个版本的安装， 这里不再介绍。<br>
&emsp;&emsp;安装 Robot Framwork：<br>
&emsp;&emsp;https://pypi.python.org/pypi/robotframework<br>
&emsp;&emsp;它同样支持 pip 命令安装：<br>
&emsp;&emsp;`pip install robotframework`<br>
&emsp;&emsp;安装 Requests：<br>
&emsp;&emsp;robotframework-requests 的运行依赖于 Requests 库， 在本书的第十章中会详细介绍 Requests 库的使用， 这
里我们先通过 pip 命令进行安装。<br>
&emsp;&emsp;`pip install requests`<br>
&emsp;&emsp;安装 robotframework-requests：<br>
&emsp;&emsp;目前 PyPi 仓库中的 robotframework-requests 库暂时还不支持 Python3.x， 不过我们可以在 GitHub 上获取
最新的项目代码来安装。<br>
&emsp;&emsp;GitHub 地址： https://github.com/bulkan/robotframework-requests<br>
&emsp;&emsp;将项目克隆或下载并解压， 执行目录下的 setup.py 文件进行安装。<br>
&emsp;&emsp;`...\robotframework-requests-master>python3 setup.py install`<br>
&emsp;&emsp;那么， 接下来应该练习编写如何 Robot Framework 脚本； 用什么 IDE 来编写脚本呢？ 如果你阅读过其它
Robot Framework 的安装资料的话， 也许会认为我所介绍的安装过程遗留了 Robot Framework -RIDE（以下简
称 RIDE） ， 是的！ 对于编写 Robot Framework 脚本来说， RIDE 几乎是必不可少的。 然而它的角色是依然只是
一款 IDE， 也就是说不用它一样可以编写和运行 Robot Framework 脚本。 这里之所以没有介绍 RIDE 的安装，
主要原因是因为它目前还不并支持 Python3， 我想， 之所以还不支持 Python3 的原因之一是因为 RIDE 是基于
wxPython（该库是 Python 下非常有名的 GUI 库） 开发的， 而 wxPython 目前并不支持 Python3， 所以， RIDE
想支持 Python3 就变得比较困难。<br>
&emsp;&emsp;那么除了 RIDE 之外， 还可以用什么工具来编写 Robot Framework 脚本？ Robot Framework 目前提供了各
种主流编辑器的插件支持。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.23.PNG)<br>
&emsp;&emsp;读者可以选择在自己熟悉的编辑器中安装相应的插件， 介于本书第一章中介绍了 Sublime Text2， 所以，
这里我们选择 Sublime assistant 插件安装。<br>
&emsp;&emsp;Github 地址： https://github.com/andriyko/sublime-robot-framework-assistant<br>
&emsp;&emsp;同样的方式克隆或下载插件代码到本地， 将解压目录放到 Sublime Text2 的 Packages\目录下， 重启动
Sublimt Text2。<br>
&emsp;&emsp;在 Sublimt Text2 菜单栏“查看”-->“语法”-->“Botot Framework syntax highlighting”，选择 Robot Framework
类型的语法。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.24.PNG)<br>
### 9.3.2、 基本概念与用法
&emsp;&emsp;在 Robot Framework 中创建测试项目和单元测试框架（unittest） 中基本一致。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.25.PNG)<br>
&emsp;&emsp;回忆一下， 当我们用单元测试框架 unittest 创建测试用例的过程， 首先创建一个.py 文件。 在文件中当创
建测试类并继承 unittest.TestCase 类， 再接下来就是在测试类下面创建以“test” 开头的方法， 称之为一个一个
的用例。 如果创建的测试文件（.py） 多了， 可以把这些文件放到一个目录下， 或者一个目录的子目录下面，
最后通过 discover()方法指定这个目录来运行测试用例。 <br>
&emsp;&emsp;Robot Framework 框架测试用例的创建相似， 首先， 如果你的用例很少， 可以只创建一个文件。 一般后缀
名为.robot 或 .txt， 也可以将后缀名命名为.tsv 或.html。 在文件中编写一个一个的用例。 如果创建了多用例文
件， 也可以将这些文件放到一个测试目录下， 通过“pybot” 命令指定对该目录下的所有用例运行。<br>
&emsp;&emsp;接下来练习一下 Robot Framework 用例的创建与运行。<br>
&emsp;&emsp;首先创建测试目录 rf_test/ ， 在该目录下创建 test.robot 文件。 通过 Sublime Text2 打开文件， 编写如下内
容。<br>
test.robot:<br>
```
*** Settings ***
*** Test Cases ***
testcase
    log robot framework
```
&emsp;&emsp;`*** Settings ***` 部分用于引用 Library， 当前没有引用， 默认为空。<br>
&emsp;&emsp;`*** Test Cases ***` 部分用于编写测试用例。<br>
&emsp;&emsp;testcase 顶格写， 表示用例的名称。<br>
&emsp;&emsp;log robot framework log 前面四个空格， 表示该行为 testcase 的一行语句， log 为打印关键字， 与 Python 的
print()方法类似，“robot framework”为打印的字符串， 注意关键字与字符串之间的间距为四个空格。 在 Sublime
Text3 中的显示如图 9.23。<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.26.PNG)<br>
&emsp;&emsp;如何运行 Robot Framework 用例？ 首先， 在安装好 Robot Framework 之后， 在 Python 的 Script/目录下会
多出一个 pybot.bat 文件， 并且确保“C:\Python35\Scripts\” 目录已经添加到了环境变量 path 下面。 接下来， 打
开 Windows 命令提示符， 在任意目录下输入“pybot -h” 命令回车。 如果出现帮助信息， 说明 pybot 命令可用，
如果提示 pybot 不是内部或外部命令， 请检查环境变量是否正确的配置。<br>
&emsp;&emsp;运行测试：<br>
```
...\rf_test>pybot test.robot
==============================================================================
Test
==============================================================================
testcase | PASS |
------------------------------------------------------------------------------
Test | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output: D:\rf_test\output.xml
Log: D:\rf_test\log.html
Report: D:\rf_test\report.html
```
&emsp;&emsp;除了运行过程中的打印信息外， Robot Framework 还生成了三个文件， 分别为 output.xml 、 log.html 和
report.html。<br>
&emsp;&emsp;output.xml 是以 XML 格式记录测试结果。 阅读起来不够直观， 在我看来， 它的作用是提供给我们测试结
果， 让我们读取该文件生成定制化的测试报告。 例如， 你可以使用 Python 语言读取该文件生成自定义的测试
报告。<br>
&emsp;&emsp;log.html 和 report.html 要美观的得多， log.html 偏向于测试日志， 记录脚本每一步的执行情况。 report.html
偏向于测试报告， 总体性的展示测试用例的执行情况。 log.html 文件通过浏览器打开， 如图 9.24<br>
![image](https://github.com/15529343201/guest/blob/chapter9/image/9.27.PNG)<br>
&emsp;&emsp;最后， 介绍几种“pybot” 命令的运行测试用例的策略：<br>
```
...\rf_test>pybot test.robot #运行指定文件
...\rf_test>pybot *.robot #运行当前目录下以.robot 为后缀名的测试文件
...\rf_test>pybot test_a #运行当前 test_a 目录下的所有用例
...\rf_test>pybot ./ #运行当前目录下的所有以.robot 为后缀名的测试文件
```
&emsp;&emsp;关于， 更多用法， 读者可以通过“pybot -h” 查看帮助。<br>
### 9.3.3、 接口测试
&emsp;&emsp;Robot Framework 测试框架更像一个自动化测试平台， 它本身只提供了最基础的测试功能， 例如， 测试用
例的组织、 运行、 测试报告的生成， 以及最基本的 Builtin 库， 该库提供了最基本的关键字来实现打印， 变量
定义， if 语句， for 循环等。<br>
&emsp;&emsp;那么， 我们想要完成不同类型的测试， 就需要安装不同的 Library。 Robot Framework 提供了非常丰富的
Library。<br>
&emsp;&emsp;Web 自动化测试： SeleniumLibrary， Selenium2Library， Selenium2Library for Java、 watir-robot 等。<br>
&emsp;&emsp;Windows GUI 测试： AutoItLibrary。<br>
&emsp;&emsp;移动测试： Android library、 iOS library、 AppiumLibrary 等。<br>
&emsp;&emsp;数据库测试： Database Library (Java)、 Database Library (Python)、 MongoDB library 等。<br>
&emsp;&emsp;文件对比测试： Diff Library。<br>
&emsp;&emsp;HTTP 测试： HTTP library (livetest)、 HTTP library (Requests)等。<br>
&emsp;&emsp;夸完了 Robot Framework 的强大， 接下来介绍接口测试用例的编写。 在前面环境搭建一节， 已经教读者
安装好了 robotframework-requests 库， 接下来使用该库来编写接口测试用例。<br>
test_if.robot:<br>
```
*** Settings ***
Library        RequestsLibrary
Library        Collections

*** Test Cases ***

testget
    ${payload}= Create Dictionary eid=1
    Create Session event http://127.0.0.1:8000/api
    ${r}= Get Request event /get_event_list/ params=${payload}
    Should Be Equal As Strings ${r.status_code} 200
    log ${r.json()}
    ${dict} Set variable ${r.json()}
    #断言结果
    ${msg} Get From Dictionary ${dict} message
    Should Be Equal ${msg} success
    ${sta} Get From Dictionary ${dict} status
    ${status} Evaluate int(200)
    Should Be Equal ${sta} ${status}
```
&emsp;&emsp;虽然前面已经对 Robot Framework 的语法有了一定的认识， 但我相信在你看到上面这一段脚本时内心几
乎是崩溃的。<br>
&emsp;&emsp;如果用 RIDE 编写脚本， 这些脚本会横竖整齐的填写在“表格” 中。 如果用 Sublime Text3 编写脚本的话，
起码有代码着色和空格位。 然而， 这样的脚本确实看起来比较杂乱， 不过， 还是希望你能耐下心来和我一起
学习。<br>
```
----------------------------------------------------------
Library RequestsLibrary
Library Collections
--------------------------------------
```
&emsp;&emsp;首先， 引用了 RquestsLibrary 库和 Collections 库， RquestsLibrary 就是我们安装的 robotframework-requests，
用来进行接口测试的相关操作。 而 Collections 库是用来操作字典的， 因为接口的返回数据是 Json 格式， 转化
成字典才能进行断言。<br>
```
----------------------------------------------------------
testget
...
--------------------------------------
```
&emsp;&emsp;testget 用来操作 GET 接口的用例。<br>
```
----------------------------------------------------------
${payload}= Create Dictionary eid=1
Create Session event http://127.0.0.1:8000/api
${r}= Get Request event /get_event_list/ params=${payload}
----------------------------------------------------------
```
&emsp;&emsp;先来看 testget 用例的前三行， 通过“Create Dictionary” 关键字定义字典变量${payload}， 字典有一个键
值 eid=1。 该字典将会作为接口的参数。<br>
&emsp;&emsp;“Create Session”关键字用来创建一个 HTTP 会话服务器。event 为该会话的别名，http://127.0.0.1:8000/api
为该会话的基本 url.<br>
&emsp;&emsp;“Get Requests” 关键字用来发起一个 GET 请求， 接口 URL 为 event + /get_event_list/， 接口参数为
${payload}。 最后将接口返回信息赋值给变量${r}。<br>
```
----------------------------------------------------------
Should Be Equal As Strings ${r.status_code} 200
log ${r.json()}
----------------------------------------------------------
```
&emsp;&emsp;通过${r.status_code}可以得到请求的 HTTP 状态码， 通过“Should Be Equal As Strings” 关键字判断其是
否为 200。<br>
&emsp;&emsp;通过${r.json()}可得将 json 格式的返回值转化为字典， 并通过 log 打印。<br>
```
----------------------------------------------------------
${dict} Set variable ${r.json()}
#断言结果
${msg} Get From Dictionary ${dict} message
Should Be Equal ${msg} success
${sta} Get From Dictionary ${dict} status
${status} Evaluate int(200)
Should Be Equal ${sta} ${status}
----------------------------------------------------------
```
&emsp;&emsp;再接下来的操作主要是对返回字典的验证。 将${r.json()}通过定义变量关键字“Set Variable” 赋值给变量
${dict}。<br>
&emsp;&emsp;“Get From Dictionary” 关键字由前面的引入的 Collections 库提供， 可以取到字典中 key 对应 value。 这
里获取 key 为“message” 对应的 value 赋值给变量${msg}。<br>
&emsp;&emsp;“Should Be Equal” 关键字用于比较${msg}是否等于“success” 。<br>
&emsp;&emsp;接下来以同样的方式获取到字典 key 为“status” 对应的 value。 可是得到的 value 200 是整数类型。 然而，
在 Robot Framework 中直接编写的内容为字符串。 所以， 这里借助强大的 Evaluate， 它可以直接调用 Python
所提供的方法。 例如， 这里调用 Python 的 int()方法把 200 转整数类型， 并与字典中的取出来的整数 200 进行
比较。<br>
&emsp;&emsp;到此， 这一个完整接口用例介绍完毕。 接下来再编写一个 POST 请求的接口测试用例。<br>
```
testpost
    ${header} Create Dictionary Content-Type=application/json
    ${payload}= Create Dictionary eid=1
    Create Session event http://127.0.0.1:8000/api ${header}
    ${r}= Post Request event /add_event/ data=${payload}
    Should Be Equal As Strings ${r.status_code} 200
    log ${r.json()}
    ${dict} Set variable ${r.json()}
    #断言结果
    ${msg} Get From Dictionary ${dict} message
    Should Be Equal ${msg} parameter error
    ${sta} Get From Dictionary ${dict} status
    ${status} Evaluate int(10021)
    Should Be Equal ${sta} ${status}
```
&emsp;&emsp;POST 接口用例基本与前面介绍的 GET 接口用例相似， 但略有不同。<br>
```
----------------------------------------------------------------
${header} Create Dictionary Content-Type=application/json
${payload}= Create Dictionary eid=1
Create Session event http://127.0.0.1:8000/api ${header}
${r}= Post Request event /add_event/ data=${payload}
----------------------------------------------------------------
```
&emsp;&emsp;首先， POST 请求一般需要创建 header 标头， 用来指定请求信息的内容类型。 在创建 HTTP 会话服务器
时指定。 另外， POST 请求所用到的关键字为“Post Request” 。<br>
&emsp;&emsp;最后， 关于 Robot Framework 框架的介绍就到此为止， 不得不说它是一个非常优秀的测试框架， 应用范
围也很广泛。 另外， 关于 RequestsLibrary 中所提供的关键字， 可以在下面的文档中查看。<br>
&emsp;&emsp;http://bulkan.github.io/robotframework-requests/<br>
# chapter10 接口测试框架设计
## 10.1、 接口测试工具的不足
&emsp;&emsp;相信读者一定产生了疑问， 在第九章中通过各种接口测试工具来完成测试， 看上去简单方便， 为何还要
学习编程的方式来做接口测试呢？ 工具虽然方便， 但也不足之处， 这里简单总结几条工具的不足。<br>
&emsp;&emsp;测试数据不可控制<br>
&emsp;&emsp;接口测试本质是对数据的测试， 调用接口， 输入一些数据， 随后， 接口返回一些数据。 验证接口返回数
据的正确性。<br>
&emsp;&emsp;假设有一个用户查询接口， 要输入用户名 username， 返回用户的年龄、 性别、 邮箱、 手机号等数据。 在
测试该接口时传参 username=zhangsan。 首先， 数据库里一定要有一条 zhangsan 的数据， 否则接口返回为空。
如果要想断言接口返回值， 如 assert age==22； 那么一定预先确定参数的返回数据。<br>
&emsp;&emsp;要想接口测试用例可以正确的执行并断言通过，必须要事先插入测试数据（username=zhangsan ; age=22...），
一般的接口测试工具并不具备数据插入的功能。 在用工具运行测试用例之前不得不手动向数据库中插入测试
数据。 这样我们的接口测试是不是就没有那么“自动化了” 。<br>
&emsp;&emsp;无法测试加密接口<br>
&emsp;&emsp;这是接口测试工具的一大硬伤， 如我们前面开发的接口用工具测试完全没有问题， 但遇到需要对接口参
数进行加密/解密的接口， 例如 md5、 base64、 AES 等常见加密方式。 本书第十一章会对加密接口进行介绍。
又或者接口的参数需要使用时间戳， 也是工具很难模拟的。<br>
&emsp;&emsp;扩展能力不足<br>
&emsp;&emsp;当我们在享受工具所带来的便利的同时， 往往也会受制于工具所带来的局限。 例如， 我想将测试结果生
成 HMTL 格式测试报告， 我想将测试报告发送到指定邮箱。 我想对接口测试做定时任务。 我想对接口测试做
持续集成。 这些需求都是工具难以实现的。<br>
&emsp;&emsp;备注： 关于上面的几点不足， 大多情况 Robot Framework 可以满足， 严格意义上来说 Robot Framework 并
不属于“工具” ， 虽然我将其划分到了测试工具一章。 但 Robot Framework 有着与编程一样的扩展性， 前提是
你需要熟悉 Python 语言， 并且可以为 Robot Framework 开发系统关键字。 然而， Robot Framework 的脚本难读
在我看来是它的最大弱点。 既然都要开发系统关键字了， 为何不直接写 Python 脚本更加自由。<br>
## 10.2、 接口自动化测试设计
&emsp;&emsp;既然讨论了自动化接口测试工具的不足， 接下来介绍一下接口自动化项目的实现。<br>
![image](https://github.com/15529343201/guest/blob/chapter10/image/10.1.PNG)<br>
&emsp;&emsp;一般的接口工具测试过程：<br>
&emsp;&emsp;1、 接口工具调用被测系统的接口（传参 username="zhangsan"） 。<br>
&emsp;&emsp;2、 系统接口根据传参（username="zhangsan"） 向正式数据库中查询数据。<br>
&emsp;&emsp;3、 将查询结果组装成一定格式的数据， 并返回给被调用者。<br>
&emsp;&emsp;4、 人工或通过工具的断言功能检查接口测试的正确性。<br>
&emsp;&emsp;而我们设计的接口自动化测试项目， 为了使接口测试对数据的变得可控， 测试过程如下：<br>
&emsp;&emsp;1、 接口测试项目先向测试数据库中插入测试数据（zhangsan 的个人信息） 。<br>
&emsp;&emsp;2、 调用被测系统接口（传参 username="zhangsan"） 。<br>
&emsp;&emsp;3、 系统接口根据传参（username="zhangsan"） 向测试数据库中进行查询并得到 zhangsan 个人信息。<br>
&emsp;&emsp;4、 将查询结果组装成一定格式的数据， 并返回给被调用者。<br>
&emsp;&emsp;5、 通过单元测试框架断言接口返回的数据（zhangsan 的个人信息） ， 并生成测试报告。<br>
&emsp;&emsp;为了使正式数据库的数据不被污染， 建议使用独立的测试数据库。 Web 项目配置数据库非常简单。 参考
本书第四章。<br>
## 10.3、 Request 库
&emsp;&emsp;Requests 是使用 Apache2 Licensed 许可证的 HTTP 库。 用 Python 编写。<br>
&emsp;&emsp;Requests 使用的是 urllib3， 因此继承了它的所有特性。 Requests 支持 HTTP 连接保持和连接池， 支持
使用 cookie 保持会话， 支持文件上传， 支持自动确定响应内容的编码， 支持国际化的 URL 和 POST 数据
自动编码。 现代、 国际化、 人性化。<br>
&emsp;&emsp;Requests 以 PEP 20 的习语为中心开发：<br>
&emsp;&emsp;1、 Beautiful is better than ugly.（美丽优于丑陋）<br>
&emsp;&emsp;2、 Explicit is better than implicit.（清楚优于含糊）<br>
&emsp;&emsp;3、 Simple is better than complex.（简单优于复杂）<br>
&emsp;&emsp;4、 Complex is better than complicated.（复杂优于繁琐）<br>
&emsp;&emsp;5、 Readability counts.（重要的是可读性）<br>
&emsp;&emsp;官方网站： http://docs.python-requests.org/en/master/<br>
&emsp;&emsp;中文文档： http://cn.python-requests.org/zh_CN/latest/<br>
### 10.3.1、 安装与例子
&emsp;&emsp;通过 pip 安装 Requests：<br>
&emsp;&emsp;`> python3 -m pip install requests`<br>
&emsp;&emsp;`> git clone git://github.com/kennethreitz/requests.git`<br>
&emsp;&emsp;通过 Requests 官方文档所提供的第一个例子来体会它的使用。<br>
```
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)]
on win32
Type "copyright", "credits" or "license()" for more information.
>>> import requests
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf-8'
>>> r.encoding
'utf-8'
>>> r.text
'{"login":"user","id":1000588,"avatar_url"……
>>> r.json()
{'public_gists': 0, 'id': 1000588, 'type': ……
```
&emsp;&emsp;不过， 要想尝试执行这个例子， 前提是你得有个 GitHub 账号， 因为“user” 和“pass” 需要使用具体的
GitHub 账号密码才行。 建议读者申请 GitHub 帐号， 并将尝试将自己开发的项目通过 GitHub 托管<br>
### 10.3.2、 接口测试
&emsp;&emsp;通过上面的例子， 不难发现用代码方式去调用接口并不比工具复杂， 甚至更加简单。 只需要简单的几行
代码就可以得到接口的返回值。 接下来编写一个完整的接口测试用例。<br>
interface_test.py:<br>
```Python
import requests

# 查询发布会接口
url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url, params={'eid': '1'})
result = r.json()
print(result)
assert result['status'] == 200
assert result['message'] == "success"
assert result['data']['name'] == "xx 产品发布会"
assert result['data']['address'] == "北京林匹克公园水立方"
assert result['data']['start_time'] == "2016-10-15T18:00:00"
```
&emsp;&emsp;因为“发布会查询接口” 是 GET 类型， 所以， 通过 requests 库的 get()方法调用， 第一个参数为调用接口
的 URL 地址， params 设置接口的数， 参数以字典形式组织。<br>
&emsp;&emsp;json()方法可以将接口返回的 json 格式的数据转化为字典。<br>
&emsp;&emsp;接下来就是通过 assert 语句对接字典中的数据进行断言。分别断言 status、 message 和 data 的相关数据等。<br>
### 10.3.3、 接口自动化测试
&emsp;&emsp;使用 unittest 单元测试框架开发接口测试用例.<br>
```Python
import requests
import unittest

class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''

    def setUp(self):
        self.url="http://127.0.0.1:8000/api/get_event_list/"

    def test_get_event_null(self):
        '''发布会id为空'''
        r=requests.get(self.url,params={'eid':''})
        result=r.json()
        print(result)
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")

    def test_get_event_success(self):
        '''发布会id为1,查询成功'''
        r=requests.get(self.url,params={'eid':'1'})
        result=r.json()
        print(result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],"success")
        self.assertEqual(result['data']['name'], "xx 产品发布会")
        self.assertEqual(result['data']['address'], "北京林匹克公园水立方")
        self.assertEqual(result['data']['start_time'], "2016-10-15T18:00:00")

if __name__ == '__main__':
    unittest.main()
```
## 10.4 接口自动化测试框架实现
&emsp;&emsp;关于接口自动化测试， unittest 已经帮我们做了大部分工作， 接下来只需要集成数据库操作， 以及
HTMLTestRunner 测试报告生成扩展即可。<br>
### 10.4.1、 框架结构介绍
&emsp;&emsp;自动化测试框架目录结构如下：<br>
![image](https://github.com/15529343201/guest/blob/chapter10/image/10.2.PNG)<br>
&emsp;&emsp;`pyrequests` 框架：<br>
&emsp;&emsp;`db_fixture/`： 初始化接口测试数据。<br>
&emsp;&emsp;`interface/`： 用于编写接口自动化测试用例。<br>
&emsp;&emsp;`report/`： 生成接口自动化测试报告。<br>
&emsp;&emsp;`db_config.ini` ： 数据库配置文件。<br>
&emsp;&emsp;`HTMLTestRunner.py` unittest 单元测试框架扩展， 生成 HTML 格式的测试报告。<br>
&emsp;&emsp;`run_tests.py` ： 执行所有接口测试用例。<br>
&emsp;&emsp;GitHub 项目地址： https://github.com/defnngj/pyrequest<br>
### 10.4.2、 数据库配置
&emsp;&emsp;首先， 需要修改被测系统将数据库指向测试数据库。 以 MySQL 数据库为例， 修改.../guest/settings.py 文
件。 你可以在本机或虚拟中安装一个数据库； 或者在系统测试环境单独创建一个测试库。 这样做的目的是让
接口测试的数据不会清空或污染到功能测试库的数据。<br>
settings.py:<br>
```Python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'guest_test',
        'USER': 'root',
        'PASSWORD': 'root',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```
&emsp;&emsp;修改了数据库配置之后需要重新执行“python3 manage.py migrate” 生成数据库表结构， 参考本书第四章
3.5 节， 或者读者也可以借助数据库管理工具的导出和导入功能， 将一个数据库的所有表结构导入到另一个数
据库。<br>
### 10.4.3、 代码实现
&emsp;&emsp;首先， 创建数据库配置文件.../db_config.ini<br>
db_config.ini:<br>
```
[mysqlconf]
host=127.0.0.1
port=3306
user=root
password=root
db_name=guest_test
```
&emsp;&emsp;接下来简单封装数据库操作， 数据库表数据的插入和清除， `.../db_fixture/mysql_db.py`。<br>
mysql_db.py:<br>
```Python
# coding=utf8
import pymysql.cursors
import os
import configparser as cparser

# ======== Reading db_config.ini setting ===========
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf = cparser.ConfigParser()

cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


# ======== MySql base operating ===================
class DB:
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        # print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


if __name__ == '__main__':
    db = DB()
    table_name = "sign_event"
    data = {'id': 1, 'name': '红米', '`limit`': 2000, 'status': 1, 'address': '北京会展中心',
            'start_time': '2016-08-20 00:25:42'}
    table_name2 = "sign_guest"
    data2 = {'realname': 'alen', 'phone': 12312341234, 'email': 'alen@mail.com', 'sign': 0, 'event_id': 1}

    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
```
&emsp;&emsp;首先， 读取 db_config.ini 配置文件。<br>
&emsp;&emsp;创建 DB 类， __init__()方法初始化， 通过 pymysql.connect()连接数据库。<br>
&emsp;&emsp;因为这里只用到数据库表的清除和插入， 所以只创建 clear()和 insert()两个方法。 其中， insert()方法对数
据的插入做了简单的格式转化， 可将字典转化成 SQL 插入语句， 这样格式转化了方便了数据库表数据的创建。<br>
&emsp;&emsp;最后， 通过 close()方法用于关闭数据库连接。<br>
&emsp;&emsp;接下来创建测试数据， .../db_fixture/test_data.py<br>
test_data.py:<br>
```Python
import sys, time

sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# 定义过去时间
past_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() - 100000))

# 定义将来时间
future_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 10000))

# create data
datas = {
    'sign_event': [
        {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': future_time,'create_time':'2018-05-03 16:39:00'},
        {'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '北京会展中心', 'start_time': future_time,'create_time':'2018-05-03 16:39:00'},
        {'id': 3, 'name': '当前状态为0关闭', '`limit`': 2000, 'status': 0, 'address': '北京会展中心', 'start_time': future_time,'create_time':'2018-05-03 16:39:00'},
        {'id': 4, 'name': '发布会已结束', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': past_time,'create_time':'2018-05-03 16:39:00'},
        {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京国家会议中心', 'start_time': future_time,'create_time':'2018-05-03 16:39:00'},
    ],
    'sign_guest': [
        {'id': 1, 'realname': 'alen', 'phone': 13511001100, 'email': 'alen@mail.com', 'sign': 0, 'create_time':'2018-05-03 16:39:00','event_id': 1},
        {'id': 2, 'realname': 'has sign', 'phone': 13511001101, 'email': 'sign@mail.com', 'sign': 1, 'create_time':'2018-05-03 16:39:00','event_id': 1},
        {'id': 3, 'realname': 'tom', 'phone': 13511001102, 'email': 'tom@mail.com', 'sign': 0, 'create_time':'2018-05-03 16:39:00','event_id': 5},
    ],
}


# Inster table datas
def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()



if __name__ == '__main__':
    init_data()
```
&emsp;&emsp;init_data()函数用于读取 datas 字典中的数据， 调用 DB 类中的 clear()方法清除数据库， 然后， 调用 insert()
方法插入表数据。<br>
&emsp;&emsp;编写接口测试用例。 创建添加发布会接口测试文件.../interface/add_event_test.py。<br>
add_event_test.py:<br>
```Python
import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from ..db_fixture import test_data


class AddEventTest(unittest.TestCase):
    ''' 添加发布会 '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        print(self.result)

    def test_add_event_all_null(self):
        ''' 所有参数为空 '''
        payload = {'eid':'','':'','limit':'','address':"",'start_time':''}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    def test_add_event_eid_exist(self):
        ''' id已经存在 '''
        payload = {'eid':1,'name':'一加4发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        ''' 名称已经存在 '''
        payload = {'eid':11,'name':'红米Pro发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        ''' 日期格式错误 '''
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])

    def test_add_event_success(self):
        ''' 添加成功 '''
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017-05-10 12:00:00'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')


if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
```
&emsp;&emsp;在测试接口之前， 调用 test_data.py 文件中的 init_data()方法初始化数据库中的测试数据。<br>
&emsp;&emsp;创建 AddEventTest 测试类继承 unittest.TestCase 类， 通过创建测试用例， 调用相关接口， 并验证接口返回
的数据。<br>
&emsp;&emsp;当我们开发的接口达到一定数量后， 就需要考虑分文件分目录的来划分接口测试用例， 如何批量的执行
不同文件目录下的用例呢？ unittest 单元测试框架提供的 discover()方法可以帮助我们做到这一点。 并使用
HTMLTestRunner 扩展生成 HTML 格式的测试报告。<br>
&emsp;&emsp;创建 run_tests.py 文件。<br>
run_tests.py:<br>
```Python
import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from db_fixture import test_data


# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir, pattern='*_test.py')


if __name__ == "__main__":
    test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='发布会签到系统接口自动化测试',
                            description='运行环境：MySQL(PyMySQL), Requests, unittest ')
    runner.run(testsuit)
    fp.close()
```
&emsp;&emsp;首先， 通过调用 test_data.py 文件中的 init_data()函数来初始化接口测试数据。<br>
&emsp;&emsp;使用 unittest 框架所提供的 discover()方法， 查找 interface/ 目录下， 所有匹配*_test.py 的测试文件（*星
号匹配任意字符） 。<br>
&emsp;&emsp;HTMLTestRunner 为 unittest 单元测试框架的扩展， 利用它所提供的 HTMLTestRunner()类来替换 unittest
单元测试框架的 TextTestRunner()类， 从而生成 HTML 格式的测试报告。<br>
&emsp;&emsp;遗憾的是 HTMLTestRunner 并不支持 Python3.x， 我对其做了少量的修改， 其它可以在 Python3 下执行。<br>
&emsp;&emsp;HTMLTestRunner for Python3：<br>
&emsp;&emsp;https://github.com/defnngj/HTMLTestRunner<br>
&emsp;&emsp;为了方便接口自动化测试的使用， 将其放到了 pyrequest 项目中， 当你然克隆 pyrequest 项目后， 不需要
再单独安装 HTMLTestRunner 了。<br>
&emsp;&emsp;通过 time 的 strftime()方法获取当前时间， 并且转化成一定的时间格式。 作为测试报告的名称。 这样做目
的是是为了避免因为生成的报告的名称重名而造成报告的覆盖。 最终， 将测试报告存放于 report/目录下面。 如
图 10.3， 一张完整的接口自动化测试报告。<br>
![image](https://github.com/15529343201/guest/blob/chapter10/image/10.3.PNG)<br>
# chapter11 接口的安全机制
&emsp;&emsp;一般在实际项目的接口开发中， 接口的安全机制是绕不开的一个话题。 不管理自己内部使用的接口也好，
还是给第三方使用的接口也好。 如果毫无限制可以给任何人调用， 那么必然会带来诸多安全问题， 例如， 重
要数据泄密， 系统瘫痪等。<br>
&emsp;&emsp;这一章介绍在接口开发中常见的向种安全机制。<br>
## 11.1 用户认证
&emsp;&emsp;在测试 Web 接口时， 不管所用的接口工具还是 Requests 库都提供的 Auth 的选项/参数， 这个选项提供了
username 和 password 的选项， 但这里 Auth 的用户名和密码与系统登录的用户名密码有所区别， 登录的用户名
/密码是作为接口的参数来传输， 而 Auth 不是， 但它仍然包含在 request 请求中。<br>
&emsp;&emsp;通过 Postman 填写 Auth（Authorization） 选项。<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.1.PNG)<br>
&emsp;&emsp;通过 Fiddler 工具抓取请求。<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.2.PNG)<br>
&emsp;&emsp;其实， 这个问题难点并不再测试上面。 你是否和我一样好奇， Django 如何来接收这个参数， 以及如何处
理或验证。 为此我翻了很久的 Django 文档， 然而并没有找到想要的结果。 Django-REST-framwork 框架（后面
章节会介绍该框架的使用） 自带的有这样的一个 Auth 的功能， 在接口调用的时候需要填写 Auth 认证。 通过
查看 Django-REST-framwork 框架的源码， 找到了答案。<br>
### 11.1.1、 开发带 Auth 接口
&emsp;&emsp;相信学到这里关于 Django 的开发过程你已经比较熟悉了， 为了练习与安全有关的接口开发， 重新创
建.../sign/views_if_sec.py 视图文件。<br>
&emsp;&emsp;接口的处理逻辑主要由 views 层完成。 所以， 这里只提供 views 层的实现。<br>
views_if_sec.py:<br>
```Python
from django.contrib import auth as django_auth
import hashlib
import base64


# 用户认证
def user_auth(request):
    get_http_auth = request.META.get('HTTP_AUTHORIZATION', b'')
    auth = get_http_auth.split()
    try:
        auth_parts = base64.b64decode(auth[1]).decode('iso-8859-1').partition(':')
    except IndexError:
        return "null"
    userid, password = auth_parts[0], auth_parts[2]
    user = django_auth.authenticate(username=userid, password=password)
    if user is not None and user.id_active:
        django_auth.login(request, user)
        return "success"
    else:
        return "fail"
```
&emsp;&emsp;`get_http_auth = request.META.get('HTTP_AUTHORIZATION', b'')`<br>
&emsp;&emsp;request.META 是一个 Python 字典， 包含了所有本次 HTTP 请求的 Header 信息， 比如用户认证、 IP 地址
和用户 Agent（通常是浏览器的名称和版本号） 等。<br>
&emsp;&emsp;`HTTP_AUTHORIZATION` 用于获取 `HTTP authorization`。如果为空,将得到一个空的bytes对象。<br>
&emsp;&emsp;当客户端传输的认证数据为:admin/admin123456,这里得到的数据是:<br>
&emsp;&emsp;`Basic YWRtaW46YWRtaW4xMjM0NTY=`<br>
&emsp;&emsp;通过 split()方法将其拆分成 list。 拆分后的数据是这样的： `['Basic', 'YWRtaW46YWRtaW4xMjM0NTY=']`<br>
&emsp;&emsp;`auth_parts = base64.b64decode(auth[1]).decode('iso-8859-1').partition(':')`<br>
&emsp;&emsp;取出 list 中的加密串， 通过 base64 对加密串进行解码。 通过decode()方法以UTF-8编码对字符串进行解码。partition()方法以冒号":"为分隔符对字符串进行分割,得到的数据是： ('admin', ':', 'admin123456')<br>
&emsp;&emsp;执行到这一行， 如果获取不到 Auth 信息， 将会抛 IndexError 异常， 通过 try...except...进行异常捕捉， 如
果捕捉到异常将返回“null” 。<br>
&emsp;&emsp;`userid, password = auth_parts[0], auth_parts[2]`<br>
&emsp;&emsp;最后， 取出元组中对应的用户 id 和密码。 最终于数据： admin admin123456<br>
&emsp;&emsp;再接来的处理过程我们就很熟悉了。 调用 Django 的认证模块， 对得到 Auth 信息进行认证。 成功将返回
“success” ， 失败则返回“fail” 。<br>
&emsp;&emsp;在发布会查询接口中调用刚开发的用户认证功能。<br>
```Python
# 发布会查询接口---增加用户认证
def get_event_list(request):
    auth_result = user_auth(request)  # 调用认证函数
    if auth_result == "null":
        return JsonResponse({'status': 10011, 'message': 'user auth null'})
    if auth_result == "fail":
        return JsonResponse({'status': 10012, 'message': 'user auth fail'})
    eid = request.GET.get("eid", "")  # 发布会 id
    name = request.GET.get("name", "")  # 发布会名称
```
&emsp;&emsp;在.../sign/urls.py 文件中添加新的安全接口指向。<br>
```Python
from sign import views_if,views_if_security
urlpatterns = [
......
    # security interface:
    # ex : /api/sec_get_event_list/
    url(r'^sec_get_event_list/', views_if_sec.get_event_list,name='get_event_list'),
]
```
&emsp;&emsp;需要说明的是， 这种认证方式是一种相对较弱的认证方式， 安全性较低。<br>
### 11.1.2、 编写接口文档
&emsp;&emsp;发布会查询接口文档：<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.3.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.4.PNG)<br>
### 11.1.3、接口测试用例
&emsp;&emsp;按照惯例,接下来需要针对开发的接口编写测试用例了,Requests库的get()和post()方法均提供有auth参数,用于设置用户签名。<br>
sec_test_cast.py:<br>
```Python
import unittest
import requests


class GetEventListTest(unittest.TestCase):
    ''' 查询发布会信息（带用户认证） '''

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"
        self.auth_user = ('admin', 'admin123456')

    def test_get_event_list_auth_null(self):
        ''' auth 为空 '''
        r = requests.get(self.base_url, params={'eid': ''})
        result = r.json()
        self.assertEqual(result['status'], 10011)
        self.assertEqual(result['message'], 'user auth null')

    def test_get_event_list_auth_error(self):
        ''' auth 错误 '''
        r = requests.get(self.base_url, auth=('abc', '123'), params={'eid': ''})
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user auth fail')

    def test_get_event_list_eid_null(self):
        ''' eid 参数为空 '''
        r = requests.get(self.base_url, auth=self.auth_user, params={'eid': ''})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'parameter error')

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.base_url, auth=self.auth_user, params={'eid': 1})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['name'], u'mx6 发布会')
        self.assertEqual(result['data']['address'], u'北京国家会议中心')
if __name__ == "__main__":
    unittest.main()
```
## 11.2 数字签名
&emsp;&emsp;在使用 HTTP/SOAP 协议传输数据的时候， 签名作为其中一个参数， 可以起到关键作用：<br>
&emsp;&emsp;一、 鉴权： 通过客户的密钥， 服务端的密钥匹配；<br>
&emsp;&emsp;这个很有好理解， 例如一个接口传参为：<br>
&emsp;&emsp;http://127.0.0.1:8000/api/?a=1&b=2<br>
&emsp;&emsp;假设签名的密钥为： @admin123<br>
&emsp;&emsp;加上签名之后的接口参数为：<br>
&emsp;&emsp;http://127.0.0.1:8000/sign/?a=1&b=2&sign=@admin123<br>
&emsp;&emsp;显然， sign 参数明文传输是不安全的， 所以， 一般会通过加密算法进行加密。<br>
mdt_test.py:<br>
```Python
import hashlib

md5 = hashlib.md5()
sign_str = "@admin123"
sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
md5.update(sign_bytes_utf8)
sign_md5 = md5.hexdigest()
print(sign_md5)
```
&emsp;&emsp;执行程序将会得到： `4b9db269c5f978e1264480b0a7619eea`<br>
&emsp;&emsp;所以， 单做为鉴权， 带签名的接口为：<br>
&emsp;&emsp;http://127.0.0.1:8000/sign/?a=1&b=2&sign=4b9db269c5f978e1264480b0a7619eea<br>
&emsp;&emsp;因为 MD5 算法是不可逆向的， 所以， 当服务器接收到请求后， 同样需要对“@admin123” 进行 MD5 加
密， 然后， 比对与调用者传来的 sign 加密串是否一致， 从而来鉴别调用者是否有权限方位该接口。<br>
&emsp;&emsp;什么是 MD5？<br>
&emsp;&emsp;MD5 即 Message-Digest Algorithm 5（中文名为消息摘要算法第五版） ， 用于确保信息传输完整一致。
是计算机广泛使用的杂凑算法之一， 主流编程语言普遍已有 MD5 实现。<br>
&emsp;&emsp;二、 数据防篡改： 参数是明文传输， 将参数及密钥加密作为签名与服务器匹配；<br>
&emsp;&emsp;同样是这样一个带参数的接口：<br>
&emsp;&emsp;http://127.0.0.1:8000/sign/?a=1&b=2<br>
&emsp;&emsp;加密方式比前者要复杂。<br>
&emsp;&emsp;假设签名的密钥为： @admin123<br>
&emsp;&emsp;签名的明文为： a=1&b=2&api_key=@admin123<br>
&emsp;&emsp;再次通过上面的代码对整个接参与值生成 MD5 加密串： 786bfe32ae1d3764f208e03ca0bfaf13<br>
&emsp;&emsp;所以， 带参数的接口串为：<br>
&emsp;&emsp;http://127.0.0.1:8000/sign/?a=1&b=2&sign=786bfe32ae1d3764f208e03ca0bfaf13<br>
&emsp;&emsp;因为整个接口的参数做了加密， 所以， 只要任意一个参数发改变， 那签名的验证就会失败。 从而起到了
鉴权及数据完整性的保护。<br>
&emsp;&emsp;不过， 接口全参数的加密签名也存在弊端， 因为 MD5 加密是不可逆的， 所以， 服务器端必须已知客户
端的接口参数和值， 否则签名的验证就会失败。 但一般接口在设计时对客户端所请求的参数并不完全已知，
例如， 嘉宾手机号查询， 服务器并不知道客户传的手机号具体是什么， 只是通过数据库来查询该号码是否存
在。<br>
### 11.2.1、 开发接口
&emsp;&emsp;打开.../sign/views_if_security.py 视图文件， 实现接口签名代码。<br>
views_if_security.py:<br>
```Python
import time, hashlib


# 用户签名+时间戳
def user_sign(request):
    if request.method == 'POST':
        client_time = request.POST.get('time', '')  # 客户端时间戳
        client_sign = request.POST.get('sign', '')  # 客户端签名
    else:
        return "error"
    if client_time == '' or client_sign == '':
        return "sign null"
    # 服务器时间
    now_time = time.time()  # 1466426831
    server_time = str(now_time).split('.')[0]
    # 获取时间差
    time_difference = int(server_time) - int(client_time)
    if time_difference >= 60:
        return "timeout"
    # 签名检查
    md5 = hashlib.md5()
    sign_str = client_time + "&Guest-Bugmaster"
    sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    sever_sign = md5.hexdigest()
    if sever_sign != client_sign:
        return "sign error"
    else:
        return "sign right"
```
&emsp;&emsp;实现的代码不多， 但过程有些复杂。 我们来解释一下过程。<br>
&emsp;&emsp;首先，通过 POST 方法获取两个参数 time 和 sign 两个参数，并判断它们其中的任一一个为空，则返回“sign
null” ， 这个逻辑很好理解。<br>
&emsp;&emsp;接下来， 是判断时间戳。 需要客户端获取一个“当前时间戳” ， 取当前的时间。 （例如， 1466830935）<br>
```Python
import time

# 当前时间戳
now_time = time.time()
print('当前时间戳:' + str(now_time))
# 将时间戳转化为字符串类型,并截取小数点前的时间
print(str(now_time).split('.')[0])
# 转换成日期格式
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now_time))
print('日期格式:' + str(otherStyleTime))
"""
D:\Python35\python3.exe C:/Users/Administrator/git/guest/sign/time_test.py
当前时间戳:1525352026.589537
1525352026
日期格式:2018-05-03 20:53:46
"""
```
&emsp;&emsp;Python3 生成的的时间戳精度太高， 我们只需要小数点前面的 10 位即可。 所以， 使用 split()函数截取小
数点前面的时间。<br>
&emsp;&emsp;同样， 当服务器端口拿到客户端传来的时间戳后， 服务器端也需要重新再获取一下当前时间戳。 如果服
务器端的当前时间戳减法去客户端时间戳小于 60， 说明这个接口的请求时间是离现在最近的 60 秒之内。 那么
允许接口访问， 如果超过 60 秒， 则返回“timeout” 。<br>
&emsp;&emsp;这样就要求请求的客户端不断的获取当前戳作为接口参来访问接口。 所以， 一直用固定的参数访问接口
是无效的。<br>
&emsp;&emsp;关于是签名参数的生成。 需要将 api_key（密钥字符串： “&Guest-Bugmaster” ） 和客户端发来的时间戳，
两者拼接成一个新的字符串。 并且通过 MD5 对其进行加密。 从而将加密后的字符串作为 sign 的字段的参数。<br>
&emsp;&emsp;服务器端以同样的规则来生成这样一个加密后的字符串， 从而比较这个串是否相等， 如果相等说明签名
验证通过； 如果不相等， 则返回“sign fail” 。<br>
&emsp;&emsp;将签名功能应用到添加发布会接口中。<br>
views_if_sec.py:<br>
```Python
# 添加发布会接口---增加签名+时间戳
def add_event(request):
    sign_result = user_sign(request)  # 调用签名函数
    if sign_result == "error":
        return JsonResponse({'status': 10011, 'message': 'request error'})
    elif sign_result == "sign null":
        return JsonResponse({'status': 10012, 'message': 'user sign null'})
    elif sign_result == "timeout":
        return JsonResponse({'status': 10013, 'message': 'user sign timeout'})
    elif sign_result == "sign error":
        return JsonResponse({'status': 10014, 'message': 'user sign error'})
```
urls.py:<br>
```Python
from sign import views_if,views_if_security
urlpatterns = [
    ......
    # security interface:
    # ex : /api/sec_add_event/
    url(r'^sec_add_event/', views_if_security.add_event, name='add_event'),
]
```
### 11.2.2、 编写接口文档
&emsp;&emsp;添加发布会接口文档：<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.5.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.6.PNG)<br>
### 11.2.3、 编写接口用例
&emsp;&emsp;学会了带签名接口的实现， 参靠接口文档的描述。 接下来就是编写接口用例环节。 这个接口用现成的接
口工具很难测试。 因为由时间戳和 MD5 加密就让很多接口工具无功为力了。 所以， 写代码才是万能的！<br>
```Python
# coding=utf-8
import unittest
import requests
from time import time
import hashlib


class AddEventTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/api/sec_add_event/"
        # app_key
        self.api_key = "&Guest-Bugmaster"
        # 当前时间
        now_time = time()
        self.client_time = str(now_time).split('.')[0]
        # sign
        md5 = hashlib.md5()
        sign_str = self.client_time + self.api_key
        sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
        md5.update(sign_bytes_utf8)
        self.sign_md5 = md5.hexdigest()

    def test_add_event_request_error(self):
        '''请求方法错误'''
        r=requests.get(self.base_url)
        result=r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'request error')

    def test_add_event_sign_null(self):
        ''' 签名参数为空 '''
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '', 'time': '', 'sign': ''}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10012)
        self.assertEqual(result['message'], 'user sign null')

    def test_add_event_time_out(self):
        ''' 请求超时 '''
        now_time = str(int(self.client_time) - 61)
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '', 'time': now_time, 'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10013)
        self.assertEqual(result['message'], 'user sign timeout')

    def test_add_event_sign_error(self):
        ''' 签名错误 '''
        payload = {'eid': 1, '': '', 'limit': '', 'address': '', 'start_time': '', 'time': self.client_time,
                   'sign': 'abc'}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10014)
        self.assertEqual(result['message'], 'user sign error')

    def test_add_event_eid_exist(self):
        ''' id已经存在 '''
        payload = {'eid': 1, 'name': '一加4发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017',
                   'time': self.client_time, 'sign': self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'event id already exists')

    def test_add_event_name_exist(self):
        ''' 名称已经存在 '''
        payload = {'eid': 11, 'name': '一加3手机发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017',
                   'time': self.client_time, 'sign': self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10023)
        self.assertEqual(result['message'], 'event name already exists')

    def test_add_event_data_type_error(self):
        ''' 日期格式错误 '''
        payload = {'eid': 11, 'name': '一加5手机发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017',
                   'time': self.client_time, 'sign': self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 10024)
        self.assertIn('start_time format error.', result['message'])

    def test_add_event_success(self):
        ''' 添加成功 '''
        payload = {'eid': 11, 'name': '一加4手机发布会', 'limit': 2000, 'address': "深圳宝体", 'start_time': '2017-05-10 12:00:00',
                   'time': self.client_time, 'sign': self.sign_md5}
        r = requests.post(self.base_url, data=payload)
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'add event success')


if __name__ == '__main__':
    unittest.main()
```
## 11.3 接口加密
&emsp;&emsp;PyCrypto 是一个免费的加密算法库， 支持常见的 DES、 AES 加密以及 MD5、 SHA 各种 HASH 运算。 我
们可以在其官方网站下载最新版本： https://www.dlitz.net/software/pycrypto/<br>
&emsp;&emsp;另外， 也可以在 PyPi 仓库中下载安装： https://pypi.python.org/pypi/pycrypto<br>
&emsp;&emsp;目前来看只提供了.tar.gz 包， 所以只能下载安装了。<br>
&emsp;&emsp;PyCrypto 在 Windows 下面安装需要依赖于“vcvarsall.bat”文件， 解决办法是需要安装庞大的 Visual Studio
或者通过其它繁琐的安装才能成功。 所以， 建议读者切换到 Linux（Ubuntu） 下完成本小节的练习。<br>
### 11.3.1、 PyCrypto 库
&emsp;&emsp;PyCrypto 可以做什么？ 在 PyPi 的下载与介绍页面给出了几个简单例子。 接下来就通过这些例子演示
PyCrypto 的强大之处。<br>
例一：<br>
&emsp;&emsp;SHA-256 算法属于密码 SHA-2 系列哈希。 它产生了一个消息的 256 位摘要。<br>
&emsp;&emsp;哈希值用作表示大量数据的固定大小的唯一值。 两组数据的哈希值仅在相应数据也匹配时才应当匹配。
数据的少量更改会在哈希值中产生不可预知的大量更改。<br>
&emsp;&emsp;接下来的例子演示 SHA256 模块的使用。<br>
SHA256_test.py:<br>
```Python
from Crypto.Hash import SHA256

hash = SHA256.new()
hash.update(b'message')
h = hash.digest()
# h= hash.hexdigest
print(h)
```
&emsp;&emsp;执行程序：<br>
```Python
fnngj@fnngj-pc:~/pydj$ python3 SHA256_test.py
b'\xabS\n\x13\xe4Y\x14\x98+y\xf9\xb7\xe3\xfb\xa9\x94\xcf\xd1\xf3\xfb"\xf7\x1c\x
ea\x1a\xfb\xf0+F\x0cm\x1d'
```
&emsp;&emsp;该加密字符串就是通过将“message” 加密之后得到。 当然， 也可以将其转换为 16 进制的字符串。 只需
要将 digest()方法替换为 hexdigest()方法即可。<br>
&emsp;&emsp;再次执行程序：<br>
```Python
fnngj@fnngj-pc:~/pydj$ python3 SHA256_test.py
ab530a13e45914982b79f9b7e3fba994cfd1f3fb22f71cea1afbf02b460c6d1d
```
例二：<br>
&emsp;&emsp;AES 是 Advanced Encryption Standard 的缩写， 高级加密标准， 是目前非常流行的加密算法之一。<br>
&emsp;&emsp;通过例子演示 AES 算法的加密与解密。<br>
AES_test.py:<br>
```Python
from Crypto.Cipher import AES

# 加密
obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
message = "The answer is no"
ciphertext = obj.encrypt(message)
print(ciphertext)

# 解密
obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
s = obj2.decrypt(ciphertext)
print(s)
```
&emsp;&emsp;加密：<br>
&emsp;&emsp;`“This is a key123”` 为 key， 长度有着严格的要求， 必须为 16、 24 或 32 位， 否则将会看到下面的错误。<br>
&emsp;&emsp;`ValueError: AES key must be either 16, 24, or 32 bytes long`<br>
&emsp;&emsp;`“This is an IV456”` 为 VI， 长度要求更加严格， 只能为 16 位。 否则， 你将会看到下面的错误。<br>
&emsp;&emsp;`ValueError: IV must be 16 bytes long`<br>
&emsp;&emsp;然后， 通过 encrypt()方法对“message” 字符串进行加密。 然后， 通过打印将会得到：<br>
```
fnngj@fnngj-pc:~/pydj$ python3 crypto_demo.py
b'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
```
&emsp;&emsp;解密：<br>
&emsp;&emsp;当接收到加密的字符串后， 解密者必须知道加密时所用的 key 和 VI 才能正能够解密。<br>
&emsp;&emsp;通过 decrypt()方法对加密后的字符串进行解密。<br>
```
fnngj@fnngj-pc:~/pydj$ python3 crypto_demo.py
b'The answer is no'
```
&emsp;&emsp;如果 key 和 VI 错误将无法得到正确的字符串。 例如， 把 key 修改为： 'This is a key888'， 解密失败， 我
们将会得到另一个加密字符串：<br>
```
b'\xb1\xf7\xc2\x9d\xf7|&\x05\x89\\\xa7\x17\x16\x06\x9b\xf4'
```
例三：<br>
&emsp;&emsp;除此之外， PyCrypto 还提供一个强大的随机算法。<br>
random_test.py:<br>
```Python
from Crypto.Random import random

r = random.choice(['dogs', 'cats', 'bears'])
print(r)
```
### 11.3.2、 AES 加密接口开发
&emsp;&emsp;按照管例， 既然对加密算法有了初步的了解， 接下来要让其应用到接口开发中。 嗯， 我们要开发一个用
AES 加密算法的接口。<br>
&emsp;&emsp;这一小节的例子最为复杂， 涉及到不少知识点。 为了实现这一节的例子， 我翻阅了不少资料， 做好准备
和我一起实现它吧！<br>
interface_AES_test.py:<br>
```Python
from Crypto.Cipher import AES
import base64
import requests
import unittest
import json


class AESTest(unittest.TestCase):
    def setUp(self):
        BS = 16
        self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

        self.base_url = "http://127.0.0.1:8000/api/sec_get_guest_list/"
        self.app_key = 'W7v4D60fds2Cmk2U'

    def encryptBase64(self, src):
        return base64.urlsafe_b64encode(src)

    def encryptAES(self, src, key):
        """
        生成AES密文
        """
        iv = b"1172311105789011"
        cryptor = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cryptor.encrypt(self.pad(src))
        return self.encryptBase64(ciphertext)

    def test_aes_interface(self):
        '''test aes interface'''
        payload = {'eid': '1', 'phone': '13800138000'}
        # 加密
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()

        r = requests.post(self.base_url, data={"data": encoded})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "success")

if __name__ == '__main__':
    unittest.main()
```
&emsp;&emsp;将上面的代码拆解后分别进行介绍。<br>
&emsp;&emsp;`self.app_key = 'W7v4D60fds2Cmk2U'`<br>
&emsp;&emsp;首先， 定义好 app_key 和接口参数， app_key 是密钥， 只有合法的调用者才知道， 这个一定要保密噢！ 这
里同样选择使用字典格式来存放接口参数。<br>
&emsp;&emsp;`payload = {'eid': '1', 'phone': '13800138000'}`<br>
&emsp;&emsp;`encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()`<br>
&emsp;&emsp;首先将 payload 参数转化为 json 格式， 然后将参数和 app_key 传参给 encryptAES()方法用于生成加密串。<br>
```Python
def encryptAES(self,src, key):
    """生成 AES 密文"""
    iv = b"1172311105789011"
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cryptor.encrypt(self.pad(src))
    return self.encryptBase64(ciphertext)
```
&emsp;&emsp;IV 同样是保密的， 并且我们前面知道它必须是 16 位字节。 然后通过 encrypt()方法对 src 接口参数生成
加密串， 但是这里会有问题。 encrypt()要加密的字符串有严格的长度要求， 长度必须是 16,24,32 位。 如果直接
生成可能会提示：`ValueError: Input strings must be a multiple of 16 in length`<br>
&emsp;&emsp;可是， 被加密字符串的长度是不可控。 接口参数的个数和长度可能会随意的变化。 所以， 为了解决这个
问题， 还需要对参数字符串时行处理， 使其长度固定。<br>
&emsp;&emsp;`self.pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)`<br>
&emsp;&emsp;这是函数式编程的一种用法， 通过 lambda 定义匿名函数来对字符串进行补足， 使其长度为 16,24,32 位。
再接下来生成的字符串是这样的：<br>
&emsp;&emsp;`b'>_\x80\x1fi\x97\x8f\x94~\xeaE\xectBm\x9d\xa9\xc5\x85<+e\xa5lW\xe1\x84}\xfa\x8b\xb9\xde\x1a\x10J\xcd\
xc5\xa1A4Z\xff\x05x\xe3\xf1\x00Z'`<br>
&emsp;&emsp;但这样的字符串太长， 并不太适合传输。<br>
```Python
def encryptBase64(self,src):
    return base64.urlsafe_b64encode(src)
```
&emsp;&emsp;通过 base64 模块的 urlsafe_b64encode()方法对 AES 加密串进行二次加密。
然后得到的字符串是这样的：<br>
&emsp;&emsp;`b'gouBbuKWEeY5wWjMx-nNAYDTion0ADOysaLw1uzzGOpvTTASpQGJu5p0WuDhZMiM'`<br>
&emsp;&emsp;到此， 加密过程结束。<br>
&emsp;&emsp;`r = requests.post(self.base_url, data={"data": encoded})`<br>
&emsp;&emsp;将加密后的字符串作为接口的 data 参数发送给接口。<br>
&emsp;&emsp;当服务器接收到字符串之后， 如何对加密串进行解密处理呢？ 下接来开发服务器端的处理。<br>
views_if_sec_example.py:<br>
```Python
from Crypto.Cipher import AES

# =======AES 加密算法===============
BS = 16
unpad = lambda s: s[0: - ord(s[-1])]


def decryptBase64(src):
    return base64.urlsafe_b64decode(src)


def decryptAES(src, key):
    """
    解析 AES 密文
    """
    src = decryptBase64(src)
    iv = b"1172311105789011"
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    text = cryptor.decrypt(src).decode()
    return unpad(text)


def aes_encryption(request):
    app_key = 'W7v4D60fds2Cmk2U'
    if request.method == 'POST':
        data = request.POST.get("data", "")
    else:
        return "error"
    # 解密
    decode = decryptAES(data, app_key)
    # 转化为字典
    dict_data = json.loads(decode)
    return dict_data
```
&emsp;&emsp;`app_key = 'W7v4D60fds2Cmk2U'`<br>
&emsp;&emsp;服务器端与合法客户端约定的密钥 app_key。<br>
```Python
if request.method == 'POST':
    data = request.POST.get("data", "")
else:
    return "error"
```
&emsp;&emsp;判断客户端请求是否为 POST， 通过 POST.get()方法接收 data 参数。<br>
&emsp;&emsp;`decode = decryptAES(data, app_key)`<br>
&emsp;&emsp;调用解密函数 decryptAES() ， 传参加密字符串和 app_key。<br>
```Python
def decryptAES(src, key):
    """解析 AES 密文 """
    src = decryptBase64(src)
    iv = b"1172311105789011"
    cryptor = AES.new(key, AES.MODE_CBC, iv)
    text = cryptor.decrypt(src).decode()
    return unpad(text)
```
&emsp;&emsp;首先， 调用 decryptBase64()方法， 将 Base64 加密字符串解密为 AES 加密字符串。 然后， 通过 decrypt()
对 AES 加密串进行解密。<br>
```Python
def decryptBase64(src):
return base64.urlsafe_b64decode(src)
```
&emsp;&emsp;对 Base64 字符串解密。<br>
```Python
BS = 16
unpad = lambda s : s[0: - ord(s[-1])]
```
&emsp;&emsp;最后， 通过 upad 匿名函数对字符串的长度还原。 到此， 解密过程结束。<br>
```Python
dict_data = json.loads(decode)
return dict_data
```
&emsp;&emsp;将解密后字符串通过 json.loads()方法转化成字典， 并将该字典做为 aes_encryption()函数的返回值。<br>
&emsp;&emsp;在获取嘉宾例表的接口中调用 aes_encryption()函数进行 AES 加密字符串解密。<br>
views_if_sec_example.py:<br>
```Python
# 嘉宾查询接口----AES 算法
def get_guest_list(request):
    dict_data = aes_encryption(request)

    if dict_data == "error":
        return JsonResponse({'status': 10011, 'message': 'request error'})

    eid = dict_data['eid']
    phone = dict_data['phone']

    if eid == '':
        return JsonResponse({'status': 10021, 'message': 'eid cannot be empty'})
    if eid != '' and phone == '':
        datas = []
        results = Guest.objects.filter(event_id=eid)
        if results:
            for r in results:
                guest = {}
                guest['realname'] = r.realname
                guest['phone'] = r.phone
                guest['email'] = r.email
                guest['sign'] = r.sign
                datas.append(guest)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
        else:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
    if eid != '' and phone != '':
        guest = {}
        try:
            result = Guest.objects.get(phone=phone, event_id=eid)
        except ObjectDoesNotExist:
            return JsonResponse({'status': 10022, 'message': 'query result is empty'})
        else:
            guest['realname'] = result.realname
            guest['phone'] = result.phone
            guest['email'] = result.email
            guest['sign'] = result.sign
            return JsonResponse({'status': 200, 'message': 'success', 'data': guest})
```
&emsp;&emsp;在.../sign/urls.py 文件中添加新的安全接口指向。<br>
```Python
from sign import views_if,views_if_security
urlpatterns = [
    ......
    # security interface:
    # ex : /aip/sec_add_event/
    url(r'^sec_get_guest_list/', views_if_sec_example.get_guest_list,name='get_guest_list'),
]
```
### 11.3.3、 编写接口文档
&emsp;&emsp;查询嘉宾接口文档：<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.7.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.8.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter11/image/11.9.PNG)<br>
### 11.3.4、 补充接口测试用例
&emsp;&emsp;最后， 再来补充一些 AES 加密接口的测试用例。<br>
```Python
def test_get_guest_list_eid_null(self):
        ''' eid 参数为空 '''
        payload = {'eid': '', 'phone': ''}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()

        r = requests.post(self.base_url, data={"data": encoded})
        result = r.json()
        self.assertEqual(result['status'], 10021)
        self.assertEqual(result['message'], 'eid cannot be empty')

    def test_get_event_list_eid_error(self):
        ''' 根据 eid 查询结果为空 '''
        payload = {'eid': '901', 'phone': ''}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()

        r = requests.post(self.base_url, data={"data": encoded})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        payload = {'eid': '1', 'phone': ''}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()

        r = requests.post(self.base_url, data={"data": encoded})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data'][0]['realname'], '张三')
        self.assertEqual(result['data'][0]['phone'], '13800138000')

    def test_get_event_list_eid_phone_null(self):
        ''' 根据 eid 和phone 查询结果为空 '''
        payload = {'eid': 2, 'phone': '10000000000'}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()

        r = requests.post(self.base_url, data={"data": encoded})
        result = r.json()
        self.assertEqual(result['status'], 10022)
        self.assertEqual(result['message'], 'query result is empty')

    def test_get_event_list_eid_phone_success(self):
        ''' 根据 eid 和phone 查询结果成功 '''
        payload = {'eid': 1, 'phone': '18633003301'}
        encoded = self.encryptAES(json.dumps(payload), self.app_key).decode()

        r = requests.post(self.base_url, data={"data": encoded})
        result = r.json()
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], 'success')
        self.assertEqual(result['data']['realname'], 'alen')
        self.assertEqual(result['data']['phone'], '18633003301')


if __name__ == '__main__':
    unittest.main()
```
&emsp;&emsp;定义好 AES 算法的加密方法， 接口测试是需要调用即可， 过程并不复杂。<br>
# chapter12 Web Service
## 12.1 Web Service 相关概念
### 1.SOA
&emsp;&emsp;Service Oriented Ambiguity 中文一般理解为， 面向服务架构， 简称 SOA。<br>
&emsp;&emsp;SOA 的提出是在企业计算领域， 就是要将紧耦合的系统， 划分为面向业务的， 粗粒度， 松耦合， 无状态
的服务。 服务发布出来供其他服务调用， 一组互相依赖的服务就构成了 SOA 架构下的系统。<br>
&emsp;&emsp;既然说是一种架构的话， 所以一般认为 SOA 是包含了运行环境， 编程模型， 架构风格和相关方法论等在
内的一整套新的分布式软件系统构造方法和环境， 涵盖服务的整个生命周期。<br>
&emsp;&emsp;Service-architecture.com 将 SOA 定义为：<br>
&emsp;&emsp;本质上是服务的集合。 服务间彼此通信， 这种通信可能是简单的数据传送， 也可能是两个或更多的服务
协调进行某些活动。 服务间需要某些方法进行连接。<br>
&emsp;&emsp;所谓服务就是精确定义、 封装完善、 独立于其他服务所处环境和状态的函数。<br>
&emsp;&emsp;虽然不同厂商或个人对 SOA 有着不同的理解， 但是我们仍然可以从上述的定义中看到 SOA 的几个关键
特性：<br>
&emsp;&emsp;一种粗粒度、 松耦合服务架构， 服务之间通过简单、 精确定义接口进行通讯， 不涉及底层编程接口和通
讯模型。<br>
&emsp;&emsp;对于 SOA 来说， 读者并不需要太过较真 SOA 到是一个怎样的架构。 只要符合它的定义和规范的软件系
统都可以认为是 SOA 架构。<br>
### 2.SOA 与 Web Service
&emsp;&emsp;早在 1996 年 Gartner 就前瞻性地提出了面向服务架构的思想(SOA)， Web Service 不知为何物， SOA 还只
是束之高阁的理论概念。 直到 2000 年以后， W3C 才成立了相关的委员会， 开始讨论 Web Service 的相关标准，
各大厂商一边积极参与标准制定， 一边推出了一系列实实在在的产品。 新的技术和新的产品出现， SOA 找到
了可以依托的凭借。 随着 Web Service 技术的推出和应用， SOA 的思想被一个个效益显著的信息系统建设项
目不断的示范， 才逐渐成为现今的热门话题。<br>
&emsp;&emsp;因为现在几乎所有的 SOA 应用场合都是和 Web Service 绑定的， 所以不免有时候这两个概念混用。 不可
否认 Web Service 是现在最适合实现 SOA 的技术， SOA 的走红在很大程度上归功于 Web Service 标准的成熟和
应用普及。 因为现在大家基本上认同 Web Service 技术在几方面体现了 SOA 的需要：<br>
&emsp;&emsp;首先， 是基于标准访问的独立功能实体满足了松耦合要求： 在 Web Service 中所有的访问都通过 SOAP
访问进行， 用 WSDL 定义的接口封装， 通过 UDDI 进行目录查找， 可以动态改变一个服务的提供方而无需影
响客户端的配置， 外界客户端是根本不关心访问服务器端的实现。<br>
&emsp;&emsp;其次， 适合大数据量低频率访问符合服务大颗粒度功能： 基于性能和效率平衡的要求， SOA 的服务提供
的是大颗粒度的应用功能， 而且跨系统边界的访问频率也不会象程序间函数调用那么频繁。 通过使用 WSDL
和基于文本(Literal)的 SOAP 请求， 可以实现能一次性接收处理大量数据。<br>
&emsp;&emsp;最后， 基于标准的文本消息传递为异构系统提供通讯机制： Web Service 所有的通讯是通过 SOAP 进行的，
而 SOAP 是基于 XML 的， XML 是结构化的文本消息。 从最早的 EDI 开始， 文本消息也许是异构系统间通讯
最好的消息格式， 适用于 SOA 强调的服务对异构后天宿主系统的透明性。<br>
&emsp;&emsp;综合上述观点， Web Service 不愧为当前 SOA 的最好选择。 然而， 就 SOA 思想本身而言， 并不一定要局
限于 Web Service 方式的实现。 更应该看到的是 SOA 本身强调的是实现业务逻辑的敏捷性要求， 是从业务应
用角度对信息系统实现和应用的抽象。 随着人们认识的提高， 还会有新技术不断的发明出来， 更好的来满足
这个要求。<br>
&emsp;&emsp;上面涉及的名词太多， 我们等一下还会单一的来介绍， 用一句话总结它们之间的关系。 “SOA 不是 Web
Service， Web Service 是目前最适合实现 SOA 的技术。 ”<br>
### 3.Web Service
&emsp;&emsp;在解释 Web Service 之前， 先抛出一个问题。 有没有一种办法可以实现跨应用程序进行通信和跨平台进
行通信呢？<br>
&emsp;&emsp;跨应用程序， 主要是指开发的 A 系统和开发的 B 系统之间是否可以通信。<br>
&emsp;&emsp;跨平台， 主要是指用 Java 开发的系统和用.NET 开发的系统是否可以通信。<br>
&emsp;&emsp;这样的需求有很多， 例如腾讯 QQ 上面自带的天气功能。<br>
![image](https://github.com/15529343201/guest/blob/chapter12/image/12.1.PNG)<br>
&emsp;&emsp;腾讯要想获得实时的天气信息怎么办呢？ 有一种办法， 那就是腾讯公司放个卫星上天， 并且在公司中成
立一个气象部门， 实时的收集天气信息， 然后实时为腾讯 QQ 提供天气预报信息； 这显然不是一种明智的做法，
腾讯 QQ 只是想获取一下天气信息， 居然要如此高的成本。<br>
&emsp;&emsp;更简单的做法是由中国气象台提供实时的天气信息， 然后， 通过提供接口的方式给腾讯 QQ 调用。 那么
这就遇到我上面所说的问题， 如何跨应用与跨平台调用接口。<br>
&emsp;&emsp;这个时候有聪明的读者会跳出来说， 你傻啊！ 用 HTTP 协议啊， 主流的编程语言都可以实现基于 HTTP
协议的应用开发。 让中国气象台写个基于 HTTP 协议的天气接口给腾讯 QQ 调用就可以了。 嗯！ 这是完全可以
的。 不过， Web Service 之所以在 HTTP 之后被提出自然有它的特点。<br>
&emsp;&emsp;当然， 这里拿 Web Service 与 HTTP 进行比较是不太合适的。 因为 HTTP 是互联网上应用最为广泛的一
种网络协议。 而 Web Service 是一种部署在 Web 上的对象或者是应用程序组件， Web Service 数据的传输同样
需要借助 HTTP 协议。<br>
&emsp;&emsp;Web Service 详细的描述：<br>
&emsp;&emsp;Web Service 是一个平台独立的， 低耦合的， 自包含的、 基于可编程的 web 的应用程序， 可使用开放的
XML（标准通用标记语言下的一个子集） 标准来描述、 发布、 发现、 协调和配置这些应用程序， 用于开发分
布式的互操作的应用程序。<br>
### 4.SOAP
&emsp;&emsp;Simple Object Access Protocol， 中文为简单对象访问协议， 简称 SOAP。<br>
&emsp;&emsp;SOAP 是基于 XML 在分散或分布式的环境中交换信息的简单的协议。允许服务提供者和服务客户经过防
火墙在 INTERNET 进行通讯交互。<br>
&emsp;&emsp;SOAP 的设计是为了在一个松散的、分布的环境中使用 XML 对等地交换结构化的和类型化的信息提供了
一个简单且轻量级的机制。<br>
&emsp;&emsp;XML 是可以扩展标记语言。<br>
```HTML
<bookstore>
    <book category="COOKING">
        <title lang="en">Everyday Italian</title>
        <author>Giada De Laurentiis</author>
        <year>2005</year>
        <price>30.00</price>
    </book>
</bookstore>
```
&emsp;&emsp;SOAP 消息的基本结构<br>
```HTML
<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2001/12/soap-envelope"
soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">
    <soap:Header>
        ...
        ...
    </soap:Header>
    <soap:Body>
        ...
        ...
        <soap:Fault>
        ...
        ...
        </soap:Fault>
    </soap:Body>
</soap:Envelope>
```
&emsp;&emsp;当 SOAP 消息真正需要在网络上实际传输的时候， SOAP 消息能够与不同的底层传输协议进行绑定， 同
时， SOAP 消息可以在很多种消息传输模式中使用。包括超文本传输协议（HTTP）， 简单邮件传输协议（SMTP），
多用途网际邮件扩充协议（MIME） 。 它还支持从消息系统到远程过程调用协议（RPC） 等大量的应用程序。<br>
&emsp;&emsp;当然，最多的情况还是还是绑定在 HTTP 协议上面传输。所以，导致大多数人认为 SOAP 就是 HTTP + XML，
或者认为 SOAP 是 HTTP post 请求的一个专用版本， 遵循一种特殊的 XML 消息格式。<br>
&emsp;&emsp;虽然， 我们看到的情况确实如此， 但这并不是 SOAP 本质与全部。<br>
![image](https://github.com/15529343201/guest/blob/chapter12/image/12.2.PNG)<br>
&emsp;&emsp;如图 12.2， 为 SOAP 消息实例， 通过 SOAP 消息实例： 利用 HTTP 传输协议向手机号码查询服务请求的
SOAP 消息。<br>
### 5.WSDL
&emsp;&emsp;Web Services Description Language， 网络服务描述语言， 简称 WSDL。 它是一门基于 XML 的语言， 用
于描述 Web Services 以及如何对它们进行访问。<br>
&emsp;&emsp;WSDL 文档主要使用以下几个元素来描述某个 Web Service：<br>
&emsp;&emsp;<portType> web service 执行的操作。<br>
&emsp;&emsp;<message> web service 使用的消息。<br>
&emsp;&emsp;<types> web service 使用的数据类型。<br>
&emsp;&emsp;<binding> web service 使用的通信协议。<br>
```HTML
<wsdl:definitions xmlns:wsa="http://schemas.xmlsoap.org/ws/2003/03/addressing"
xmlns:tns="tns" xmlns:plink="http://schemas.xmlsoap.org/ws/2003/05/partner-li
nk/" xmlns:xop="http://www.w3.org/2004/08/xop/include"xmlns:senc="http://schem
as.xmlsoap.org/soap/encoding/" xmlns:s12env="http://www.w3.org/2003/05/soap-en
velope/" xmlns:s12enc="http://www.w3.org/2003/05/soap-encoding/" xmlns:xs="htt
p://www.w3.org/2001/XMLSchema"xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" xm
lns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:senv="http://schemas
.xmlsoap.org/soap/envelope/" xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/
"targetNamespace="tns" name="Application">
<wsdl:types>
<xs:schema targetNamespace="tns" elementFormDefault="qualified">
<xs:import namespace="http://www.w3.org/2001/XMLSchema"/>
<xs:complexType name="say_hello">
<xs:sequence>
<xs:element name="name" type="xs:string" minOccurs="0" nillable="true"
/>
</xs:sequence>
</xs:complexType>
<xs:complexType name="say_helloResponse">
<xs:sequence>
<xs:element name="say_helloResult" type="xs:string" minOccurs="0" nill
able="true"/>
</xs:sequence>
</xs:complexType>
<xs:element name="say_hello" type="tns:say_hello"/>
<xs:element name="say_helloResponse" type="tns:say_helloResponse"/>
</xs:schema>
</wsdl:types>
<wsdl:message name="say_hello">
<wsdl:part name="say_hello" element="tns:say_hello"/>
</wsdl:message>
<wsdl:message name="say_helloResponse">
<wsdl:part name="say_helloResponse" element="tns:say_helloResponse"/>
</wsdl:message>
<wsdl:portType name="Application">
<wsdl:operation name="say_hello" parameterOrder="say_hello">
<wsdl:input name="say_hello" message="tns:say_hello"/>
<wsdl:output name="say_helloResponse" message="tns:say_helloResponse"/>
</wsdl:operation>
</wsdl:portType>
<wsdl:binding name="Application" type="tns:Application">
<soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/h
ttp"/>
<wsdl:operation name="say_hello">
<soap:operation soapAction="say_hello" style="document"/>
<wsdl:input name="say_hello">
<soap:body use="literal"/>
</wsdl:input>
<wsdl:output name="say_helloResponse">
<soap:body use="literal"/>
</wsdl:output>
</wsdl:operation>
</wsdl:binding>
<wsdl:service name="Application">
<wsdl:port name="Application" binding="tns:Application">
<soap:address location="http://10.2.70.10:7789/SOAP/?wsdl"/>
</wsdl:port>
</wsdl:service>
</wsdl:definitions>
```
- WSDL 端口

&emsp;&emsp;<portType> 元素是最重要的 WSDL 元素。<br>
&emsp;&emsp;它可描述一个 web service、 可被执行的操作， 以及相关的消息。 可以把 <portType> 元素比作传统编程
语言中的一个函数库（或一个模块、 或一个类） 。<br>
- WSDL 消息

&emsp;&emsp;<message> 元素定义一个操作的数据元素。<br>
&emsp;&emsp;每个消息均由一个或多个部件组成。 可以把这些部件比作传统编程语言中一个函数调用的参数。<br>
- WSDL types

&emsp;&emsp;<types> 元素定义 web service 使用的数据类型。<br>
&emsp;&emsp;为了最大程度的平台中立性， WSDL 使用 XML Schema 语法来定义数据类型。<br>
- WSDL Bindings

&emsp;&emsp;<binding> 元素为每个端口定义消息格式和协议细节。<br>
&emsp;&emsp;对于接口来说， 接口文档非常重要， 它描述如何访问接口。 那么 WSDL 就可以看作 Web Service 接口的
一种标准格式的“文档” 。 我们通过阅读 WSDL 就知道如何调用 Web Service 接口了。<br>
### 6.UDDI
&emsp;&emsp;Universal Description, Discovery and Integration"， 可译为“通用描述、 发现与集成服务”， 简称 UDDI。<br>
&emsp;&emsp;WSDL 用来描述了访问特定的 Web Service 的一些相关的信息， 那么在互联网上， 或者是在企业的不同
部门之间， 如何来发现我们所需要的 Web Service 呢？ 而 Web Service 提供商又如何将自己开发的 Web Serivce
公布到因特网上呢？ 这就需要使用到 UDDI 了。<br>
&emsp;&emsp;UDDI 是一个独立于平台的框架， 通过使用 Internet 来描述服务， 发现企业， 并对企业服务进行集成。<br>
&emsp;&emsp;UDDI 指的是通用描述、 发现与集成服务。<br>
&emsp;&emsp;UDDI 是一种用于存储有关 Web Services 的信息的目录。<br>
&emsp;&emsp;UDDI 是一种由 WSDL 描述的 Web Services 界面的目录。<br>
&emsp;&emsp;UDDI 经由 SOAP 进行通信。<br>
&emsp;&emsp;UDDI 被构建入了微软的 .NET 平台<br>
&emsp;&emsp;如图 12.3、 图 12.4， 为 UDDI 的安装与发布。<br>
![image](https://github.com/15529343201/guest/blob/chapter12/image/12.3.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter12/image/12.4.PNG)<br>
&emsp;&emsp;UDDI 可以帮助 Web 服务提供商在互联网上发布 Web Services 的信息。 UDDI 是一种目录服务， 企业可
以通过 UDDI 来注册和搜索 Web Services。<br>
&emsp;&emsp;通过上面的介绍， SOAP、 WSDL 和 UDDI 就构成了 Web Service 的三要素。<br>
### 7.Web Services 体系结构
在 Web Serivce 的体系结构中涉及到三个角色， 一个是 Web Service 提供者， 一个是 Web Service 中介， 还
有一个就是 Web Service 请求者； 同时还涉及到三类动作， 即发布， 查找， 绑定。<br>
- Web Service 提供者：

&emsp;&emsp;可以发布 Web Service， 并且对使用自身服务的请求进行响应， Web Service 的拥有者， 它会等待其他的服
务或者是应用程序访问自己。<br>
- Web Service 请求者：

&emsp;&emsp;也就是 Web Service 功能的使用者，它通过服务注册中心也就是 Web Service 中介者查找到所需要的服务，
再利用 SOAP 消息向 Web Service 提供者发送请求以获得服务。<br>
- Web Service 中介：

&emsp;&emsp;也称为服务代理， 用来注册已经发布的 Web Service 提供者， 并对其进行分类， 同时提供搜索服务， 简单
来说的话， Web Service 中介者的作用就是把一个 Web Service 请求者和合适的 Web Service 提供者联系在一起，
充当一个管理者的角色， 一般是通过 UDDI 来实现。<br>
&emsp;&emsp;发布： 通过发布操作， 可以使 Web Serivce 提供者向 Web Service 中介注册自己的功能以及访问的接口。<br>
&emsp;&emsp;发现（查找）： 使得 Web Service 请求者可以通过 Web Service 中介者来查找到特定种类的 Web Service 接
口。<br>
&emsp;&emsp;绑定： 这里就是实现让 Web Serivce 请求者能够使用 Web Serivce 提供者提供的 Web Serivce 接口。<br>
&emsp;&emsp;最后， 回答前面的问题， Web Service 相对于 HTTP 有何不同？<br>
&emsp;&emsp;1.接口中实现的方法和要求参数一目了然。<br>
&emsp;&emsp;2.不用担心大小写问题。<br>
&emsp;&emsp;3.不用担心中文 urlencode 问题。<br>
&emsp;&emsp;4.代码中不用多次声明认证（账号， 密码） 参数。<br>
&emsp;&emsp;5.传递参数可以为数组， 对象等。<br>
&emsp;&emsp;那么， 第二个问题， Web Service 能被 HTTP 替代么？ 答案是肯定的。<br>
## 12.2 Web Service 开发与调用
&emsp;&emsp;开发 Web Service 接口并非 Python 语言所擅长的， 而且开发出来的 Web Service 接口的性能也不敢恭维，
好在， 谁让 Python 简单呢。 能找不少相关的开发和测试类库。<br>
### 12.2.1、 suds-jurko 调用接口
&emsp;&emsp;Suds 是 Web Service 客户端是一个轻量级的基于 SOAP 的 python 客户端。<br>
&emsp;&emsp;Suds 项目在 pypi 仓库的地址： https://pypi.python.org/pypi/suds/<br>
&emsp;&emsp;然后， 2010 年 9 月之后， 该项目就不再更新了， 虽然， 在 Python2.x 下面仍然可以使用该项目， 但是我们
更希望能用到较新的库。<br>
&emsp;&emsp;于是， 我又在 Python 仓库中找到了 Suds-jurko， Suds-jurko 基于 Suds， 它的目的是希望是原有的 Suds 项
目继续得到发展。<br>
&emsp;&emsp;Suds-jurko 项目在 pypi 仓库的地址： https://pypi.python.org/pypi/suds-jurko<br>
&emsp;&emsp;然而， 该项目的更新只持续到 2014 年 1 月， 好在， 它支持了 Python3.x， 我们将 zip 包下载并解压， 然后
进入解压目录执行以下命令进行安装。<br>
```Python
...\suds-jurko-0.6> python3 setup.py install
……
Installed c:\python35\lib\site-packages\suds_jurko-0.6-py3.5.egg
Processing dependencies for suds-jurko==0.6
Finished processing dependencies for suds-jurko==0.6
```
&emsp;&emsp;`python3 -m pip install suds-jurko`<br>
&emsp;&emsp;下来就 Web Service 接口的调用了， 前提是得先有 Web Service 接口才行， 别着急， wexml.com.cn 网站提
供了一些发布的 Web Service 接口， 例如， 天气的查询、 电话号码归属地查询、 以及国内飞机航班的查询等服
务。<br>
&emsp;&emsp;网站地址： http://www.webxml.com.cn/zh_cn/web_services.aspx<br>
&emsp;&emsp;有了这些， 就可以给我们拿来练手了。<br>
&emsp;&emsp;先以手机号码归属地的查询为例， 创建 soap_client.py 文件：<br>
soap_client.py:<br>
```Python
# -*- coding=utf-8 -*-
from suds.client import Client
# 使用库 suds_jurko： https://bitbucket.org/jurko/suds
# web service 查询： http://www.webxml.com.cn/zh_cn/web_services.aspx
# 电话号码归属地查询
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
print(client)
```
&emsp;&emsp;执行程序， 得到如下结果：<br>
```Python
...\test> python3 soap_client.py
Suds ( https://fedorahosted.org/suds/ ) version: 0.6
Service ( MobileCodeWS ) tns="http://WebXml.com.cn/"
	Prefixes (1)
		ns0 = "http://WebXml.com.cn/"
	Ports (2):
		(MobileCodeWSSoap)
			Methods (2):
				getDatabaseInfo()
				getMobileCodeInfo(xs:string mobileCode, xs:string userID)
			Types (1):
				ArrayOfString
		(MobileCodeWSSoap12)
			Methods (2):
				getDatabaseInfo()
				getMobileCodeInfo(xs:string mobileCode, xs:string userID)
			Types (1):
				ArrayOfString
```
&emsp;&emsp;通过打印信息， 我们知道该接口提供 getDatabaseInfo()方法用来查询号码归属地。 那么就可以在程序中调
用该方法了。<br>
soap_client.py:<br>
```Python
# 使用库 suds_jurko： https://bitbucket.org/jurko/suds
# web service 查询： http://www.webxml.com.cn/zh_cn/web_services.aspx
# 电话号码归属地查询
url = 'http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl'
client = Client(url)
result = client.service.getMobileCodeInfo(186xxxxxxxx)
print(result)
```
&emsp;&emsp;为了隐私， 我故意到将代码中的电话号码后 8 位用“x” 字母做了替换， 读者可以使用任意号码来替换。
再次运行程序得到结果如下。<br>
```
...\test> python3 soap_client.py
186xxxxxxxx： 河南 郑州 河南联通 GSM 卡
```
&emsp;&emsp;这么简单就可以实现调用了， 那我们再来调用一下首都北京的天气。<br>
soap_client2.py:<br>
```Python
from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import
url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
imp = Import('http://www.w3.org/2001/XMLSchema',
location='http://www.w3.org/2001/XMLSchema.xsd')
imp.filter.add('http://WebXml.com.cn/')
client = Client(url, plugins=[ImportDoctor(imp)])
result = client.service.getWeatherbyCityName("北京")
print(result)
```
```
C:\Users\Administrator\git\guest>python3 soap_client2.py
(ArrayOfString){
   string[] =
      "直辖市",
      "北京",
      "54511",
      "54511.jpg",
      "2018/5/4 12:47:49",
      "16℃/27℃",
      "5月4日 晴转多云",
      "西南风转北风小于3级",
      "0.gif",
      "1.gif",
      "今日天气实况：气温：23℃；风向/风力：南风 2级；湿度：34%；紫外线强度：强
。空气质量：中。",
      "紫外线指数：强，涂擦SPF大于15、PA+防晒护肤品。
健臻·血糖指数：易波动，血糖易波动，注意监测。
感冒指数：少发，无明显降温，感冒机率较低。
穿衣指数：舒适，建议穿长袖衬衫单裤等服装。
洗车指数：较适宜，无雨且风力较小，易保持清洁度。
空气污染指数：中，易感人群应适当减少室外活动。
",
      "15℃/25℃",
      "5月5日 多云",
      "北风小于3级",
      "1.gif",
      "1.gif",
      "13℃/27℃",
      "5月6日 晴",
      "西南风小于3级",
      "0.gif",
      "0.gif",
      "北京位于华北平原西北边缘，市中心位于北纬39度，东经116度，四周被河北省围着
，东南和天津市相接。全市面积一万六千多平方公里，辖12区6县，人口1100余万。北京为
暖温带半湿润大陆性季风气候，夏季炎热多雨，冬季寒冷干燥，春、秋短促，年平均气温10
-12摄氏度。北京是世界历史文化名城和古都之一。早在七十万年前，北京周口店地区就出
现了原始人群部落“北京人”。而北京建城也已有两千多年的历史，最初见于记载的名字为
“蓟”。公元前1045年北京成为蓟、燕等诸侯国的都城；公元前221年秦始皇统一中国以来
，北京一直是中国北方重镇和地方中心；自公元938年以来，北京又先后成为辽陪都、金上
都、元大都、明清国都。1949年10月1日正式定为中华人民共和国首都。北京具有丰富的旅
游资源，对外开放的旅游景点达200多处，有世界上最大的皇宫紫禁城、祭天神庙天坛、皇
家花园北海、皇家园林颐和园，还有八达岭、慕田峪、司马台长城以及世界上最大的四合院
恭王府等各胜古迹。全市共有文物古迹7309项，其中国家文物保护单位42个，市级文物保护
单位222个。北京的市树为国槐和侧柏，市花为月季和菊花。另外，北京出产的象牙雕刻、
玉器雕刻、景泰蓝、地毯等传统手工艺品驰誉世界。",
}
```
### 12.2.2、 spyne 开发接口
&emsp;&emsp;比起 Web Service 接口的调用， 我更好奇如何开发 Web Service 接口。 因为通过前面的概念介绍， 它看上
去是个很复杂的技术。 万能的 Python， 我想应该能找到开发 Web Service 应用的库。 还真有。<br>
&emsp;&emsp;soaplib 项目在 PyPi 仓库的地址： https://pypi.python.org/pypi/soaplib<br>
&emsp;&emsp;然后， 这个项目到 2011 年 3 月就停止更新了。 Python2.x 的用户仍然可以使用该库开发 Web Service 接
口， 然后， 它确实有点旧了。 于是， 我又找到了 spyne。<br>
&emsp;&emsp;spyne 项目在 PyPi 仓库的地址： https://pypi.python.org/pypi/spyne<br>
&emsp;&emsp;spyne官方网站:http://spyne.io/<br>
&emsp;&emsp;用 spyne 开发 Web Service 应用和 soaplib 一样简单， 最主要的是它支持 Python3.x， 并且在持续更新。<br>
&emsp;&emsp;spyne 支持使用 pip 命令安装（建议在 Linux 系统下安装） 。<br>
&emsp;&emsp;`> python3 -m pip install spyne`<br>
&emsp;&emsp;参考 spyne 官方文档， 开发一个简单的 Web Service 接口。<br>
```Python
from spyne import Application, rpc, ServiceBase, Iterable, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication


class HelloWorldService(ServiceBase):

	@rpc(Unicode, Integer, _returns=Iterable(Unicode))
	
	def say_hello(ctx, name, times):
		"""Docstrings for service methods appear as documentation in the wsdl.
		<b>What fun!</b>
		@param name the name to say hello to
		@param times the number of times to say hello
		@return the completed array
		"""
		for i in range(times):
			yield u'Hello, %s' % name

application = Application([HelloWorldService], 'spyne.examples.hello.soap',
						   in_protocol=Soap11(validator='lxml'),
						   out_protocol=Soap11())

wsgi_application = WsgiApplication(application)



if __name__ == '__main__':
	import logging
	from wsgiref.simple_server import make_server
	logging.basicConfig(level=logging.DEBUG)
	logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
	logging.info("listening to http://127.0.0.1:8000")
	logging.info("wsdl is at: http://127.0.0.1:8000/?wsdl")
	server = make_server('127.0.0.1', 8000, wsgi_application)
server.serve_forever()
```
&emsp;&emsp;这里开发了一个 say_hello()的接口，它需要两个参数， name 和 times，接口会对 name 返回一定次数（itmes）
的“hello, name” ， 相当简单。<br>
```
C:\Users\Administrator\git\guest>python3 soap_server.py
INFO:root:listening to http://127.0.0.1:8000
INFO:root:wsdl is at: http://127.0.0.1:8000/?wsdl
```
&emsp;&emsp;前面已经介绍了 Suds-jurko 的使用， 这里直接使用它来调用接口。<br>
```Python
from suds.client import Client
url = "http://192.168.127.128:8000/?wsdl"
client = Client(url)
result = client.service.say_hello("bugmaster", 3)
print(result)
```
&emsp;&emsp;执行结果：<br>
```
...\test> python3 soap_client3.py
(stringArray){
	string[] =
		"Hello, bugmaster",
		"Hello, bugmaster",
		"Hello, bugmaster",
}
```
## 12.3 Jmeter 测试 SOAP 接口
&emsp;&emsp;在本书的第九章中介绍了 Jmeter 工具的使用， 对于 SOAP 协议开发的 Web Service 接口。 Jmeter 同样支
持 SOAP 接口的的测试。<br>
&emsp;&emsp;打开 Jmeter 工具， 创建 SOAP 接口测试。 如图 12.5， 右键点击“线程组” -->“添加” -->“Sampler” -->
“SOAP/XML-RPC Requests” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter12/image/12.5.PNG)<br>
&emsp;&emsp;以查询手机号码归属地的接口为例：<br>
&emsp;&emsp;http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl<br>
&emsp;&emsp;通过 Wireshark 抓包工具捕捉 SOAP 请求。<br>
![image](https://github.com/15529343201/guest/blob/chapter12/image/12.6.PNG)<br>
&emsp;&emsp;XML 格式的 SOAP 请求信息如下：<br>
```
<SOAP-ENV:Envelope
	xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/"
	xmlns:ns1="http://WebXml.com.cn/"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
	<SOAP-ENV:Header/>
	<ns0:Body>
		<ns1:getMobileCodeInfo>
			<ns1:mobileCode>186xxxxxxxx</ns1:mobileCode>
		</ns1:getMobileCodeInfo>
	</ns0:Body>
</SOAP-ENV:Envelope>
```
![image](https://github.com/15529343201/guest/blob/chapter12/image/12.7.PNG)<br>
&emsp;&emsp;如图 12.7，配置SOAP/XML-RPC请求。URL填写查询手机号码归属地的Web Service地址。Soap/XML-PRC
Data 填写 XML 格式的 SOAP 请求数据。<br>
&emsp;&emsp;运行测试， 查看结果树， 如图 12.8。<br>
![image](https://github.com/15529343201/guest/blob/chapter12/image/12.8.PNG)<br>
# chapter13 REST
&emsp;&emsp;关于 Web Service 技术， 关于上一章中介绍的并不完整， REST 同样属于 Web Service 技术。 REST 定义
了一组体系架构原则， 您可以根据这些原则设计以系统资源为中心的 Web 服务， 包括使用不同语言编写的客
户端如何通过 HTTP 处理和传输资源状态。 如果考虑使用它的 Web 服务的数量， REST 近年来已经成为最主
要的 Web 服务设计模型。 事实上， REST 对 Web 的影响非常大， 由于其使用相当方便， 已经普遍地取代了基
于 SOAP 和 WSDL 的接口设计。<br>
## 13.1 RPC 与 REST
### 1.RPC
&emsp;&emsp;RPC 即 Remote Procedure Call 的缩写，远程过程调用。它是 Web Service 领域广为流行的一个种开发风格。<br>
&emsp;&emsp;RPC 风格的开发关注于服务器/客户端之间的方法调用， 而并不关注基于哪个网络层的哪种协议。 RPC 风
格的代表是 XML-RPC 和大 Web 服务。<br>
&emsp;&emsp;（1） XML-RPC<br>
&emsp;&emsp;XML-RPC 是一种使用 XML 格式封装方法调用， 并使用 HTTP 协议作为传送机制的 RPC 风格的实现。
XML-RPC 的请求方法都是 HTTP 协议的 POST 方法， 请求和响应的数据格式均为 XML。<br>
&emsp;&emsp;XML-RPC 是一种遗留技术， 已经被 SOAP 取代。 著名的测试用例管理系统 TestLink 的对外接口就是使
用 PHP 开发的 XML-RPC。<br>
&emsp;&emsp;（2） 大 Web 服务<br>
&emsp;&emsp;大 Web 服务（Big Web Service） 是对基于 SOAP+WSDL+UDDI 等技术实现 RPC 风格的大型 Web 服务的
统称。 本书第十二章介绍就是该项技术。<br>
### 2.REST
&emsp;&emsp;REST（即 Representational State Transfer 的缩写） 中文翻译为“表现层状态转化” 。<br>
&emsp;&emsp;REST 具有夸语言、 夸平台的特点。 所以， 它是一种遵循 REST 式风格的 Web Service。<br>
&emsp;&emsp;如果一个架构符合 REST 原则， 就称它为 RESTful 架构。 要理解 RESTful 架构， 最好的方法就是去理解
Representational State Transfer 这个词组到底是什么意思， 它的每一个词代表了什么涵义。 如果你把这个名称搞
懂了， 也就不难体会 REST 是一种什么样的设计。<br>
&emsp;&emsp;一、 资源（Resources）<br>
&emsp;&emsp;REST 的名称"表现层状态转化"中， 省略了主语。 "表现层"其实指的是"资源"（Resources） 的"表现层"。
所谓"资源"， 就是网络上的一个实体， 或者说是网络上的一个具体信息。 它可以是一段文本、 一张图片、
一首歌曲、 一种服务， 总之就是一个具体的实在。 你可以用一个 URI（统一资源定位符） 指向它， 每种资源对
应一个特定的 URI。 要获取这个资源， 访问它的 URI 就可以， 因此 URI 就成了每一个资源的地址或独一无二
的识别符。<br>
&emsp;&emsp;所谓"上网"， 就是与互联网上一系列的"资源"互动， 调用它的 URI。<br>
&emsp;&emsp;二、 表现层（Representation）<br>
&emsp;&emsp;"资源"是一种信息实体， 它可以有多种外在表现形式。 我们把"资源"具体呈现出来的形式， 叫做它的"表
现层"（Representation） 。<br>
&emsp;&emsp;比如， 文本可以用 txt 格式表现， 也可以用 HTML 格式、 XML 格式、 JSON 格式表现， 甚至可以采用二
进制格式； 图片可以用 JPG 格式表现， 也可以用 PNG 格式表现。<br>
&emsp;&emsp;URI 只代表资源的实体， 不代表它的形式。 严格地说， 有些网址最后的“.html” 后缀名是不必要的， 因
为这个后缀名表示格式， 属于“表现层” 范畴， 而 URI 应该只代表“资源” 的位置。 它的具体表现形式， 应
该在 HTTP 请求的头信息中用 Accept 和 Content-Type 字段指定， 这两个字段才是对"表现层"的描述。<br>
&emsp;&emsp;三、 状态转化（State Transfer）<br>
&emsp;&emsp;访问一个网站， 就代表了客户端和服务器的一个互动过程。 在这个过程中， 势必涉及到数据和状态的变
化。<br>
&emsp;&emsp;互联网通信协议 HTTP 协议， 是一个无状态协议。 这意味着， 所有的状态都保存在服务器端。 因此， 如
果客户端想要操作服务器， 必须通过某种手段， 让服务器端发生“状态转化” （State Transfer） 。 而这种转化
是建立在表现层之上的， 所以就是"表现层状态转化"。<br>
&emsp;&emsp;客户端用到的手段， 只能是 HTTP 协议。 具体来说， 就是 HTTP 协议里面， 四个表示操作方式的动词：
GET、 POST、 PUT、 DELETE。 它们分别对应四种基本操作： GET 用来获取资源， POST 用来新建资源（也可
以用于更新资源） ， PUT 用来更新资源， DELETE 用来删除资源。<br>
&emsp;&emsp;综合上面的解释， 我们总结一下什么是 RESTful 架构：<br>
&emsp;&emsp;（1） 每一个 URI 代表一种资源；<br>
&emsp;&emsp;（2） 客户端和服务器之间， 传递这种资源的某种表现层；<br>
&emsp;&emsp;（3） 客户端通过四个 HTTP 动词， 对服务器端资源进行操作， 实现"表现层状态转化"。<br>
&emsp;&emsp;引用资料:http://www.ruanyifeng.com/blog/2011/09/restful<br>
&emsp;&emsp;关于 Web Service 相关的概念基本都做了介绍， 通过一个图来表明概念和技术的包含关系。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.1.PNG)<br>
## 13.2 Django-REST-Framework
&emsp;&emsp;Django REST Framework,顾名思义,是一套基于Django的REST风格的框架。<br>
&emsp;&emsp;它具有以下特点:<br>
- 功能强大、灵活,可以帮助你快速开发Web API。
- 支持认证策略,包括OAuth 1a和OAuth 2。
- 支持ORM和非ORM数据源的序列化。
- 丰富的文档以及良好的社区支持。

&emsp;&emsp;`python3 -m pip install djangorestframework`<br>
### 13.2.1、 创建简单的 API
&emsp;&emsp;当Django REST Framework安装好之后,创建一个新的项目django_test,在项目下创建"api"应用。<br>
```
>django-admin startproject django_rest
>cd django_rest
\django_rest>python3 manage.py startapp api
```
&emsp;&emsp;打开 settings.py 文件添加应用：<br>
settings.py:<br>
```
# Application definition
INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'api',
] 

# 在文件末尾添加
REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
	'PAGE_SIZE': 10
}
```
&emsp;&emsp;"rest_framework"为Django RESTFramework应用,"api"为我们自己创建的应用。默认的权限策略可以设置
在全局范围内,通过DEFAULT_PERMISSION_CLASSES设置。<br>
&emsp;&emsp;通过"migrate"命令执行数据库迁移。<br>
&emsp;&emsp;`\django_rest>python3 manage.py migrate`<br>
&emsp;&emsp;创建超级管理员账户。<br>
```Python
\django_rest>python3 manage.py createsuperuser
Username (leave blank to use 'fnngj'): admin
Email address: admin@mail.com
Password:
Password (again):
Superuser created successfully.
```
&emsp;&emsp;创建数据序列化， 创建.../api/serializers.py 文件。<br>
```Python
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url', 'username', 'email', 'groups')
		
class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')
```
&emsp;&emsp;Serializers用于定义API的表现形式,如返回哪些字段,返回怎样的格式等.这里序列化Django自带的User和Group。<br>
&emsp;&emsp;编写视图文件,打开api应用下的views.py文件,编写如下代码。<br>
views.py:<br>
```Python
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer

# ViewSets定义视图的展现形式
class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
```
&emsp;&emsp;在Django REST Framework中,ViewSets用于定义视图的展现形式,例如返回哪些内容,需要做哪些权限处理。<br>
&emsp;&emsp;在URL中会定义相应的规则到ViewSet。ViewSets则通过serializer_class找到对应的Serializers。这里
将User和Group的所有对象赋予queryset,并返回这些值。在UserSerializer和GroupSerializer中定义要返回的字段。<br>
&emsp;&emsp;打开/django_test/urls.py文件,添加api的路由配置。<br>
urls.py:<br>
```Python
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from api import views

#Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^',include(router.urls)),
	url(r'^api-auth/',include('rest_framework.urls',namespace='rest_framework')),
]
```
&emsp;&emsp;因为我们使用的是 viewset， 所以我们可以使用 routers 类自动生成 URL conf。<br>
&emsp;&emsp;通过"runserver"命令启动服务。<br>
```Python
...\django_rest>python3 manage.py runserver
Performing system checks...
System check identified no issues (0 silenced).
November 21, 2016 - 21:50:18
Django version 1.10.3, using settings 'django_rest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
&emsp;&emsp;通过浏览器打开： http://127.0.0.1:8000/， 图 13.2<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.2.PNG)<br>
### 13.2.2、 添加接口数据
&emsp;&emsp;现在， 点击页面右上角“Log in” 登录系统， 账号为刚刚创建的超级管理员帐号登录。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.3.PNG)<br>
&emsp;&emsp;点击： http://127.0.0.1:8000/groups/ 链接， 添加用户组。 图 13.4。 添加“test” 组和“developer” 组。<br>
&emsp;&emsp;点击： http://127.0.0.1:8000/users/链接， 添加用户。 图 13.5。 添加用户“tom” 和“jack” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.4.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.5.PNG)<br>
### 13.2.3、 测试接口
&emsp;&emsp;关于 REST 风格实现的 API 并无特别之处， 我们通过同样可以使用 requests 库进其进行测试。 针对用户
组与用户的查询编写测试用例。<br>
rest_test.py:<br>
```Python
import unittest
import requests

class UserTest(unittest.TestCase):
	'''用户查询测试'''
	def setUp(self):
		self.base_url = 'http://127.0.0.1:8000/users'
		self.auth = ('admin', 'admin123456')
		
	def test_user1(self):
		'''test user 1 '''
		r = requests.get(self.base_url+'/1/', auth=self.auth)
		result = r.json()
		self.assertEqual(result['username'], 'admin')
		self.assertEqual(result['email'], 'admin@mail.com')
		
	def test_user2(self):
		'''test user 2 '''
		r = requests.get(self.base_url+'/2/', auth=self.auth)
		result = r.json()
		self.assertEqual(result['username'], 'jack')
		self.assertEqual(result['email'], 'jack@mail.com')
		
	def test_user3(self):
		'''test user 3 '''
		r = requests.get(self.base_url+'/3/', auth=self.auth)
		result = r.json()
		self.assertEqual(result['username'], 'tom')
		self.assertEqual(result['email'], 'tom@mail.com')
		
class GroupsTest(unittest.TestCase):
	'''用户组查询测试'''
	
	def setUp(self):
		self.base_url = 'http://127.0.0.1:8000/groups'
		self.auth = ('admin','admin123456')
		
	def test_groups1(self):
		'''test groups 1 '''
		r = requests.get(self.base_url+'/1/', auth=self.auth)
		result = r.json()
		self.assertEqual(result['name'], 'test')
		
	def test_groups2(self):
		'''test groups 2 '''
		r = requests.get(self.base_url+'/2/', auth=self.auth)
		result = r.json()
		self.assertEqual(result['name'], 'developer')
		
if __name__ == '__main__':
	unittest.main()
```
&emsp;&emsp;需要注意的是,请求接口的资源不是通过接口参数(?user=1)访问,而是通过URI路径(/1/)访问。
另外,接口的访问需要用户签名,在发送get()请求时需要指定auth参数。<br>
## 13.3 集成发布会系统 API
&emsp;&emsp;在本书的第八章， 根据发布会签到系统我们开发相关的接口， 通过 Django-REST-Framework 框架来实现
接口要简单得多。<br>
13.3.1、 添加发布会 API
&emsp;&emsp;接下来在 django_rest 项目的基础上增加发布会和嘉宾管理的接口。<br>
&emsp;&emsp;创建模型， 打开.../api/models.py 文件。<br>
models.py:<br>
```Python
from django.db import models

# Create your models here.
# 发布会
class Event(models.Model):
	name = models.CharField(max_length=100)
	limit = models.IntegerField()
	status = models.BooleanField()
	address = models.CharField(max_length=200)
	start_time = models.DateTimeField('events time')
	create_time = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

# 嘉宾
class Guest(models.Model):
	event = models.ForeignKey(Event)
	realname = models.CharField(max_length=64)
	phone = models.CharField(max_length=16)
	email = models.EmailField()
	sign = models.BooleanField()
	create_time = models.DateTimeField(auto_now=True)
	class Meta:
		unique_together = ('phone', 'event')
	def __str__(self):
		return self.realname
```
&emsp;&emsp;进行数据库迁移：<br>
&emsp;&emsp;`python3 manage.py makemigrations api`<br>
&emsp;&emsp;`python3 manage.py migrate`<br>
&emsp;&emsp;添加发布会数据序列化， 打开.../api/serializers.py 文件， 添加。<br>
serializers.py:<br>
```Python
from api.models import Event, Guest
class EventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Event
		fields = ('url','name','address','start_time','limit','status')
		
class GuestSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Guest
		fields = ('url','realname','phone','email','sign','event')
```
&emsp;&emsp;打开api应用下的views.py文件,定义发布会和嘉宾视图类<br>
```Python
from api.serializers import EventSerializer, GuestSerializer
from api.models import Event, Guest
class EventViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows events to be viewed or edited.
	"""
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	
class GuestViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows guests to be viewed or edited.
	"""
	queryset = Guest.objects.all()
	serializer_class = GuestSerializer
```
&emsp;&emsp;打开.../django_rest/urls.py 文件， 添加 URL 配置.<br>
urls.py:<br>
```Python
router.register(r'event', views.EventViewSet)
router.register(r'guest', views.GuestViewSet)
```
&emsp;&emsp;重新启动项目,通过浏览器打开http://127.0.0.1:8000/,如图13.6所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.6.PNG)<br>
### 13.3.2、 测试接口
&emsp;&emsp;使用Django REST Framework开发的接口,除了可以使用GET方法查询接口之外,还可以调用接口添加数据,
并不需要关心接口插入数据的细节,只需将接口请求改为POST即可。使用Postman添加一条发布会数据,如图13.7所示<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.7.PNG)<br>
&emsp;&emsp;Postman 接口配置参数如下：<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.8.PNG)<br>
## 13.4 soapUI测试工具
&emsp;&emsp;soapUI是一款针对REST和SOAP的功能和性能测试工具。<br>
&emsp;&emsp;官方地址:https://www.soapui.org/<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.9.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.10.PNG)<br>
### 13.4.1 创建SOAP测试项目
&emsp;&emsp;创建一个 SOAP 项目， 左侧项目列表， 右键“Projects” --->“New SOAP Project” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.11.PNG)<br>
&emsp;&emsp;以查询号码归属地为例：<br>
&emsp;&emsp;Project Name： MobileCodeWS 为项目名称。<br>
&emsp;&emsp;Initial WSDL： http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl 为接口地址。<br>
&emsp;&emsp;点击“OK” 按钮， 创建项目完成。<br>
&emsp;&emsp;依次展开 MobileCodeWS-->MobileCodeWSSoap-->getMobileCodeInfo/， 双击“Request 1” ， 如下图 13.11。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.12.PNG)<br>
&emsp;&emsp;点击 Request 1 窗口左上角的运行按钮， 发送 SOAP 请求。 右侧窗口将会显示接口返回结果。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.13.PNG)<br>
### 13.4.2、 创建 REST 测试项目
&emsp;&emsp;创建一个 SOAP 项目， 左侧项目列表， 右键“Projects” --->“New REST Project” 。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.14.PNG)<br>
&emsp;&emsp;URI： http://127.0.0.1:8000/users/ 为接口地址。<br>
&emsp;&emsp;点击“OK” 按钮， 创建项目完成。<br>
&emsp;&emsp;依次展开： REST Project 1-->User[/users/]-->Users-->Request 1。 如下图 13.11。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.15.PNG)<br>
&emsp;&emsp;单击"Request 1"窗口左下角的"Auth"按钮,在Authorization选项中选择"add New Authorization",在
弹出的窗口中选择"Basic"选项,单击"OK"按钮,如图13.14所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.16.PNG)<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.17.PNG)<br>
&emsp;&emsp;填写用户认证 Username 和 Password（admin/admin123456） ， 勾选“Authenticate pre-emptvely”
选项。<br>
- Username:用于填写基本认证的用户名。
- Password:用于填写基本认证的密码。
- Domain:域名是基本认证的可选项,设置为空。
- Pre-emptive auth:设置定义认证的行为。
- Use global preference:用于定义HTTP设置为全局首选项。
- Authenticate pre-emptively:仅适用于此请求,不需要等待身份验证时才发送凭据。

&emsp;&emsp;如果想要查询具体的某一条发布会信息,则可以在Resource输入框中指定发布会id.<br>
&emsp;&emsp;随后， 点击 Request 1 窗口中左上角的运行按钮， 右则窗口显示接口查询结果。<br>
![image](https://github.com/15529343201/guest/blob/chapter13/image/13.18.PNG)<br>
&emsp;&emsp;关于 soapUI 工具就介绍到这里， 想了解该工具的更多使用， 请参考官方文档：<br>
&emsp;&emsp;https://www.soapui.org/soapui-projects/soapui-projects.html<br>
# chapter14 Django项目部署
&emsp;&emsp;VMware:http://www.vmware.com/cn.html<br>
&emsp;&emsp;Ubuntu:https://www.ubuntu.com<br>
## 14.1 uWSGI
### 14.1.1 uWSGI介绍
&emsp;&emsp;什么是WSGI?<br>
&emsp;&emsp;WSGI,全称为Web Server Gateway Interface,是为Python语言定义的Web服务器和Web应用程序或框架之间的
一种简单而通用的接口。<br>
&emsp;&emsp;WSGI是Web服务器与Web应用程序或应用框架之间的一种低级别的接口,用以提升可移植Web应用开发的共同点。
许多Python Web框架都自带WSGI服务,如Flask、webpy、Django等。但自带的WSGI服务性能一般,更多的是用来测试,在项目正式
发布时,大多数情况使用生产环境的WSGI服务或者联合Nginx做uwsgi。<br>
&emsp;&emsp;什么是uWSGI?<br>
&emsp;&emsp;uWSGI是一个Web服务器,它实现了WSGI、uwsgi、HTTP等协议。在Nginx中ngx_http_uwsgi_module的作用
是与uWSGI服务器进行交换。<br>
&emsp;&emsp;关于WSGI、uwsgi、uWSGI三个概念的区分:<br>
- WSGI是Web服务器与Web应用程序或应用框架之间的接口,也可以看做一个协议。
- uwsgi是一种传输协议
- uWSGI是实现了uwsgi和WSGI两种协议的Web服务器。

&emsp;&emsp;uwsgi协议是一个uWSGI服务器自带的协议,它用于定义传输信息的类型,每一个uwsgi packet的前4byte都为传输
信息类型描述,它与WSGI相比是不同的两个协议。<br>
&emsp;&emsp;uwsgi协议:http://uwsgi-docs.readthedocs.io/en/latest/Protocol.html<br>
### 14.1.2 安装uWSGI
&emsp;&emsp;PyPi仓库地址:https://pypi.python.org/pypi/uWSGI<br>
&emsp;&emsp;测试uWSGI,创建test.py文件。<br>
test.py:<br>
```Python
def application(env, start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b"Hello World"]
```
&emsp;&emsp;通过"uwsgi"命令运行test.py文件。<br>
&emsp;&emsp;`root@ubuntu-virtual-machine:~/桌面/guest# uwsgi --http :8001 --wsgi-file test.py`<br>
&emsp;&emsp;通过浏览器访问:http://127.0.0.1:8001/,如图14.1所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter14/image/14.1.png)<br>
### 14.1.3 uWSGI运行Django
&emsp;&emsp;接下来通过uWSGI运行Django项目,此处假定Django的项目路径为/home/fnngj/pydj/guest<br>
`uwsgi --http :8000 --chdir /home/fnngj/pydj/guest/ --wsgi-file guest/wsgi.py --master --processes 4 --stats 127.0.0.1:9191`<br>
&emsp;&emsp;uwsgi命令常用参数如下。<br>
- --http:协议类型和端口号
- --processes:开启的进程数量
- --workers:开启的进程数量,等同于processes
- --chdir:指定运行目录
- --wsgi-file:载入wsgi-file(加载wsgi.py文件)
- --stats:在指定的地址上开启状态服务
- --threads:开启的线程数量
- --master:允许主进程存在
- --daemonize:使进程在后台运行,并将日志输出到指定的日志文件或者UDP服务器
- --pidfile:指定pid文件的位置,记录主进程的PID号
- --vacuum:当服务器退出时自动清理环境,删除Unix Socket文件和PID文件

# 14.2 Nginx
&emsp;&emsp;Nginx是一款轻量级的Web服务器/反向代理服务器及电子邮件(IMAP/POP3)代理服务器,并在一个BSD-like协议下进行。<br>
&emsp;&emsp;采用Nginx+uWSGI的组合来部署Django是较为常见的部署方案之一.在这个方案中,通常的做法是将Nginx作为服务器
最前端,用它来接受Web的所有请求,统一管理请求。Nginx可用来处理所有静态请求,这是Nginx的强项。然后,Nginx将所有非静态请求
通过uWSGI传递给Django,由Django处理,从而完成一次Web请求。可见,uWSGI的作用类似于一个桥接器,起到链接Nginx和Django的作用。<br>
&emsp;&emsp;Nginx官网:http://nginx.org/<br>
### 14.2.1 安装Nginx
&emsp;&emsp;`sudo apt-get install nginx #安装`<br>
&emsp;&emsp;`/etc/init.d/nginx start #启动`<br>
&emsp;&emsp;`/etc/init.d/nginx stop #关闭`<br>
&emsp;&emsp;`/etc/init.d/nginx restart #重启`<br>
&emsp;&emsp;`nginx -v # 查看版本`<br>
&emsp;&emsp;修改Nginx默认端口号,打开/etc/nginx/sites-available/default配置文件,修改端口号<br>
```
server {
	listen 8088 default_server;
	listen [::]:8088 default_server ipv6only=on;
```
&emsp;&emsp;将默认的80端口号修改成其他端口号,如8088,因为默认的80端口号通常会被其他程序占用。然后,通过上面
的命令重启Nginx。访问http://127.0.0.1:8088/<br>
&emsp;&emsp;如图14.2所示,说明Nginx已经可以工作了。<br>
![image](https://github.com/15529343201/guest/blob/chapter14/image/14.2.png)<br>
### 14.2.2 Nginx+uWSGI+Django
&emsp;&emsp;接下来,我们将Nginx、uWSGI和Django三者整合起来。发布会签到系统的目录结构如下。<br>
```
guest/
|--manage.py
|--guest/
|  |--__init__.py
|  |--settings.py
|  |--urls.py
|  |--wsgi.py
|--django_uwsgi.ini
```
&emsp;&emsp;在创建guest项目时,在guest/目录下默认已经生成了wsgi.py文件。创建django_uwsgi.ini文件,配置uWSGI参数,
uWSGI支持多种类型的配置文件,如xml、ini等。此处使用ini类型的配置。<br>
django_uwsgi.ini:<br>
```
[uwsgi]
# 请求方式与端口号
socket = :8000
# Django项目路径
chdir = /home/ubuntu/桌面/guest
# wsgi文件
module = guest.wsgi
# 允许主进程存在
master = true
# 开启进程数
processes = 3
# 当服务器退出时自动清理环境
vacuum = true
```
&emsp;&emsp;这个配置文件,其实就相当于把"uwsgi"命令运行Django项目的参数给文件化了。<br>
&emsp;&emsp;socket:指定请求的方式和端口号。这里要特别注意,如果想直接通过uWSGI访问Django项目,那么这里要配置为http;
如果想要通过Nginx请求uWSGI来访问Django项目,那么这里就要配置为socket。<br>
&emsp;&emsp;8000为通过uWSGI访问Django项目的端口号<br>
&emsp;&emsp;chdir:指定Web项目的根目录<br>
&emsp;&emsp;module:配置guest.wsgi.可以这样理解这个配置,对于django_uwsgi.ini文件来说,与它平级的有一个guest/目录,
这个目录下有一个swgi.py文件。<br>
&emsp;&emsp;另外几个参数,可以参考前面uWSGI的常用参数说明。<br>
&emsp;&emsp;接下来切换到guest项目中,通过"uwsgi"命令读取django_uwsgi.ini文件启动Web项目。<br>
&emsp;&emsp;`root@ubuntu-virtual-machine:~/桌面/guest# uwsgi --ini django_uwsgi.ini`<br>
&emsp;&emsp;注意查看uWSGI的启动信息,如果有错,就要检查配置文件的的参数是否设置错误。<br>
&emsp;&emsp;接下来修改Nginx配置文件。打开/etc/nginx/sites-available/default文件,在文件底部添加如下配置。<br>
```
server {
	listen 8089;
	listen [::]:8089;

	server_name 127.0.0.1 192.168.240.137;

	location / {
		include /etc/nginx/uwsgi_params;
		uwsgi_pass 127.0.0.1:8000;
	}
}
```
&emsp;&emsp;这是一个极简配置。<br>
&emsp;&emsp;listen指定的是Nginx代理uWSGI对外的端口号。<br>
&emsp;&emsp;server_name指定Nginx代理uWSGI对外的IP地址;可以指定多个IP或域名,127.0.0.1指向的是本机,192.168.240.137为本机的IP地址,配置这个IP地址是为了给局域网内的其他主机访问。<br>
&emsp;&emsp;Nginx是如何将请求转发给uWSGI的呢?现在看来大概最主要的就是这两行配置:<br>
```
include /etc/nginx/uwsgi_params;
uwsgi_pass 127.0.0.1:8000;
```
&emsp;&emsp;include必须指定为uwsgi_params文件,如果启动失败,则需要指定该文件的绝对路径,通常在/etc/nginx/目录下;而uwsgi_pass所指的本机IP端口号与guest_uwsgi.ini配置文件中的IP端口号必须一致。<br>
&emsp;&emsp;配置完成后,保存退出default文件,重新启动Nginx。<br>
&emsp;&emsp;访问http://127.0.0.1:8089/或http://192.168.240.137:8089/。<br>
&emsp;&emsp;访问页面时,请求会先到Nginx,再由Nginx转到uWSGI Web容器来处理,如图14.3所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter14/image/14.3.png)<br>
### 14.2.3 处理静态资源
&emsp;&emsp;当访问页面时,发现所有静态资源都无法访问了<br>
&emsp;&emsp;打开/etc/nginx/sites-available/default文件,添加Web项目的静态资源。<br>
```
server {
	listen 8089;
	listen [::]:8089;

	server_name 127.0.0.1 192.168.240.137;

	location / {
		include /etc/nginx/uwsgi_params;
		uwsgi_pass 127.0.0.1:8000;
	}
	# 配置静态文件目录
	location /static {
		alias /home/ubuntu/桌面/guest/sign/static;
	}
}
```
&emsp;&emsp;guest项目的静态文件的存放目录为../sign/static/,所以配置如上。重启nginx,再来访问签到页面,样式文件即可正常引用了。<br>
## 14.3 创建404页面
settings.py:<br>
`DEBUG = False`<br>
&emsp;&emsp;把DEBUG设置为"False"。关闭DEGUG后,需要设置ALLOWED_HOSTS<br>
&emsp;&emsp;ALLOWED_HOSTS是为了限定请求中的host值,以防止黑客构造包来发送请求。只有列表中的host才能访问。一般不建议使用"*"通配符去配置,当DEBUG设置为"Fasle"时必须设置这个配置,否则会抛出异常。<br>
&emsp;&emsp;在.../guest/settings.py文件中,配置模板如下。<br>
`ALLOWED_HOSTS = ['www.baidu.com']`<br>
&emsp;&emsp;在.../sign/templates/目录下面创建404.html页面。<br>
404.html:<br>
```html
</html>
<html lang="zh-CN">
<head>
    <title>404</title>
</head>
<body>
    <div>
        <img src="/static/image/404error.jpg" />
    </div>
</body>
</html>
```
# chapter15 接口性能测试
## 15.1 Locust性能测试工具
&emsp;&emsp;谈到性能测试工具,我们首先想到的是LoadRunner或JMeter<br>
&emsp;&emsp;LoadRunner是非常有名的商业性能测试工具,功能非常强大,使用也较为复杂,目前大多介绍性能测试
的书籍都以该工具为基础,甚至有些书整本都在介绍LoadRunner的使用。<br>
&emsp;&emsp;JMeter同样是非常有名的开源性能测试工具,功能也很完善,在本书中介绍它作为接口测试工具的使用。但实际上,
它是一个标准的性能测试工具。JMeter相关的资料也非常丰富,它的官方文档也很完善。<br>
&emsp;&emsp;Locust同样是性能测试工具,虽然官方这样来描述它:"An open source laod testing tool.",但他和前面两个工具有着较大
的不同。与前面两个工具相比,他在功能上要差上很多,但也并非全无优点。<br>
&emsp;&emsp;Locust完全基于Python编程语言,采用Pure Python描述测试脚本,并且HTTP请求完全基于Requests库。
除了HTTP/HTTPS协议外,Locust还可以测试其他协议的系统,只需采用Python调用对应的库进行请求描述即可。<br>
&emsp;&emsp;LoadRunner和JMeter这类采用进程和线程的测试工具,都很难在单机上模拟出较高的并发压力。Locust
的并发机制摒弃了进程和线程,采用协程(gevent)的机制。协程避免了系统级资源调度,因此可以大幅度提高单机的并发能力。<br>
&emsp;&emsp;正是基于这样的特点,我选择了使用Locust工具来做性能测试,另外一个原因是它可以让我们换一种方式认识性能测试,
可以更容易的看清性能测试的本质。<br>
&emsp;&emsp;Locust官方网址:http://locust.io<br>
### 15.1.1 安装Locust
&emsp;&emsp;虽然Locust仍然可以使用pip安装,但如果你使用的是Python3,那么建议你从GitHub克隆或下载项目进行安装。<br>
&emsp;&emsp;GitHub地址:https://github.com/locustio/locust<br>
&emsp;&emsp;这里不再介绍具体的安装过程。下面简单介绍Locust都基于了那些库。打开Locust安装目录下的setup.py
文件,查看安装要求:<br>
&emsp;&emsp;`install_requires=["gevent>=1.1.2","flask>=0.10.1","requests>=2.9.1","msgpack-python>=0.4.2","six>=1.10.0","pyzmq==15.2.0"]`<br>
- gevent:在Python中实现协程的一个第三方库。协程,又称微线程(Coroutine)。使用gevent可以获得极高的并发性能。
- flask:Python的一个Web开发框架,它与Django的地位相当。
- requests:我们应该很熟悉了,本书中使用该库来做HTTP接口测试。
- msgpack-python:一种快速、紧凑的二进制序列化格式,适用于类似JSON的数据。
- six:它提供了一些简单的工具来封装Python2和Python3之间的差异性。
- pyzmq:如果你打算把Locust运行在多个进程/机器,建议你安装pyzmq。

&emsp;&emsp;当我们在安装时Locust时,它会检测我们当前的Python环境是否已经安装了这些库,如果没有安装,那么它会先把
这些库一一装上。并且对这些库版本有要求,有些是必须等于某版本,有些是大于某版本。我们也可以把这些库全部按要求装好,
这样在安装Locust时就会快上许多。<br>
&emsp;&emsp;检测是否安装成功.打开Windows命令提示符,输入"locust --help"回车。<br>
```
D:\Python35\locust>locust --help
Usage: locust [options] [LocustClass [LocustClass2 ... ]]

Options:
  -h, --help            show this help message and exit
  -H HOST, --host=HOST  Host to load test in the following format:
                        http://10.21.32.33
  --web-host=WEB_HOST   Host to bind the web interface to. Defaults to '' (all
                        interfaces)
  -P PORT, --port=PORT, --web-port=PORT
                        Port on which to run web host
  -f LOCUSTFILE, --locustfile=LOCUSTFILE
                        Python module file to import, e.g. '../other.py'.
                        Default: locustfile
  --csv=CSVFILEBASE, --csv-base-name=CSVFILEBASE
                        Store current request stats to files in CSV format.
  --master              Set locust to run in distributed mode with this
                        process as master
  --slave               Set locust to run in distributed mode with this
                        process as slave
  --master-host=MASTER_HOST
                        Host or IP address of locust master for distributed
                        load testing. Only used when running with --slave.
                        Defaults to 127.0.0.1.
  --master-port=MASTER_PORT
                        The port to connect to that is used by the locust
                        master for distributed load testing. Only used when
                        running with --slave. Defaults to 5557. Note that
                        slaves will also connect to the master node on this
                        port + 1.
  --master-bind-host=MASTER_BIND_HOST
                        Interfaces (hostname, ip) that locust master should
                        bind to. Only used when running with --master.
                        Defaults to * (all available interfaces).
  --master-bind-port=MASTER_BIND_PORT
                        Port that locust master should bind to. Only used when
                        running with --master. Defaults to 5557. Note that
                        Locust will also use this port + 1, so by default the
                        master node will bind to 5557 and 5558.
  --expect-slaves=EXPECT_SLAVES
                        How many slaves master should expect to connect before
                        starting the test (only when --no-web used).
  --no-web              Disable the web interface, and instead start running
                        the test immediately. Requires -c and -r to be
                        specified.
  -c NUM_CLIENTS, --clients=NUM_CLIENTS
                        Number of concurrent Locust users. Only used together
                        with --no-web
  -r HATCH_RATE, --hatch-rate=HATCH_RATE
                        The rate per second in which clients are spawned. Only
                        used together with --no-web
  -t RUN_TIME, --run-time=RUN_TIME
                        Stop after the specified amount of time, e.g. (300s,
                        20m, 3h, 1h30m, etc.). Only used together with --no-
                        web
  -L LOGLEVEL, --loglevel=LOGLEVEL
                        Choose between DEBUG/INFO/WARNING/ERROR/CRITICAL.
                        Default is INFO.
  --logfile=LOGFILE     Path to log file. If not set, log will go to
                        stdout/stderr
  --print-stats         Print stats in the console
  --only-summary        Only print the summary stats
  --no-reset-stats      [DEPRECATED] Do not reset statistics once hatching has
                        been completed. This is now the default behavior. See
                        --reset-stats to disable
  --reset-stats         Reset statistics once hatching has been completed.
                        Should be set on both master and slaves when running
                        in distributed mode
  -l, --list            Show list of possible locust classes and exit
  --show-task-ratio     print table of the locust classes' task execution
                        ratio
  --show-task-ratio-json
                        print json data of the locust classes' task execution
                        ratio
  -V, --version         show program's version number and exit
```
### 15.1.2 性能测试案例
&emsp;&emsp;先来一个简单的案例热热身,熟悉一下Locust工具的基本使用流程。如果使用的是LoadRunner性能测试工具,
那么首先想到的应该是怎样录制/编写性能测试脚本。其实,对于Web应用来说,它本质是由一个个的Web页面构成,一般我们可以通过
不同的URL地址来得到不同的页面。<br>
&emsp;&emsp;1.编写性能测试脚本<br>
&emsp;&emsp;使用Locust编写一个简单性能测试行为表述脚本。<br>
locustfile.py:<br>
```Python
from locust import HttpLocust,TaskSet,task
# 定义用户行为
class UserBehavior(TaskSet):

	@task
	def baidu_page(self):
		self.client.get("/")
		
class WebsiteUser(HttpLocust):
	task_set=UserBehavior
	min_wait=3000
	max_wait=6000
```
&emsp;&emsp;UserBehavior类继承TaskSet类,用于描述用户行为。<br>
&emsp;&emsp;baidu_page()方法表示一个用户行为,访问百度首页。使用@task装饰该方法为一个事务。client.get()
用于指定请求的路径"/",因为是百度首页,所以指定为根路径。<br>
&emsp;&emsp;WebsiteUser类用于设置性能测试。<br>
- task_set:指向一个定义的用户行为类
- min_wait:执行事务之间用户等待时间的下界(单位:毫秒)
- max_wait:执行事务之间用户等待时间的上界(单位:毫秒)

&emsp;&emsp;2.执行性能测试<br>
&emsp;&emsp;首先,启动性能测试。<br>
```
C:\Users\Administrator\git\guest>locust -f locustfile.py --host=https://www.baid
u.com
[2018-05-05 19:48:37,638] I0QZ95XPAAXLPJP/INFO/locust.main: Starting web monitor
 at *:8089
[2018-05-05 19:48:37,642] I0QZ95XPAAXLPJP/INFO/locust.main: Starting Locust 0.8.
1
```
- -f:指定性能测试脚本文件
- --host:指定被测试应用的URL地址,注意访问百度使用得HTTPS协议。

&emsp;&emsp;通过浏览器访问,http://127.0.0.1:8089(Locust启动网络监控器,默认为端口号为8089)。显示如图15.1所示。<br>
![image](https://github.com/15529343201/guest/blob/chapter15/image/15.1.PNG)<br>
- Number of users to simulate是模拟用户的数量（虚拟用户数）
- Hatch rate (users spawned/second）表示产生模拟用户的速度，(每秒产生启动的虚拟用户数)

&emsp;&emsp;填写完成后点击“Start swarming”即可开始测试<br>
![image](https://github.com/15529343201/guest/blob/chapter15/image/15.2.PNG)<br>
&emsp;&emsp;性能测试参数如下:<br>
- Type：请求的类型，例如GET/POST；
- Name：请求的路径，这里为百度首页，即https://www.baidu.com/；
- request：当前请求的数量；
- fails：当前请求失败的数量；
- Median：中间值，单位毫秒，一半的服务器响应时间低于该值，而另一半高于该值；
- Average：平均值，单位毫秒，所有请求的平均响应时间；
- Min：请求的最小服务器响应时间，单位毫秒；
- Max：请求的最大服务器响应时间，单位毫秒；
- Content Size：单个请求的大小，单位字节；
- reqs/sec：每秒钟请求的个数。

## 15.2 发布会系统性能测试
&emsp;&emsp;性能测试涉及的知识点非常多，包括：<br>
- 性能测试的需求分析： 客户需求、新系统性能验证、旧系统扩容、优化系统瓶颈等；
- 性能测试工具的选型： 商业工具LoadRunner、开源工具JMeter、Locust，或者自研性能工具；
- 性能测试环境准备： 软件环境、硬件环境、网络环境；
- 性能测试业务分析： 针对哪些业务做性能测试；
- 性能测试数据准备： 准备性能测试所需要的基础数据；
- 性能测试执行策略： 不同业务的用户分配比例，运行时长、思考时间、集合点的设置等；
- 性能测试监控： 中间件的监控、数据库服务器的监控、系统服务器的监控；
- 性能测试分析与调优： 分析整个系统各个部分的监控结果；对程序处理过程优化，程序算法优化，中间件各种配置参数的调整，数据库SQL语句、索引、表结构的优化；

### 15.2.1 性能测试准备
&emsp;&emsp;性能测试目的： 发布会签到系统、新系统能力验证；<br>
&emsp;&emsp;业务分析： 根据发布会签到系统的应用场景，主要包括发布会管理页面、嘉宾管理页面、嘉宾查询功能和发布会签到功能；<br>
&emsp;&emsp;性能测试环境： <br>
![image](https://github.com/15529343201/guest/blob/chapter15/image/15.3.PNG)<br>
&emsp;&emsp;测试数据准备：<br>
- 发布会数据：10条
- 嘉宾数据：3000条
- 待签到嘉宾：3000条

&emsp;&emsp;测试数据构造：
- 执行SQL语句，分别使sign_event、sign_guest两张表的create_time字段在插入数据时直接取当前时间：

```
ALTER TABLE `sign_event` CHANGE `create_time` `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE `sign_guest` CHANGE `create_time` `create_time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP;
```
- 先创建一条插入嘉宾信息的SQL语句

&emsp;&emsp;`INSERT INTO sign_guest (realname,phone,email,sign,event_id) VALUES ("jack",13800110000,"jack@mail.com",0,1);`<br>
- 通过Python脚本批量生成3000条插入数据的SQL语句：

```Python
f = open("guests.txt", 'w')

for i in range(1, 3001):
    str_i = str(i)
    realname = "jack" + str_i
    phone = 13800110000 + i
    email = "jack" + str_i + "@mail.com"
    sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id) VALUES ("'+realname+'", '+str(phone)+', "'+email+'", 0, 1);'
    f.write(sql)
    f.write("\n")

f.close()
```
- 将生成好的SQL语句，在SQL命令行中执行，生成测试数据。

### 15.2.2 编写性能测试脚本
&emsp;&emsp;当性能测试的准备工作完成之后,接下来根据业务分析的情况,使用Locust编写性能测试脚本。<br>
locustfile.py:<br>
```Python
#! /usr/bin/python
# -*- coding:utf-8 -*-

from locust import HttpLocust, TaskSet, task

# Web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        """
        on_start is called when a Locust start before any task is scheduled
        """
        self.login()

    def login(self):
        self.client.post("/login_action", {"username":"admin", "password":"admin123456"})

    @task(2)
    def event_manage(self):
        self.client.get("/event_manage/")

    @task(2)
    def guest_manage(self):
        self.client.get("/guest_manage/")

    @task(1)
    def search_manage(self):
        self.client.get("/search_phone/", params={"phone":"13800112451"})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
```
- 通过@task()装饰的方法为一个事务，方法的参数用于指定该行为的执行权重。参数越大，每次被虚拟用户只需的概率越高，如果不设置，则默认为1，发布会管理页、嘉宾管理页和嘉宾搜索功能的执行权重比例为2:2:1。
- min_wait、max_wait用于指定用户执行事务之间暂停的下限和上限，即3-6秒；
- 每个事务的请求路径、是GET请求还是POST请求、是否需要传参数等，都可以根据Django项目中对视图函数的定义来决定，调用方法与Requests库基本相同。

### 15.2.3 执行性能测试
&esmp;&emsp;启动性能测试：<br>
`locust -f locustfile.py --host=http://192.168.127.134:8089`<br>
&esmp;&emsp;其中,http://192.168.127.134:8089为发布会签到系统的部署主机的IP地址和端口号。<br>
- 通过浏览器访问Locust工具:http://127.0.0.1:8089
- Number of users to simulate:设置模拟用户数为100.
- Hatch rate(users spawned/second):每秒产生(启动)的用户数为10,即每秒启动10个模拟用户

&emsp;&emsp;单击"Start swarming"按钮,运行性能测试。<br>
## 15.3 接口性能测试
&emsp;&emsp;接口性能测试相比系统性能测试来说要简单许多,当前系统处理能力场景和用户行为,只需模拟调用接口,
验证接口的最大处理能力即可。<br>
- 1.接口性能测试需求:考虑到嘉宾签到功能,发布会现场需要多通道并行对嘉宾进行签到,所以,需要充分验证签到接口的并发签到处理能力。
- 2.接口性能测试环境
- 3.接口性能测试数据准备

### 15.3.1 编写接口性能测试脚本
locustfile.py:<br>
```Python
!/usr/bin/python
# -*- coding:utf-8 -*-

from locust import HttpLocust, TaskSet, task
from random import randint

# Web接口测试
class UserBehavior(TaskSet):

    @task()
    def user_sign(self):
        number = randint(1, 3001)
        phone = 13800110000 + number
        str_phone = str(phone)
        self.client.post("/api/user_sign/", data={"eid":"1", "phone":str_phone})

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
```
### 15.3.2 执行接口性能测试
&emsp;&emsp;`locust -f locustfile.py --host=http://127.0.0.1:8089 --no-web -c 10 -r 10 -n 3000`<br>
- –no-web：表示不使用web界面运行测试
- -c：设置虚拟用户数
- -r：设置每秒启动虚拟用户数
- -n：设置请求个数

`update sign_guest set sign=0;`<br>
### 15.3.3 多线程测试接口性能
&emsp;&emsp;重复签到和签到失败是两个不同的服务器处理过程，注意不能混淆。<br>
&emsp;&emsp;如果需要对3000个嘉宾计算多长时间内可以完成全部签到，那么可以使用Python的多线程技术来实现这个需求：<br>
thread_if_test.py:<br>
```Python
#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import threading
from time import time

# 定义接口基本地址
base_url = "http://127.0.0.1:8089"

# 签到线程
def sign_thread(start_user, end_user):
    for i in range(start_user, end_user):
        phone = 13800110000 + i
        datas = {"eid":"1", "phone":phone}
        r = requests.post(base_url+'/api/user_sing/', data=datas)
        result = r.json()
        try:
            assert result['message'] == "sign success"
        except AssertionError as e:
            print "phone:" + str(phone) + ", user sign fail!"

# 设置用户分组（即5个线程）
lists = {1:601, 601:1201, 1201:1801, 1801:2401, 2401:3001}

# 创建线程数组
threads = []

# 创建线程
for start_user, end_user in lists.items():
    t = threading.Thread(target=sign_thread, args=(start_user, end_user))
    threads.append(t)

if __name__ == '__main__':
    # 开始时间
    start_time = time()
    # 启动线程
    for i in range(len(lists)):
        threads[i].start()
    for i in range(len(lists)):
        threads[i].join()
    # 结束时间
    end_time = time()
    print "start time: " + str(start_time)
    print "end time: " + str(end_time)
    print "run time: " + str(end_time - start_time)
```
&emsp;&emsp;将3000个数平均分为5组，放到字典中，其中每一组数通过线程类Thread，调用sign_thread()函数生成一个线程。所以，是5个线程（可以理解为“虚拟用户数”）并发调用接口测试。<br>
&emsp;&emsp;start()方法用于启动线程，join()方法用于守护线程。<br>
&emsp;&emsp;相比专业性能测试工具，这个多线程测试程序要简陋得多，但是直接编程的灵活性也是工具所不具备的。<br>














































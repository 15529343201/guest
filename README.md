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
在 Windows 系统中， 安装好的 Python 提供了四个选项。
&emsp;&emsp;IDLE(Python 3.5 64-bit) ： 该选项为 Python 自带的 IDE， 推荐新手使用。
&emsp;&emsp;Python 3.5 (64-bit)： 该选项会直接在 window 名称提示符下进入 Python Shell 模式。
&emsp;&emsp;Python 3.5 Manuals(64-bit) ： 该选项为 Python 自带的官方文档。
&emsp;&emsp;Python 3.5 Module Docs(64-bit)： 该选项为 Python 的模块文档。 它自动启动一个服务， 并打 Web 形式的文档。


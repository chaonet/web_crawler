# IPython 和 Jupyter

IPython 是一个不断成长的项目，有很多语言无关的组件。

IPython 3.x 是最后的单一集合版本，包括 notebook server, qtconsole, 等等，集成对python以外的语言的支持。在 IPython 4.0 中, 语言无关的部分，也就是可以为所有语言工作的组件： notebook format, 消息协议, qtconsole, notebook web application, 等等，被移到一个名为 Jupyter 的新项目中。IPython 本身专注于交互式 Python, 有一部分作用是为 Jupyter 提供一个 Python 内核。

## jupyter

开源的，交互式数据科学和科学计算工具，支持超过 40 种编程语言

[jupyter](http://jupyter.org/)

- Jupyter Notebook

Jupyter Notebook 是一个web应用程序,允许你创建和共享包含 代码,方程,可视化和解释性 文字 的文档。可用于:数据清洗和转换、数值模拟、统计建模、机器学习和更多。

- Notebook 文档格式
Jupyter Notebooks 是一个开放的基于JSON格式的文档。包含一个 用户的会话和嵌入代码,叙事文本,方程和丰富输出 的完整记录。

- 交互计算协议
Notebook 与 计算内核 使用交互式计算协议 通信,这是一个开放的网络协议，运行于ZMQ和WebSockets上，基于JSON数据。

- 核心
内核在一个特定的编程语言中处理、运行交互代码并返回输出给用户。内核也响应标签完成和内省请求。

两种使用方法：

- 在浏览器中尝试[在线版 jupyter](https://try.jupyter.org/)
- 安装[jupyter](http://jupyter.readthedocs.org/en/latest/install.html)

### 安装

`pip install jupyter`

这样安装 Jupyter Notebook，会同时安装 IPython内核 , 允许在 notebooks 中使用 Python 编程语言。如果想在 notebooks 中运行其他语言, 需要另外安装内核。更多信息[可用内核的列表](https://github.com/ipython/ipython/wiki/IPython-kernels-for-other-languages)。

### 运行 jupyter notebook 服务器

`$ jupyter notebook`

可以指定端口，默认`8888`

```
➜  1w git:(master) jupyter notebook --port=8000
[W 23:50:23.819 NotebookApp] ipywidgets package not installed.  Widgets are unavailable.
[I 23:50:23.834 NotebookApp] Serving notebooks from local directory: /Users/chao/Desktop/projects/OMOOCData/code/1w
[I 23:50:23.834 NotebookApp] 0 active kernels
[I 23:50:23.834 NotebookApp] The IPython Notebook is running at: http://localhost:8000/
[I 23:50:23.834 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
^C[I 23:50:36.290 NotebookApp] interrupted
Serving notebooks from local directory: /Users/chao/Desktop/projects/OMOOCData/code/1w
0 active kernels
The IPython Notebook is running at: http://localhost:8000/
Shutdown this notebook server (y/[n])? y
[C 23:50:39.295 NotebookApp] Shutdown confirmed
[I 23:50:39.296 NotebookApp] Shutting down kernels
```

`Control-C`停止 服务器，并关闭所有内核

在哪个文件夹下开启 ipython notebook，就以哪个目录作为工作目录，创建、读取 文件

获取命令行帮助

这是一个基于 HTML 的 Tornado 框架的 notebook 服务器,它提供了一个HTML5 / Javascript notebook 客户端。

```
$ jupyter -h

$ jupyter notebook -h
The Jupyter HTML Notebook.

This launches a Tornado based HTML Notebook Server that serves up an
HTML5/Javascript Notebook client.

Subcommands
-----------

Subcommands are launched as `jupyter-notebook cmd [args]`. For information on
using subcommand 'cmd', do: `jupyter-notebook cmd -h`.

list
    List currently running notebook servers in this profile.

Options
-------

Arguments that take values are actually convenience aliases to full
Configurables, whose aliases are listed on the help line. For more information
on full configurables, see '--help-all'.

--script
    DEPRECATED, IGNORED
--pylab
    DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
--debug
    set log level to logging.DEBUG (maximize logging output)
--ip=<Unicode> (NotebookApp.ip)
    Default: 'localhost'
    The IP address the notebook server will listen on.
--pylab=<Unicode> (NotebookApp.pylab)
    Default: 'disabled'
    DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
--port=<Integer> (NotebookApp.port)
    Default: 8888
    The port the notebook server will listen on.

To see all available configurables, use `--help-all`

Examples
--------

    ipython notebook                       # start the notebook
    ipython notebook --profile=sympy       # use the sympy profile
    ipython notebook --certfile=mycert.pem # use SSL/TLS certificate

➜  1w git:(master)
```

在 notebook 中，使用`%pylab`或者`%matplotlib`, 开启`matplotlib`

文件 标签
点击文件/文件夹前的选择框，重命名、删除

点击文件运行

### 菜单栏

更改其他语言核心 `Kernel` -> `Change kernel`

修改 notebook 的文件名: 双击左上方文件名

- 快捷键

菜单栏`Help Keyboard Shortcuts`

`Return`，进入编辑模式

`B`，在下面插入一个 cell
`D + D`，不区分大小写，删除当前 cell
`Y`，输入的内容视为代码
`M`，输入的内容视为 markdown 格式文本
`S`，保存

- 工具栏

模式指示：

命令模式，可以使用快捷键

编辑模式，在输入文本区域输入内容

输入文本区的内容类型：code、markdown

### 运行代码

`Control + Return`，运行当前 cell，并保持选中当前 cell
`Shift + Return`，运行当前 cell，并移到下一个 cell
`Option + Return`，运行当前cell，并在下面插入一个 cell

### 获取帮助

`?`，获得函数的定义(调用所需的参数)、文档字符串、使用示例、使用的 python 文件、对象类型

`??`，获得更详细的信息，增加了函数的实现代码
>help()

`object_name.<TAB>`，可以查看对象的属性
>dir()

`%quickref`，快速参考卡

### 交互工作流

>我原本以为，每个 cell 是独立的

`_`，打印上一个cell的结果

`__`，上上个结果

`___`，上上上个结果
>print 的结果不会存储

`;`，不输出结果、也不存储结果

`_N`

`Out[N]`

`Out`，字典形式打印所有 cell 号和输出值，不会存入`_`快捷方式中

`In[N]`，显示输入的历史

`_i`，上一个的输入

`_ii`，上上个输入

`_iii`

`%history`，显示历史输入

### 访问底层操作系统

### 魔法函数

IPyhton“魔法”功能是一组命令,通过在命令前添加一个或两个`%`调用,生活在一个名称空间独立于正常Python变量和提供更多的命令接口。

### 运行 python 代码

不仅可以正常输入代码，也可以从 shell 以及 IPython 中复制代码 并运行。

### 导入模块

## 添加 ipynb 文件

运行服务器后，在`Files`标签下

可以直接将文件拖到文件列表中，点击右边的`upload`

或者

点击右边的`Upload`选择文件上传

### 创建文件、文件夹

运行服务器后，在`Files`标签下，`New`

### json

保存后的文件，是 json 格式，可以直接在浏览器中打开

## IPython

单独使用 IPython 核心

```
➜  1w git:(master) ipython
Python 2.7.9 (v2.7.9:648dcafa7e5f, Dec 10 2014, 10:10:46)
Type "copyright", "credits" or "license" for more information.

IPython 4.0.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: print 'hello, world!'
hello, world!

In [2]: a = 1;b = 2;

In [3]: a + b
Out[3]: 3

In [4]: exit
➜  1w git:(master)
```

### 双进程模型

允许几个客户端连接到同一个内核, 甚至允许客户端与内核不在同一台设备上。

不带子命令的`ipython`，运行传统的基于终端的单进程 IPython

其他所有的 IPython 形式都使用`双进程模型`，包括`ipython console`(shell 方式), `ipython qtconsole`(pyqt，类似 终端的 GUI 界面), 和 `ipython notebook`(python 核心的浏览器客户端)

当你运行`ipython qtconsole`,你实际开启了两个进程,一个内核 和 一个可以想内核发送命令并接收结果的 Qt-based客户端。

[IPython 核心](http://ipython.readthedocs.org/en/stable/)

## IPython Parallel

使用 IPython 进行并行计算[IPython Parallel](http://ipyparallel.readthedocs.org/en/stable/)
以前的 IPython 的`IPython.Parallel`子包, 现在独立出来

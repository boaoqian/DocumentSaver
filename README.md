# 简单易用的多页说明文档&教程下载工具
仅需三步即可将网页文档保存为markdown,下面以golang官方教程为例展示使用流程.
## 使用
### 1.运行程序
双击*get_doc.py* 这将打开一个终端\
或打开终端手动输入

    $ python get_doc.py

正常输出如图
![0](readme_res\0.png)

### 2.确定目录链接
链接对应页面应当包含目录信息,如[https://golang.google.cn/doc/](https://golang.google.cn/doc/)
在目录url>>后输入链接

    目录url>>https://golang.google.cn/doc/

你将得到文档结构信息
![1](readme_res\1.png)

### 3.确定文档链接
根据提示输入数字,如果目标有子目录,则自动保存子目录全部文件
eg: 获取https://golang.google.cn/doc/tutorial/下全部文件
![2](readme_res\2.png)
依次输入,根,doc,tutorial所对应的数字.\
**注意** 根对应上图空行

    0-->

输入99后,将自动开始下载保存到工作目录下.
![3](readme_res\3.png)
![4](readme_res\4.png)

## 效果
golang官网![6](readme_res\6.png)
输出![5](readme_res\5.png)
在[src\outputExample](src\outputExample)有输出示例可供参考
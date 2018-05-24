# 2017-2018kechuangjihua
Chinese-Font-Style Transfer
---updated 2018.5.24---
构建数据步骤
0.保证所有东西是在一个文件夹里面
1.新建Font1, Font2文件夹作为两种字体的字符数据仓库
2.【windows下】建立一个txt文本文件，输入200-300汉字的文本，每个字占一行，enter换行，没有标点和数字。保存utf-8编码。之后可以复制到
Linux工程目录下面
3.在test.py倒数第三行把txt文件的名字输入在参数中（替换your_file_path），之后运行该文件，正确的话应该会在Font1/Font2文件夹里面看到
对应字体的图片，不过需要花一点时间。

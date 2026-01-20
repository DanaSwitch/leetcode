# linux常见用法积累

## 一.文件的创建和删除

创建单个文件

> touch filename.txt    #创建单个文件

创建目录夹

> mkdir filename



删除单个文件

> rm filename.txt

删除多个文件

> rm file1.txt file2.txt file3.txt

删除文件夹及其内容 -r表示递归

> rm -r foldername

删除所有特定类型文件

> rm *.txt          # 删除所有.txt文件
> rm *.pdf          # 删除所有.pdf文件
>
> ls music*    #查看所有以music开头的文件
>
> rm music*  #在当前目录下删除所有以music开头的文件





## 二.WSL下Ubuntu和Window的文件移动和复制

移动

> mv xiaowang/C++/EmbedJourney   /mnt/d/STM32/



复制 如果路径中有空格或特殊字符，需要用引号括起来：

> cp -r "xiaowang/C++/EmbedJourney" "/mnt/d/STM32/"
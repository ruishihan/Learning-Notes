git 学习笔记
============
基本命令
--------
#本地仓库
>创建仓库

`git init`

>把文件添加到暂存库中

`git add <file>`		`git add .`

>撤销工作区的修改

`git checkout -- <file>`
**(回到版本库的最新状态，包括暂存区和已提交的版本)**

>把添加到暂存库中的文件移除/递归删除

`git rm --cache <file>`	
`git rm -r --cache .`
`git reset <file>`		
`git reset .`

>把文件从版本库删除

`git rm <file>`

>把暂存库中的文件提交

`git commit -m "...."`
`git commit -a` **跳过暂存区直接把工作区的文件提交**

>查看工作区、暂存区状态

`git status`

>显示工作区和暂存区的同名文件的差别

`git diff <file>`          [读懂diff](http://www.ruanyifeng.com/blog/2012/08/how_to_read_diff.html)
**NOT:git diff shows the difference(s) between the file(s) that are not added and the added files.**

>查看版本信息

`git log`	
`git log --pretty=oneline`
>版本回退

`git reset --hard HEAD^`	**回退到上一个版本**
**(HEAD/HEAD^/HEAD^^/HEAD^^^/HEAD~100)**
`git reset --hard fsaf2132134`

>查看命令历史

`git reflog`

>查看工作区和版本库里面最新版本的区别

`git diff HEAD -- readme.txt`

#远程协作
>github创建新的版本库

>本机生成SSH-KEY

>github添加SSH-KEY

>本地与远程关联

`git remote add origin git@github.com:michaelliao/learngit.git`
**(添加后，远程库的名字就是origin（是远程库在本地的别名），这是Git默认的叫法，也可以改成别的，但是origin这个名字一看就知道是远程库)**
>把本地库推送到github

`git push -u origin master`
**由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。**
`git push origin master`
**origin是远程库的代称，master是要推送的本地库的分支名称**
>从远程克隆一个库

`git clonegit@github.com:michaelliao/gitskills.git`
**使用ssh协议传输**
`https://github.com/michaelliao/gitskills.git`
**使用https协议**

#分支管理
>创建分支

`git branch <name>`
>切换到分支

`git checkout <name>`
>创建+切换到分支

`git checkout -b <name>`
>查看分支列表

`git branch`
>合并某分支到当前分支

`git merge <name>`
>删除分支

`git branch -d <name>`

基本概念
------------
>工作区		working directory

>版本库(repository).git，里面有暂存区index,有HEAD,有第一个分支master

>暂存区index/stage	属于版本库的一部分

>git跟踪管理的是修改而不是文件。

>git rm 的用法

    git rm [-f|-n|-r|--cached|-q] <file>
	-f
	--force
	Override the up-to-date check.

	-n
	--dry-run

	Don’t actually remove any file(s). Instead, just show if they exist in the index and would otherwise be removed by the command.

	-r
	Allow recursive removal when a leading directory name is given.

	This option can be used to separate command-line options from the list of files, (useful when filenames might be mistaken for command-line options).

	--cached
	Use this option to unstage and remove paths only from the index. Working tree files, whether modified or not, will be left alone.

	--ignore-unmatch
	Exit with a zero status even if no files matched.

	-q
	--quiet
	git rm normally outputs one line (in the form of an rm command) for each file removed. This option suppresses that output.

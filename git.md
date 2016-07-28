git 学习笔记
============
基本命令
--------
#本地仓库
1. **创建仓库**

		git init

2. **把文件添加到暂存库中**

		git add <file>		git add .

3. **撤销工作区的修改**

		git checkout -- <file>
**(回到版本库的最新状态，包括暂存区和已提交的版本)**

4. **把添加到暂存库中的文件移除/递归删除**

		git rm --cache <file>`
		git rm -r --cache .
		git reset <file>		
		git reset .

5. **把文件从版本库删除**

		git rm <file>

6. **把暂存库中的文件提交**

		git commit -m "...."
		git commit -a  跳过暂存区直接把工作区的文件提交

7. **查看工作区、暂存区状态**

		git status

8. **显示工作区和暂存区的同名文件的差别**

		git diff <file>        
[读懂diff](http://www.ruanyifeng.com/blog/2012/08/how_to_read_diff.html)
**NOT:git diff shows the difference(s) between the file(s) that are not added and the added files.**

9. **查看版本信息**

		git log
		git log --pretty=oneline

10. **版本回退 **

		git reset --hard HEAD^	回退到上一个版本
	**(HEAD/HEAD^/HEAD^^/HEAD^^^/HEAD~100)**
		git reset --hard fsaf2132134

11. **查看命令历史**

		git reflog

12. **查看工作区和版本库里面最新版本的区别**

		git diff HEAD -- readme.txt

13. **忽略特殊文件**

	**.gitignore**
	**.gitignore文件本身要放在版本库中，并且可以对其做版本管理**

#远程协作
1. **github创建新的版本库**

1. **本机生成SSH-KEY**

1. **github添加SSH-KEY**

1. **本地与远程关联**

		git remote add origin git@github.com:michaelliao/learngit.git
**(添加后，远程库的名字就是origin（是远程库在本地的别名），这是Git默认的叫法，也可以改成别的，但是origin这个名字一看就知道是远程库)**

1. **把本地库推送到github**

		git push -u origin master
**由于远程库是空的，我们第一次推送master分支时，加上了-u参数，Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令。**

		git push origin master
**origin是远程库的代称，master是要推送的本地库的分支名称**

1. **从远程克隆一个库**

	**使用ssh协议传输**

		git clone git@github.com:michaelliao/gitskills.git

	**使用https协议**		

		git clone https://github.com/michaelliao/gitskills.git


1. **查看远程库的信息**

		git remote
		git remote -v

1. *远程抓取分支*

		git checkout -b dev origin/dev
	**创建远程origin的dev分支到本地dev**

1. **制定本地分支与远程分支的链接**
		
		git branch --set-upstream dev origin/dev


#分支管理
1. **创建分支**

		git branch <name>

1. **切换到分支**

		git checkout <name>

1. **创建+切换到分支**

		git checkout -b <name>

1. **查看分支列表**

		git branch

1. **合并某分支到当前分支**

		git merge <name>

1. **删除分支**

		git branch -d <name>

1. **stash**
		
		git stash
	**压栈**
		git stash list
	**查看stash内容**
		git stash apply
	**把stash恢复到工作区，且不删除stash中的内容**
		git stash drop
	**删除stash中的内容**
		git stash pop
	**弹出栈**
1. **标签**
	
		git tag <tagname>
		git tag
		git show <tagname>
		git push origin <tagname>
		git push origin --tags
		git tag -d <tagname>
		git push origin :refs/tages/<tagnames>
	**删除本地标签和远程标签**

#创建Git服务器

[**搭建Git服务器教程**](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/00137583770360579bc4b458f044ce7afed3df579123eca000)

基本概念
------------
1. **工作区		working directory**

1. **版本库(repository).git，里面有暂存区index,有HEAD,有第一个分支master**

1. **暂存区index/stage	属于版本库的一部分**

1. **git跟踪管理的是修改而不是文件。**

1. **git rm 的用法**

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

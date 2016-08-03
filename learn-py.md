python
=========

1. **print'hello world'**

2. **常量**
    
    >字面意义上的常量

    >数：整数、长整数、浮点数、复数

    >字符串：单引号、双引号（双引号里面可以使用单引号）、三引号（三引号里面可以换行、使用单引号、使用双引号）、反斜杠充当转义符、反斜杠在行尾表示字符串载下一行继续，而不是开始一个新的行。

    >自然字符串：表示该字符串内的特殊字符不做特殊字符处理

    >Unicode字符串

3. **数据类型**

4. **对象**

5. **逻辑行与物理行** 分号

6. **缩进**

    >逻辑行首的空白称为缩进，缩进决定语句的分组，相同的缩进为一个语句块，不能随意开始一个新的语句块。

    >不要混合使用制表符和空格进行缩进，建议使用一个制表符或两个或四个空格表示一个缩进层次。

---------------------------------

1. **运算符和表达式**

    >or and not is isnot < > <= >= == != | ^ & << >> * / % ~ **(指数)

    >x[index] 下标	x[index:index] 寻址段	f(arguments) 函数调用

    >(expression,……) 绑定或元组显示	[expression,……] 列表显示	{key:datum,……} 字典显示

2. **控制流**

    >if

    	if i==number:
		    ……
        elif i<dsf:
		    ……
        else:
		    ……


    >for

        for i in range(1,5):
            ……
        else:
            ……
    **内建的range函数返回一个序列的数，从第一个数开始到第二个数为止，可提供第三个数作为步长，range生成的数包括第一个数但不包括第二个数**

	    
    >while

        while condition:
		  ……
        else:
		  ……
**for /while中的else选项可有可没有，包含时总在循环结束后执行一次，但是遇到break时，else会被跳过。**

    >break 跳出循环，如果从循环中跳出，任何对应的循环else块将不执行。

    >continue

3. **函数**

    > `def func(……):`

    >函数形参

    >默认参数值：`def f(a,b=2):` ***带默认值的形参必须放在最后***
    
    >关键参数：`def func(a,b=2,c=1)`然后在使用时`func(10,c=3)`，即在传参时，对有默认值的形参选择性传参。

    >函数内的局部变量（函数内的变量名可与函外的复用，彼此之间没有关系）

    >使用global语句，可以载函数中为函数外的变量赋值：`global x`

    >return语句	
    **注意,没有返回值的return语句等价于return None。None是Python中表示没有任何东西的特殊类型。**

    >文档字符串 Docstrings

    >>文档字符串的惯例是一个多行字符串,它的首行以大写字母开始,句号结尾。第二行是空行,从第三行开始是详细的描述。强烈建议 你在你的函数中使用文档字符串时遵循这个惯例。

    >>可以使用__doc__(注意双下划线)调用printMax函数的文档字符串属性(属于函数的名称)。请记住Python把 每一样东西 都作为对象,包括这个函数。

    >>help()函数就是调取的函数的文档字符串，我们也可以在自定义的函数中使用help()函数来调取自定义的函数的文档字符串。


4. **模块**

    >模块的文件名必须以.py为扩展名
    
    >sys模块包含了与Python解释器和它的环境有关的函数

    >sys模块中的argv变量通过使用点号指明——sys.argv——

		#!/usr/bin/python
		#Filename using_sys.py
	
		import sys
	
		print'The command line arguments are'
		for i in sys.argv:
			print i

	print'\n\n The PYTOHNPATH is',sys.path,'\n'
    **这样通过调用sys模块中的argv，就可以实现带参数执行Python程序**

    >字节编译的.pyc文件

    >from……import……语句,只输入某模块中的一部分，提高效率

    >模块的__name__

    **自定义的模块应该被放置在输入它的程序的同一个目录中,或者在sys.path所列目录之一。**

    >dir()函数
    
    **当你为dir()提供一个模块名的时候,它返回模块定义的名称列表。如果不提供参数,它返回当前模块中定义的名称列表。**

    >del 用于删除一个变量/名称

5. **数据结构**

    >列表

	[a,b,c,d,e,f,g,h,...]
	list.append()
	list.extend()
    ***注意append(list1)与extend(list1)的区别***

	list.__sizeof__()
	len(list)
	list.sort()
    ***len返回个数，__sizeof__返回字节数***

	list.reverse()

	list[0]	list[1]	……
	del list[0]

	repr(list)

	list+y
	n*list
	list.count(value)
	list.index(value,[start,[stop]])
	list.insert(index,object)
	list.pop([index])	(default last)
	liSt.remove(value)	根据value移除匹配的第一个项
	
	value in list		True or False


    >>列表可以用在 for 中
		for item in list
			print item,
    ***在print 的结尾加上逗号，消除每个print自动的换行符***
    >>列表可以整体输出
		print list

    >元组

    >>元组用()来定义，按照index访问时还是用[]

    >>元组与列表十分类似，但是元组和字符串一样时不可变的，即你不能修改元组。

    >>元组通常用在时语句或用户定义的函数能够安全地采用一组值的时候，即被使用的元组的值不会改变。

    >>元组最常用在打印语句中。
	print '%s is %d years old'%(name,old)
	print'why is %s playing with that python?'%name	
    ***格式输出***

	
    >字典`d={key1:value1,key2:value2}`
    >>字典是键和值的对应，只能使用不可变的对象作为字典的键，但可以把不可变或可变的对象作为字典的值。

    >>字典中的键/值对时没有顺序的

    >>通过键，而非index来访问值

	ab['key3']=value3	增加键值对
	del ab['key1']		删除键值对
	
	cmp(x,y)
	ab.__contains__(k)
	
	x>=y
	x==y	字典的比较表示什么意思？

	iter(x)
	len(x)
	repr(x)
	
	ab.__sizeof__()
	
	ab.clear()	remove all items from ab
	ab.copy()	a shallow copy of ab

	ab.fromkeys(s[,v])	**New dict with keys from s and values equal to v.**
	
	ab.get(k[,d])		**return ab[k] if k in ab,else return d. d defaults to None
	ab.setdefault(k[,d])	**get(k,d) and set D[k]=d if k not in ab.**

	ab.pop(k[,d])		**remove specified key and return the corresponding value.**
    **get 和pop 一个是得到，一个是得到并删除。**	
	ab.popitem()		**remove and return some key/value pairs**

	ab.has_key(k)

	ab.items()
	ab.keys()
	ab.values()	***list all values***
	ab.iteritems()
	ab.iterkeys()
	ab,itervalues()
	ab.viewitems()
	ab.viewkeys()
	ab.viewvalues()

	ab.update()	


6. **序列**

    >序列的两个特点是索引操作符和切片操作符

    >>索引为负数时，表示位置时从序列尾开始计算的。

    >>切片操作符中的第一个数(冒号之前)表示切片开始的位置,第二个数(冒号之后)表示切片到哪里结束。如果不指定第一个数,Python就从序列首开始。如果没有指定第二个数,则Python会停止在序列尾。

    >>开始位置是包含在序列切片中的,而结束位置被排斥在切片外。

    **注意：list1=list5	与	list1=list2[:]的区别**	
    **前者只是浅拷贝，只是创建一个指针，并没有真正复制；后者才是深拷贝，时真正的复制内存**



7. **输入输出**

`raw_input`	`print`

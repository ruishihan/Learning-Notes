>sys
>>sys.argv
>>sys.stdin
>>sys.stdout
>>sys.stderr
>>sys.builtin_module_names
>>sys.exit()	退出程序
>>sys.version
>>sys.version_info
>>sys.getsizeof(...)	输出对象的大小（字节）

-----------------------------------------------------

>os
>>os.name	操作系统的名称
>>os.getcwd	获取当前工作目录
>>os.listdir()	相当于ls
>>os.system('commands')	运行shell命令
>>os.path.split('path')
>>os.path.isfile()
>>os.path.isdir()
>>os.path.exists()函数用来检验给出的路径是否真地存在
>>os.path.abspath(name):获得绝对路径
>>os.path.getsize(name):获得文件大小，如果name是目录返回0L
>>os.path.splitext():分离文件名与扩展名
>>os.path.basename(path):返回文件名
>>os.path.dirname(path):返回文件路径

-----------------------------------------

>time
>>time.time()
>>time.localtime()	当地时间
>>time.gmtime()		格林尼治时间
>>time.sleep([seconds])	
>>time.ctime([second])	以标准格式返回给定（或当前）秒数的时间
>>time.clock()		进程运行实际时间

-----------------------------

对流控制的简单命令	stdin stdout stderr files ...
read()
readline()
readlines()
write()
writelines()
fileno()
repr()
open('filename','rwb+')
flush()		清理缓存区域，强制输入输出等

seek()		seek(0)	Move tothe start of file.
		seek(1) current 
		seek(2)	Move to the end of file



--------------------


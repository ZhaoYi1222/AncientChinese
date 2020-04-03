import os
import chardet
import sys
"""
小说分割器
#1.用户交互：获取当前目录小说名，1）每个文件的大小  2）分割的文件数量
#2.处理数据：
    1.打开指定文件（检测文件是否存在），读取数据
    2.遍历，创建新文件名  文件名+数字.txt
        3.打开新文件，写入数据
    3.写入完成，再见
"""
class fileSplit:
    CODE = "utf-8"
    def __init__(self,file_obj = None):
        self.file_obj = file_obj
        self.filename = ""


    def get__code(self,filename):
        fileSplit.CODE = chardet.detect(open(filename,"rb").read())["encoding"]

    def user_interactive(self):
        mode_str = """选择切割文件的模式：
1.按照文件大小切割
2.按照文件数量切分
           """
        filename = input("filename:>>")
        if os.path.isfile(filename):
            print("ok")
            self.file_obj = open(filename,"r",encoding=self.CODE)
            self.filename = os.path.basename(filename)
        else:
            print("文件不存在")
            return
        print(mode_str)
        try:
            mode = int(input(">>:").strip())   #做一个错误检验，类型错误
            if mode == 1:
                per_file_size = int(input("each file size(kb)>>:").strip()) #做一个类型错误检验
                self._split_file(part_size= per_file_size*1024) #转化为  n kb容量
            elif mode == 2:
                file_number = int(input("file parts >>:").strip()) #做一个类型错误检验
                self._split_file(file_number = file_number)
            else:
                print("没有该选项")
                return
        except ValueError as e:
            print("只能输入数字！！！")


    def cmd_interactive(self,filename,file_number):
        if os.path.isfile(filename):
            print("ok")
            self.file_obj = open(filename,"r",encoding=self.CODE)
            self.filename = os.path.basename(filename)
        else:
            print("文件不存在")
            return
        self._split_file(file_number = file_number)

    def _split_file(self,part_size = None,file_number = None):
        """
        part_size：输入切分后每个文件大小，得到切分文件
        file_number：输入切分后文件个数，得到文件数目
        :return:
        """
        #1.获取每部分文件的大小
        file_obj = self.file_obj
        file_size = os.path.getsize(self.filename)   #文件总大小
        filename = self.filename.split(".")[0]  #文件去后缀名

        if part_size:   #1.按照文件大小切割,求出需要切割的文件数目
            file_number = file_size // part_size + 1 #切割后文件数目
            print("part_size:%d file_size:%d file_number:%d filename:%s"%(part_size,file_size,file_number,filename))
            if file_size < part_size:
                print("输入错误")
                return
        else:  #2.按照文件数量切分,求出每个文件的大小
            part_size = file_size // file_number

        for i in range(1,file_number):   #一个文件一个文件的写入
            new_name_str = '%s part%d.txt'%(filename,i)
            with open(new_name_str,"w",encoding=self.CODE) as f:
                while f.tell() < part_size:#文件没有到末尾
                    line = file_obj.read(1024)
                    f.write(line)
                spend = file_obj.tell()/file_size*100
                print("进度：%.2f"%spend)
                print("文件名：%s  字节数：%d 创建完成"%(new_name_str,f.tell()))

        #如果不能整除，将文件最后一部分单独写入下一个文件+
        print("最后一个文件")
        end_size = file_size % part_size
        if end_size:
            new_name_str = "%s part%d.txt"%(filename,file_number)
            with open(new_name_str,"w",encoding=self.CODE) as f:
                for line in file_obj:
                    f.write(line)
                spend = file_obj.tell()/file_size *100
                print("进度：%.2f"%spend)
                print("文件名：%s  字节数：%d 创建完成"%(new_name_str,f.tell()))


    def __del__(self):
        if self.file_obj:
            self.file_obj.close()

if __name__ == "__main__":
    #导入命令行接口
    fs = fileSplit()
    parameter_list = sys.argv[1:]
    if len(parameter_list) == 2: #默认按切割文件数目
        filename = parameter_list[0]
        if isinstance(type(parameter_list),int):
            file_number = int(parameter_list[1])
        else:
            print("文件切割数量必须为整数")
            exit(1)
        fs.cmd_interactive(filename,file_number)
    else:
        fs.user_interactive()
    print("bye")




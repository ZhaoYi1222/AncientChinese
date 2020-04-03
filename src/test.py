import os
import shutil
import sys

def _split_file(filepath_par,filename):
    """
    part_size：输入切分后每个文件大小，得到切分文件
    file_number：输入切分后文件个数，得到文件数目
    :return:
    """
    #1.获取每部分文件的大小
    # file_obj = self.file_obj
    file_size = os.path.getsize(filepath_par+filename)   #文件总大小

    fp = open(filepath_par+filename,'r')
    backup = filepath_par+filename
    filename = filename.split(".")[0]  #文件去后缀名

    part_size = 4194304
    file_number = file_size // part_size + 1 #切割后文件数目

    for i in range(1,file_number):   #一个文件一个文件的写入
        new_name_str = '%s_part%d.txt'%(filename,i)
        with open(filepath_par+new_name_str,"w") as f:
            while f.tell() < part_size:#文件没有到末尾
                line = fp.read(1024)
                f.write(line)
            #spend = file_obj.tell()/file_size*100
            # print("进度：%.2f"%spend)
            # print("文件名：%s  字节数：%d 创建完成"%(new_name_str,f.tell()))

    #如果不能整除，将文件最后一部分单独写入下一个文件+
    # print("最后一个文件")
    end_size = file_size % part_size
    if end_size:
        new_name_str = "%s_part%d.txt"%(filename,file_number)
        with open(filepath_par+new_name_str,"w") as f:
            line = fp.read()
            f.write(line)
            #spend = file_obj.tell()/file_size *100
            # print("进度：%.2f"%spend)
            # print("文件名：%s  字节数：%d 创建完成"%(new_name_str,f.tell()))
    fp.close()
    os.remove(backup)

_split_file('./','御定佩文韵府.txt')








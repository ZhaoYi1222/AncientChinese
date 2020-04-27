import os
import shutil
import random
fg=open("neg_all.txt","r")
fp=open("record_pos.txt","r")
fm=open("out_file.txt","w")
ls_1=fg.readlines()
ls_2=fp.readlines()
ls_1+=ls_2
random.shuffle(ls_1)
fm.writelines(ls_1)


fg.close()
fp.close()
fm.close()



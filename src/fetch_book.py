import os
import shutil
fp=open("neg_1.txt","r")
fg=open("neg_2.txt","r")
fm=open("neg_all.txt","w")
ls_1 = fp.readlines()
ls_2 = fg.readlines()
ls_1 += ls_2
ls_3 = []
for i in ls_1:
    st="0 "
    st=st+str(i)
    ls_3.append(st)
ls_3=ls_3[:36081]
fm.writelines(ls_3)

fp.close()
fg.close()
fm.close()















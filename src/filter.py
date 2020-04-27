import os
import shutil
from tqdm import tqdm
import re

reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
fpp=open("words.txt","r")
fp_ls=fpp.readlines()
stri=""
for i in range(len(fp_ls)):
    fp_ls[i]=re.sub(reg,'',fp_ls[i])
    if i==len(fp_ls)-1:
        stri+=fp_ls[i]
    else:
        stri+=fp_ls[i]+"|"
print(stri)
pattern=re.compile(stri)



path = '../data/book_small/'
out_path = '../data/book_small_filtered/'
print(os.listdir(path))
for ii in os.listdir(path):        # 藏
    ls_1 = path + ii + '/'
    for jj in os.listdir(ls_1):    # 部
        data_list=[]
        ls_2 = ls_1 + jj + '/'
        for kk in os.listdir(ls_2):
            book_path = ls_2 + kk 
            fp = open(book_path, 'r')
            isexist = os.path.exists(out_path+ii+'/'+jj+'/')
            if not isexist:
                os.makedirs(out_path+ii+'/'+jj+'/')
            fg = open(out_path+ii+'/'+jj+'/'+kk,'w')
            ls = fp.readlines()
            out_ls=[]
            put_ls=[]
            for i in range(len(ls)):
                result=pattern.findall(ls[i])
                if result:
                    result.insert(0,str(i+1))
                    out_ls.append(result)
            for i in out_ls:
                stri=""
                for j in i:
                    stri+=j+" "
                stri+="\n"
                put_ls.append(stri)
            fg.writelines(put_ls)
            fp.close()
            fg.close()
fpp.close()







import jieba
import os
import shutil
import re
import jieba.posseg as pseg
jieba.enable_parallel(8)
jieba.enable_paddle()
fp=open("words.txt","r")
#fg=open("zhejiang.txt","r")
#fn=open("zj.out","w")
reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
fp_ls=fp.readlines()
stri=""
for i in range(len(fp_ls)):
    fp_ls[i]=re.sub(reg,'',fp_ls[i])
    if i==len(fp_ls)-1:
        stri+=fp_ls[i]
    else:
        stri+=fp_ls[i]+"|"
# print(stri)
pattern=re.compile(stri) #构造正则过滤

path = '../../data/book_small/'
out_path = '../../data/book_small_cut/'
print(os.listdir(path))
for ii in os.listdir(path):        # 藏
    ls_1 = path + ii + '/'
    for jj in os.listdir(ls_1):    # 部
        data_list=[]
        ls_2 = ls_1 + jj + '/'
        for kk in os.listdir(ls_2):
            book_path = ls_2 + kk 
            fg = open(book_path, 'r')
            isexist = os.path.exists(out_path+ii+'/'+jj+'/')
            if not isexist:
                os.makedirs(out_path+ii+'/'+jj+'/')
            fn = open(out_path+ii+'/'+jj+'/'+kk,'w')
            out_ls=[]
            put_ls=[]
            fg_ls=fg.readlines()
            for i in range(len(fg_ls)):
                result=pattern.findall(fg_ls[i])
                if result:
                    result.insert(0,str(i+1)) 
                    out_ls.append(result)
                    doc=pseg.cut(fg_ls[i],use_paddle=True)
                    tmp_ls=[]
                    strj=""
                    for word,flag in doc:
                        strj+=word+" "+flag+" "
                    tmp_ls.append(strj)
                    out_ls.append(tmp_ls)
             
            for i in out_ls:
                stri=""
                for j in i:
                    stri+=j+" "
                stri+="\n"
                put_ls.append(stri)
            fn.writelines(put_ls)


            fg.close()
            fn.close()


fp.close()




































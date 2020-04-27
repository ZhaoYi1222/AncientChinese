# words.txt
# ming_origin.txt

import re
fp=open("words.txt","r")
fg=open("shandong.txt","r")
fn=open("tt.out","w")
reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
fp_ls=fp.readlines()
stri=""
for i in range(len(fp_ls)):
    fp_ls[i]=re.sub(reg,'',fp_ls[i])
    if i==len(fp_ls)-1:
        stri+=fp_ls[i]
    else:
        stri+=fp_ls[i]+"|"
print(stri)
pattern=re.compile(stri)
out_ls=[]
put_ls=[]

fg_ls=fg.readlines()
for i in range(len(fg_ls)):
    result=pattern.findall(fg_ls[i])
    if result:
        result.insert(0,str(i+1)) 
        out_ls.append(result)
for i in out_ls:
    stri=""
    for j in i:
        stri+=j+" "
    stri+="\n"
    put_ls.append(stri)
fn.writelines(put_ls)
fp.close()
fg.close()
fn.close()















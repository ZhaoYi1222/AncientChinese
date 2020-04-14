from jiayan import PMIEntropyLexiconConstructor
from jiayan import CharHMMTokenizer
from jiayan import WordNgramTokenizer
from jiayan import CRFSentencizer
from jiayan import CRFPunctuator
from jiayan import CRFPOSTagger
from jiayan import load_lm
import os
import shutil
from tqdm import tqdm
import re

lm = load_lm('/home/zy/mnt/nlp_test/Jiayan/jiayan_models/jiayan.klm')
punctuator = CRFPunctuator(lm, '/home/zy/mnt/nlp_test/Jiayan/jiayan_models/cut_model')
punctuator.load('/home/zy/mnt/nlp_test/Jiayan/jiayan_models/punc_model')

sentencizer = CRFSentencizer(lm)
sentencizer.load('/home/zy/mnt/nlp_test/Jiayan/jiayan_models/cut_model')

reg = "[^0-9A-Za-z\u4e00-\u9fa5]"

path = './books_small/'
out_path = './book_small_preprocessed/'
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
            for i in tqdm(range(len(ls))):
                tmp_list=sentencizer.sentencize(ls[i])
                merge_list=[]
                for j in range(len(tmp_list)):
                    tmp_list[j]=re.sub(reg,'',tmp_list[j])
                    tmp_list[j]+='\n'
                    if (tmp_list[j]=='\n'):
                        pass
                    else:
                        merge_list.append(tmp_list[j])
                out_ls += merge_list
            fg.writelines(out_ls)
            fp.close()
            fg.close()



# fp = open('./gd_raw.txt','r')
# fg = open('./gd_after.txt','w')
# reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
# 
# ls = fp.readlines()
# out_ls=[]
# for i in tqdm(range(len(ls))):
#     tmp_list=sentencizer.sentencize(ls[i])
#     merge_list=[]
#     for j in range(len(tmp_list)):
#         tmp_list[j]=re.sub(reg,'',tmp_list[j])
#         tmp_list[j]+='\n'
#         if (tmp_list[j]=='\n'):
#             pass
#         else:
#             merge_list.append(tmp_list[j])
#     out_ls += merge_list
# fg.writelines(out_ls)
     
# for i in tests:
#     print(punctuator.punctuate(i))

# for i in tests:
#     print(sentencizer.sentencize(i))

# big_test = ''
# for i in tests:
#     big_test += i
# print(punctuator.punctuate(big_test)) 
# print(sentencizer.sentencize(big_test))

# fp.close()
# fg.close()










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
from collections import Counter
from pprint import pprint

lm = load_lm('/home/zy/mnt/nlp_test/Jiayan/jiayan_models/jiayan.klm')
tokenizer = CharHMMTokenizer(lm)
out_ls=[]
words=[]
reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
fp=open("origin_record.txt","r")
fg=open("tmp.out","w")
ls=fp.readlines()
for i in ls:
    i=re.sub(reg,"",i)
    tstr=""
    gg=list(tokenizer.tokenize(i))
    for j in gg:
        tstr= tstr+j+" "
        words.append(j)
    tstr+="\n"
    out_ls.append(tstr)
fg.writelines(out_ls)

counter = Counter(words)
tr=counter.most_common(2000)
# pprint(counter.most_common(2000))
for i in tr:
    print(i[0])



fp.close()
fg.close()




























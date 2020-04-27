# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020-02-12 17:33
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
import pandas as pd
import numpy as np
from bert.extract_feature import BertVector
from keras.models import load_model

import keras.backend.tensorflow_backend as KTF
import tensorflow as tf
config = tf.ConfigProto()
config.gpu_options.allow_growth=True   #不全部占满显存, 按需分配
sess = tf.Session(config=config)
KTF.set_session(sess)

load_model = load_model("visit_classify.h5")

fp=open("jiangnan.txt","r")
texts=fp.readlines()
fp.close()

labels = []

bert_model = BertVector(pooling_strategy="REDUCE_MEAN", max_seq_len=100)

# 对上述句子进行预测
for text in texts:

    # 将句子转换成向量
    vec = bert_model.encode([text])["encodes"][0]
    x_train = np.array([vec])

    # 模型预测
    predicted = load_model.predict(x_train)
    y = np.argmax(predicted[0])
    label = 'Y' if y else 'N'
    labels.append(label)

for text,label in zip(texts, labels):
    print('%s\t%s'%(label, text),end="")

df = pd.DataFrame({'句子':texts, "是否属于气候描述类": labels})
df.to_excel('./result.xlsx', index=False)

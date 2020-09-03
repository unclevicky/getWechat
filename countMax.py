# _*_ coding:utf-8 _*_

import re,os
from collections import Counter


#file_path = "./download/html/20190628010623_1.html"
file_folder = "./download/html/"
f_list = os.listdir(file_folder)
words=[]
for f in f_list:
    if (not f[-5:] == ".html") or ("tmp" in f):  # 不是html文件的不转换，含有tmp的不转换
        continue
    f_path=file_folder+f
    _words = re.findall(r'[\u4E00-\u9FA5\s]',open(f_path,mode='r',encoding='UTF-8').read().replace(' ','').replace('\n','').replace('\t',''))
    words.extend(_words)
    #print(type(_words))

with open('words_count.txt','w',encoding='UTF-8') as f:
    f.write(str(Counter(words).most_common()))

#print(Counter(words).most_common(100))
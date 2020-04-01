# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 20:02:06 2019

@author: zhy323
"""

import re         #正则表达书去除空格和标点符号,数字
punctuation = '.!,;:?"\''+"("+")"+"0"+"1"+"2"+"3"+"4"+"5"+"6"+"7"+"8"+"9"

import operator

import matplotlib.pyplot as plt



#加入GUI
from tkinter import *



def removePunctuation(text):
    text = re.sub(r'[{}]+'.format(punctuation),'',text)
    return text.strip().lower()


def read():
    with open(r'test.txt','r') as f1:
        print(f1.read())
    
def numbersta():
    with open(r'test.txt','r') as f1:
        list1=f1.readlines()
    list2=[]

    for i in list1:
        list1_1=i.split()
        for j in list1_1:
            j1=removePunctuation(j)
            list2.append(j1)
        list3=[]
        
    for i in list2:
        if i!="":
            list3.append(i)
          
    print("单词的个数为：",len(list3))

def sta():
    with open(r'test.txt','r') as f1:
        list1=f1.readlines()
        list2=[]

    for i in list1:
        list1_1=i.split()
        for j in list1_1:
            j1=removePunctuation(j)
            list2.append(j1)
    list3=[]
    for i in list2:
        if i!="":
            list3.append(i)

#利用字典统计词频

    dic = {}   #创建字典
    for i in list3:   #对于所有的英语单词，如果在字典中，则令值+1，若不在字典中，则创建这个值并赋值为1
        if i not in dic:  
            dic[i] = 1
        else:
            dic[i] = dic[i] + 1
    v1 = sorted(dic.items(),key=operator.itemgetter(1),reverse=True)  
#利用停表去除
    with open(r'stopword.txt','r') as f2:
        list11=f2.readlines()
        line12=[]
        line13=[]
    for i in list11:
        i2=i.strip()
        line12.append(i2)
        for i in range(0,len(line12)):
            for j in line12[i].split():
                line13.append(j)

    list2x=[]
    list2y=[]
    for k,v in v1:
        if k not in line13:
            print(k,v)
            list2x.append(k)
            list2y.append(v)
    list2m=[]
    list2n=[]
    for i in range(0,6):
        list2m.append(list2x[i])
        list2n.append(list2y[i])
    plt.bar(list2m,list2n)
    plt.show()
#制作统计表

window=Tk()                                                      #创建登录界面
window.title(u'文本编辑器')                          #加入标题

Button(window,text='显示文本',command=read).grid(row=3, column=0, sticky=W, padx=10, pady=5)    #输入按钮
Button(window,text=u'统计字数',command=numbersta).grid(row=3, column=1, sticky=E, padx=10, pady=5)
Button(window,text=u'高频词查询',command=sta).grid(row=3, column=2, sticky=W, padx=10, pady=5)
Button(window,text=u'退出程序',command=window.destroy).grid(row=3, column=3, sticky=W, padx=10, pady=5)

mainloop()   #执行循环
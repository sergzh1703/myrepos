# -*- coding: utf-8 -*-
new3=open('D:/new3','w')
new1=open('D:/1new','r',  encoding='utf-8')
new1l=new1.readlines()
with open('D:/2new','r',  encoding='utf-8') as new2:
    for line in new2:
          for line1 in new1l:
            if line1.rstrip() in line:
                new3.write(line)
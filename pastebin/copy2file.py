#encoding utf-8
import re
from os.path import exists
import sys

#set encoding to utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

def copy(fileName,text,mode):#mode 0: not overwrite
                             #     1: overwrite
  if not exists("%s%s"%(fileName,'.txt')) or mode == 1:
    f=open("%s%s"%(fileName,'.txt'),"wb")
    f.write(text)
    f.close()


#encoding utf-8
import requests
from bs4 import BeautifulSoup
from sys import argv

import pastebin_login
import pastebin_get_paste_list
import copy2file
session_key=''

def main():
  tlist=[]
  urlist=[]

  #login and get
  if len(argv)==4:
    session_key=pastebin_login.get_session_key(argv[1],argv[2],argv[3])
    pastebin_get_paste_list.getList(tlist,urlist,argv[2])

  #just get target account
  elif len(argv)==2:
    pastebin_get_paste_list.getList(tlist,urlist,argv[1])

  #get default account
  else:
    session_key=pastebin_login.get_session_key()
    pastebin_get_paste_list.getList(tlist,urlist)



  for iteration in range(len(tlist)):
    res =requests.get(urlist[iteration])
    code =BeautifulSoup(res.text)
    print '\n\nPaste :%s      url :%s\n'%(tlist[iteration],urlist[iteration])
    for item in code.select(".paste_code"):
      copy2file.copy(tlist[iteration],item.text,1)

  #this is test line

if __name__=='__main__':
  main()

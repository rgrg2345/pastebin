#encoding utf-8
import requests
from bs4 import BeautifulSoup
import re

import pastebin_login
session_key=''

def test():
  string='123456'
  print string[1:]
  print string[:3]
  print string[1:3]

def getList(*arg):
  """
  arg [0]: title list
      [1]: url   list
      [2]: appoint account
  """

  #didn't need to login account to get to list except operation on paste
  #session_key = pastebin_login.get_session_key()
  if len(arg)!=3:
    res =requests.get("http://pastebin.com/u/py_test_acc")
  else:
    res =requests.get("http://pastebin.com/u/%s"%arg[2])
  code = BeautifulSoup(res.text)
  for item in code.select('td'):
    if len(item.contents) > 1:
      string = str(item.contents[2])#get title
      arg[0].append(item.contents[2].text)
      arg[1].append('http://pastebin.com/%s'%string[10:18])
      print "Title : %s  url : "%item.contents[2].text ,'http://pastebin.com/%s'% string[10:18]

if __name__=='__main__':
  getList([],[])

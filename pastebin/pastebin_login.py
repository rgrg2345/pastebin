#ecoding utf-8
import requests
from bs4 import BeautifulSoup

#I know this is bad write for login ,but just practice acc nothing

def get_session_key(*arg):
  uni_key="47e10b5a03d527bb254790f8213c274b"
  account='py_test_acc'
  password='123456'

  if len(arg)==3:
    uni_key,account,password = arg
  #print uni_key,account,password
  payload={
      'api_dev_key':uni_key,
      'api_user_name':account,
      'api_user_password':password
      }
  print "login..."
  print "Account : %s"%(account)
  res = requests.post("http://pastebin.com/api/api_login.php",data = payload)
  session_key = res.text
  return session_key


#encoding utf-8
from bs4 import BeautifulSoup
import requests

def main():
  print 'Post testing'
  payload={
      'api_dev_key':'47e10b5a03d527bb254790f8213c274b',
      'api_user_name':'py_test_acc'
      }
  res = requests.post("http://pastebin.com/api/api_login.php",data = payload)
  print res.text

if __name__=='__main__':
  main()

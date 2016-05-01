#ecoding utf-8
import requests
from bs4 import BeautifulSoup
import pastebin_login
from sys import argv

def check_file(filename):
  import re
  import sys
  match=re.search('(?:.txt)',filename)
  if not match:
    print 'not a txt file'
    sys.exit(-1)
    return False
  return True

def main():

  #default setting
  paste_code='use default code\n'
  title='Title'
  uni_key='47e10b5a03d527bb254790f8213c274b'

  arg_len=len(argv)
  if arg_len == 2 or arg_len == 3:#use default account
    filename=str(argv[1])

    if check_file(filename):
      f=open(filename,'r')
      paste_code=f.read()
      title =filename

    if arg_len == 3 :
      title=argv[2]
    key = pastebin_login.get_session_key()

  elif arg_len == 5:
                    #arg [1] : filename
                    #    [2] : uni key
                    #    [3] : account
                    #    [4] : password
    filename=str(argv[1])

    if check_file(filename):
      uni_key=argv[2]
      key=pastebin_login.get_session_key(uni_key,argv[3],argv[4])

      #read file
      f=open(filename,'r')
      paste_code=f.read()
      title=filename
  else:
    key=pastebin_login.get_session_key()

  payload = {
      'api_dev_key':uni_key,#dev key is unique for every account
      'api_paste_code':paste_code,
      'api_paste_private':'0',    #0=public 1=unlisted,2=private
      'api_paste_name':title,#this is title
      'api_paste_expire_date':'N',# N for never
                                  # 10M=10mins
                                  # 1H=1 hour
                                  # 1D=1 day
                                  # 1W=1 week
                                  # 1M=1 month
      'api_paste_format':'text',
      'api_user_key':key, #temp session key
      'api_option':'paste'
      }
  res =requests.post("http://pastebin.com/api/api_post.php",data =payload)
  print res.text

  print payload
  """
  res2 = requests.get(res.text)
  code = BeautifulSoup(res2.text)
  for item in code.select('#paste_code'):
    print item.text
  """


if __name__=='__main__':
  main()

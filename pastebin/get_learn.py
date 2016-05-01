#encoding utf-8
import requests
from bs4 import BeautifulSoup
def main():
  res = requests.get("http://pastebin.com/","html.parser")
  #print res.text
  code = BeautifulSoup(res.text)
  for item in code.select('a'):
    print item.select('.header_icons')
if __name__=='__main__':
  main()

from Unit2 import *


def test():
  Log.Message("hello testing")
  Browsers.Item[btChrome].Run('https://www.facebook.com/')
  chrome = Sys.Browser('Chrome').Page("https://www.facebook.com/")
  chrome.FindChildByXPath('//*[@id="u_0_m"]').SetText('Tanmaya')
  Log.Message("hello testing1")
  
  
def test2():
  Log.Message("Hello Automation testing")
  library()

import os, subprocess
from writeTest import test

def testDir(dir):
   contents = os.listdir(dir)
   for item in contents:
      if not(os.path.isdir(dir+"/"+item)):
         testSource = os.path.abspath(dir+"/"+item)
         testOut = os.path.abspath("temp/test.js")
         test(testSource,testOut)
   for item in contents:
      if os.path.isdir(dir+"/"+item):
         testDir(dir+"/"+item)

#testDir("testCases")
test("testCases/unitstest1.txt","temp/test.js")
#recursive search version
import os, subprocess
filename = 'myListFile.html'

def getDir(dir,depth,html):
   contents = os.listdir(dir)
   for item in contents:
      if not(os.path.isdir(dir+"/"+item)):
         print(item)
         html.write('<p style="margin-left: '+str(depth)+'px">'+item+'</p>\n')
   for item in contents:
      if os.path.isdir(dir+"/"+item):
         print(item)
         #print(os.listdir(dir+"/"+item))
         html.write('<p style="margin-left: '+str(depth)+'px">&#x1F4C1 '+item+'</p>\n')
         getDir((dir+"/"+item),depth+40,html)
   
      
#   for root in os.walk(dir, topdown=True):   
      

htmlfile = open(filename, "w+")
htmlfile.write('''<!DOCTYPE html>\n
<html lang="en-US" style="height: 100%;">\n
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>My List HTML Output</title>\n''')

getDir(".",40,htmlfile)
	
print("done")
htmlfile.write('''</head>''')
htmlfile.close()

# top layer only
#import os, subprocess

#filename = 'myListFile.html'

#htmlfile = open(filename, "w+")
#htmlfile.write('''<!DOCTYPE html>\n
#<html lang="en-US" style="height: 100%;">\n
##<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
#<title>HTML Text Formatting</title>\n''')
#for file in os.listdir("."):
#    print(file)
#    htmlfile.write(file+'<br>')
#htmlfile.write('''</head>''')
#htmlfile.close()

subprocess.call(['xdg-open', filename])

# recursive search version
# import os
# for root, dirs, files in os.walk(".", topdown=False):
#    for name in files:
#       print(os.path.join(root, name))
#    for name in dirs:
#       print(os.path.join(root, name))
# print("done")

# top layer only
import os, subprocess

filename = 'myListFile.html'

htmlfile = open(filename, "w+")
htmlfile.write('''<!DOCTYPE html>\n
<html lang="en-US" style="height: 100%;">\n
<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>HTML Text Formatting</title>\n''')
for file in os.listdir("."):
    print(file)
    htmlfile.write(file+'<br>')
htmlfile.write('''</head>''')
htmlfile.close()

subprocess.call(['xdg-open', filename])

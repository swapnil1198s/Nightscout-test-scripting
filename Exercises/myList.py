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
for file in os.listdir("."):
    print(file)
    htmlfile.write(file+'\n')
htmlfile.close()

subprocess.call(['open', filename])
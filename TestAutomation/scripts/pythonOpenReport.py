import os, subprocess

dirname = os.path.dirname(__file__)
reportname = '../reports/testReport.html'
filename = os.path.join(dirname, reportname)
try:subprocess.call(['xdg-open', filename])
except: 
    try:subprocess.call(['open', filename])
    except:os.startfile(filename)
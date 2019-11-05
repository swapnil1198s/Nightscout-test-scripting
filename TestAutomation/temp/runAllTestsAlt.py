import os, subprocess
from shutil import copy
import time
from exegen import exeGen
from writeTest import test

# MAIN TEST SCRIPT
# TO RUN THIS SCRIPT, CD TO 'TestAutomation',
# then execute the command 'python3 scripts/runAllTests.py

filename = os.path.join('.', 'reports', 'testReport.html')
casepath = os.path.join('.', 'testCases')
outpath = os.path.join(os.path.dirname(__file__), 'testCasesExecutables')
exectemplatepath = os.path.join('.', 'scripts', 'executableTemplate')
outfilepath = os.path.join('.', 'testCasesExecutables', 'test.js')

with open(filename, "w") as htmlfile:
        htmlfile.write('''<!DOCTYPE html>\n
        <html lang="en-US" style="height: 100%;">\n
        <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Testing Report</title>\n''')

        for infilepath in sorted(os.listdir(casepath)):
                print('generate test: ', infilepath)
                htmlfile.write('<p style="margin-left: 0px">'+'Test ' +infilepath +'\t')

                test(os.path.join(casepath, infilepath),outfilepath)

                proc = subprocess.Popen('npm test 2>&1', shell=True,stdout=subprocess.PIPE)
                line = proc.stdout.readline()
                j = 0
                while line:
                        line = line.decode('utf-8').strip('\t').strip('\r').strip('\n').strip('\@').strip('>')
                        if len(line.strip(' ')) > 0 and j > 2:
                                if '1 passing' in line:  #                              # write output to htmlfile
                                        htmlfile.write("- Pass &#x2705")
                                elif 'Test failed' in line:
                                        htmlfile.write("- Fail &#x26D4")
                        line = proc.stdout.readline()
                        j += 1
        print("done")
        htmlfile.write('''</head>''')

try: subprocess.call(['xdg-open', filename])
except:
        try: os.startfile(filename)
        except: pass

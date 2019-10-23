import os, subprocess

# MAIN TEST SCRIPT
# TO RUN THIS SCRIPT, CD TO 'TestAutomation',
# then execute the command 'python3 scripts/runAllTests.py

filename = os.path.join('.', 'reports', 'testReport.html')
casepath = os.path.join('.', 'testCases')
outpath = os.path.join(os.path.dirname(__file__), 'testCasesExecutables')

casetemplatepath = os.path.join('.', 'scripts', 'testcaseTemplate')
exectemplatepath = os.path.join('.', 'scripts', 'executableTemplate')

outfilepath = os.path.join('.', 'testCasesExecutables', 'test.js')

try: os.remove(filename)
except: print('No infilepath to delete!')

print(filename, os.path.exists(filename))

from exegen import exeGen
# './reports/testReport.html' == os.path.join('.', 'reports', 'testReport.html')
# hacky minithread to fake exegen
from shutil import copy
import time
from tempgen import tempGen

with open(filename, "w+") as htmlfile:
        htmlfile.write('''<!DOCTYPE html>\n
        <html lang="en-US" style="height: 100%;">\n
        <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>My List HTML Output</title>\n''')

        for infilepath in os.listdir(casepath):
                print('generate test: ', infilepath, outpath)
                htmlfile.write('<p style="margin-left: 0px">'+'Test ' +infilepath +'</p>\n')

                # break

                # generate executable based on line
                exeGen(os.path.join(casepath, infilepath), outfilepath, exectemplatepath)

        # for i in range(4):
        #         print('running test', i)
        #         tempGen(i)
        #         time.sleep(.25)
                print('executing')
                proc = subprocess.Popen('npm test 2>&1', shell=True,stdout=subprocess.PIPE)

                line = proc.stdout.readline()
                if line is not None:
                        htmlfile.write('<p style="margin-left: 40px">')
                j = 0
                while line:
                        line = line.decode('utf-8').strip('\t').strip('\r').strip('\n').strip('\@').strip('>')
                        if len(line.strip(' ')) > 0 and j > 2:
                                # write output to htmlfile
                                # print(line)
                                htmlfile.write(line + '\t|\t')
                        line = proc.stdout.readline()
                        j += 1
                htmlfile.write('</p>\n')
        print("done")

        htmlfile.write('''</head>''')

try: subprocess.call(['xdg-open', filename])
except:
        try: os.startfile(filename)
        except: pass

# delete old html, generate new empty one

# For each infilepath in Test Cases
#     delete all executables
#     generate executable from infilepath
        # import from script
#     subprocess.execute('NPM TEST')
#     pipe output to resutls.hmtl
        # import from script

# open 'finished' html infilepath
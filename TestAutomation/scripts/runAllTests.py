import os, subprocess

# MAIN TEST SCRIPT
# TO RUN THIS SCRIPT, CD TO 'TestAutomation',
# then execute the command 'python3 scripts/runAllTests.py

filename = os.path.join('.', 'reports', 'testReport.html')
casepath = os.path.join('.', 'testCases')
outpath = os.path.join(os.path.dirname(__file__), 'testCasesExecutables')

casetemplatepath = os.path.join('.', 'scripts', 'testcaseTemplate')
exectemplatepath = os.path.join('.', 'scripts', 'executableTemplate')

outfilepath = os.path.join('.', 'testCaseExecutables', 'test.js')

try: os.remove(filename)
except: print('No infilepath to delete!')

print(filename, os.path.exists(filename))

def exeGen(infilepath):
        print('exegen', infilepath, outpath)
        # infilepath == 'infilepath'

        # remove old executables
        # for file in outfilepath:
        #         os.remove(file)

        # generate new executable
        exeTemplate = open(exectemplatepath, "w+")
        testCase = open(infilepath, "r")
        inputs = testCase.readLines()
        for i in inputs:
                pass
        # do stuff here

        exeTemplate.close()
        testCase.close()

# './reports/testReport.html' == os.path.join('.', 'reports', 'testReport.html')
# hacky minithread to fake exegen
from shutil import copy
import time
def tempGen(i):
        if i == 0:
                copy('temp/test-1.js', 'testCasesExecutables/test.js')
        if i == 1:
                copy('temp/test-2.js', 'testCasesExecutables/test.js')
        if i == 2:
                copy('temp/test-3.js', 'testCasesExecutables/test.js')
        if i == 3:
                copy('temp/test-4.js', 'testCasesExecutables/test.js')


with open(filename, "w+") as htmlfile:
        htmlfile.write('''<!DOCTYPE html>\n
        <html lang="en-US" style="height: 100%;">\n
        <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>My List HTML Output</title>\n''')

        for infilepath in os.listdir(casepath):
                print('generate test: ', infilepath, outpath)
                htmlfile.write('<p style="margin-left: 0px">'+'Test ' +infilepath +'</p>\n')
                
                break

                # generate executable based on line
                exeGen(os.path.join(casepath, infilepath))

        for i in range(4):
                print('running test', i)
                tempGen(i)
                time.sleep(.25)
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
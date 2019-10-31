import os, subprocess
import importlib.util
from shutil import copy
import time
from exegen import exeGen
from writeTest import test
from minigen import minigen
from reportgen import reportline
from oracle_exegen import oracle_exegen

oraclepath = os.path.abspath(os.path.join('.', 'oracles', 'oracle.py'))
spec = importlib.util.spec_from_file_location("oracle.oracle", oraclepath)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
# res = foo.oracle(1, 2)
# from ..oracles.oracle import oracle

# MAIN TEST SCRIPT
# TO RUN THIS SCRIPT, CD TO 'TestAutomation',
# then execute the command 'python3 scripts/runAllTests.py

def reportHeader():
    header = ''
    header += '''
    <table border="2" width="100%">
        <tr align="center">
            <th colspan="9">Testing Report</th>
        <tr>
            <th> Test # </th>
            <th> Pass/Fail </th>
            <th> Test ID </th>
            <th> Requirements Being Tested </th>
            <th> Component </th>
            <th> Method </th>
            <th> Input </th>
            <th> Expected Output </th>
            <th> Actual Output </th>
        </tr>\n'''
    return header

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

    htmlfile.write(reportHeader())
    lineCount = 0
    # set maxTableSize to -1 for no limit
    maxTableSize = -1
    for infilepath in sorted(os.listdir(casepath)):
        print('generate test: ', infilepath, outpath)

        oracle_exegen(os.path.join(casepath, infilepath),outfilepath)

        print('executing')
        proc = subprocess.Popen('npm run oracle 2>&1', shell=True,stdout=subprocess.PIPE)

        # os.system('npm run oracle')
        # break

        lines = proc.stdout.readlines()
        expectval = lines[-3].decode('utf-8').strip('\n').strip('\r').strip()
        returnval = lines[-2].decode('utf-8').strip('\n').strip('\r').strip()
        resval = lines[-1].decode('utf-8').strip('\n').strip('\r')

        print('results:', resval)
        print('expectval:', expectval)
        print('returnval:', returnval)

        casefile = open(os.path.join(casepath, infilepath),"r")
        lines = casefile.readlines()
        casefile.close()

        reportLine='\t\t<tr>\n\t\t\t<td>'+str(lineCount+1)+'</td>\n\t\t\t<td>'
        if (lineCount % maxTableSize == 0 and lineCount != 0 and maxTableSize != -1):
            reportLine='\t</table>\n\t\t<br>'+reportHeader()+reportLine

        if resval == "Pass":
            reportLine += 'Pass &#x2705</td>\n'
        elif resval == "Fail":
            reportLine += 'Fail &#x26D4</td>\n'
        else:
            reportLine += 'Error</td>\n'

        for input in lines:
            elementsList = input.split(':')
            element = elementsList[1].strip()
            reportLine += '\t\t\t<td>' + element + '</td>\n'

        reportLine += '\t\t\t<td>' + returnval.strip() + '</td>\n'
        reportLine += '\t\t</tr>\n'
        htmlfile.write(reportLine)
        lineCount += 1
    print("done")
    htmlfile.write('\t\t</table>\n\t</head>')

try: subprocess.call(['xdg-open', filename])
except:
    try: os.startfile(filename)
    except: pass
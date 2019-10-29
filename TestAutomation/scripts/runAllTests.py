import os, subprocess
import importlib.util
from shutil import copy
import time
from exegen import exeGen
from writeTest import test
from minigen import minigen
from reportgen import reportline
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
        
        # exeGen(os.path.join(casepath, infilepath), outfilepath, exectemplatepath)
        # test(os.path.join(casepath, infilepath),outfilepath)
        minigen(os.path.join(casepath, infilepath),outfilepath)

        print('executing')
        proc = subprocess.Popen('npm start 2>&1', shell=True,stdout=subprocess.PIPE)

        lines = proc.stdout.readlines()
        resval = lines[-1].decode('utf-8')


        casefile = open(os.path.join(casepath, infilepath),"r")
        lines = casefile.readlines()
        casefile.close()

        expectval = lines[-1].split(':')[-1]      
        reportLine='\t\t<tr>\n\t\t\t<td>'+str(lineCount+1)+'</td>\n\t\t\t<td>'
        if (lineCount % maxTableSize == 0 and lineCount != 0 and maxTableSize != -1):
            reportLine='\t</table>\n\t\t<br>'+reportHeader()+reportLine
  
        if (mod.oracle(expectval, resval) == "Pass"):
            reportLine += 'Pass &#x2705</td>\n'
        elif (mod.oracle(expectval, resval) == "Fail"):
            reportLine += 'Fail &#x26D4</td>\n'
        elif (mod.oracle(expectval, resval) == "TypeError"):
            reportLine += 'Error</td>\n'
        else:
            reportLine +='</td>\n'

        for input in lines:
            elementsList = input.split(':')
            element = elementsList[1].strip()
            reportLine += '\t\t\t<td>' + element + '</td>\n'
        
        reportLine += '\t\t\t<td>' + resval.strip() + '</td>\n'
        reportLine += '\t\t</tr>\n'
        htmlfile.write(reportLine)
        lineCount += 1
    print("done")
    htmlfile.write('\t\t</table>\n\t</head>')

try: subprocess.call(['xdg-open', filename])
except:
    try: os.startfile(filename)
    except: pass
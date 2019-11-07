import os, subprocess
import importlib.util
from oracle_exegen import oracle_exegen

# MAIN TEST SCRIPT
# TO RUN THIS SCRIPT, CD TO 'TestAutomation',
# then execute the command 'python3 scripts/runAllTests.py

def reportHeader(funcname=None):
    header = '''
    <table border="2" width="100%">
        <tr align="center">
            <th colspan="10"> Testing: '''+(funcname if funcname is not None else 'Testing')+'''</th>
        <tr>
            <th> Test # </th>
            <th> Pass/Fail </th>
            <th> Test ID </th>
            <th> Requirements Being Tested </th>
            <th> Component </th>
            <th> Method </th>
            <th> Input </th>
            <th> *args </th>
            <th> Expected Output </th>
            <th> Actual Output </th>
        </tr>\n'''
    return header

report = os.path.join('.', 'reports', 'testReport.html')
testcases = os.path.join('.', 'testCases')
testcaseexecutable = os.path.join('.', 'testCasesExecutables', 'test.js')

with open(report, "w") as htmlfile:
    htmlfile.write('''<!DOCTYPE html>\n
    <html lang="en-US" style="height: 100%;">\n
    <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Testing Report</title>\n''')
    lineCount = 0

    prevtest = None

    # set maxTableSize to -1 for no limit
    maxTableSize = -1
    for testcase in sorted(os.listdir(testcases)):
        print('\ntesting', testcase)
        inF = open(os.path.join(testcases, testcase))
        fileText = inF.readlines()
        inF.close()

        if len(fileText) < 7:
            fileText.insert(5, " :")

        testName = fileText[0].split(":")[1].strip("\n").strip()
        testReq = fileText[1].split(":")[1].strip("\n").strip()
        testFile = fileText[2].split(":")[1].strip("\n").strip()
        testMethod = fileText[3].split(":")[1].strip("\n").strip()
        testInput = fileText[4].split(":")[1].strip("\n").strip()
        testObjcall = fileText[5].split(":")[1].strip("\n").strip()
        testOracle = fileText[6].split(":")[1].strip("\n").strip()

        # print('  testname:\t', testName)
        # print('  testreq:\t', testReq)
        # print('  testfile:\t', testFile)
        # print('  testMethod:\t', testMethod)
        # print('  testinput:\t', testInput)
        # print('  objcall:\t', testObjcall)
        print('  oracle:\t', testOracle)

        print('  generating test')
        oracle_exegen(testFile, testMethod, testInput, testObjcall, testOracle, testcaseexecutable)

        print('  executing test')
        proc = subprocess.Popen('npm run oracle 2>&1', shell=True,stdout=subprocess.PIPE)

        lines = proc.stdout.readlines()
        expectval = lines[-3].decode('utf-8').strip('\n').strip('\r').strip()
        returnval = lines[-2].decode('utf-8').strip('\n').strip('\r').strip()
        resval = lines[-1].decode('utf-8').strip('\n').strip('\r')
        print('  expectval:\t', expectval)
        print('  returnval:\t', returnval)
        print('  results:\t', resval)

        casefile = open(os.path.join(testcases, testcase),"r")
        lines = casefile.readlines()
        casefile.close()

        print('  writing to report')
        reportLine='\t\t<tr>\n\t\t\t<td>'+str(lineCount+1)+'</td>\n\t\t\t<td>'

        if prevtest is None:
            htmlfile.write(reportHeader(testcase.split('_')[0]))
        elif prevtest != ''.join(i for i in testcase if not i.isdigit()):
            reportLine='\t</table>\n\t\t<br>'+reportHeader(testcase.split('_')[0])+reportLine
        prevtest = ''.join(i for i in testcase if not i.isdigit())

        if resval == "Pass":
            reportLine += 'Pass &#x2705</td>\n'
        elif resval == "Fail":
            reportLine += 'Fail &#x26D4</td>\n'
        else:
            reportLine += 'Error</td>\n'

        lines = [testName, testReq, testFile, testMethod, testInput, testObjcall, testOracle]
        for line in lines:
            reportLine += '\t\t\t<td>' + line + '</td>\n'

        reportLine += '\t\t\t<td>' + returnval.strip() + '</td>\n'
        reportLine += '\t\t</tr>\n'
        htmlfile.write(reportLine)
        lineCount += 1
    htmlfile.write('\t\t</table>\n\t</head>')
    print("\nall tests done")

print('opening report')
try: subprocess.call(['xdg-open', report])
except:
    try: os.startfile(report)
    except: pass
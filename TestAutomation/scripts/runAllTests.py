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
         for file in outfilepath:
                 os.remove(file)

        # generate new executable
                

        # do stuff here
        exeTemplate = open(exectemplatepath, "r")
        testCase = open(infilepath, "r")
        executable = open(outfilepath, "a+")
        executableString = executable.read()
        inputs = testCase.readLines()
        for line in inputs:
                value = line.split(':')
                replacement = value[1] 
                executableString.replace("%", replacement, 1)
        executable.write(executableString)


'./reports/testReport.html' == os.path.join('.', 'reports', 'testReport.html')

with open(filename, "w+") as htmlfile:
        htmlfile.write('''<!DOCTYPE html>\n
        <html lang="en-US" style="height: 100%;">\n
        <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>My List HTML Output</title>\n''')

        for infilepath in os.listdir(casepath):
                print('generate test: ', infilepath, outpath)
                htmlfile.write('<p style="margin-left: 0px">'+'Test ' +infilepath +'</p>\n')

                # generate executable based on line
                exeGen(infilepath)

                # run NPM test and catch output
                # line = subprocess.check_output('npm test exit 0', shell=True).decode('utf-8')

                proc = subprocess.Popen('npm test 2>&1', shell=True,stdout=subprocess.PIPE)

                line = proc.stdout.readline()
                while line:
                        line = line.decode('utf-8')

                        # write output to htmlfile
                        # print(line)
                        htmlfile.write('<p style="margin-left: 40px">'+str(line) +'</p>\n')
                        line = proc.stdout.readline()
                break
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
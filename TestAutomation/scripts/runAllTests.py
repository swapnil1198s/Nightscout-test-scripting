import os, subprocess

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
        exeTemplate = open(exectemplatepath, "w+")
        testCase = open(infilepath, "r")
        inputs = testCase.readLines()
        for i in inputs:
                
        # do stuff here

'./reports/testReport.html' == os.path.join('.', 'reports', 'testReport.html')

with open(filename, "w+") as htmlfile:
        htmlfile.write('''<!DOCTYPE html>\n
        <html lang="en-US" style="height: 100%;">\n
        <head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>My List HTML Output</title>\n''')

        for infilepath in os.listdir(casepath):
                print('generate test: ', infilepath, outpath)

                # generate executable based on line
                exeGen(infilepath)

                # run NPM test and catch output
                # line = subprocess.check_output('npm test exit 0', shell=True).decode('utf-8')

                proc = subprocess.Popen('npm test exit 0', shell=True,stdout=subprocess.PIPE)
                while True:
                        line = proc.stdout.readline()
                        if not line: break

                        # write output to htmlfile
                        print(line)
                        htmlfile.write('<p style="margin-left: 0px">'+infilepath+': '+str(line) +'</p>\n')

                break
        print("done")

        htmlfile.write('''</head>''')

try: subprocess.call(['xdg-open', filename])
except: os.startfile(filename)

# delete old html, generate new empty one

# For each infilepath in Test Cases
#     delete all executables
#     generate executable from infilepath
        # import from script
#     subprocess.execute('NPM TEST')
#     pipe output to resutls.hmtl
        # import from script

# open 'finished' html infilepath
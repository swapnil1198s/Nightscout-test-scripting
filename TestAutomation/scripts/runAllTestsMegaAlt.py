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
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
# res = foo.oracle(1, 2)
# from ..oracles.oracle import oracle

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
    <title>My List HTML Output</title>\n''')

    for infilepath in os.listdir(casepath):
        print('generate test: ', infilepath, outpath)

        # exeGen(os.path.join(casepath, infilepath), outfilepath, exectemplatepath)
        # test(os.path.join(casepath, infilepath),outfilepath)
        minigen(os.path.join(casepath, infilepath),outfilepath)

        print('executing')
        proc = subprocess.Popen('npm start 2>&1', shell=True,stdout=subprocess.PIPE)

        print(proc)

        lines = proc.stdout.readlines()
        infilepath += ': '
        infilepath += foo.oracle(1, 2)
        rline = reportline(infilepath,
        lines)

        htmlfile.write(rline)
    print("done")
    htmlfile.write('''</head>''')

try: subprocess.call(['xdg-open', filename])
except:
    try: os.startfile(filename)
    except: pass

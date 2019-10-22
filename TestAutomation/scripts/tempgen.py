from shutil import copy
def tempGen(i):
        if i == 0:
                copy('temp/test-1.js', 'testCasesExecutables/test.js')
        if i == 1:
                copy('temp/test-2.js', 'testCasesExecutables/test.js')
        if i == 2:
                copy('temp/test-3.js', 'testCasesExecutables/test.js')
        if i == 3:
                copy('temp/test-4.js', 'testCasesExecutables/test.js')
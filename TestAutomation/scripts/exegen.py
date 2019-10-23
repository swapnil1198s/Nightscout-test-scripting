def exeGen(infilepath, outfilepath, exectemplatepath):
    print('exegen', infilepath, outfilepath)

    # generate new executable, overriding old
    exeTemplate = open(exectemplatepath, "r")
    testCase = open(infilepath, "r")
    executable = open(outfilepath, "w")
    executableString = exeTemplate.read()
    inputs = testCase.readLines()

    for line in inputs:
        value = line.split(':')
        replacement = value[1]
        executableString.replace("%", replacement, 1)
    executable.write(executableString)

    exeTemplate.close()
    testCase.close()
    executable.close()

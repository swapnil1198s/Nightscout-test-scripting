def oracle_exegen(inFile, outFile):
    inF = open(inFile)
    output = ""
    fileText = inF.readlines()

    testName = fileText[0].split(":")[1]
    testReq = fileText[1].split(":")[1]
    testFile = fileText[2].split(":")[1]
    testMethod = fileText[3].split(":")[1]
    testInput = fileText[4].split(":")[1]
    testOracle = fileText[5].split(":")[1]

    testID = testName
    descr = testReq.strip("\n").strip()
    component = testFile.strip("\n").strip()
    methodName = testMethod.strip("\n").strip()
    inputReceived = testInput.strip("\n").strip()
    expectedOutput = testOracle.strip("\n").strip()

    output = 'srcname = "' +component +'"\n'
    output += 'funcname = "' +methodName +'"\n'
    output += 'inval = ' +inputReceived +'\n'
    output += 'expectval = ' +expectedOutput +'\n'
    output += '\n'
    output += 'pathval = "../project/src/" +srcname\n'
    output += '\n'
    output += 'var src = require(pathval)\n'
    output += '\n'
    output += 'function runtest(){\n'
    output += '    return [expectval, src.funcname(inval)]\n'
    output += '};'
    output += '\n'
    output += 'module.exports = runtest\n'

    print("Done")

    outF = open(outFile, "w")
    outF.write(output)
    inF.close()
    outF.close()
def minigen(inFile, outFile):
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
    descr = testReq.strip("\n")
    component = testFile.strip("\n")
    methodName = testMethod.strip("\n")
    inputReceived = testInput.strip("\n")
    expectedOutput = testOracle.strip("\n")

    output = 'var src = require("../project/src/'+component+'");\n'
    output += 'var Var = src.'+methodName +'('+str(inputReceived)+')'+';\n'
    output += 'console.log(Var)'

    print("Done")

    outF = open(outFile, "w")
    outF.write(output)
    inF.close()
    outF.close()



#test("testCases/unitstest1.txt","temp/testResults.txt")
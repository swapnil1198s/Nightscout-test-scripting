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

    output = '''
        var src = require("../project/src/'''+component+'''")
        function runtest(){
            res = [
                '''+expectedOutput +''',
                src.'''+methodName +'('+inputReceived +''')
            ];
            console.log(res[0])
            console.log(res[1])
            return(res)
        }
        module.exports = runtest;'''

    print("Done")

    outF = open(outFile, "w")
    outF.write(output)
    inF.close()
    outF.close()
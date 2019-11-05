def test(inFile, outFile):
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

    
    output = "//Test Name - " + testID
    output = output+"var unit = require(\"../project/src/"+str(component)+"\");\n"
    output = output+"var expect = require('chai').expect;\n"

    output = output + "describe('"+str(descr)+"', function() {\n"
    output = output + "\tcontext('', function(){\n"
    output = output + "\t\tit('', function(){\n"
    output = output + "\t\t\texpect(unit."+str(methodName)+"("+str(inputReceived)+")).to.equal("+str(expectedOutput)+")\n"
    output = output + "\t\t})\n"
    output = output + "\t})\n"
    output = output + "})"

##    output = testName
##    output = output + testReq
##    output = output + testFile
##    output = output + testMethod
##    output = output + testInput
##    output = output + testOracle                
##    output = output + "\nEnd of Test\n\n"

    print("Done")

    outF = open(outFile, "w")
    outF.write(output)
    inF.close()
    outF.close()



#test("testCases/unitstest1.txt","temp/testResults.txt")
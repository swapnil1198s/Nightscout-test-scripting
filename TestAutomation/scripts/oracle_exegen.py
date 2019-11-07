def oracle_exegen(testFile, testMethod, testInput, testObjcall, testOracle, outFile):

    output = (
        '''var src = require("../project/src/'''+testFile+'''")
        function runtest(){
            res = [
                '''+testOracle +''',
                src'''+('.'+testMethod if testMethod != '' else '')\
                +('('+(testInput if testInput != '_' else '') +')' if testInput != '' else '')\
                +('.'+testObjcall if testObjcall != '' else '') +'''
            ]
            return(res)
        }
        module.exports = runtest;'''
    ).replace('\n        ', '\n')

    outF = open(outFile, "w")
    outF.write(output)
    outF.close()
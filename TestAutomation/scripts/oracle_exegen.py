def oracle_exegen(testFile, testOracle, outFile, subFuncs):
    output = (
        '''var src = require("../project/src/''' +testFile +'''")
        function runtest(){
            res = [
                '''+ testOracle +''',
                src''' +subFuncs +'''
            ]
            return(res)
        }
        module.exports = runtest;'''
    ).replace('\n        ', '\n')

    outF = open(outFile, "w")
    outF.write(output)
    outF.close()
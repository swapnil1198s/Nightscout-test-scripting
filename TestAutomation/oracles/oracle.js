'use strict'

var tst = require("../testCasesExecutables/test.js")

var res = tst.runtest()
var expectval = res[0]
var returnval = res[1]

if (expectval === returnval){
    // return 'Pass'
    console.log('Pass')
}
else if (isNaN(expectval) && isNaN(outval)){
    // return 'Pass'
    console.log('Pass')
}
else{
    // return 'Fail'
    console.log('Fail')
}
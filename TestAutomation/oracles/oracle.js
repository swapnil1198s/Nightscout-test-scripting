'use strict'

var src = require("../testCasesExecutables/test.js")

function oracle(inval, expectval) {
    expectval = src.runtest(inval)
    if (expectval === outval){
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
}

module.exports = oracle